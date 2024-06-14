from pipeline.extract import requisicao, raspasgem
from pipeline.transform import cria_dataframe
from pipeline.load import carrega_csv
if __name__ == "__main__":
    response = requisicao('https://myanimelist.net/anime/season')
    if response:
        dados = raspasgem(response)
        df = cria_dataframe(dados)
        carrega_csv(df,'data/output',"animes_temporada")