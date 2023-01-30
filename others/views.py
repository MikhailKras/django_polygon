from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def get_menu_page(request):
    data = {
        'urls_names': [['reeves', 'Info about Keanu Reeves'], ['interesting_facts', 'Interesting facts']],
    }
    return render(request, 'menu/index.html', context=data)


def get_info_keanu(request):
    data = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'Мой личный штат Айдахо'
    }
    return render(request, 'reeves/index.html', context=data)


def get_info_facts(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'interest_facts/index.html', context=context)
