from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# from superlists.lists.views import home_page


def home_page(request):
    return render(request, 'home.html')

