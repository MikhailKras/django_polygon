from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound
from math import pi
import re
# Create your views here.


def rectangle_area(request, width: int, height: int) -> HttpResponse:
    area = width * height
    return render(request, 'geometry/rectangle.html')
    # return HttpResponse(f'<h1>The area of {width}x{height} rectangle is {area}<h1/>')


def square_area(request, size: int) -> HttpResponse:
    area = size ** 2
    return render(request, 'geometry/square.html')
    # return HttpResponse(f'<h1>The area of {size}x{size} square is {area}<h1/>')


def circle_area(request, radius: int) -> HttpResponse:
    area = round(pi * radius ** 2, 1)
    return render(request, 'geometry/circle.html')
    # return HttpResponse(f'<h1>The area of a circle of radius {radius} is {area}<h1/>')


def redirect_area(request, **kwargs):
    figure = request.path.split('/')[2]
    match figure:
        case 'get_circle_area':
            redirect_url = reverse('circle_name', args=(kwargs["radius"], ))
            return redirect(redirect_url)
        case 'get_rectangle_area':
            redirect_url = reverse('rectangle_name', args=(kwargs["width"], kwargs["height"]))
            return redirect(redirect_url)
        case 'get_square_area':
            redirect_url = reverse('square_name', args=(kwargs["size"], ))
            return redirect(redirect_url)
