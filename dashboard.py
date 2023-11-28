
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('PRSA_Data_Wanshouxigong_20130301-20170228.csv')

# Title of the dashboard
st.title('Air Quality Analysis Dashboard: Wanshouxigong Station')


# Description
st.write('This dashboard provides an interactive way to explore air quality data, specifically focusing on PM2.5 levels and their relationship with various weather conditions.')

# Adding a sidebar for interactive inputs
st.sidebar.header('User Input Features')

# Let users select a year and month to view data
selected_year = st.sidebar.selectbox('Select Year', list(data['year'].unique()))
selected_month = st.sidebar.selectbox('Select Month', list(data['month'].unique()))

# Filter data based on the selected year and month
data_filtered = data[(data['year'] == selected_year) & (data['month'] == selected_month)]

# Displaying data statistics
st.subheader('Data Overview for Selected Period')
st.write(data_filtered.describe())

# Line chart for PM2.5 levels over selected month
st.subheader('Daily PM2.5 Levels')
fig, ax = plt.subplots()
ax.plot(data_filtered['day'], data_filtered['PM2.5'])
plt.xlabel('Day of the Month')
plt.ylabel('PM2.5 Concentration')
st.pyplot(fig)

# Correlation heatmap for the selected month
st.subheader('Correlation Heatmap of Air Quality Indicators')
corr = data_filtered[['PM2.5', 'NO2', 'SO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
plt.title('Correlation Heatmap')
st.pyplot(fig)

# Seasonal Trend Analysis
st.subheader('Seasonal Trend Analysis')
seasonal_trends = data.groupby('month')['PM2.5'].mean()
fig, ax = plt.subplots()
seasonal_trends.plot(kind='bar', color='skyblue', ax=ax)
plt.title('Average Monthly PM2.5 Levels')
plt.xlabel('Month')
plt.ylabel('Average PM2.5')
st.pyplot(fig)

To create a detailed and comprehensive Streamlit dashboard that aligns with your assignment requirements and aims for a 5-star rating, we should focus on making the dashboard interactive, insightful, and user-friendly, while avoiding machine learning techniques as per the assignment's guidelines. Here's an expanded and detailed guide for your dashboard:
Expanded Streamlit Dashboard Script

python

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_csv('path_to_your_dataset.csv')

# Title of the dashboard
st.title('Air Quality Analysis Dashboard: Wanshouxigong Station')

# Description
st.write('This dashboard provides an interactive way to explore air quality data, specifically focusing on PM2.5 levels and their relationship with various weather conditions.')

# Adding a sidebar for interactive inputs
st.sidebar.header('User Input Features')

# Let users select a year and month to view data
selected_year = st.sidebar.selectbox('Select Year', list(data['year'].unique()))
selected_month = st.sidebar.selectbox('Select Month', list(data['month'].unique()))

# Filter data based on the selected year and month
data_filtered = data[(data['year'] == selected_year) & (data['month'] == selected_month)]

# Displaying data statistics
st.subheader('Data Overview for Selected Period')
st.write(data_filtered.describe())

# Line chart for PM2.5 levels over selected month
st.subheader('Daily PM2.5 Levels')
fig, ax = plt.subplots()
ax.plot(data_filtered['day'], data_filtered['PM2.5'])
plt.xlabel('Day of the Month')
plt.ylabel('PM2.5 Concentration')
st.pyplot(fig)

# Correlation heatmap for the selected month
st.subheader('Correlation Heatmap of Air Quality Indicators')
corr = data_filtered[['PM2.5', 'NO2', 'SO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
plt.title('Correlation Heatmap')
st.pyplot(fig)

# Seasonal Trend Analysis
st.subheader('Seasonal Trend Analysis')
seasonal_trends = data.groupby('month')['PM2.5'].mean()
fig, ax = plt.subplots()
seasonal_trends.plot(kind='bar', color='skyblue', ax=ax)
plt.title('Average Monthly PM2.5 Levels')
plt.xlabel('Month')
plt.ylabel('Average PM2.5')
st.pyplot(fig)

# Daily PM2.5 Levels
st.subheader('Daily PM2.5 Levels')
fig, ax = plt.subplots()
ax.plot(data_filtered['day'], data_filtered['PM2.5'])
plt.xlabel('Day of the Month')
plt.ylabel('PM2.5 Concentration')
st.pyplot(fig)

# Pollutant Distribution
st.subheader('Pollutant Distribution')
selected_pollutant = st.selectbox('Select Pollutant', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO'])
fig, ax = plt.subplots()
sns.boxplot(x='month', y=selected_pollutant, data=data[data['year'] == selected_year], ax=ax)
st.pyplot(fig)

# Time Series Decomposition
st.subheader('Time Series Decomposition of PM2.5')
decomposed = seasonal_decompose(data_filtered['PM2.5'], model='additive', period=24)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
decomposed.trend.plot(ax=ax1, title='Trend')
decomposed.seasonal.plot(ax=ax2, title='Seasonality')
decomposed.resid.plot(ax=ax3, title='Residuals')
plt.tight_layout()
st.pyplot(fig)

# Hourly Averages Heatmap
st.subheader('Hourly Averages of PM2.5')
hourly_avg = data.groupby(['hour']).mean()['PM2.5']
fig, ax = plt.subplots()
sns.heatmap([hourly_avg.values], ax=ax, cmap='coolwarm')
plt.title('Hourly Averages of PM2.5')
st.pyplot(fig)

# Wind Direction Analysis
st.subheader('Wind Direction Analysis')
wind_data = data_filtered.groupby('wd')['PM2.5'].mean()
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)
theta = np.linspace(0, 2 * np.pi, len(wind_data))
bars = ax.bar(theta, wind_data.values, align='center', alpha=0.5)
plt.title('PM2.5 Levels by Wind Direction')
st.pyplot(fig)

# Rainfall vs. Air Quality
st.subheader('Rainfall vs. PM2.5 Levels')
fig, ax = plt.subplots()
sns.scatterplot(x='RAIN', y='PM2.5', data=data_filtered, ax=ax)
plt.title('Rainfall vs. PM2.5 Levels')
st.pyplot(fig)

# Correlation Heatmap - Interactive
st.subheader('Interactive Correlation Heatmap')
selected_columns = st.multiselect('Select Columns for Correlation', data.columns, default=['PM2.5', 'NO2', 'TEMP', 'PRES', 'DEWP'])
corr = data[selected_columns].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
st.pyplot(fig)




# Conclusion
st.subheader('Conclusion')
st.write("""
- The dashboard provides an in-depth and interactive analysis of air quality data.
- Various visualizations offer insights into PM2.5 levels, their distribution, and factors affecting them.
- Seasonal trends and the impact of different weather conditions and pollutants on air quality are clearly depicted.
- Users can explore the data dynamically to gain a deeper understanding of air quality trends.
""")