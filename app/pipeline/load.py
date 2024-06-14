import os

import pandas as pd


def carrega_csv(p_dataframe: pd.DataFrame, p_caminho: str, p_nome_arquivo: str):
    
    """
    funcao para criar um arquivo em excel

    args: p_dataframe: pd.DataFrame dataframe que vai ser transformado em excel
    p_caminho: str Caminho que deseja salvar
    p_nome_arquivo: str Nome do arquivo
    """

    if not os.path.exists(p_caminho):
        os.mkdir(p_caminho)
    
    p_dataframe.to_excel(f"{p_caminho}/{p_nome_arquivo}.xlsx", index=False)