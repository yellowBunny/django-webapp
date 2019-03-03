from django.shortcuts import render
import os
print(os.getcwd())
from rasp import blink as b
from django.http import HttpResponse

# Create your views here.

def home(request):
    varible = b.t_func
    return render(request, 'home.html', {'on': varible})

def blink(request):
    varible = b.t_func
    return render(request, 'blink.html', {'on': varible})

def process(request):
    print('tu process')    
    return HttpResponse(b.set_pin(21,1))

def process2(request):
    print('tu process2')    
    return HttpResponse(b.set_pin(21,0))


