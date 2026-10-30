from django.urls import path
from website.views import *

urlpatterns = [
    path('home', home),
    path('about-us', about_us),
]