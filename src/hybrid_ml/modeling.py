from pathlib import Path
import json, joblib, numpy as np, pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor
from sklearn.metrics import roc_auc_score, average_precision_score, balanced_accuracy_score, brier_score_loss, mean_absolute_error
from sklearn.inspection import permutation_importance

def split_time(df,val_frac=.2,test_frac=.2):
    x=df.sort_values("entry_time").reset_index(drop=True)
    n=len(x); nte=max(1,int(n*test_frac)); nva=max(1,int(n*val_frac)); ntr=n-nte-nva
    if ntr<20: raise ValueError(f"Too few rows: {n}")
    return x.iloc[:ntr],x.iloc[ntr:ntr+nva],x.iloc[ntr+nva:]

def cls(seed):
    return Pipeline([("imputer",SimpleImputer(strategy="median")),
        ("model",HistGradientBoostingClassifier(max_depth=3,learning_rate=.05,max_iter=250,l2_regularization=1,random_state=seed))])

def reg(seed):
    return Pipeline([("imputer",SimpleImputer(strategy="median")),
        ("model",HistGradientBoostingRegressor(max_depth=3,learning_rate=.05,max_iter=250,l2_regularization=1,loss="absolute_error",random_state=seed))])

def cmetrics(m,X,y):
    p=m.predict(X); q=m.predict_proba(X)[:,1]
    z={"balanced_accuracy":balanced_accuracy_score(y,p),"brier":brier_score_loss(y,q)}
    z["roc_auc"]=roc_auc_score(y,q) if len(np.unique(y))==2 else np.nan
    z["pr_auc"]=average_precision_score(y,q) if len(np.unique(y))==2 else np.nan
    return z

def train(df,features,model_dir,reports_dir,cfg):
    md=Path(model_dir); rd=Path(reports_dir); md.mkdir(exist_ok=True); rd.mkdir(exist_ok=True)
    mc=cfg["model"]; seed=int(mc["random_state"]); rows=[]
    for eng in ["MR","RUNNER","TF"]:
        d=df[df.engine==eng].dropna(subset=["return_pct"]).copy()
        if len(d)<int(mc["minimum_engine_rows"]):
            rows.append({"engine":eng,"status":f"SKIP {len(d)} rows"}); continue
        tr,va,te=split_time(d,float(mc["validation_fraction"]),float(mc["test_fraction"]))
        cm=cls(seed); rm=reg(seed)
        cm.fit(tr[features],tr.is_win.astype(int)); rm.fit(tr[features],tr.return_pct.astype(float))
        met=cmetrics(cm,te[features],te.is_win.astype(int))
        pred=rm.predict(te[features])
        met.update({"mae_return_pct":mean_absolute_error(te.return_pct,pred),
                    "mean_actual_return_pct":float(te.return_pct.mean()),
                    "mean_pred_return_pct":float(pred.mean())})
        joblib.dump(cm,md/f"{eng.lower()}_win_classifier.joblib")
        joblib.dump(rm,md/f"{eng.lower()}_return_regressor.joblib")
        rows.append({"engine":eng,"status":"OK","rows":len(d),"test_rows":len(te),**met})
        try:
            pi=permutation_importance(cm,te[features],te.is_win.astype(int),n_repeats=8,random_state=seed,scoring="roc_auc")
            pd.DataFrame({"feature":features,"importance_mean":pi.importances_mean,"importance_std":pi.importances_std})              .sort_values("importance_mean",ascending=False).to_csv(rd/f"feature_importance_{eng.lower()}.csv",index=False)
        except Exception: pass

    mr=df[df.engine=="MR"].copy()
    if len(mr)>=int(mc["minimum_engine_rows"]) and mr.is_mr_fail.nunique()==2:
        tr,va,te=split_time(mr,float(mc["validation_fraction"]),float(mc["test_fraction"]))
        fm=cls(seed); fm.fit(tr[features],tr.is_mr_fail.astype(int))
        met=cmetrics(fm,te[features],te.is_mr_fail.astype(int))
        joblib.dump(fm,md/"mr_fail_classifier.joblib")
        rows.append({"engine":"MR_FAIL_RISK","status":"OK","rows":len(mr),"test_rows":len(te),**met})

    pd.DataFrame(rows).to_csv(rd/"model_metrics.csv",index=False)
    (md/"feature_columns.json").write_text(json.dumps(features,indent=2),encoding="utf-8")
    return pd.DataFrame(rows)
