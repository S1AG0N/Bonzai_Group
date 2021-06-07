"""Bonzai_Group URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from schools import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("news/", views.news, name='news'),
    path("about/", views.about, name='about'),
    path("enroll/", views.enroll, name='enroll'),
    path("gallery/", views.gallery, name='gallery'),
    path("contact-us/", views.contact_us, name='contact-us'),
    path('bonzai-northend/', views.bhs, name='bonzai-northend'),
    path('bonzai-newton-park/', views.np, name='bonzai-newton-park'),
    path('bonzai-uitenhage/', views.ut, name='bonzai-uitenhage'),
    path('bonzai-kabega/', views.kabega, name='bonzai-kabega'),
    path('bonzai-sydenham/', views.sydenham, name='bonzai-sydenham'),
    path('<slug:slug>/', views.details, name='details'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)