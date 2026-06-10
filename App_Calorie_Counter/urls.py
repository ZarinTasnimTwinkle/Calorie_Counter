from django.urls import path
from .views import *

urlpatterns = [
    path('register/',registerPage,name='register'),
    path('',loginPage,name='login'),
    path('logout/',logoutPage,name='logout'),
    path('UserEdit/',UserEditPage,name='UserEdit'),
    path('dashboard/',dashboardPage,name='dashboard')
]
