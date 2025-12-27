#  Milestone 2: Feature Extraction and Modeling  
**FitPulse – Health Anomaly Detection from Fitness Devices**

---

##  Objective of Milestone 2

Milestone 2 focuses on **deriving meaningful insights from preprocessed fitness datasets** by applying advanced **feature extraction, trend modeling, and behavioral pattern analysis**.  
The outcomes of this milestone establish a strong analytical foundation for **robust anomaly detection** in subsequent stages of the project.

Specifically, this milestone aims to:
- Convert raw time-series sensor data into informative statistical features
- Model temporal and seasonal trends in fitness metrics
- Identify normal and atypical behavioral patterns using unsupervised learning


### Folder Description
- **`data/`**  
  Contains cleaned and preprocessed datasets generated from Milestone 1, including heart rate, step count, and sleep data.

- **`feature_extraction.py`**  
  Script for automated time-series feature extraction using TSFresh and feature selection using variance thresholding.

- **`modeling.py`**  
  Implements trend modeling with Facebook Prophet and unsupervised clustering techniques for behavioral pattern analysis.

- **`requirements.txt`**  
  Lists all Python libraries required to reproduce this milestone.

- **`README.md`**  
  Documentation for Milestone 2, including objectives, methodology, tools, and observations.

---

##  Dataset Description

The datasets used in this milestone originate from **fitness tracking devices** and include the following key metrics:

- **Heart Rate (HR):** Continuous time-series data representing physiological activity
- **Step Count:** Daily or time-window-based physical activity measurements
- **Sleep Duration:** Total sleep time captured per day or session

All datasets are **cleaned, normalized, and timestamp-aligned** during Milestone 1 before being used here.

---

##  Steps Performed

### 1. Feature Extraction
- Applied **TSFresh** to automatically extract time-series features from:
  - Heart rate
  - Step count
  - Sleep duration
- Extracted features include:
  - Mean, variance, standard deviation
  - Skewness and kurtosis
  - Frequency-domain and autocorrelation features
- Performed **feature selection** using:
  - Variance thresholding to remove low-information features

---

### 2️ Trend Modeling
- Used **Facebook Prophet** to model:
  - Long-term trends
  - Daily and weekly seasonality
- Forecasted expected values for:
  - Heart rate
  - Steps
  - Sleep duration
- Computed **residuals/deviations** between observed and predicted values to highlight unusual behavior
- Visualized:
  - Trend lines
  - Confidence intervals
  - Actual vs. predicted values

---

### 3️ Behavioral Pattern Clustering
- Applied **unsupervised clustering** to group similar behavior patterns:
  - **KMeans** for centroid-based clustering
  - **DBSCAN** for density-based anomaly-aware clustering
- Performed **dimensionality reduction** using PCA for visualization
- Identified:
  - Clusters representing normal behavior
  - Sparse or isolated clusters indicating atypical patterns

---

##  Tools and Libraries Used

- **Google Colaboratory** – Experimentation and execution environment
- **Python**
- **Pandas, NumPy** – Data manipulation
- **TSFresh** – Automated time-series feature extraction
- **Facebook Prophet** – Trend and seasonality modeling
- **Scikit-learn** – Clustering and dimensionality reduction
- **Matplotlib, Seaborn** – Visualization

---

##  Key Observations

- TSFresh successfully transformed raw sensor signals into **high-dimensional informative features**
- Prophet captured **clear daily and weekly trends**, especially in step count and sleep duration
- Residual analysis highlighted **behavioral deviations** useful for anomaly detection
- Clustering revealed:
  - Well-defined groups of consistent user behavior
  - Outlier clusters representing irregular or potentially anomalous activity patterns


