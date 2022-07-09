import requests
from django.shortcuts import render

def index(request):

	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f308856b26263c8f13c2c191c9ae1ab1'
	city = 'Karaganda'

	r = requests.get(url.format(city)).json()

	city_weather = {
		'city' : city,
		'temperature' : r['main']['temp'], 
		'description' : r['weather'][0]['description'],
		'icon' : r['weather'][0]['icon'],
	}

	context = {'city_weather': city_weather}

	return render(request, 'index.html', context)