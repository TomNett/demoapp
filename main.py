# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load RFM data
@st.cache
def load_data():
    return pd.read_csv("rfm_sample_data.csv")

data = load_data()

# App title
st.title('RFM Analysis Visualization')

# Displaying the dataframe
st.dataframe(data)

# Plot RFM analysis
fig = px.scatter_3d(data, x='Recency', y='Frequency', z='Monetary', 
                    color='Segment', size_max=18, opacity=0.7)

# Show the plot
st.plotly_chart(fig)
