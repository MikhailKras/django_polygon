from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound


def get_home_page(request):
    data = {
        'resources': [
            ['others', 'others'],
        ]
    }
    return render(request, 'home/index.html', context=data)
