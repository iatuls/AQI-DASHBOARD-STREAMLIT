import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



aqi = pd.read_csv('AQI_cleaned.csv')
#data Cleaning
aqi['Date'] = pd.to_datetime(aqi['Date'])
aqi['Month'] = aqi['Date'].dt.month_name()


country_avg_aqi = round(aqi['aqi_value'].mean(),2)


def aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif 50 < aqi <= 100:       
        return "Satisfactory"
    elif 100 < aqi <= 200:     
        return "Moderately Polluted"
    elif 200 < aqi <= 300:     
        return "Poor"
    elif 300 < aqi <= 400:     
        return "Very Poor"
    else:
        return "Severe"


def load_state(state):
  state_data = aqi.groupby(['state','area'])['aqi_value'].mean().reset_index().sort_values(by='aqi_value',ascending=False)
  state_data = state_data[state_data['state']==state]
  state_air_quality = aqi.groupby('state')['air_quality_status'].value_counts().reset_index()
  state_air_quality = state_air_quality[state_air_quality['state']=='Andaman and Nicobar Islands']
  Avg_AQI = round(state_data[state_data['state']==state]['aqi_value'].mean(),2)


  #col1, col2, col3, col4 = st.columns(4)
  #ol1, col2, col3, col4 = st.columns([1.2, 3, 3, 1])
  a, b = st.columns(2)
  c, d = st.columns(2)
  e, f = st.columns(2)
  a.metric("Average AQI", Avg_AQI, border=True, delta=aqi_category(Avg_AQI))
  b.metric("Total Areas", state_data.shape[0], border=True)
  c.metric("Most Polluted", state_data.iloc[0, 1], border=True, delta=f'AQI ={int(state_data[state_data['area']==state_data.iloc[0, 1]].iloc[0,2])}')
  d.metric("Least Polluted", state_data.iloc[-1, 1], border=True, delta=f'AQI ={int(state_data[state_data['area']==state_data.iloc[-1, 1]].iloc[0,2])}')

  df2 = state_data[state_data['state']==state].head()
  if df2.shape[0] >=1:
    st.bar_chart(data=df2, x='area', y='aqi_value', color="#0080FF")
    st.subheader(f"Upto Top 5 Worst areas of {state}")
    st.dataframe(state_data.head(),hide_index=True)
    st.subheader("Number of Areas by AQI Category")
    st.bar_chart(state_air_quality,x='air_quality_status',y='count')
    st.header(f"{state} VS Country's Avg AQI Comparison")
  x,y = st.columns(2)
  x.metric("Country's Avg AQI",country_avg_aqi, border=True,delta=aqi_category(country_avg_aqi))
  y.metric(f"Avg AQI of {state}",Avg_AQI, border=True,delta=aqi_category(Avg_AQI))





