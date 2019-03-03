from django.http import HttpResponse
import RPi.GPIO as GPIO
import json
print('imprted {}'.format(GPIO.__name__))


def set_pin(pin, signal):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, signal)
    if signal:
    	signal = 'ON'
    else:
    	signal = 'OFF'
    dane2 = dict(signal=signal) 
    data = json.JSONEncoder() # konwersja danych z pythona na JSON
    dane = data.encode(dane2)
    return dane
    

def t_func():
    return 'udalo sie'

def home(request):
    return HttpResponse('HOME PAGE')

def turnOn(request):
	# set_pin(21,1)
    print('gpio on')
    return HttpResponse(set_pin(21,1))

def turnOff(request):
    print('gpio off')
    # set_pin(21,0)
    return HttpResponse(set_pin(21,0))




