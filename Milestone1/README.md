**FitPulse Health Anomaly Detection from Fitness Devices  
Milestone 1: Data Collection and Preprocessing**

**Objective**  
For this milestone, the goal was simple: gather a bunch of fitness tracker data—heart rate, steps, and sleep logs—then clean it up, get everything on the same timeline, and prep it for the real work ahead: spotting health anomalies.

Dataset Source
i pulled from open fitness tracking datasets, which gave us heart rate, step counts, and sleep records. All the raw data came as CSV or JSON files, each with timestamps and numbers coming straight from wearable devices by kaggle.

Some examples:
- Heart rate time series
- Daily activity and step counts
- Sleep durations

Tools and Technologies Used  
- Python
- Google Colab for processing and experiments
- Hugging Face Hub to host and version the project
- Pandas for data wrangling
- NumPy for crunching numbers
- Matplotlib and Seaborn for quick plots and data checks

Steps Performed

1. Data Ingestion  
   uploaded the CSV and JSON files to Colab, wrote scripts to read and validate the different formats, and checked that each dataset had the columns we needed.

2. Timestamp Normalization  
   All timestamps got converted to Pandas datetime, then set to UTC so everything lined up. We tossed any entries with broken or invalid times.

3. Handling Missing and Null Values  
   For gaps in the heart rate data, we used interpolation to fill them in. Sparse stuff, like sleep logs, got forward-filled. By the end, there were no critical missing values left.

4. Time Alignment and Resampling  
    resampled everything—heart rate, steps, sleep—down to clean 1-minute intervals. All data got aggregated and aligned to the same timeline, with proper chronological order.

5. Dataset Consolidation  
   Finally, we merged the prepped heart rate, activity, and sleep data into one tidy, time-series dataset. That went out as the final, ready-to-use file for the next step: anomaly detection.

**Output**  
The end result? A cleaned, normalized dataset with:
- Heart rate values at 1-minute intervals
- Step counts matched up with physiological data
- Sleep metrics woven right into the timeline

Everything’s in order for analysis and building models to find health anomalies.

Key Observations 
- The raw data was messy, with weird timestamps and missing values all over.
- Normalizing the times made a huge difference—suddenly, the data just made sense.
- Resampling was key for lining up different metrics so we could actually compare them.
