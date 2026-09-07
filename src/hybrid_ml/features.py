import numpy as np
import pandas as pd

def true_range(df):
    prev = df["close"].shift(1)
    return pd.concat([
        df["high"]-df["low"],
        (df["high"]-prev).abs(),
        (df["low"]-prev).abs()
    ], axis=1).max(axis=1)

def atr(df, n):
    return true_range(df).ewm(alpha=1/n, adjust=False, min_periods=n).mean()

def er(close, n):
    change=(close-close.shift(n)).abs()
    path=close.diff().abs().rolling(n).sum()
    return change/path.replace(0,np.nan)

def slope(series, n):
    xx=np.arange(n,dtype=float); xx-=xx.mean(); denom=(xx*xx).sum()
    return series.rolling(n).apply(lambda y: np.dot(xx, y-y.mean())/denom, raw=True)

def causal_nw(series, bandwidth, lookback):
    a=series.to_numpy(float); out=np.full(len(a),np.nan)
    idx=np.arange(lookback,dtype=float)
    weights=np.exp(-(idx**2)/(2.0*bandwidth**2))
    for t in range(lookback-1,len(a)):
        wv=a[t-lookback+1:t+1][::-1]
        valid=np.isfinite(wv)
        if valid.any():
            w=weights[valid]
            out[t]=(wv[valid]*w).sum()/w.sum()
    return pd.Series(out,index=series.index)

def wma(series,n):
    w=np.arange(1,n+1,dtype=float)
    return series.rolling(n).apply(lambda y: np.dot(y,w)/w.sum(),raw=True)

def build_features(df,cfg):
    x=df.copy(); c=x["close"]; core=cfg["core"]; fc=cfg["features"]
    x["ret_1"]=c.pct_change()
    x["log_ret_1"]=np.log(c).diff()
    for n in fc["momentum_windows"]:
        x[f"mom_{n}"]=c.pct_change(n)
    for n in fc["realized_vol_windows"]:
        x[f"rv_{n}"]=x["log_ret_1"].rolling(n).std()*np.sqrt(n)
    x["atr"]=atr(x,int(fc["atr_length"]))
    x["natr"]=100*x["atr"]/c
    x["natr_ref"]=x["natr"].rolling(int(fc["volatility_reference"])).mean()
    x["vol_ratio"]=x["natr"]/x["natr_ref"].replace(0,np.nan)
    for n in fc["er_lengths"]:
        x[f"er_{n}"]=er(c,int(n))
    for n in fc["slope_windows"]:
        x[f"slope_{n}"]=slope(c,int(n))/c

    nw=causal_nw(c,int(core["nw_bandwidth"]),int(core["nw_lookback"]))
    nw_s=nw.diff()
    sd=nw_s.rolling(int(core["normalization_length"])).std()
    raw=nw_s/sd.replace(0,np.nan)
    osc=wma(raw,int(core["oscillator_smoothing"]))
    signal=osc.ewm(span=int(core["signal_length"]),adjust=False).mean()
    x["osc"]=osc; x["signal"]=signal
    x["osc_minus_signal"]=osc-signal
    x["osc_abs"]=osc.abs()
    x["osc_slope_1"]=osc.diff()
    x["osc_slope_3"]=osc.diff(3)
    x["signal_slope_1"]=signal.diff()
    cu=(osc>signal)&(osc.shift(1)<=signal.shift(1))
    cd=(osc<signal)&(osc.shift(1)>=signal.shift(1))
    x["cross_count"]=(cu|cd).astype(float).rolling(int(fc["cross_lookback"])).sum()
    sgn=np.sign(osc)
    x["osc_same_sign_6"]=(sgn==sgn.shift()).rolling(6).mean()
    x["osc_same_sign_12"]=(sgn==sgn.shift()).rolling(12).mean()
    x["price_direction_12"]=np.sign(c.diff()).rolling(12).mean().abs()
    x["price_direction_24"]=np.sign(c.diff()).rolling(24).mean().abs()
    x["range_pct"]=(x["high"]-x["low"])/c
    x["body_pct"]=(x["close"]-x["open"]).abs()/c
    x["close_location"]=(x["close"]-x["low"])/(x["high"]-x["low"]).replace(0,np.nan)
    return x
