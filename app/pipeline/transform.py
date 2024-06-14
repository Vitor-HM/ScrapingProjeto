import pandas as pd
from typing import Dict
def cria_dataframe(p_dados: dict) -> pd.DataFrame:
    """
    Funcao que cria um dataframe e remove caracteres indesejados

    agrs: p_dados
    
    return: dataframe
    """
    df = pd.DataFrame(p_dados)
     #Removendo colchetes. Chama o metodo astype para converter a coluna para string e ranca os colchetes
    df['genero'] = df['genero'].astype(str).str.replace('[', '', regex=False).str.replace(']', '', regex=False)
    #Removendo as aspas. Chama o metodo astype para converter a coluna para string e ranca os aspas
    df['genero'] = df['genero'].astype(str).str.replace("'", '', regex=False).str.replace("'", '', regex=False)

    df['estudio'] = df['estudio'].astype(str).str.replace('[', '', regex=False).str.replace(']', '', regex=False)

    df['estudio'] = df['estudio'].astype(str).str.replace("'", '', regex=False).str.replace("'", '', regex=False)

    df.loc[df['qtd_episodios'] == '?', 'qtd_episodios'] = 0

    df['ano'] = pd.to_datetime(df['data_lancamento']).dt.year

    df['mes'] = pd.to_datetime(df['data_lancamento']).dt.month

    df['data_lancamento'] = pd.to_datetime(df['data_lancamento'])

    #Filtrando o dataframe com animes lançados somente em 2024
    df = df[df['data_lancamento'].between(pd.to_datetime('2024-01-01'),
                                                pd.to_datetime('2024-12-31'))]

    #Criando as estacoes no ano para ver cada temporada de anime
    df['estacoes'] = 'teste'

    inverno = [12,1,2]
    outuno = [9,10,11]
    verao = [6,7,8]
    primavera = [3,4,5]
    df.loc[df['mes'].isin(inverno),'estacoes'] ='Inverno'
    df.loc[df['mes'].isin(outuno),'estacoes'] ='Outono'
    df.loc[df['mes'].isin(verao),'estacoes'] ='Verao'
    df.loc[df['mes'].isin(primavera),'estacoes'] ='Primavera'

    df.loc[df['genero']== '', 'genero'] = 'nao informado'


    return df