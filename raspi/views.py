from django.shortcuts import render
import os
print(os.getcwd())
from rasp.blink import PinControler
from django.http import HttpResponse

# Create your views here.
pinControler = PinControler()

def home(request):
    status = pinControler.STATUS
    return render(request, 'home.html', {'on': status})

def blink(request):
    status = pinControler.STATUS
    return render(request, 'blink.html', {'status': status})

def process(request):
    print('tu process')
    return HttpResponse(pinControler.set_pins(21,1))

def process2(request):
    print('tu process2')
    return HttpResponse(pinControler.set_pins(21,0))


