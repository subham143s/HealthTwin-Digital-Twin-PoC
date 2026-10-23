# Test Plan

| ID | Scenario | Action | Expected result |
|---|---|---|---|
| T01 | Normal demo values | Keep defaults | Dashboard metrics display; no demo alert for default heart rate/BP/SpO₂/sleep |
| T02 | High heart rate | Set heart rate to 130 BPM | Heart-rate demo warning appears |
| T03 | Elevated BP | Set systolic to 150 mmHg | BP demo warning appears |
| T04 | Low SpO₂ simulation | Set SpO₂ to 90% | Low SpO₂ demo warning appears with safety wording |
| T05 | Short sleep | Set sleep to 4 hours | Sleep-duration warning appears |
| T06 | Low activity | Set steps to 1,000 | Activity warning appears |
| T07 | Chart rendering | Change heart rate | Trend chart and metric render without error |
| T08 | Safety disclosure | Open app | Educational prototype disclaimer is visible |

## Manual acceptance checklist
- [ ] App starts with `streamlit run app.py`.
- [ ] Sidebar controls update metrics.
- [ ] Trend chart is visible.
- [ ] Rule messages respond to inputs.
- [ ] All data is clearly described as synthetic.
- [ ] No personal health data or secrets are committed.
