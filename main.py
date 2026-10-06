import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

    st.title('INDIAs AQI OVERVIEW')
    overview_option = st.sidebar.selectbox('Select Overview',['Average AQI','Best Cities','Worst Cities','Monthly Trend'])

    btn1 = st.sidebar.button('Check Overview')

    if btn1:
        st.session_state.overview_selected = overview_option

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

