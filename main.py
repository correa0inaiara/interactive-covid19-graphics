import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo o dataset
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Melhorando o nome das colunas da tabela
df = df.rename(columns={'newDeaths': 'Novos Óbitos', 'newCases': 'Novos Casos', 'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

# Seleção do estado
state = 'RS'
estados = list(df['state'].unique())

# Seleção da coluna
column = 'Casos por 100 mil habitantes'
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']

# Seleção das linhas que pertencem ao estado
df = df[df['state'] == state]

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x': 0.5} )

print('DADOS COVID - BRASIL')
print('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a amostragem.')

fig.show()

print('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
