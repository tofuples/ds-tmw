# %%
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd

headers = {
        'accept': 'text/html,application/xhtml+xml,application/ xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,    application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://www.residentevildatabase.com/personagens/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

def get_content(url):
    response = requests.get(url, headers=headers)
    return response

def get_basic_info(soup): 
    div_page = soup.find("div", class_="td-page-content") #busca a div 
    paragrafo = div_page.find_all("p")[1] #busca o parágrafo
    ems = paragrafo.find_all("em")
    data = {}
    for i in ems:
        chave, valor, *_ = i.text.split(":") #cada parto do split é atribuido chave e valor
        chave = chave.strip(" ")    
        data[chave] = valor.strip(" ")  
    
    return data

def get_aparicoes(soup): 
    lis = (soup.find("div", class_="td-page-content")
          .find("h4")
          .find_next()
          .find_all("li"))

    aparicoes = [i.text for i in lis]
    return aparicoes

def get_personagem_infos(url):   
    response = get_content(url)
    if response.status_code != 200:
        print("Não foi possível coletar os dados!")
        return {}
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = get_basic_info(soup)
        data["Aparicoes"] = get_aparicoes(soup)    
        return data

def get_links():
    url = "https://www.residentevildatabase.com/personagens/"
    response = requests.get(url, headers=headers)
    soup_personagens = BeautifulSoup(response.text, 'html.parser')
    ancoras = (soup_personagens.find("div", class_="td-page-content")
                    .find_all("a"))

    links = [i["href"] for i in ancoras]           
    return links

# %%
links = get_links()
data = []
for i in tqdm(links):
    print(i)
    d = get_personagem_infos(i)
    d["link"] = i
    nome = i.strip("/").split("/")[-1].replace("-", " ").title()
    d["Nome"] = nome
    data.append(d)
# %%
df = pd.DataFrame(data)
df

# %%
