# Architecture and Data Flow

```text
User controls (synthetic values)
          |
          v
Input validation (Streamlit widgets)
          |
          v
Digital twin state (current demo profile)
          |
          +------> Synthetic trend generator
          |
          v
Transparent rule checks
          |
          v
Dashboard: metrics, chart, alerts, progress
```

## Components
- **UI:** Streamlit controls and visualizations.
- **State:** current session's widget values; no persistent database.
- **Trend generator:** NumPy creates a synthetic illustrative series.
- **Rules:** explicit if-statements in `app.py`; not medical-grade logic.
- **Deployment:** Streamlit Community Cloud can host the app after the owner pushes it to GitHub.

## Data flow
All current readings originate from manual controls. The heart-rate chart is randomly generated for visual demonstration. No device or external API is contacted.
