from bs4 import BeautifulSoup

import requests

# objeto site recebendo o conteúdo da requisição http do site
site = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/1383/canoas-rs").content

# objeto soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

# transforma html em string e o print vai exibir o html
print(soup.prettify())

canoas_temperatura_min = soup.find("span", id="min-temp-1")
canoas_temperatura_max = soup.find("span", id="max-temp-1")

print("Canoas\nTemperatura mínima: {}\nTemperatura máxima: {}".format(canoas_temperatura_min.string, canoas_temperatura_max.string))
# Canoas
# Temperatura mínima: 23°
# Temperatura máxima: 31°

print(soup.p.string)
# Previsão