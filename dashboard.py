
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_csv('PRSA_Data_Wanshouxigong_20130301-20170228.csv')

# Title of the dashboard
st.title('Air Quality Analysis Dashboard: Wanshouxigong Station')