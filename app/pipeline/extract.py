import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from datetime import datetime
import pandas as pd

#Funcao que faz requisicao a pagina
def requisicao(p_url):
    """
    Funcao que faz a requisicao na pagina 

    args: p_url url da pagina

    return: codigo da pagina em formato de string
    """
    
    #Requisição ao site e me retorna uma resposta
    response = requests.get(p_url)
    if response.status_code == 200:
       #Conteudo caso tiver sido aceito o response
        content = response.content
        return content
    else:
        return ('Nao foi possivel fazer requisicao ao site')


#Funcao que faz a raspagem
def raspasgem(p_content):
    """
    Funcao que faz o web scrapping

    agrs: resposta da pagina

    return: dicionario de dados
    """
    animes_temporada = {}
    site = BeautifulSoup(p_content,'html.parser')
    #Listas para guardar o nome dos animes
    l_nome_anime = []
    l_imagem = []
    l_data_lancamento = []
    l_qtd_episodios = []
    l_duracao = []
    l_generos_animes = []
    l_sinopse = []
    l_estudio = []
    l_fonte = []
    l_tema_anime =[]
    l_id = []

    anime = site.find('div', class_='js-categories-seasonal')

    div_animes = anime.find_all('div', class_='js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1')

    v_parada = anime.find('div', class_="anime-header").text

    tradutor = GoogleTranslator(source= "en", target= "pt")

    for id, anime in enumerate(div_animes, start=1):
        
        v_nome_anime = anime.find('h2', class_='h2_anime_title')
        v_nome_anime = v_nome_anime.text
        
        if v_nome_anime:
            l_nome_anime.append(v_nome_anime)
        
        #buscando a div de imagem
        img_data = ['src', 'data-src']
        v_tag_imagem = anime.find('div', class_='image')

        for attr in img_data:
        # Encontrar a tag 'img' dentro de v_tag_imagem
            v_tag_img = v_tag_imagem.find('img')
        # Verificar se a tag 'img' existe
            if v_tag_img:
                # Verificar se o atributo está presente na tag 'img'
                if v_tag_img.get(attr):
                    v_img = v_tag_img.get(attr)
        l_imagem.append(v_img)
        

        data_ep_tempo = anime.find('div', class_="info").text

        #extraindo a data da string
        data = data_ep_tempo.replace(' ', '').split('\n')[0]

        #formatando a data
        data = datetime.strptime(data,'%b%d,%Y').date()
        if data:
            l_data_lancamento.append(data)
        else:
            print('Anime: ', '', v_nome_anime, '', 'Nao possui uma data definida')
        
        #extraindo os ep da string
        ep = data_ep_tempo.replace(' ', '').split('\n')[1].rstrip(',')
        
        #total de episodios
        qtd_episodios = ep[:-3]
        l_qtd_episodios.append(qtd_episodios)


        
        #extraindo o tempo de cada ep pela string
        duracao = data_ep_tempo.replace(' ', '').split('\n')[2]
        
        #Este numero se refere ao tempo de cada episodios em minutos
        duracao = duracao[:-3] 
        #print(duracao)
        l_duracao.append(duracao)

        #Buscando o genero dos animes
        generos = anime.find_all('span', class_='genre')

        #lista que vai armazenar os animes temporariamente dentro do loop
        l_genero_anime = []
        for genero in generos:
            v_genero = genero.text.replace('\n','').lstrip(',')
            l_genero_anime.append(v_genero)

        #colocando o valor da lista dentro de outra lista
        l_generos_animes.append(l_genero_anime)

        sinopse = anime.find('p', class_='preline')

        sinopse = sinopse.text

        sinopse = tradutor.translate(sinopse)


        l_sinopse.append(sinopse)
        
        div_proriedades = anime.find('div', class_='properties')
        
        informacoes = div_proriedades.find_all('div', class_='property')

        estudios = ['Studio','Studios']
        
        l_estudios =[]
        
        v_estudio = 'nao informado'
        
        for informacao in informacoes:
            

            if informacao.find('span', text=estudios):
                estudios = informacao.find_all('span', class_='item')
                
                for estudio in estudios:
                    if estudio:
                        v_estudio_tag = estudio.a
                        if v_estudio_tag:
                            v_estudio = v_estudio_tag.text
                        l_estudios.append(v_estudio)
                
                l_estudio.append(l_estudios)
                
            if informacao.find('span', text='Source'):
                fonte = informacao.find('span', class_='item').text
                l_fonte.append(fonte)
        
            v_temas = 'Não especificado'

            themas = ['Themes', 'Theme']

            l_temas = []
            
            if informacao.find('span', text=themas):
                temas_tags = informacao.find_all('span', class_='item')
                l_temas = [tema.text for tema in temas_tags]  # Extrai os temas em uma lista
                v_temas = ', '.join(l_temas)  # Transforma a lista em uma string separada por vírgula
                break  # Saindo do loop assim que encontrar os temas
        l_tema_anime.append(v_temas)  # Adiciona o tema à lista de temas
        l_id.append(id)
    animes_temporada['id'] =l_id
    animes_temporada['nome'] = l_nome_anime
    animes_temporada['data_lancamento'] = l_data_lancamento
    animes_temporada['qtd_episodios'] = l_qtd_episodios
    animes_temporada['duracao'] = l_duracao
    animes_temporada['genero'] = l_generos_animes
    animes_temporada['sinopse'] = l_sinopse
    animes_temporada['estudio'] = l_estudio
    animes_temporada['fonte'] = l_fonte
    animes_temporada['tema_anime'] = l_tema_anime
    animes_temporada['img_anime'] = l_imagem

    return animes_temporada
