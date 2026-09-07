from pathlib import Path
import json, joblib, pandas as pd

def score_latest(row,model_dir,cfg):
    md=Path(model_dir)
    cols=json.loads((md/"feature_columns.json").read_text(encoding="utf-8"))
    X=row.reindex(columns=cols); dc=cfg["decision"]; out=[]
    for eng in ["MR","RUNNER","TF"]:
        cp=md/f"{eng.lower()}_win_classifier.joblib"; rp=md/f"{eng.lower()}_return_regressor.joblib"
        if not cp.exists() or not rp.exists(): continue
        c=joblib.load(cp); r=joblib.load(rp)
        pw=float(c.predict_proba(X)[0,1]); er=float(r.predict(X)[0])
        decision="TRADE" if pw>=dc["min_probability"] and er>dc["min_expected_return_pct"] else ("CAUTION" if pw>=dc["caution_probability"] and er>dc["min_expected_return_pct"] else "OFF")
        z={"engine":eng,"p_win":pw,"expected_return_pct":er,"decision":decision}
        if eng=="MR" and (md/"mr_fail_classifier.joblib").exists():
            f=joblib.load(md/"mr_fail_classifier.joblib")
            pf=float(f.predict_proba(X)[0,1]); z["p_mr_fail"]=pf
            if pf>dc["max_mr_fail_probability"]: z["decision"]="OFF"
        out.append(z)
    return pd.DataFrame(out)
