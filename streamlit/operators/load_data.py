import pandas as pd
import streamlit as st

@st.cache_data
def load_data(rows, data_source):
    st.text('Loading data')
    data = pd.read_csv(data_source, nrows=rows)
    st.text('Data loaded!')

    return data
