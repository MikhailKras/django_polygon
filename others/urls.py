from django.urls import path
from . import views as views_others

urlpatterns = [
    path('reeves', views_others.get_info_keanu),
]