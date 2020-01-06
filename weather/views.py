from django.shortcuts import render
from .models import City
import requests
from .forms import CityForm



# Create your views here. 
def index(request):
    appid="3d22940be1eb70fcfe47f0fc0de9a7fa"
    url="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+ appid
    
    if(request.method=="POST"):
        form=CityForm(request.POST)
        if form.is_valid():
            form.save()
           
    
    form=CityForm()

    cities=City.objects.all()
    all_cities=[]
    for city in cities:
        res=requests.get(url.format(city.name)).json()

        city_info={
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
            }
        all_cities.append(city_info)
    context={
        'all_info': all_cities,
        'form': form
    }

    return render (request, 'weather/index.html', context)

