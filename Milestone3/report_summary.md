# Milestone 3: Anomaly Detection and Visualization

## Objective
The objective of Milestone 3 is to identify, label, and visualize health-related anomalies from fitness device data. This milestone builds upon the predictive modeling and clustering outcomes from previous milestones to detect abnormal patterns in heart rate and sleep behavior using statistical, rule-based, and cluster-driven techniques.

---

## Steps Followed

### 1. Residual Analysis (Model-Based Detection)
- Time-series forecasting was performed using **Facebook Prophet** models for physiological metrics.
- Residuals were computed as the difference between actual and predicted values.
- Large residual deviations were flagged as potential anomalies, indicating unexpected behavior beyond normal trends.

### 2. Threshold-Based Anomaly Detection
- Domain-specific thresholds were applied to key health metrics:
  - Elevated heart rate beyond safe physiological limits
  - Abnormally low sleep duration indicating fatigue or stress
- Data points violating these thresholds were marked as anomalies.

### 3. Cluster-Based Outlier Detection
- Clustering results obtained in **Milestone 2** were leveraged.
- Small or sparsely populated clusters were treated as outlier clusters.
- Observations belonging to these clusters were classified as anomalous patterns.

### 4. Anomaly Labeling
- Each data point was assigned a clear label (`Normal` / `Anomalous`).
- Labeling ensured distinction between healthy behavioral patterns and abnormal observations.

### 5. Visualization of Anomalies
- Interactive and static time-series visualizations were created.
- Anomalies were highlighted using markers and color differentiation.
- Annotations were added to explain detected abnormal events.

---

## Tools and Technologies Used
- **Python**
- **Google Colaboratory (.ipynb)**
- **Pandas & NumPy** for data manipulation
- **Facebook Prophet** for time-series forecasting
- **Scikit-learn** for clustering and analysis
- **Matplotlib / Plotly** for visualization

---

## Key Insights and Visualizations

### Heart Rate Analysis
- Sudden spikes in heart rate were successfully detected using residual-based and threshold-based methods.
- These anomalies may indicate stress, overexertion, or sensor irregularities.

*Visualization:*  
`visualizations/heart_rate_anomalies.png`

### Sleep Pattern Analysis
- Abnormally low or inconsistent sleep durations were identified.
- Such anomalies may correlate with fatigue, irregular routines, or health risks.

*Visualization:*  
`visualizations/sleep_anomalies.png`

---

## outcomes
Milestone 3 demonstrates a robust anomaly detection pipeline by combining predictive modeling, rule-based thresholds, and clustering-based insights. The integration of clear labeling and visual interpretation enhances explainability and practical usability, laying a strong foundation for real-world health monitoring and alert systems.

---
