from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def get_info_keanu(request):
    data = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'Мой личный штат Айдахо'
    }
    return render(request, 'reeves/index.html', context=data)
