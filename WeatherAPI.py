import requests
import json 
from datetime import datetime

class weather():
    

    def __init__(self, lat:float, lon:float):
        self.lat = lat
        self.lon = lon


    def prevTempo(self):
        latitude = self.lat
        longitude = self.lon
        key = "707807e0922f41c621c5c65f70ecd528"
        api  =f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={key}"
        response = requests.get(api)
        return response.text

coord = weather(-22.212481,-49.938074)



PrevTempoStr = coord.prevTempo()

result = json.loads(PrevTempoStr)


tempAtual = float(result['main']['temp'])-273.15

cidade = result['name']

porDosol = datetime.fromtimestamp(result['sys']['sunset'])

print(f"Olá! Você atualmente está em {cidade}, a temperatura atual é: {tempAtual} graus célcius, o pôr do sol foi em: {porDosol}")

