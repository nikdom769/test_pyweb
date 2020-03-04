from django.urls import path, include
from login.views import LoginView

urlpatterns = [
    path('', LoginView.as_view()),
]
