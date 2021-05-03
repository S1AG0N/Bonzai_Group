from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import School, New
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CreateUserForm


def home(request):
    xul = School.objects.all()
    return render(request, 'schools/home.html', {'xul': xul})


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully created your account!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'schools/register.html', context)


def logout_request(request):
    logout(request)
    messages.warning(request, "Logged out successfully!")
    return redirect("home")


def login_request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect!")

    context = {}
    return render(request, "schools/login.html", context)


def news(request):
    articles = New.objects.all()
    return render(request, "schools/news.html", {'articles': articles})


def details(request, slug):
    detail = New.objects.get(slug=slug)
    return render(request, "schools/detail.html", {'detail': detail})

