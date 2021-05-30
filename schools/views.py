from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import School, New
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CreateUserForm
from django.core.mail import send_mail


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


'''bonzai high school northend '''


def bhs(request):
    context = {}
    return render(request, 'schools/bonzai-northend.html', context)


def np(request):
    context = {}
    return render(request, 'schools/bonzai-newton-park.html', context)


def ut(request):
    context = {}
    return render(request, 'schools/bonzai-uitenhage.html', context)


def sydenham(request):
    context = {}
    return render(request, 'schools/bonzai-sydenham.html', context)


def kabega(request):
    context = {}
    return render(request, 'schools/bonzai-kabega.html', context)


def details(request, slug):
    detail = New.objects.get(slug=slug)
    return render(request, "schools/detail.html", {'detail': detail})


'''schools header'''


def schools_header(request):
    xul = School.objects.all()
    return render(request, 'schools/schools_header.html', {'xul': xul})


'''enroll'''


def enroll(request):
    schools = School.objects.all()
    return render(request, 'schools/enroll.html', {'schools': schools})


def contact_us(request):
    schools = School.objects.all()
    if request.method == 'POST':
        fname = request.POST.get('fname')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        data = {
            'fname': fname,
            'subject': subject,
            'email': email,
            'comment': comment,
        }
        message = '''
        From: {}
        Subject: {}       
        Message: {}
        
        '''.format(data['email'], data['subject'], data['comment'])
        send_mail(data['subject'], message, data['email'], ['acconline17@gmail.com'])
    return render(request, 'schools/contact-us.html', {'schools': schools})


def gallery(request):
    return render(request, 'schools/gallery.html', {})