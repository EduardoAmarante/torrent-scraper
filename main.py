import requests
from bs4 import BeautifulSoup

mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
urlsite = 'https://megatorrentshd1.biz/lancamentos/'
scrape_url = urlsite
sb_get = requests.get(scrape_url, headers=mozhdr)
soupeddataPrincipal = BeautifulSoup(sb_get.content, "html.parser")


def imagemfilme(i):

    images = [x.find('img')['src'] for x in soupeddataPrincipal.find_all('div', class_="peli")]
    return images[i]

def pegatitulo():
    
    filmes = [x.find('a') for x in soupeddataPrincipal.find_all('div', class_="box-filme-container card_")]
    links_filmes = []
    titulos2 = []

    for item in filmes:
        if 'Temporada' in str(item):
            pass
        else:
            links = str(item)[28:]
            links = links.split("/\"")
            links_filmes.append(links[0])
            
            t = str(item).split('title=')
            t = t[1].replace('></a>','')
            t = t.replace("\"","")
            titulos2.append(t)
            
    return titulos2, links_filmes

def pega_torrents(links_filmes):
    cont = 0
    
    for item in links_filmes[1]:
        link_torrent = requests.get(item, headers=mozhdr)
        l2soupeddata = BeautifulSoup(link_torrent.content, "html.parser")

        
        torrentsmagnet = [x.find('a')['href'] for x in l2soupeddata.find_all('div', style="padding: 10px;text-align: center;font-size: 16px;")]

        print((links_filmes[0])[cont],'\n', torrentsmagnet[0])
        print('\n')
        cont+=1

pega_torrents(pegatitulo())
