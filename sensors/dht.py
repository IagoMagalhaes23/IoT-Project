'''
    Autor: Iago, Rhuan, Katielly, Acassio e Flavia
    Data: 17/06/2024
    Descrição: Classe responsável pelo controle do sensor DHT.
'''

import Adafruit_DHT
import time

# Definir o tipo de sensor e o pino de dados
sensor = Adafruit_DHT.DHT11
pin = 27

def getTemperatura():
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
        
    if humidity is not None and temperature is not None:
        print("Temperatura: {:.1f}°C  Umidade: {:.1f}%".format(temperature, humidity))
    else:
        print("Falha ao ler do sensor.")

    return humidity, temperature