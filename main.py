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
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"

#Loading State Details
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
  a.metric("Average AQI", Avg_AQI, border=True)
  b.metric("Total Areas", state_data.shape[0], border=True)
  c.metric("Most Polluted", state_data.iloc[0, 1], border=True)
  d.metric("Least Polluted", state_data.iloc[-1, 1], border=True)
  e.metric("AQI Category", aqi_category(Avg_AQI), border=True)

  df2 = state_data[state_data['state']==state].head()
  if df2.shape[0] >=1:

    plt.bar(df2['area'], df2['aqi_value'])
    plt.xlabel('Area')
    plt.title(f"Top polluted Cities in {state}")
    plt.ylabel("AQI Value")
    plt.xticks(rotation=90)
    plt.tight_layout()

    st.pyplot(plt)
    #Top 5 rows
    st.subheader(f"Upto Top 5 Rows of {state}")
    st.dataframe(state_data.head(),hide_index=True)
    st.subheader("Number of Areas by AQI Category")
    st.bar_chart(state_air_quality,x='air_quality_status',y='count')
    st.header(f"{state} VS Country's Avg AQI Comparison")
    x,y = st.columns(2)
    x.metric("Country's Avg AQI",country_avg_aqi, border=True)
    y.metric(f"Avg AQI of {state}",Avg_AQI, border=True)








st.sidebar.title('AQI Analysis')
options = st.sidebar.selectbox('Select One',['Overview','State Analysis','Time Analysis','Insights'])

if options=='Overview':
    st.title('INDIAs AQI OVERVIEW')
    st.sidebar.selectbox('Select Overview',['Average AQI','Best Cities','Worst Cities','Monthly Trend'])
    btn1 = st.sidebar.button('Check Overview')
    




elif options=='State Analysis':
    #st.title('STATE ANALYSIS')
    selected_state = st.sidebar.selectbox('Select State',sorted(aqi['state'].unique().tolist()))
    btn2 = st.sidebar.button('Analyse State')
    if btn2:
       st.title(f"{selected_state} Analysis")
       load_state(selected_state)




elif options=='Time Analysis':
    st.title('TIME ANALYSIS')
    st.sidebar.selectbox('Select Time',['Month','Season','Year'])
    btn1 = st.sidebar.button('Time Wise AQI')




else:
    st.title('INSIGHTS')
    st.sidebar.selectbox('Select Overview',['Highest Pollution Periods','Major Pollutants','City-Wise Patterns'])
    btn1 = st.sidebar.button('Check Insights')