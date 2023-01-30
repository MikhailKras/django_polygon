from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound


def get_home_page(request):
    return render(request, 'home/index.html')
