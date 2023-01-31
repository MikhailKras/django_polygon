from django.urls import path
from . import views as views_others

urlpatterns = [
    path('', views_others.get_menu_page),
    path('reeves', views_others.get_info_keanu),
    path('interesting_facts', views_others.get_info_facts),
    path('people', views_others.get_info_people)
]
