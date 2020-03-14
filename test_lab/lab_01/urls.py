"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from lab_01.views import Home, About, Blog, BlogDetails, Contact, Services, MessageView, BlogView, EmailView

urlpatterns = [
    path('index.html', Home.as_view()),
    path('about.html', About.as_view()),
    path('contact.html', Contact.as_view()),
    path('services.html', Services.as_view()),
    path('blog.html', Blog.as_view()),
    path('blog-details.html', BlogDetails.as_view()),
    path('', MessageView.as_view()),
    path('', BlogView.as_view()),
    path('', EmailView.as_view()),
]

