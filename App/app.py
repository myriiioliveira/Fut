import streamlit as st
import pandas as pd
import numpy as np

st.title("Web App Football Data")

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League', ['England','Germany','Italy','Spain','France','Scotland','Netherlands','Belgium','Portugal','Turkey','Greece'])

st.sidebar.header("Season")
selected_season = st.sidebar.selectbox('Season', ['2025/2024','2024/2023','2023/2022'])

# WebScraping Football Data

def load_data(league, season):
  if selected_league == 'England':
     league = 'E0'
  if selected_league == 'Germany':
     league = 'D1'
  if selected_league == 'Italy':
     league = 'I1'
  if selected_league == 'Spain':
     league = 'SP1'
  if selected_league == 'Fance':
     league = 'F1'
  if selected_league == 'Scotland':
     league = 'SC0'
  if selected_league == 'Netherlands':
     league = 'N1'
  if selected_league == 'Belgium':
     league = 'B1'
  if selected_league == 'Portugal':
     league = 'P1'
  if selected_league == 'Turkey':
     league = 'T1'
  if selected_league == 'Greece':
     league = 'G1'


  if selected_season == '2024/2025':
     season = '2025'
  if selected_season == '2023/2024':
     season = '2024'
  if selected_season == '2022/2023':
     season = '2023'
  if selected_season == '2021/2022':
     season = '2022'

  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selected_season)

st.subheader("Dataframe: "+selected_league)
st.dataframe(df)
                  

