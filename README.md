# HealthTwin — Health Digital Twin Proof of Concept

A small, interactive healthcare-themed Digital Twin prototype for demonstrating the core loop:
**simulated inputs → digital representation → rule-based insights → visual dashboard**.

> **Safety notice:** This is an educational prototype using synthetic data. It is not a medical device and must not be used to diagnose, treat, or make clinical decisions.

## Features
- Adjustable simulated heart rate, blood pressure, SpO₂, sleep and steps
- Dashboard metrics and a generated heart-rate trend
- Transparent rule-based demo alerts
- Activity/sleep progress indicators
- Explicit privacy and limitations panel

## Run locally
Requires Python 3.10+.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The app opens in your browser, usually at `http://localhost:8501`.

## Deploy
### Streamlit Community Cloud
1. Push this repository to your GitHub account.
2. Sign in to Streamlit Community Cloud.
3. Choose **Create app**, select your repository and branch.
4. Set the main file path to `app.py`, then deploy.

## Architecture
1. **Input layer:** sidebar controls provide synthetic readings.
2. **Twin state:** the current readings represent the demo person's current state.
3. **Rules engine:** simple, visible threshold checks produce explanatory alerts.
4. **Presentation layer:** Streamlit metrics, charts and progress indicators.

## Suggested repository contents
- `app.py` — application
- `requirements.txt` — dependencies
- `README.md` — setup, features and limitations
- `docs/PROJECT_REPORT.md` — project documentation
- `docs/ARCHITECTURE.md` — architecture and data flow
- `docs/TEST_PLAN.md` — test cases

## Important submission checklist
This starter PoC is **not automatically submitted** to Happiest Health. Before submitting:
- Read the official challenge brief and required submission format.
- Replace team placeholders and add team/member details only where required.
- Test the app and capture screenshots.
- Add a short demo video if required by the official guidelines.
- Confirm whether the challenge expects a different Digital Twin domain, hardware/IoT integration, real datasets, or specific deliverables.
- Do not upload identifiable health information or secrets.
