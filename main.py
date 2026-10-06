import streamlit as st
import pandas as pd
import page.State_Analysis
from data import load_data
import page.overview


aqi = load_data()

country_avg_aqi = round(aqi['aqi_value'].mean(),2)


if 'overview_selected' not in st.session_state:
    st.session_state.overview_selected = None


st.sidebar.title('AQI Analysis')

options = st.sidebar.selectbox('Select One',['Overview','State Analysis'])


if options=='Overview':

    st.markdown("""# 🇮🇳 India AQI Dashboard
## About the Project

This interactive dashboard provides an overview of **Air Quality Index (AQI) across India** using AQI data collected for the period **2022–2025**.

The dataset was obtained from **Kaggle** and further cleaned, transformed, and analyzed to make it suitable for meaningful visualization and exploration.

## What can you explore?

📊 **Overview**

Get a quick snapshot of India's air quality, including average AQI, best and worst-performing areas, and monthly AQI trends.

🗺️ **State Analysis**

Explore AQI across different states and compare their minimum, maximum, and average AQI, along with the best and worst-performing areas.

## Purpose

The goal of this project is to transform raw AQI data into an **interactive and easy-to-understand analytical dashboard**, allowing users to explore air-quality patterns across different locations and time periods.

> **Note:** This project is created for learning and data-analysis purposes. The dashboard and its insights may be improved further as the project evolves.
""")
    
    overview_option = st.sidebar.selectbox('Select Overview',['Average AQI','Best Cities','Worst Cities','Monthly Trend'])

    btn1 = st.sidebar.button('Check Overview')

    if btn1:

        st.session_state.overview_selected = overview_option
        st.title('INDIAs AQI OVERVIEW')

    if st.session_state.overview_selected == 'Average AQI':
        page.overview.load_overview()

    if st.session_state.overview_selected == 'Best Cities':
            st.subheader('CITY WISE ANALYSIS')
            page.overview.load_best_cities()
    if st.session_state.overview_selected == 'Worst Cities':
            st.subheader('CITY WISE ANALYSIS')
            page.overview.load_worst_cities()
    if st.session_state.overview_selected == 'Monthly Trend':
            st.subheader('MONTH WISE ANALYSIS')
            page.overview.load_month_wise()




    #st.session_state.clear()


elif options=='State Analysis':

    selected_state = st.sidebar.selectbox(
        'Select State',
        sorted(aqi['state'].unique().tolist())
    )

    btn2 = st.sidebar.button('Analyse State')

    if btn2:

       st.title(f"{selected_state} Analysis")

       page.State_Analysis.load_state(selected_state)

