from django.contrib import admin
from django.urls import path
from . import views
import os
print(os.getcwd(),'sciezka')

urlpatterns = [
	path('', views.home, name='home'),
    path('blink/', views.blink, name='blink'),
    path('process/', views.process, name='process'),
    path('process2/', views.process2, name='process2'),
]
