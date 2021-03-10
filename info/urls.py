from django.urls import path

from . import views


urlpatterns = [
    path('home', views.my_index, name='my_index'),
    path('home/<int:emp_id>', views.my_detailed_view, name='my_detailed_view')
    # path('end', views.end_page, name='end_page')
]
