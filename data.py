import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pydeck


def load_data():
    aqi = pd.read_csv('AQI_cleaned.csv')
    #data Cleaning
    aqi['Date'] = pd.to_datetime(aqi['Date'])
    aqi['Month'] = aqi['Date'].dt.month_name()
    aqi['Year'].fillna('2023',inplace=True)
    aqi['Year'] = aqi['Year'].astype(int)
    #aqi["aqi_value"] = aqi['aqi_value'].fillna(aqi['aqi_value'].mean(),inplace=True)
    return aqi

