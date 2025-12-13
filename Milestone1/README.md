# FitPulse Health Anomaly Detection from Fitness Devices
## Milestone 1: Data Collection and Preprocessing

---

## Objective
The objective of this milestone is to collect, clean, normalize, and preprocess fitness device data
(heart rate, steps, and sleep logs) to generate a unified, time-aligned dataset suitable for
subsequent health anomaly detection and analysis.

---

## Dataset Source
Open fitness tracking datasets were used for this milestone, consisting of heart rate, activity
(step count), and sleep records.  
The data was collected in CSV/JSON format and includes timestamped physiological and activity metrics
generated from wearable fitness devices.

Dataset examples include:
- Heart rate time-series data
- Daily activity and step count logs
- Sleep duration records

---

## Tools and Technologies Used
- **Python**
- **Google Colaboratory** (data processing and experimentation)
- **Hugging Face Hub** (project hosting and version control)
- **Pandas** (data ingestion, cleaning, preprocessing)
- **NumPy** (numerical operations)
- **Matplotlib / Seaborn** (visualization for analysis)

---

## Steps Performed

### 1. Data Ingestion
- Uploaded CSV and JSON fitness datasets into Google Colab
- Implemented ingestion logic to read and validate multiple data sources
- Verified schema consistency and required columns for each dataset

### 2. Timestamp Normalization
- Converted all timestamp columns to Pandas datetime format
- Normalized timestamps to **UTC** to ensure consistency across datasets
- Removed invalid or corrupted timestamp entries

### 3. Handling Missing and Null Values
- Applied interpolation techniques for continuous metrics such as heart rate
- Used forward-fill strategies for sparse datasets such as sleep logs
- Ensured no critical null values remained after preprocessing

### 4. Time Alignment and Resampling
- Resampled heart rate, steps, and sleep data to a consistent **1-minute interval**
- Aggregated and aligned all metrics to a common time index
- Ensured chronological ordering of records

### 5. Dataset Consolidation
- Merged preprocessed heart rate, activity, and sleep datasets
- Generated a clean, consolidated time-series dataset
- Exported the final dataset for downstream anomaly detection tasks

---

## Output
The final output is a cleaned and normalized dataset containing:
- Heart rate values aligned to 1-minute intervals
- Step counts synchronized with physiological data
- Sleep duration metrics integrated into the time series

This dataset is structured and ready for exploratory analysis and anomaly detection modeling.

---

## Key Observations
- Raw fitness data contained irregular timestamps and missing values
- Time normalization significantly improved data consistency
- Resampling enabled meaningful comparison across multiple health metrics

---

## Repository Structure
