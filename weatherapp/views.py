from django.http import HttpResponse
from django.shortcuts import render
import requests

def image(request):
     if request.method == 'POST':
        value = request.POST.get('data')  # Get city name from the form
        url = f"http://api.weatherapi.com/v1/forecast.json?key=0ca0c1fe27ab4d44879184203240510&q={value}&lang=hi&alerts=yes&aqi=yes&days=10"

        response = requests.get(url)
        data = response.json()
        
        datalist={
           "data":data,

        }
        
     return render(request,'weatherView.html',datalist)
def views(request):
    return render(request,'weatherView.html')