'''
    Autor: Iago, Rhuan, Katielly, Acassio e Flavia
    Data: 17/06/2024
    Descrição: Classe responsável pelo controle do sensor Ultrassônico.
'''

import RPi.GPIO as GPIO
import time

# Configuração dos pinos
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24

print("Configuring HC-SR04")

# Configura os pinos do TRIG e ECHO
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def distancia():
    # Certifica que o TRIG está desativado
    GPIO.output(TRIG, False)
    time.sleep(2)

    # Gera um pulso de 10us no TRIG para iniciar a medição
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calcula o tempo de duração do pulso
    pulse_duration = pulse_end - pulse_start

    # Calcula a distância (velocidade do som = 34300 cm/s)
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print("Distância: {} cm".format(distance))

    return distance