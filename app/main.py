from pipeline.extract import raspasgem, requisicao
from pipeline.load import carrega_csv
from pipeline.transform import cria_dataframe

if __name__ == '__main__':
    response = requisicao('https://myanimelist.net/anime/season')
    if response:
        dados = raspasgem(response)
        df = cria_dataframe(dados)
        carrega_csv(df, 'data/output', 'animes_temporada')
