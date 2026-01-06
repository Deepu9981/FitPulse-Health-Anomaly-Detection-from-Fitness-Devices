# Milestone 3 – Anomaly Detection & Visualization

##  Objective

The objective of Milestone 3 is to **identify health-related anomalies** from fitness device data by analyzing deviations from normal behavioral patterns.  
This milestone builds on the forecasting models developed earlier and focuses on detecting **unexpected or abnormal trends** in metrics such as heart rate, steps, and sleep using a multi-stage anomaly detection approach.

---

##  Steps Followed

###  Residual Analysis
- Forecasted values were generated using time-series models.
- **Residuals (Actual − Predicted values)** were calculated.
- Large residual magnitudes were treated as potential indicators of abnormal behavior.

###  Threshold-Based Detection
- Domain-specific thresholds were applied to key health metrics:
  - Abnormally high or low heart rate
  - Extremely low activity levels
  - Inconsistent sleep patterns
- Data points exceeding these thresholds were flagged as anomalies.

###  Cluster-Based Detection
- Unsupervised clustering techniques were applied to group similar behavior patterns.
- **Outlier clusters** representing rare or unusual combinations of features were identified as anomalies.
- This helped capture multivariate anomalies not visible through thresholds alone.

###  Visualization
- Time-series plots were used to highlight anomalous points.
- Residual plots clearly showed deviations from normal trends.
- Cluster visualizations helped distinguish normal behavior from anomalous patterns.

---

##  Tools Used

- **Python**
- **Pandas & NumPy** – Data processing and analysis
- **Matplotlib & Seaborn** – Visualization
- **Scikit-learn** – Clustering and anomaly detection
- **Jupyter Notebook** – Experimentation and analysis environment

---

### Key Insights & Visualizations

- Most anomalies were associated with **sudden spikes or drops** in heart rate and activity levels.
- Residual-based analysis effectively captured **temporal anomalies**.
- Thresholding helped detect **domain-critical health violations**.
- Cluster-based detection revealed **hidden multivariate anomalies** missed by individual metric analysis.
- Combined visualization methods improved **interpretability and reliability** of anomaly detection results.

---

##  Outcomes 

By combining **residual analysis, threshold-based rules, clustering techniques, and visual analytics**, this milestone successfully detected meaningful health anomalies from wearable fitness data.  
The approach provides a strong foundation for real-world health monitoring and personalized alert systems.
