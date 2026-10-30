from django.shortcuts import render
from django.http import HttpResponse;

def home(request):
    return HttpResponse("<h1>this is homepage</h1>")
def about_us(request):
    return HttpResponse("<h1>this is about us page</h1>")