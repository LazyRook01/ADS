import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.style as style
from matplotlib import rcParams
import matplotlib.pyplot as plt
from PIL import Image

# Load the data
df = pd.read_csv("covid.csv")  # Replace with the path to your data file

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract month from 'Date' column
df['Month'] = df['Date'].dt.strftime('%Y-%m')

# Create a Streamlit app
st.title("COVID-19 Data Dashboard")
st.subheader("  Gaurav Ojha | Harsh Jani | Faizan Siddiqi |Gaurav Patil | Jay Bharambe | Mahek Shah")
st.write("This app displays visualizations of COVID-19 data.")

# Sidebar - Selectbox for Page
selected_page = st.sidebar.selectbox('Select Page', ['Visualizations', 'Statistical Tests', 'Documentation'])

# Create a sidebar menu to select visualization type
#visualization_type = st.sidebar.selectbox("Select Visualization Type", options=["Bar Plot","Month-wise Line Plot"])

# Filter the data based on selected countries
#selected_countries = st.sidebar.multiselect("Select countries", df['Country/Region'].unique(), default=("India"))
# Set up Matplotlib style
style.use('ggplot')
rcParams['figure.figsize'] = 15, 10

# Filter the data for the selected countries
#df_selected_countries = df[df['Country/Region'].isin(selected_countries)]

# Page: Visualizations
if selected_page == 'Visualizations':
    # Create a sidebar menu to select visualization type
    visualization_type = st.selectbox("Select Visualization Type", options=["Bar Plot","Month-wise Line Plot"])

    # Filter the data based on selected countries
    selected_countries = st.multiselect("Select countries", df['Country/Region'].unique(), default=("India"))
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

elif selected_page == 'Statistical Tests':
    st.title('COVID-19 Dashboard - Statistical Tests')
    st.header('Select a Statistical Test')
    selected_test=st.selectbox("Which test do you want to run?", options=["Granger's Test","Autocorrelation Test", "ADF (Augmented Dickey Fuller) Test"])

    # Perform Granger's Test
    if selected_test == "Granger's Test":
        st.subheader("Granger's Test")
        # Perform Granger's Test here
        st.write("Perform Granger's Test on the data.")
        st.write("Granger’s Test: Granger&#39;s test, also known as the Granger causality test, is a statistical test used to determine whether one time series can be used to predict another time series. The test is based on the idea that if time series A &quot;Granger- causes&quot; time series B, then past values of A should contain information that helps predict B.")
        # Load image
        image = Image.open("granger.jpeg")  # Replace with the appropriate file path and name for your image

        # Display image using Streamlit
        st.image(image, caption="Granger's Causality", use_column_width=True)

    # Perform Autocorrelation Test
    elif selected_test == "Autocorrelation Test":
        st.subheader("Autocorrelation Test")
        # Perform Autocorrelation Test here
        st.write("Perform Autocorrelation Test on the data.")
        st.write("Autocorrelation Test: It is a statistical test that measures the degree of correlation between a time series and a lagged version of itself. The autocorrelation test is based on the idea that if a time series is serially correlated, then there is some predictable pattern in the relationship between past and future values. The test can be used to determine whether the degree of autocorrelation is statistically significant, and if so, how strong it is.")
        st.write("For our data it is seen that the autocorrelation decreases as the time lag increases (for the confirmed, recovered and deaths column). This suggests that there is a weaker relationship between the current observation and observations further back in time. In other words, the time series may be becoming less dependent on its past values as the time lag increases.")
        # Load image
        image2 = Image.open("acr1.jpeg")  # Replace with the appropriate file path and name for your image
        # Display image using Streamlit
        st.image(image2, caption="Auto-correlation for Confirmed column")

        # Load image
        image3 = Image.open("acr2.jpeg")  # Replace with the appropriate file path and name for your image
        # Display image using Streamlit
        st.image(image3, caption="Auto-correlation for Recovered column")

        # Load image
        image4 = Image.open("acr3.jpeg")  # Replace with the appropriate file path and name for your image
        # Display image using Streamlit
        st.image(image4, caption="Auto-correlation for Deaths column")
    # Perform ADF (Augmented Dickey Fuller) Test
    elif selected_test == "ADF (Augmented Dickey Fuller) Test":
        st.subheader("ADF Test")
        st.write("Perform ADF test on the data.")
        st.write("ADF (Augmented Dickey Fuller) Test: It is a statistical test used to determine whether a time series is stationary or non-stationary.")
        st.write("In a non-stationary time series, the statistical properties (such as mean, variance, etc.) change over time, making it difficult to model or predict future values. In contrast, a stationary time series has constant statistical properties over time, which makes it easier to model and forecast future values. The ADF test is based on the idea that if a time series is non-stationary, it can be transformed into a stationary series by taking the first difference between consecutive observations. The ADF test checks whether this transformation results in a stationary series.")
        st.write("Note that we have tried to make a time series stationary till a lag of 30 days after which we stopped.")
         # Load image
        image5 = Image.open("adf.jpeg")  # Replace with the appropriate file path and name for your image
        # Display image using Streamlit
        st.image(image5, caption="ADF Test")

elif selected_page == 'Documentation':
    st.title("Data Sources")
    st.write("The data has been scraped from following sources:")
    st.write("https://covid19.who.int/") 
    st.write("https://covid19.who.int/region/searo/country/in")
    st.write("https://www.worldometers.info/coronavirus/country/india/")
    st.write("https://www.worldometers.info/coronavirus/")


    st.write("This is a submission towards our ADS project on Covid-19.") 
    st.markdown("**We hereby declare that this is our original work. In case of queries feel reach out to us at:**")
    st.markdown("- Gaurav Ojha : gaurav.ojha008@nmims.edu.in")
    st.markdown("- Faizan Siddiqi: faizan.siddiqi001@nmims.edu.in")
    st.markdown("- Harsh Jani : harsh.jani006@nmims.edu.in")
    st.markdown("- Gaurav Patil : gaurav.patil002@nmims.edu.in")
    st.markdown("- Jay Bharambe : jay.bharambe004@nmims.edu.in")
    st.markdown("- Mahek Shah: mahek.shah015@nmims.edu.in")

    st.caption("The code will be made available shortly at:")


#############################################################################################################################################################
## Displaying raw data 
if st.checkbox("Show Raw Data", False):  ##Creates a checkbow that will display the raw data only if the user checks it
    st.subheader('Raw Data') ## Adds a subheading
    st.write(df) ## Displays the dataset