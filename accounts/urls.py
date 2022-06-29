from django.urls import path
from .views import *

urlpatterns = [
    path('register',register, name='register'),
    path('logout', register, name='logout'),
    path('login', register, name='login')

]