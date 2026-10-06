import streamlit as st
import pandas as pd
from data import load_data
import page.State_Analysis
import pydeck


aqi = load_data()
country_avg_aqi = round(aqi['aqi_value'].mean(),2)





country_avg_aqi = round(aqi['aqi_value'].mean(),2)
avg_aqi_year_wise = aqi.groupby(['Year'])['aqi_value'].mean().reset_index()
avg_aqi_of_all_state = aqi.groupby(['state'])['aqi_value'].mean().reset_index().sort_values(by='aqi_value',ascending=False)

def avg_aqi_of_state(state):
  return(float(round(avg_aqi_of_all_state[avg_aqi_of_all_state['state']==state].iloc[0,1],2)))


def load_overview():
    l1,l2,l3 = st.columns(3)
    l1.metric("Min AQI",aqi['aqi_value'].min(),border=True)
    l2.metric("Max AQI",aqi['aqi_value'].max(),border=True)
    l3.metric("Average AQI",country_avg_aqi,border=True)
    st.bar_chart(data=avg_aqi_year_wise, x='Year', y='aqi_value', color="#0080FF")
    state_selected = st.selectbox('Select State',sorted(aqi['state'].unique().tolist()))
    btn1 = st.button(f"Check avg AQI of {state_selected}")
    if btn1:
        st.metric(f"Avg AQI of {state_selected}",avg_aqi_of_state(state_selected),border= True,delta=page.State_Analysis.aqi_category(avg_aqi_of_state(state_selected)))


