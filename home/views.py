from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines('<h1>Hello world</h1>')
    response.write('effort to learn django')
    return response
  
