
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