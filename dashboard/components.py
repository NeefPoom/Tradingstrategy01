"""Reusable Streamlit components."""
from __future__ import annotations

from typing import Any

import pandas as pd
import streamlit as st


STATUS_COLORS = {
    "GREEN": "#16a34a",
    "PASS": "#16a34a",
    "HEALTHY": "#16a34a",
    "POSITIVE": "#16a34a",
    "YELLOW": "#f59e0b",
    "WARNING": "#f59e0b",
    "EARLY": "#f59e0b",
    "RED": "#dc2626",
    "FAIL": "#dc2626",
    "FAILED": "#dc2626",
    "STALE": "#dc2626",
    "GRAY": "#6b7280",
    "UNKNOWN": "#6b7280",
    "INSUFFICIENT": "#6b7280",
    "INSUFFICIENT_FORWARD_DATA": "#6b7280",
    "RESEARCH_ONLY": "#6b7280",
}


def inject_css() -> None:
    st.markdown(
        """
        <style>
        .block-container {padding-top: 1.4rem; padding-bottom: 2rem;}
        .phase-caption {color: #a7b0c0; font-size: .82rem; letter-spacing: 0;}
        .status-pill {display: inline-block; padding: .22rem .5rem; border-radius: 6px; font-size: .78rem; font-weight: 700; color: #0b1020;}
        .metric-card {border: 1px solid rgba(148,163,184,.22); border-radius: 8px; padding: .75rem; background: rgba(15,23,42,.45);}
        .metric-label {font-size: .76rem; color: #a7b0c0;}
        .metric-value {font-size: 1.12rem; font-weight: 750; margin-top: .15rem;}
        .small-note {color: #94a3b8; font-size: .82rem;}
        </style>
        """,
        unsafe_allow_html=True,
    )


def status_pill(label: Any) -> str:
    text = str(label or "UNKNOWN").upper()
    color = STATUS_COLORS.get(text, "#6b7280")
    return f'<span class="status-pill" style="background:{color}">{text}</span>'


def metric_card(label: str, value: Any, status: str | None = None) -> None:
    value_text = str(value)
    pill = status_pill(status) if status else ""
    st.markdown(
        f"""
        <div class="metric-card">
          <div class="metric-label">{label}</div>
          <div class="metric-value">{value_text}</div>
          {pill}
        </div>
        """,
        unsafe_allow_html=True,
    )


def progress(label: str, value: int, target: int) -> None:
    ratio = min(max(value / target, 0), 1) if target else 0
    st.caption(f"{label}: {value} / {target}")
    st.progress(ratio)


def dataframe_or_empty(df: pd.DataFrame, empty: str = "NOT YET AVAILABLE", height: int | None = None) -> None:
    if df.empty:
        st.info(empty)
    else:
        frame = df.reset_index(drop=True).copy()
        for col in frame.columns:
            has_nested = frame[col].map(lambda value: isinstance(value, (dict, list, tuple))).any()
            mixed_object = frame[col].dtype == "object" and frame[col].dropna().map(type).nunique() > 1
            if has_nested or mixed_object:
                frame[col] = frame[col].astype(str)
        kwargs: dict[str, object] = {"width": "stretch", "hide_index": True}
        if height is not None:
            kwargs["height"] = height
        st.dataframe(frame, **kwargs)


def frozen_controls_panel() -> None:
    st.markdown("#### Frozen Controls")
    rows = pd.DataFrame(
        [
            {"Item": "Model Version", "State": "H1.0"},
            {"Item": "MR_FAIL Threshold", "State": "0.45 LOCKED"},
            {"Item": "TF", "State": "OFF"},
            {"Item": "Broker Execution", "State": "OFF"},
            {"Item": "Yahoo Finance", "State": "ACTIVE"},
            {"Item": "US500", "State": "RESEARCH_ONLY"},
        ]
    )
    st.dataframe(rows, hide_index=True, width="stretch")
