from django.shortcuts import render
import django.http as http

# Create your views here.

def home(request):
    return http.HttpResponse("Hello World")
    # return render(request, 'home.html', {'name': 'Sachin'})
