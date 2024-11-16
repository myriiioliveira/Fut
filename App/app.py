import streamlit as st
import pandas as pd
import numpy as np

st.title("Web App Football Data")

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League', ['England','Germany','Italy','Spain','France','Scotland','Netherlands','Belgium','Portugal','Turkey','Greece','Argentina','Austria','Brazil','China','Denmark','Finland','Ireland','Japan','Mexico','Norway','Poland','Romania','Russia','Sweden','Switzerland','USA'])

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
  if selected_league == 'Argentina':
     league = 'ARG'
  if selected_league == 'Austria':
     league = 'AUT'
  if selected_league == 'Brazil':
     league = 'BRA'
  if selected_league == 'China':
     league = 'CHN'
  if selected_league == 'Denmark':
     league = 'DNK'
  if selected_league == 'Finland':
     league = 'FIN'
  if selected_league == 'Ireland':
     league = 'IRL'
  if selected_league == 'Japan':
     league = 'JPN'
  if selected_league == 'Mexico':
     league = 'MEX'
  if selected_league == 'Norway':
     league = 'NOR'
  if selected_league == 'Poland':
     league = 'POL'
  if selected_league == 'Romania':
     league = 'ROU'
  if selected_league == 'Russia':
     league = 'RUS'
  if selected_league == 'Sweden':
     league = 'SWE'
  if selected_league == 'Switzerland':
     league = 'SWZ'
  if selected_league == 'USA':
     league = 'USA'

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

  url = "https://www.football-data.co.uk/new/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selected_season)

st.subheader("Dataframe: "+selected_league)
st.dataframe(df)
                  

