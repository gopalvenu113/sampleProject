from django.urls import path

from . import views


urlpatterns = [
    path('home', views.my_index, name='my_index'),
    path('end', views.end_page, name='end_page')
]
