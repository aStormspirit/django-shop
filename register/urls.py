from django.contrib import admin
from django.urls import path, include
from .views import login_view, RegisterView, user_logout, LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='Login'),
    path('register/', RegisterView.as_view(), name='Register'),
    path('logout/', user_logout, name='Logout'),
]
