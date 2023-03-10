from django.urls import path
from . import views as views_others

urlpatterns = [
    path('', views_others.get_menu_page, name='other-home'),
    path('reeves', views_others.get_info_keanu),
    path('interesting_facts', views_others.get_info_facts),
    path('people', views_others.get_info_people),
    path('beautiful_table', views_others.get_beautiful_table)
]
