# Air Quality Analysis Project: Wanshouxigong Station

## Live Dashboard
https://maliki-airquality.streamlit.app/

## Project Overview
This project, submitted for the "Learn Data Analysis with Python" course from Dicoding, focuses on analyzing air quality data, particularly PM2.5 levels, from the Wanshouxigong station. The objective is to uncover trends, seasonal variations, and the impact of different weather conditions on air quality.

## Course Submission
This analysis serves as a course submission for "Learn Data Analysis with Python" offered by Dicoding. It demonstrates the application of data analysis techniques and visualization skills learned in the course.

## Table of Contents
- [Introduction](#introduction)
- [Data Source](#data-source)
- [Libraries Used](#libraries-used)
- [Key Insights](#key-insights)
- [How to Run the Dashboard](#how-to-run-the-dashboard)
- [About Me](#about-me)

## Introduction
The goal of this project is to analyze air quality data, specifically PM2.5 pollutant levels, and understand their relationship with various environmental factors. The analysis includes identifying trends, seasonal patterns, and correlations with weather conditions.

## Data Source
The dataset used in this project includes air quality measurements from the Wanshouxigong station, with a focus on PM2.5 levels and other related environmental data.

## Libraries Used
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- Statsmodels

## Key Insights
- Seasonal variation in PM2.5 levels with higher concentrations in colder months.
- Correlation between PM2.5 levels and weather conditions like temperature and humidity.
- Trends and patterns revealed through time series analysis.

## How to Run the Dashboard

To run the Air Quality Analysis Dashboard, follow these steps:

### Setup Environment

1. **Create and Activate a Python Environment**:
   - If using Conda (ensure [Conda](https://docs.conda.io/en/latest/) is installed):
     ```
     conda create --name airquality-ds python=3.9
     conda activate airquality-ds
     ```
   - If using venv (standard Python environment tool):
     ```
     python -m venv airquality-ds
     source airquality-ds/bin/activate  # On Windows use `airquality-ds\Scripts\activate`
     ```

2. **Install Required Packages**:
   - The following packages are necessary for running the analysis and the dashboard:
     ```
     pip install pandas numpy scipy matplotlib seaborn streamlit statsmodels
     ```

     or you can do
     ```
     pip install -r requirements.txt
     ```
### Run the Streamlit App

1. **Navigate to the Project Directory** where `dashboard.py` is located.

2. **Run the Streamlit App**:
    ```
    streamlit run dashboard.py
    ```

### Additional Files

- The dataset used for this analysis is included in the project repository.
- A detailed Python notebook (`maliki-dicoding-ds-airquality.ipynb`) containing the data analysis and visualizations is also provided.
---
### P.S.

Since Dicoding recommended creating the good and tidy folder structures, as `dashboard.py` in `dashboard` folder, then the deployment for Streamlit App affected.
That was why I put the `requirements.txt` in the `dashboard` folder as well.  

---

## About Me
- **Name**: Reza Maliki Akbar
- **Email Address**: rezamaliki.akbar@gmail.com
- **Dicoding ID**: [maliki_borneo](https://www.dicoding.com/users/maliki_borneo/)

---
Find also the Python Notebook in here
[Kaggle - maliki_borneo - Air Quality](https://www.kaggle.com/malikiborneo/maliki-dicoding-ds-airquality)
