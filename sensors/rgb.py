'''
    Autor: Iago, Rhuan, Katielly, Acassio e Flavia
    Data: 17/06/2024
    Descrição: Classe responsável pelo controle do led RGB.
'''

import RPi.GPIO as GPIO

# Define os pinos para os LEDs vermelho, verde e azul
LED_RED = 18
LED_GREEN = 22
LED_BLUE = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(LED_BLUE, GPIO.OUT)

# Função para ligar os LEDs vermelho, verde e azul
def set_color(red, green, blue):
    GPIO.output(LED_RED, red)
    GPIO.output(LED_GREEN, green)
    GPIO.output(LED_BLUE, blue)