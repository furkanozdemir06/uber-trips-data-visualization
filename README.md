# 🚕 Uber Trips Visualization & EDA — New York City

A Python data analysis and visualization project that explores **Uber pickup activity in New York City during September 2014**.

The project combines a **Jupyter Notebook for exploratory data analysis (EDA)** with an **interactive Streamlit dashboard** for exploring trip patterns, pickup locations, Uber bases, and time-based demand.

## 📌 Project Overview

The main goal of this project is to analyze Uber trip data and identify meaningful patterns in urban mobility. Using timestamps, geographic coordinates, and Uber base information, the project explores how ride demand changes by **hour, day, weekday, location, and base**.

The analysis focuses on questions such as:

- What are the busiest hours for Uber pickups?
- Which days of the week have the highest trip volume?
- Where are the main pickup hotspots in New York City?
- How does demand vary between weekdays and weekends?
- Which Uber bases handle the most trips?
- How do location and time interact in NYC ride activity?

## 📊 Dataset

The project uses the file:

```text
uber-raw-data-sep14.csv
```

The dataset contains **1,028,136 Uber pickup records** from September 2014 with the following original columns:

| Column | Description |
|---|---|
| `Date/Time` | Date and time of the Uber pickup |
| `Lat` | Pickup latitude |
| `Lon` | Pickup longitude |
| `Base` | Uber base code associated with the trip |

Additional time-based features are created during the analysis, including `Hour`, `Day`, `Month`, `Year`, `DayOfWeek`, and `Weekday`.

> The CSV file must be placed in the project root directory before running the notebook or Streamlit application.

## 🔎 Exploratory Data Analysis

The Jupyter Notebook (`UBER.ipynb`) includes:

- Dataset inspection and summary statistics
- Missing-value checks
- Datetime conversion and feature engineering
- Trips by hour
- Trips by weekday
- Weekday vs. hour heatmap
- Daily trip distribution
- Geographic pickup hotspot visualization
- Trip distribution by Uber base
- Top pickup coordinate areas
- Weekday vs. weekend comparison
- Interactive 3D visualization of longitude, latitude, and hour

## 🖥️ Streamlit Dashboard

The project also includes an interactive Streamlit application (`uber.py`).

### Dashboard Features

- Filter trips by **Uber base**
- Filter trips by **day of the month**
- Display total number of filtered trips
- Identify the busiest hour
- Identify the busiest weekday
- Visualize trips by hour and weekday
- Explore a weekday/hour demand heatmap
- View daily trip volume
- Explore pickup locations on an interactive map
- Display the top 10 pickup coordinate areas
- Compare trip volume across Uber bases
- Compare weekday and weekend ride share
- Preview the filtered dataset

The dashboard is organized into four sections:

1. **Time Patterns**
2. **Locations**
3. **Bases**
4. **Data**

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

## 📁 Project Structure

```text
uber-trips-analysis/
│
├── UBER.ipynb
├── uber.py
├── uber-raw-data-sep14.csv
└── README.md
```

## ⚙️ Installation

Clone or download the project, open a terminal in the project directory, and install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn plotly streamlit jupyter
```

Make sure `uber-raw-data-sep14.csv` is located in the same directory as `uber.py` and `UBER.ipynb`.

## 🚀 Running the Project

### Run the Streamlit Dashboard

```bash
streamlit run uber.py
```

Streamlit will start a local web server and open the interactive dashboard in your browser.

### Run the Jupyter Notebook

```bash
jupyter notebook UBER.ipynb
```

You can then execute the notebook cells to reproduce the exploratory analysis and visualizations.

## 📈 Main Analysis Areas

### Temporal Analysis

Trip timestamps are transformed into useful time features to analyze demand across hours, weekdays, and individual days of the month.

### Geographic Analysis

Latitude and longitude values are used to visualize NYC pickup activity and identify high-frequency pickup areas.

### Uber Base Analysis

Trips are grouped by base code to compare the activity handled by different Uber bases.

### Interactive Visualization

Plotly and Streamlit are used to turn the exploratory analysis into an interactive dashboard where users can filter and explore the data dynamically.

## 💡 Possible Future Improvements

- Add data from additional months for long-term trend analysis
- Add borough or neighborhood names using geographic mapping
- Add machine-learning models for trip-demand prediction
- Deploy the Streamlit dashboard online
- Add additional map visualizations and clustering
- Add automated data-cleaning and preprocessing pipelines

## 🎯 Project Purpose

This project demonstrates practical skills in:

- Exploratory Data Analysis (EDA)
- Data cleaning and feature engineering
- Time-based demand analysis
- Geographic data visualization
- Interactive dashboard development
- Communicating data insights visually

---

Built with Python to explore Uber mobility patterns in New York City. 🚕📊
