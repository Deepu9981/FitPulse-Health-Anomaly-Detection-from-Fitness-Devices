FitPulse: Health Anomaly Detection
Milestone 1: Data Collection and Preprocessing
Project Overview
FitPulse is a data-driven project focused on detecting health irregularities using wearable device data. This first milestone establishes the foundation: converting messy, raw fitness tracker logs into a clean, synchronized dataset ready for analysis.
Tools Used
Python: Core programming logic.
Pandas & NumPy: Data cleaning, resampling, and mathematical operations.
Matplotlib & Seaborn: Data visualization and quality checks.
Google Colab: Cloud-based development environment.
The Workflow
1. Data Ingestion
Collected raw data in CSV and JSON formats containing heart rate, step counts, and sleep records.
Validated the data structure to ensure all necessary health metrics were present.
2. Timestamp Normalization
Standardized all time formats using Pandas Datetime.
Converted all entries to UTC to ensure that data from different sources (activity vs. sleep) lined up perfectly on the same timeline.
3. Handling Missing Values
Heart Rate: Filled gaps using Linear Interpolation to maintain a smooth physiological curve.
Sleep/Activity: Used Forward-Filling to maintain state consistency (e.g., keeping the user "asleep" until the wake-up log).
4. Resampling and Alignment
Downsampled all data into 1-minute intervals.
This step was critical to compare different types of data—like seeing exactly how heart rate changes during a specific minute of high step activity.
5. Dataset Consolidation
Merged all separate files into one Master Time-Series Dataset.
The final output provides a minute-by-minute view of a user's health metrics.
Key Observations
Data Quality: Raw wearable data is inherently "noisy" with broken timestamps and gaps; normalization is the most important step for accuracy.
Synchronization: Converting everything to a single timeline (UTC) immediately resolved conflicts between activity logs and sleep logs.
Model Ready: By resampling to 1-minute intervals, the data is now structured perfectly for Machine Learning models like Isolation Forests or LSTMs.
Output
The result of this milestone is a cleaned, unified CSV file containing:
Synchronized Heart Rate (BPM)
Aggregated Step Counts
Categorized Sleep States
