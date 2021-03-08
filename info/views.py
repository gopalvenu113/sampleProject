from django.shortcuts import render

from django.http import HttpResponse


def my_index(request):
    return HttpResponse("Welcome to my index page")


def end_page(request):
    return HttpResponse("Thank You for visiting my site")