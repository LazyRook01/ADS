import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.style as style
from matplotlib import rcParams
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("covid.csv")  # Replace with the path to your data file

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract month from 'Date' column
df['Month'] = df['Date'].dt.strftime('%Y-%m')

# Create a Streamlit app
st.title("COVID-19 Data Dashboard")
st.subheader("Harsh Jani | Faizan Siddiqi | Gaurav Ojha | Gaurav Patil | Jay Bharambe | Mahek Shah")
st.write("This app displays visualizations of COVID-19 data.")

# Create a sidebar menu to select visualization type
visualization_type = st.sidebar.selectbox("Select Visualization Type", options=["Bar Plot","Month-wise Line Plot"])

# Filter the data based on selected countries
selected_countries = st.sidebar.multiselect("Select countries", df['Country/Region'].unique(), default=("India"))
# Set up Matplotlib style
style.use('ggplot')
rcParams['figure.figsize'] = 15, 10

# Filter the data for the selected countries
df_selected_countries = df[df['Country/Region'].isin(selected_countries)]

# Generate the selected visualization
if visualization_type == "Bar Plot":
    # Create the bar plot
    ax = sns.barplot(x='Country/Region', hue="variable", y="value", data=pd.melt(df_selected_countries, id_vars=['Country/Region'], value_vars=['Confirmed', 'Deaths', 'Recovered']))
    ax.set_xlabel('Country/Region')
    ax.set_ylabel('Cases')
    ax.set_title('COVID-19 Cases by Country/Region (Bar Plot)')
    ax.legend(title='Type', loc='upper right')
    # Display the bar plot in Streamlit
    st.pyplot(ax.figure)
elif visualization_type == "Month-wise Line Plot":
    # Create the month-wise line plot
    ax = sns.lineplot(x='Month', hue="Country/Region", y="Confirmed", data=df_selected_countries)
    ax.set_xlabel('Month')
    ax.set_ylabel('Confirmed Cases')
    ax.set_title('COVID-19 Confirmed Cases by Month and Country/Region (Line Plot)')
    ax.legend(title='Country/Region', loc='upper left')
    # Display the line plot in Streamlit
    st.pyplot(ax.figure)
