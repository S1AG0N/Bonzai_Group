from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import School
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def home(request):
    xul = School.objects.all()
    return render(request, 'schools/home.html', {'xul': xul})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} you have been successfully registered!")
            login(request, user)
            messages.info(request, f"You are now logged in as: {username}")
            return redirect('/')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = UserCreationForm
    return render(request, 'schools/register.html', {'form': form})


