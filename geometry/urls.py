from django.urls import path
from . import views as views_geometry

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views_geometry.rectangle_area),
    path('square/<int:size>/', views_geometry.square_area),
    path('circle/<int:radius>/', views_geometry.circle_area),
]
