from django.urls import path
from . import views as views_geometry

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views_geometry.rectangle_area),
    path('square/<int:size>/', views_geometry.square_area),
    path('circle/<int:radius>/', views_geometry.circle_area),
    path('get_rectangle_area/<int:width>/<int:height>', views_geometry.redirect_area),
    path('get_square_area/<int:size>/', views_geometry.redirect_area),
    path('get_circle_area/<int:radius>/', views_geometry.redirect_area),
]
