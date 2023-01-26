from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from math import pi
import re
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


def redirect_area(request, **kwargs):
    figure = request.path.split('/')[2]
    match figure:
        case 'get_circle_area':
            return redirect(f'/calculate_geometry/circle/{kwargs["radius"]}')
        case 'get_rectangle_area':
            return redirect(f'/calculate_geometry/rectangle/{kwargs["width"]}/{kwargs["height"]}')
        case 'get_square_area':
            return redirect(f'/calculate_geometry/square/{kwargs["size"]}')
