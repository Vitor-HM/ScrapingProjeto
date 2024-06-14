import streamlit as st
import pandas as pd
from datetime import datetime
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source= "en", target= "pt")

st.set_page_config(
    page_title="Detalhes",
#    page_icon='',
     layout="wide",
     initial_sidebar_state='collapsed'
)
df = pd.read_excel('../data/output/animes_temporada.xlsx')


animes = st.selectbox(
    'Ver Detalhe de qual anime? ',
    df['nome']
)

df_anime = df[df['nome'] == animes]
anime = df_anime['nome'].value_counts().index
nome = anime[0]

animes_info = df[df['nome'] == nome].iloc[0]

st.title(animes_info['nome'])

col1, col2 = st.columns(2, gap='large')

with col1:
    st.subheader(f"Tema(s): {animes_info['tema_anime']}")
    st.markdown(animes_info['sinopse'])

with col2:
    st.subheader(f"Estação: {animes_info['estacoes']}")
    st.image(animes_info['img_anime'])

col1, col2, col3 = st.columns(3, gap='small')

with col1:
    data = animes_info['data_lancamento']
    dia_semana = data.strftime('%A')
    dia_semana = tradutor.translate(dia_semana)
    st.text(f"Data Lançamento: {data.strftime('%d/%m/%Y')}, {dia_semana}")

with col2:
    st.text(f"Estudio: {animes_info['estudio']}")

with col3:
    st.text(f"Fonte: {animes_info['fonte']}")