def load_best_cities():
   top_ten_cities_with_lowest_aqi = aqi.groupby(['state','area'])['aqi_value'].mean().reset_index().sort_values(by='aqi_value').head(10)
   low_aqi_area = aqi.sort_values(by='aqi_value')[['state','area','aqi_value']]
   best_state = low_aqi_area.iloc[0,0]
   best_city = low_aqi_area.iloc[0,1]
   best_aqi = int(low_aqi_area.iloc[0,2])
   c1,c2 = st.columns(2)
   col1, col2 = st.columns(2)
   with col1:
      st.metric(label="🏆 Best Air Quality City", value=best_city, delta=f"{best_state}") 
   with col2:
      st.metric(label="🍃 Lowest AQI Recorded", value=best_aqi, delta="Healthy", delta_color="normal")
   st.subheader("Top 10 Cities (AQI Wise)")
   city1,city2 = st.columns(2)
   city3,city4= st.columns(2)
   city5,city6 = st.columns(2)
   city7,city8 = st.columns(2)
   city9,city10 = st.columns(2)
   city1.metric(label = f'🥇1st, {top_ten_cities_with_lowest_aqi.iloc[0,0]}', border= True, value=top_ten_cities_with_lowest_aqi.iloc[0,1],delta=round(top_ten_cities_with_lowest_aqi.iloc[0,2],2))
   city2.metric(label = f'🥈2nd, {top_ten_cities_with_lowest_aqi.iloc[1,0]}', border= True, value=top_ten_cities_with_lowest_aqi.iloc[1,1],delta=round(top_ten_cities_with_lowest_aqi.iloc[1,2],2))
   city3.metric(label = f'🥉3rd, {top_ten_cities_with_lowest_aqi.iloc[2,0]}', border= True, value=top_ten_cities_with_lowest_aqi.iloc[2,1],delta=round(top_ten_cities_with_lowest_aqi.iloc[2,2],2))
   city4.metric(label = f'4️⃣4th, {top_ten_cities_with_lowest_aqi.iloc[3,0]}', border= True, value=top_ten_cities_with_lowest_aqi.iloc[3,1],delta=round(top_ten_cities_with_lowest_aqi.iloc[3,2],2))
   city5.metric(label = f'5️⃣5th, {top_ten_cities_with_lowest_aqi.iloc[4,0]}', border= True, value=top_ten_cities_with_lowest_aqi.iloc[4,1],delta=round(top_ten_cities_with_lowest_aqi.iloc[4,2],2))
   city6.metric(label = f'6️⃣6th, {top_ten_cities_with_lowest_aqi.iloc[5,0]}', border= True, value=top_ten_cities_with_lowest_aqi.iloc[5,1],delta=round(top_ten_cities_with_lowest_aqi.iloc[5,2],2))
   city7.metric(label = f'7️⃣7th, {top_ten_cities_with_lowest_aqi.iloc[6,0]}', border= True, value=top_ten_cities_with_lowest_aqi.iloc[6,1],delta=round(top_ten_cities_with_lowest_aqi.iloc[6,2],2))
   city8.metric(label = f'8️⃣8th, {top_ten_cities_with_lowest_aqi.iloc[7,0]}', border= True, value=top_ten_cities_with_lowest_aqi.iloc[7,1],delta=round(top_ten_cities_with_lowest_aqi.iloc[7,2],2))
   city9.metric(label = f'9️⃣9th, {top_ten_cities_with_lowest_aqi.iloc[8,0]}', border= True, value=top_ten_cities_with_lowest_aqi.iloc[8,1],delta=round(top_ten_cities_with_lowest_aqi.iloc[8,2],2))
   city10.metric(label = f'🔟10th, {top_ten_cities_with_lowest_aqi.iloc[9,0]}', border= True, value=top_ten_cities_with_lowest_aqi.iloc[9,1],delta=round(top_ten_cities_with_lowest_aqi.iloc[9,2],2))
   low_aqi_area = aqi.sort_values(by='aqi_value')[['state','area','aqi_value','Month']].head(10)
   low_aqi_area['Longitude']=0.0
   low_aqi_area['Latitude']=0.0
   low_aqi_area.loc[low_aqi_area["area"] == "Silchar", ["Latitude", "Longitude"]] = [24.83, 92.80]
   low_aqi_area.loc[low_aqi_area["area"] == "Aizawl", ["Latitude", "Longitude"]] = [23.73, 92.72]
   low_aqi_area.loc[low_aqi_area["area"] == "Naharlagun", ["Latitude", "Longitude"]] = [27.10, 93.69]
   low_aqi_area.loc[low_aqi_area["area"] == "Davanagere", ["Latitude", "Longitude"]] = [14.47, 75.92]
   low_aqi_area.loc[low_aqi_area["area"] == "Kalaburagi", ["Latitude", "Longitude"]] = [17.33, 76.83]
   low_aqi_area.loc[low_aqi_area["area"] == "Shillong", ["Latitude", "Longitude"]] = [25.58, 91.89]
   low_aqi_area.loc[low_aqi_area["area"] == "Gummidipoondi", ["Latitude", "Longitude"]] = [13.41, 80.11]

   st.subheader("Best Cities Location")
   point_layer = pydeck.Layer(
      "ScatterplotLayer",
      data=low_aqi_area,
      id="lowest-aqi-areas",
      get_position=["Longitude", "Latitude"],
      get_color="[255, 75, 75]",
      pickable=True,
      auto_highlight=True,
      get_radius=50000,
   )

   view_state = pydeck.ViewState(
      latitude=22,
      longitude=79,
      controller=True,
      zoom=4,
      pitch=30
   )

   chart = pydeck.Deck(
      point_layer,
      initial_view_state=view_state,
      tooltip={
         "text": "{area}, {state}\nAQI: {aqi_value}"
      },
   )

   event = st.pydeck_chart(
      chart,
      on_select="rerun",
      selection_mode="multi-object"
   )

   event.selection
   st.subheader("Year Wise AQI Comparison")
   st.bar_chart(aqi.groupby("Year")['aqi_value'].mean().reset_index(), x="Year", y="aqi_value")





