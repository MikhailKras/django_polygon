from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound
from faker import Faker
from random import randint

# Create your views here.


def get_menu_page(request):
    data = {
        'urls_names': [['reeves', 'info about Keanu Reeves'],
                       ['interesting_facts', 'interesting facts'],
                       ['people', 'people']
                       ],
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
    data = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'interest_facts/index.html', context=data)


def get_info_people(request):
    fake = Faker('en_US')
    number_of_people = 10
    people_info = []
    for _ in range(number_of_people):
        people_dict = {
            'name': fake.name(),
            'age': randint(20, 91),
            'phone': fake.phone_number(),
                       }
        people_info.append(people_dict)
    data = {
        'people_info': people_info
    }
    return render(request, 'people/index.html', context=data)
