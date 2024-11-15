import streamlit as st
import pandas as pd
import numpy as np

st.title ("Web App Football Data")

st.sidebar.header ("Leagues")
selected_league = st.sidebar.selectbox ('League', ['England', 'Germany', 'Italy', 'Spain', 'France', 'Scotland', 'Netherlands', 'Belgium', 'Portugal', 'Turkey', 'Greece', 'Argentina', 'Austria', 'Brazil', 'China', 'Denmark', 'Finland', 'Ireland', 'Japan', 'Mexico', 'Norway', 'Poland', 'Romania', 'Russia', 'Sweden', 'Switzerland', 'USA'])

st.sidebar.header ("Season")
selected_season = st.sidebar.selectbox ('Season", ['2026/2025', '2025/2024', '2024/2023', '2023/2022', '2025', '2024', '2023', '2022']

#WebScraping Football Data

def load_data (league,season):
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selected_season)
                  