def load_worst_cities():
   top_ten_cities_with_highest_aqi = aqi.groupby(['state','area'])['aqi_value'].mean().reset_index().sort_values(by='aqi_value',ascending=False).head(10)
   high_aqi_area = aqi.sort_values(by='aqi_value',ascending=False)[['state','area','aqi_value']]
   worst_state = high_aqi_area.iloc[0,0]
   worst_city = high_aqi_area.iloc[0,1]
   worst_aqi = int(high_aqi_area.iloc[0,2])
   c1,c2 = st.columns(2)
   col1, col2 = st.columns(2)
   with col1:
      st.metric(label="🏆 Worst Air Quality City", value=worst_city, delta=f"{worst_state}",delta_color="red") 
   with col2:
      st.metric(label="🍃 Highest AQI Recorded", value=worst_aqi, delta="Poor", delta_color="red")
   st.subheader("Top 10 Worst Cities (AQI Wise)")
   city1,city2 = st.columns(2)
   city3,city4= st.columns(2)
   city5,city6 = st.columns(2)
   city7,city8 = st.columns(2)
   city9,city10 = st.columns(2)
   city1.metric(label = f'🥇1st, {top_ten_cities_with_highest_aqi.iloc[0,0]}', border= True, value=top_ten_cities_with_highest_aqi.iloc[0,1],delta=round(top_ten_cities_with_highest_aqi.iloc[0,2],2),delta_color="red")
   city2.metric(label = f'🥈2nd, {top_ten_cities_with_highest_aqi.iloc[1,0]}', border= True, value=top_ten_cities_with_highest_aqi.iloc[1,1],delta=round(top_ten_cities_with_highest_aqi.iloc[1,2],2),delta_color="red")
   city3.metric(label = f'🥉3rd, {top_ten_cities_with_highest_aqi.iloc[2,0]}', border= True, value=top_ten_cities_with_highest_aqi.iloc[2,1],delta=round(top_ten_cities_with_highest_aqi.iloc[2,2],2),delta_color="red")
   city4.metric(label = f'4️⃣4th, {top_ten_cities_with_highest_aqi.iloc[3,0]}', border= True, value=top_ten_cities_with_highest_aqi.iloc[3,1],delta=round(top_ten_cities_with_highest_aqi.iloc[3,2],2),delta_color="red")
   city5.metric(label = f'5️⃣5th, {top_ten_cities_with_highest_aqi.iloc[4,0]}', border= True, value=top_ten_cities_with_highest_aqi.iloc[4,1],delta=round(top_ten_cities_with_highest_aqi.iloc[4,2],2),delta_color="red")
   city6.metric(label = f'6️⃣6th, {top_ten_cities_with_highest_aqi.iloc[5,0]}', border= True, value=top_ten_cities_with_highest_aqi.iloc[5,1],delta=round(top_ten_cities_with_highest_aqi.iloc[5,2],2),delta_color="red")
   city7.metric(label = f'7️⃣7th, {top_ten_cities_with_highest_aqi.iloc[6,0]}', border= True, value=top_ten_cities_with_highest_aqi.iloc[6,1],delta=round(top_ten_cities_with_highest_aqi.iloc[6,2],2),delta_color="red")
   city8.metric(label = f'8️⃣8th, {top_ten_cities_with_highest_aqi.iloc[7,0]}', border= True, value=top_ten_cities_with_highest_aqi.iloc[7,1],delta=round(top_ten_cities_with_highest_aqi.iloc[7,2],2),delta_color="red")
   city9.metric(label = f'9️⃣9th, {top_ten_cities_with_highest_aqi.iloc[8,0]}', border= True, value=top_ten_cities_with_highest_aqi.iloc[8,1],delta=round(top_ten_cities_with_highest_aqi.iloc[8,2],2),delta_color="red")
   city10.metric(label = f'🔟10th, {top_ten_cities_with_highest_aqi.iloc[9,0]}', border= True, value=top_ten_cities_with_highest_aqi.iloc[9,1],delta=round(top_ten_cities_with_highest_aqi.iloc[9,2],2),delta_color="red")



def best_area_by_month(month):
  unique_month_wise_aqi = aqi.groupby(['state','area','Month'])['aqi_value'].mean().reset_index().sort_values(by='aqi_value',ascending=True)
  unique_month_wise_aqi1 = unique_month_wise_aqi[unique_month_wise_aqi['Month']==month].head()
  area1, area2 = st.columns(2)
  area3, area4 = st.columns(2)
  area1.metric(label=f'🥇1st {unique_month_wise_aqi1.iloc[0,0]}', border= True, value=unique_month_wise_aqi1.iloc[0,1], delta=round(unique_month_wise_aqi1.iloc[0,3]))
  area2.metric(label=f'🥈2nd {unique_month_wise_aqi1.iloc[1,0]}', border= True,value=unique_month_wise_aqi1.iloc[1,1], delta=round(unique_month_wise_aqi1.iloc[1,3]))
  area3.metric(label=f'🥉3rd {unique_month_wise_aqi1.iloc[2,0]}',border= True,value=unique_month_wise_aqi1.iloc[2,1], delta=round(unique_month_wise_aqi1.iloc[2,3]))
  area4.metric(label=f'4️⃣4th {unique_month_wise_aqi1.iloc[3,0]}',border= True,value=unique_month_wise_aqi1.iloc[3,1], delta=round(unique_month_wise_aqi1.iloc[3,3]))
  st.metric(label=f'5️⃣5th {unique_month_wise_aqi1.iloc[4,0]}',border= True,value=unique_month_wise_aqi1.iloc[4,1], delta=round(unique_month_wise_aqi1.iloc[4,3]))
  




