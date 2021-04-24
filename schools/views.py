from django.shortcuts import render
from .models import School


def home(request):
    xul = School.objects.all()
    return render(request, 'schools/home.html', {'xul': xul})
