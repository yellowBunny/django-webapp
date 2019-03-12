from django.http import HttpResponse
# import RPi.GPIO as GPIO
import json
# print('imprted {}'.format(GPIO.__name__))

class PinControler():
    STATUS = 'nothing'

    def set_pins(self, pin, signal):
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(pin, GPIO.OUT)
        # GPIO.output(pin, signal)
        if signal:
            signal = 'ON'
            self.STATUS = signal
        else:
            signal = 'OFF'
            self.STATUS = signal
        dane2 = dict(signal=signal)
        data = json.JSONEncoder() # konwersja danych z pythona na JSON
        dane = data.encode(dane2)
        return dane






