import streamlit as st
import pandas as pd
import numpy as np
import base64
import warnings
warnings.filterwarnings('ignore')
from datetime import datetime, date
from io import BytesIO
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.title("Web App - FutPythonTrader")

def jogos_do_dia():
    
    # st.image('logo.jpg', width=250)
    st.header("Jogos do Dia")

    dia = st.date_input(
        "Data",
        date.today())

    ########## Importando os Jogos do Dia ##########

    @st.cache
    def load_data_jogos():

        # data_jogos = pd.read_csv(f'./Jogos_do_Dia/{dia}_Jogos_do_Dia.csv')
        data_jogos = pd.read_csv(f'https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_Betfair/{dia}_Jogos_do_Dia.csv?raw=true')

        return data_jogos

    try:
        df_jogos = load_data_jogos()
        
        df_jogos = df_jogos[['League','Date','Time','Home','Away',
                        'Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_Under25','Odd_BTTS_Yes','Odd_BTTS_No']]

        df = df_jogos[['League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]
        # Ajustando o Índice
        df.reset_index(inplace=True, drop=True)
        df.index = df.index.set_names(['Nº'])
        df = df.rename(index=lambda x: x + 1)
    
    
    
        st.dataframe(df)

        # Define a função que retorna a planilha em formato XLSX
        def download_excel():
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            df_jogos.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.close()
            processed_data = output.getvalue()
            return processed_data

        # Cria o botão de download
        button = st.download_button(
            label='Download',
            data=download_excel(),
            file_name=f'FutPythonTrader_Jogos_do_Dia_{dia}.xlsx',
            mime='application/vnd.ms-excel'
        )
    except:
        st.write("Jogos desse dia ainda não disponíveis.")
        st.write("Por Favor. Aguarde!")


def football_data():

    st.sidebar.header("Leagues")
    selected_league = st.sidebar.selectbox('League',['England','Germany','Italy','Spain','France'])

    st.sidebar.header("Season")
    selected_season = st.sidebar.selectbox('Season', ['2021/2022','2020/2021','2019/2020'])

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
      if selected_league == 'France':
        league = 'F1'
      
      if selected_season == '2021/2022':
        season = '2122'
      if selected_season == '2020/2021':
        season = '2021'
      if selected_season == '2019/2020':
        season = '1920'
        
      url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
      data = pd.read_csv(url)
      return data

    df = load_data(selected_league, selected_season)

    st.subheader("Dataframe: "+selected_league)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
        Odd_H_Max = st.number_input('Odd_H_Max', value=100.0, step=0.1)
    with col2:
        Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
        Odd_D_Max = st.number_input('Odd_D_Max', value=100.0, step=0.1)
    with col3:
        Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
        Odd_A_Max = st.number_input('Odd_A_Max', value=100.0, step=0.1)
    with col4:
        Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
        Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=100.0, step=0.1)
    with col5:
        Odd_Under25_Min = st.number_input('Odd_Under25_Min', value=1.01, step=0.1)
        Odd_Under25_Max = st.number_input('Odd_Under25_Max', value=100.0, step=0.1)
    
    # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
    df_filtrado = df[(df['B365H'] >= Odd_H_Min) & (df['B365H'] <= Odd_H_Max) &
                    (df['B365D'] >= Odd_D_Min) & (df['B365D'] <= Odd_D_Max) &
                    (df['B365A'] >= Odd_A_Min) & (df['B365A'] <= Odd_A_Max) &
                    (df['B365>2.5'] >= Odd_Over25_Min) & (df['B365>2.5'] <= Odd_Over25_Max) &
                    (df['B365<2.5'] >= Odd_Under25_Min) & (df['B365<2.5'] <= Odd_Under25_Max)]
    
    df_filtrado.reset_index(inplace=True, drop=True)
    df_filtrado.index = df_filtrado.index.set_names(['Nº'])
    df_filtrado = df_filtrado.rename(index=lambda x: x + 1)
    
    st.dataframe(df_filtrado)

    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="Base_de_Dados.csv">Download CSV File</a>'
        return href

    st.markdown(filedownload(df_filtrado), unsafe_allow_html=True)

def backtesting():
   
    st.header("Software de Backtesting")
    st.subheader("Back Home")


    @st.cache(allow_output_mutation=True)
    def load_base():
      url = "https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/futpythontraderpunter.csv?raw=true"
      data_jogos = pd.read_csv(url)

      return data_jogos

    df = load_base()

    df.loc[(df['FT_Goals_H'] >  df['FT_Goals_A']), 'Profit'] = df['FT_Odd_H'] - 1
    df.loc[(df['FT_Goals_H'] <= df['FT_Goals_A']), 'Profit'] = -1

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
        Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
    with col2:
        Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
        Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
    with col3:
        Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
        Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
    with col4:
        Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
        Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
    with col5:
        Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
        Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
    
    # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
    df_filtrado = df[(df['FT_Odd_H'] >= Odd_H_Min) & (df['FT_Odd_H'] <= Odd_H_Max) &
                    (df['FT_Odd_D'] >= Odd_D_Min) & (df['FT_Odd_D'] <= Odd_D_Max) &
                    (df['FT_Odd_A'] >= Odd_A_Min) & (df['FT_Odd_A'] <= Odd_A_Max) &
                    (df['FT_Odd_Over25'] >= Odd_Over25_Min) & (df['FT_Odd_Over25'] <= Odd_Over25_Max) &
                    (df['FT_Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df['FT_Odd_BTTS_Yes'] <= Odd_BTTS_Max)]

    # Crie uma nova coluna no dataframe filtrado com o profit acumulado
    df_filtrado['Profit_acu'] = df_filtrado.Profit.cumsum()
    df_filtrado = df_filtrado.dropna()
    df_filtrado = df_filtrado.reset_index(drop=True)
    df_filtrado.index += 1
    profit = round(df_filtrado.Profit_acu.tail(1).item(),2)
    ROI = round((df_filtrado.Profit_acu.tail(1)/len(df_filtrado)*100).item(),2)
    df_filtrado.Profit_acu.plot(title="Back Home", xlabel='Entradas', ylabel='Stakes')
    print("Profit:",profit,"stakes em", len(df_filtrado),"jogos")
    print("ROI:",ROI,"%")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_filtrado.index, y=df_filtrado['Profit_acu'], mode='lines'))

    fig.update_layout(
        title="Profit Acumulado",
        xaxis_title="Entradas",
        yaxis_title="Stakes"
    )

    # Plotando o gráfico no Streamlit
    st.plotly_chart(fig)


paginas = ['Jogos do Dia', 'Base de Dados - Football Data', 'Backtesting - Back Home']
escolha = st.sidebar.radio('', paginas)


if escolha == 'Jogos do Dia':
    jogos_do_dia()

if escolha == 'Base de Dados - Football Data':
    football_data()

if escolha == 'Backtesting - Back Home':
    backtesting()