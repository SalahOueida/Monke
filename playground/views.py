from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculate():
    x = 1
    y = 2
    z = x+y
    return z


def say_hello(request):
    z = calculate()
    return render(request, 'hello.html', {'name': 'Salah'})