def year_wise(year):
  year = int(year)
  year_wise_cat = aqi.groupby(['Year','Month'])['aqi_value'].mean()
  year_wise_cat.loc[year]
  if(year==2023 | year==2024):
   year1,year2 = st.columns(2)
   year3,year4 = st.columns(2)
   year5,year6 = st.columns(2)
   year7,year8 = st.columns(2)
   year9,year10 = st.columns(2)
   year11,year12 = st.columns(2)
   year1.metric(label = f"January-{year}" , value = float(round(year_wise_cat.loc[year].loc['January'],2)) , border = True)
   year2.metric(label = f"February-{year}" , value = float(round(year_wise_cat.loc[year].loc['February'],2)) , border = True)
   year3.metric(label = f"March-{year}" , value = float(round(year_wise_cat.loc[year].loc['March'],2)) , border = True)
   year4.metric(label = f"April-{year}" , value = float(round(year_wise_cat.loc[year].loc['April'],2)) , border = True)
   year5.metric(label = f"May-{year}" , value = float(round(year_wise_cat.loc[year].loc['May'],2)) , border = True)
   year6.metric(label = f"June-{year}" , value = float(round(year_wise_cat.loc[year].loc['June'],2)) , border = True)
   year7.metric(label = f"July-{year}" , value = float(round(year_wise_cat.loc[year].loc['July'],2)) , border = True)
   year8.metric(label = f"August-{year}" , value = float(round(year_wise_cat.loc[year].loc['August'],2)) , border = True)
   year9.metric(label = f"September-{year}" , value = float(round(year_wise_cat.loc[year].loc['September'],2)) , border = True)
   year10.metric(label = f"October-{year}" , value = float(round(year_wise_cat.loc[year].loc['October'],2)) , border = True)
   year11.metric(label = f"November-{year}" , value = float(round(year_wise_cat.loc[year].loc['November'],2)) , border = True)
   year12.metric(label = f"December-{year}" , value = float(round(year_wise_cat.loc[year].loc['December'],2)) , border = True)
  elif(year == 2025):
     year1,year2 = st.columns(2)
     year3,year4 = st.columns(2)
     year1.metric(label = f"January-{year}" , value = float(round(year_wise_cat.loc[year].loc['January'],2)) , border = True)
     year2.metric(label = f"February-{year}" , value = float(round(year_wise_cat.loc[year].loc['February'],2)) , border = True)
     year3.metric(label = f"March-{year}" , value = float(round(year_wise_cat.loc[year].loc['March'],2)) , border = True)
     year4.metric(label = f"April-{year}" , value = float(round(year_wise_cat.loc[year].loc['April'],2)) , border = True)
  else:
     year5,year6 = st.columns(2)
     year7,year8 = st.columns(2)
     year9,year10 = st.columns(2)
     year11,year12 = st.columns(2)
     year5.metric(label = f"May-{year}" , value = float(round(year_wise_cat.loc[year].loc['May'],2)) , border = True)
     year6.metric(label = f"June-{year}" , value = float(round(year_wise_cat.loc[year].loc['June'],2)) , border = True)
     year7.metric(label = f"July-{year}" , value = float(round(year_wise_cat.loc[year].loc['July'],2)) , border = True)
     year8.metric(label = f"August-{year}" , value = float(round(year_wise_cat.loc[year].loc['August'],2)) , border = True)
     year9.metric(label = f"September-{year}" , value = float(round(year_wise_cat.loc[year].loc['September'],2)) , border = True)
     year10.metric(label = f"October-{year}" , value = float(round(year_wise_cat.loc[year].loc['October'],2)) , border = True)
     year11.metric(label = f"November-{year}" , value = float(round(year_wise_cat.loc[year].loc['November'],2)) , border = True)
     year12.metric(label = f"December-{year}" , value = float(round(year_wise_cat.loc[year].loc['December'],2)) , border = True)


def load_month_wise():
    month_wise_aqi = aqi.groupby(['Month'])['aqi_value'].mean().reset_index().sort_values(by='aqi_value',ascending=False)
    st.bar_chart(month_wise_aqi,x='Month',y='aqi_value')
    month = st.selectbox("Select Month",['January',"February",'March',"April","May","June","July","August","September","October","November","December"])
    month_btn = st.button(f"Top 5 area for {month}")
    if month_btn:   
       best_area_by_month(month)
    year_wise_cat = aqi.groupby(['Year','Month'])['aqi_value'].mean()
    Yr = st.selectbox("Select Month",['2022','2023','2024','2025'])
    Year_btn = st.button(f"Average AQI for {Yr}")
    if Year_btn:
       year_wise(Yr)
   




