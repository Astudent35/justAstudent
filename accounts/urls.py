from django.urls import path, include
from . import views

urlpatterns = [
    path('SignUp', views.signup, name="SignUp"),
    path('Login', views.login, name='Login'),
    path('LogOut', views.logout, name="LogOut"),
]