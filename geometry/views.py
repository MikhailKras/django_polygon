from django.shortcuts import render
from django.http import HttpResponse
from math import pi

# Create your views here.


def rectangle_area(request, width: int, height: int) -> HttpResponse:
    area = width * height
    return HttpResponse(f'<h1>The area of {width}x{height} rectangle is {area}<h1/>')


def square_area(request, size: int) -> HttpResponse:
    area = size ** 2
    return HttpResponse(f'<h1>The area of {size}x{size} square is {area}<h1/>')


def circle_area(request, radius: int) -> HttpResponse:
    area = round(pi * radius ** 2, 1)
    return HttpResponse(f'<h1>The area of a circle of radius {radius} is {area}<h1/>')
