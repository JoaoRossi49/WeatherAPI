import requests
import json 
import csv
from datetime import datetime

class weather():
    #Método construtor armazenando key de api, url e alimentando os dados
    #em formato json
    def __init__(self, lat:float, lon:float):
        self.lat = lat
        self.lon = lon
        key = "707807e0922f41c621c5c65f70ecd528"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={key}"
        self.dados = json.loads((requests.get(api)).text)

    #Crude para acessar dados vindos da API
    def getCidade(self):
        return self.dados['name']
    
    def getTemp(self):
        return self.dados['main']['temp']-273.15

    def getPordoSol(self):
        return datetime.fromtimestamp(self.dados['sys']['sunset'])



arquivo = open(r"municipios.csv", encoding='utf-8')

tabela = csv.reader(arquivo, delimiter=',')

nome = []
lat = []
lon = []

for i in tabela:
    nome.append(i[1])
    lat.append(i[2])
    lon.append(i[3])


while True:
    index = nome.index(input('Digite o nome da cidade desejada--> '))
    coord = weather(lat[index], lon[index])
    print(f'Você escolheu a cidade {nome[index]}, a temperatura atual é {coord.getTemp()}, o por do sol foi em {coord.getPordoSol()}')
    resp = input('Gostaria de selecionar outra cidade? (Y/N)')
    try:
        if resp == 'Y':
            pass
        if resp == 'N':
            print('Obrigado por usar WeatherAPI!')
            break
    except TypeError:
        print('Valor inválido!')
        pass
        
