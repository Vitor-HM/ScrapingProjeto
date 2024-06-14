import os

import pandas as pd
import plotly.express as px

import streamlit as st

st.set_page_config(
    page_title='Animes Temporada',
    #    page_icon='',
    layout='wide',
    initial_sidebar_state='collapsed',
)

df = pd.read_excel('../data/output/animes_temporada.xlsx')


st.title('Animes Da Temporada')

# ------------------SIDE BAR---------------------------#
# Filtro de generos
lista_generos = df['genero'].unique()
lista_filtro = []

for item in lista_generos:
    genero = item.split(',')
    lista_filtro.append(genero[0].strip())
generos_unicos = list(set(lista_filtro))
st.sidebar.header('Filtros: ')

p_genero = st.sidebar.multiselect(
    'Filtre por genero: ', options=generos_unicos
)

# FILTRO POR TEMA
filtro_por_tema = df['tema_anime'].unique()

l_filtro_tema = []
for i in filtro_por_tema:
    genero = i.split(',')
    l_filtro_tema.append(genero[0])
tema_unico = list(set(l_filtro_tema))

p_tema_anime = st.sidebar.multiselect('Filtre por tema: ', options=tema_unico)

# Ativando o filtro
df_selecionado = df[
    df['genero'].str.contains('|'.join(p_genero), na=False)
    & df['tema_anime'].str.contains('|'.join(p_tema_anime), na=False)
]

df_estatistica_anime = df_selecionado[
    ['id', 'nome', 'data_lancamento', 'tema_anime', 'genero']
]

df_selecionado.set_index('id', inplace=False)
st.dataframe(df_estatistica_anime, width=2000, height=300, hide_index=True)

st.divider()

# ------------------PAGINA PRINCIPAL------------------
total_animes = df_selecionado.shape[0]

total_generos = len(
    generos_unicos
)   # procurar um jeito de fazer esse filtro ser dinamico.

col1, col2 = st.columns(2)

with col1:
    st.metric(label='Total Animes Da Temporada', value=total_animes)

with col2:
    st.metric(
        label='Total De Generos Lançados: ', value=total_generos
    )   # valor que vai dentro da primeira coluna

st.divider()


################GRAFICOS################
# Distribuição temporal dos lançamentos: Como estão distribuídos os lançamentos ao longo do tempo? Existe alguma tendência ou sazonalidade?
total_animes_temporada = (
    df_selecionado['estacoes'].value_counts().reset_index()
)

# Mudando as para estacoes e total_animes
total_animes_temporada.columns = ['estacoes', 'total_animes']

grafico_p1 = px.bar(
    total_animes_temporada,
    x='estacoes',
    y='total_animes',
    orientation='v',
    title='Total Animes Por estacao',
    text='total_animes',  # Rótulos de dados
    template='plotly_white',
)

grafico_p1.update_traces(selector=dict(type='bar'), hoverinfo='skip')

# Gêneros mais comuns: Quais são os gêneros mais comuns nas séries do dataframe? Há algum gênero dominante ou uma distribuição equilibrada?
# agrupando o df por genero pelo tamanho total e resetando o index
total_genero = (
    df_selecionado.where(df_selecionado['genero'] != 'nao revelado')
    .groupby('genero')
    .size()
    .reset_index()
)
total_genero.columns = ['generos', 'total_animes']
df_total_genero = (
    total_genero.sort_values(by='total_animes', ascending=False)
    .reset_index(drop=True)
    .head(5)
)

grafico_p2 = px.bar(
    df_total_genero,
    x='generos',
    y='total_animes',
    orientation='v',
    title='Total Animes Por Genero',
    text='total_animes',  # Rótulos de dados
    template='plotly_white',
)

animes_por_fonte = df_selecionado.groupby('fonte').size().reset_index()
animes_por_fonte.columns = ['fonte', 'total_animes']
df_animes_por_fonte = (
    animes_por_fonte.sort_values(by='total_animes', ascending=False)
    .reset_index(drop=True)
    .head(5)
)

grafico_p5 = px.bar(
    df_animes_por_fonte,
    x='fonte',
    y='total_animes',
    orientation='v',
    title='Total Animes Por Fonte',
    text='total_animes',  # Rótulos de dados
    template='plotly_white',
)
fig3 = px.scatter(
    df_selecionado,
    x='qtd_episodios',
    y='duracao',
    title='Relação entre Quantidade de Episódios e Duração Mínima',
    labels={
        'qtd_episodios': 'Quantidade de Episódios',
        'min_duracao': 'Duração Mínima (minutos)',
    },
)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(grafico_p5)
    st.plotly_chart(grafico_p2)
with col2:
    st.plotly_chart(grafico_p1)
    st.plotly_chart(fig3)
