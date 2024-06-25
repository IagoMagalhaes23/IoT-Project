import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

bt_verde = 3
bt_vermelho = 2
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(bt_verde, GPIO.IN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(bt_vermelho, GPIO.IN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

def botao_verde():
    if GPIO.input(bt_verde) == GPIO.HIGH:
        print("Button was pushed!")
    else:
        return 1
    
def botao_vermelho():
    if GPIO.input(bt_vermelho) == GPIO.HIGH:
        print("Button was pushed!")
    else:
        return 1