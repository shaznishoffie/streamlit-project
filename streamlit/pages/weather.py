import streamlit as st
import pandas as pd
import datetime

st.title("Weather Updates")

# Get data
data = pd.read_csv('open_meteo_data/data.csv')

# get current time
current_time = datetime.datetime.now()
current_day = st.date_input("Select date", datetime.date.today())

data['report_datetime'] = pd.to_datetime(data['date'])
data['report_date'] = data['report_datetime'].dt.strftime('%Y-%m-%d')
data['report_hour'] = data['report_datetime'].dt.strftime('%H')

filtered_data = data[(data['report_date']==str(current_day)) & (data['report_hour']==str(current_time.hour))]
filtered_data = filtered_data[[
    "report_date", 
    "report_hour",
    "latitude",
    "longitude",
    "precipitation_probability",
    "precipitation",
    "temperature_2m"
]]

# create a map


# show data as table
st.data_editor(
    filtered_data,
    column_config={
        "precipitation_probability": st.column_config.ProgressColumn(
            "Precipitation Probability %",
            help="Probability of rain",
            format="%f",
            min_value=0,
            max_value=100,
        ),
    },
    hide_index=True,
)
