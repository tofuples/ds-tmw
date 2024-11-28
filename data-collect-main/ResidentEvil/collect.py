# %%
import requests
from bs4 import BeautifulSoup

def get_content(url):
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/ xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,    application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
    'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://www.residentevildatabase.com/   personagens/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0    Safari/537.36',
}

    response = requests.get(url, headers=headers)
    return response
# %%
url = "https://www.residentevildatabase.com/personagens/ada-wong/"    
    
response = get_content(url)
    
response.status_code
# %%
response.text
# %%

soup = BeautifulSoup(response.text)
soup
# %%
div_page = soup.find("div", class_="td-page-content") #busca a div 
div_page
# %%
paragrafo = div_page.find_all("p")[1] #busca o parágrafo
paragrafo
# %%
ems = paragrafo.find_all("em")
ems
# %%

ems[0].text
# %%
data = {}
for i in ems:
    chave, valor = i.text.split(":") #cada parto do split é atribuido chave e valor
    chave = chave.strip(" ")
    data[chave] = valor.strip(" ")
    
data
# %%
print(data.keys())
# %%
data["Altura"]
# %%
 