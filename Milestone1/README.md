# Fitness and Sleep Data Analysis

## Project Overview
This project involves merging and analyzing fitness and sleep tracking data collected from **Fitabase**. The primary goal is to consolidate daily activity, heart rate, and sleep metrics into a single comprehensive dataset, perform data cleaning, and generate initial visualizations to uncover patterns and relationships between physical activity and sleep.

## Data Sources
The analysis uses the following datasets from Fitabase (from 2016-04-12 to 2016-05-12):

- **dailySteps_merged.csv**: Daily step counts for users.
- **heartrate_seconds_merged.csv**: Heart rate data recorded in seconds.
- **hourlySteps_merged.csv**: Hourly step counts.
- **minuteSleep_merged.csv**: Sleep data recorded in minute intervals.
- **sleepDay_merged.csv**: Daily summary of sleep records.

## Analysis Steps

### 1. Data Loading and Standardization
- Each CSV file was loaded into a Pandas DataFrame.
- Date and time columns (`ActivityDay`, `Time`, `ActivityHour`, `date`, `SleepDay`) were converted to datetime objects.
- A consistent `ActivityDate` column (date-only) was created to facilitate merging across datasets.

### 2. Granular Data Aggregation to Daily Level
- **Heart Rate:** Aggregated to calculate `AvgDailyHeartRate` per user per day.
- **Hourly Steps:** Aggregated to calculate `TotalDailyStepsFromHourly` per user per day.
- **Minute-level Sleep:** Aggregated to calculate:
  - `TotalMinutesAsleepFromMinute`
  - `TotalTimeInBedFromMinute` per user per day.

### 3. Data Merging
- All daily-level DataFrames (`daily_steps_df`, `daily_avg_heartrate_df`, `daily_total_steps_from_hourly_df`, `daily_sleep_from_minute_df`, `sleep_day_df`) were merged into a single DataFrame named `merged_df` using an **outer join** on `Id` and `ActivityDate`.

### 4. Handling Missing Values
- NaN values in `AvgDailyHeartRate` were imputed with the **median heart rate**.
- Remaining rows with any NaN values were dropped to ensure a clean, complete dataset for analysis.

### 5. Data Visualization
- **Histograms** to visualize the distribution of daily step totals and average daily heart rate.
- **Scatter plot** to explore the relationship between daily step totals and total minutes asleep.

## Key Findings
- The final cleaned `merged_df` contains **413 entries across 12 columns**, with no missing values.
- Not all metrics (steps, heart rate, and sleep) were available for every participant each day, which reduced the number of rows after cleaning.
- Initial visualizations provide insights into activity and sleep patterns, such as the distribution of daily steps and average heart rates among participants.

## Tools and Libraries
- Python
- Pandas
- Matplotlib  (for visualization)
- NumPy

## Usage
1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```
2. Install required libraries:
    ```bash
    pip install pandas matplotlib seaborn numpy
    ```
3. Run the Google colab Notebook or Python scripts to replicate the analysis and visualizations.

---

