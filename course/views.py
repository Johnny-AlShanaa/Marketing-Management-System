from django.shortcuts import render
from .models import Course
# Create your views here.

def home(request):
    courses = Course.objects.all()
    context = {'courses' : courses}
    return render(request, 'home.html', context)