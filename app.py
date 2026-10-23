import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="HealthTwin | Digital Twin PoC", page_icon="🫀", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1.5rem; padding-bottom: 2rem;}
.metric-card {border:1px solid #243447; border-radius:14px; padding:16px; background:#111c2b;}
.small-muted {color:#9caec2; font-size:0.9rem;}
</style>
""", unsafe_allow_html=True)

st.title("🫀 HealthTwin")
st.caption("Personal Health Digital Twin • Proof of Concept • Simulated data only")
st.warning("Educational prototype only. It does not diagnose, treat, or replace advice from a qualified healthcare professional.")

with st.sidebar:
    st.header("Twin configuration")
    profile = st.text_input("Demo profile name", "Demo Patient")
    age = st.slider("Age (demo)", 18, 90, 32)
    activity = st.selectbox("Activity level", ["Low", "Moderate", "High"], index=1)
    st.divider()
    st.subheader("Simulate current readings")
    heart_rate = st.slider("Heart rate (BPM)", 45, 150, 76)
    systolic = st.slider("Systolic BP (mmHg)", 80, 200, 118)
    diastolic = st.slider("Diastolic BP (mmHg)", 45, 130, 77)
    spo2 = st.slider("SpO₂ (%)", 80, 100, 98)
    sleep = st.slider("Sleep last night (hours)", 0.0, 12.0, 7.5, 0.5)
    steps = st.slider("Steps today", 0, 25000, 6800, 500)

# Transparent, illustrative status rules — not clinical decision rules.
alerts = []
if heart_rate < 50 or heart_rate > 120: alerts.append("Heart-rate reading is outside this demo's usual range.")
if systolic >= 140 or diastolic >= 90: alerts.append("Blood-pressure reading is elevated in this demo. Consider rechecking and consulting a clinician.")
if spo2 < 92: alerts.append("SpO₂ reading is low in this demo. If this is a real reading or you feel unwell, seek prompt medical advice.")
if sleep < 6: alerts.append("Sleep duration is below 6 hours.")
if steps < 3000: alerts.append("Activity is below the demo's daily movement target.")

st.subheader(f"Digital twin overview — {profile}")
c1,c2,c3,c4 = st.columns(4)
c1.metric("Heart rate", f"{heart_rate} BPM", "Simulated")
c2.metric("Blood pressure", f"{systolic}/{diastolic}", "mmHg")
c3.metric("Blood oxygen", f"{spo2}%", "SpO₂")
c4.metric("Sleep", f"{sleep:g} h", "Last night")

left, right = st.columns([1.4,1])
with left:
    st.subheader("Twin state & recent trend")
    rng = np.random.default_rng(21)
    times = [datetime.now() - timedelta(hours=23-i) for i in range(24)]
    hr_series = np.clip(heart_rate + rng.normal(0, 5, 24), 48, 130).round().astype(int)
    df = pd.DataFrame({"Time": times, "Heart rate (BPM)": hr_series})
    df = pd.concat([df, pd.DataFrame({"Time":[datetime.now()], "Heart rate (BPM)":[heart_rate]})], ignore_index=True)
    st.line_chart(df.set_index("Time"))
    st.caption("Trend is generated for demonstration and is not collected from a wearable or medical device.")
with right:
    st.subheader("Rule-based insights")
    if alerts:
        for a in alerts:
            st.warning(a)
    else:
        st.success("No demo rules were triggered by the current simulated readings.")
    st.markdown("**Activity context**")
    st.progress(min(steps / 10000, 1.0), text=f"{steps:,} / 10,000 demo steps")
    st.progress(min(sleep / 8, 1.0), text=f"{sleep:g} / 8 hours sleep target")
    st.caption(f"Profile context: age {age} • activity level: {activity}")

st.subheader("How the digital twin works")
flow = st.columns(4)
for col, n, title, desc in [
    (flow[0],"01","Input","User-controlled simulated vitals"),
    (flow[1],"02","Twin state","Current digital representation"),
    (flow[2],"03","Rules engine","Transparent threshold checks"),
    (flow[3],"04","Dashboard","Trends, status and explanations")]:
    with col:
        st.markdown(f"### {n} · {title}")
        st.write(desc)

with st.expander("Data, privacy & limitations"):
    st.write("This PoC uses synthetic/demo readings entered in the sidebar. It does not connect to a patient record, wearable, hospital system, or external service. No database is configured. Thresholds are illustrative software rules, not validated medical guidance.")
    st.write("For real-world use, add consent, authentication, encryption, audit logging, validated clinical logic, clinician oversight, and formal privacy/security review.")

st.caption("HealthTwin PoC • Built for demonstration • Do not use for medical decisions")
