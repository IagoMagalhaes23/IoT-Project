'''
    Autor: Iago, Rhuan, Katielly, Acassio e Flavia
    Data: 23/06/2024
    Descrição: Classe responsável pelas falas do robô.
'''

from gtts import gTTS
import os
import pyttsx3

def fala(frase):
    '''
        Função para realizar uma saudação através de fala pelo robô
    '''
    lingua = 'pt'

    tts = gTTS(text=frase, lang=lingua)

    engine = pyttsx3.init()

    # Selecionar uma voz específica pelo ID
    voice_id = "com.apple.speech.synthesis.voice.diego"
    engine.setProperty('voice', voice_id)

    # Converter texto em fala com pyttsx3 para usar a voz selecionada
    engine.say(frase)
    engine.runAndWait()

def saudacao(frase):
    '''
        Função para realizar uma saudação através de fala pelo robô
    '''
    lingua = 'pt'

    tts = gTTS(text=frase, lang=lingua)

    engine = pyttsx3.init()

    # Selecionar uma voz específica pelo ID
    voice_id = "com.apple.speech.synthesis.voice.diego"
    engine.setProperty('voice', voice_id)

    # Converter texto em fala com pyttsx3 para usar a voz selecionada
    engine.say(frase)
    engine.runAndWait()