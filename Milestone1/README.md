# FitPulse – Health Anomaly Detection from Fitness Devices

##  Overview

FitPulse is a data analytics and machine learning project focused on **detecting health anomalies** using data collected from fitness devices such as smartwatches and fitness bands.  
The system analyzes time-series health data to identify unusual patterns that may indicate abnormal physiological behavior.

This repository contains **Milestone-1**, which focuses on data preprocessing, visualization, and basic anomaly detection.

---

##  Objectives

- Analyze fitness device data
- Preprocess and clean raw health datasets
- Perform exploratory data analysis (EDA)
- Detect anomalies using baseline statistical and ML techniques

---

##  Technologies Used

- **Language:** Python  
- **Libraries:** pandas, NumPy
- **Environment:** Google Colab

---

##  Dataset

The dataset includes time-series fitness data such as:
- Heart rate
- Step count
- Calories burned
- Activity duration
- Timestamped records

(Data stored in CSV format) from kaggle

---

## 📁 Project Structure

The project follows a **well-organized and modular directory structure** to ensure clarity, reproducibility, and ease of future expansion. Each folder is designed to clearly separate data, experimentation, and source code, making the overall workflow systematic and scalable.

The **`Milestone1/`** directory contains all components related to the first phase of the project, which focuses on data understanding, preprocessing, exploratory analysis, and baseline anomaly detection.

### `data/`
This directory stores the dataset obtained from Kaggle. It includes:

- **Raw data:** Original, unmodified CSV files downloaded directly from Kaggle.
- **Processed data:** Cleaned and transformed datasets generated after preprocessing in Google Colab.

Maintaining separate raw and processed datasets ensures data integrity and reproducibility.

### `notebooks/`
This folder contains Jupyter notebooks developed and executed in **Google Colab**. These notebooks document the complete experimental workflow, including:

- Data loading and preprocessing  
- Exploratory Data Analysis (EDA) using visualizations  
- Initial anomaly detection experiments  

The notebooks provide transparency and make the analysis easy to understand and replicate.

### `preprocess_py.ipynb/`
The `src` directory contains modular Python scripts that implement reusable logic for:

- Data preprocessing and normalization  
- Feature engineering for time-series data  
- Anomaly detection techniques  

Separating core logic into scripts keeps notebooks concise and supports scalability in future milestones.

### `requirements.txt`
Lists all Python dependencies required to run the project, allowing the environment to be easily recreated locally or in cloud platforms.

uvicorn
pandas
numpy
aiofiles
streamlit
requests




