# accounts/views.py
# from http.client import HTTPResponse
from copy import copy
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from course.models import Course
from .models import Marketer, Promotion
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
import copy
# from .forms import CustomUserCreationForm

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def add_promotion(request, ref_course, ref_user):
    c = Course.objects.get(reference_code = ref_course)
    u = Marketer.objects.get(reference_code = ref_user)
    promotion = Promotion()
    promotion.ref_course = ref_course
    promotion.ref_user = ref_user
    u.receive_money += (u.percentage * c.price)/100
    u.save()
    promotion.save()
    context = {'user_name' : u.user_name, 'course_name' : c.name}
    return render(request, 'thanks.html', context)

def Profile(request):
    current_user = request.user
    promotion = Promotion.objects.filter(ref_user = current_user.reference_code)
    promotions = []
    total = {
        'count': 0,
        'total': 0
        } 
    for i in promotion:
        c = Course.objects.filter(reference_code = i.ref_course)
        temp = {
        'cource_name': '',
        'cource_prise': '',
        'count': 1,
        'total': 0
        }
        if c:
            if not(serch_in_list_dict(promotions, c.name, (current_user.percentage * c.price)/100)):
                temp['cource_name'] = c.name
                temp['cource_prise'] = c.price
                temp['total'] = (current_user.percentage * c.price)/100
                promotions.append(copy.deepcopy(temp))
            
            total['count'] += 1
            total['total'] += (current_user.percentage * c.price)/100
    
    context = {'promotions' : promotions, 'total' : total}
    return render(request, 'registration/profile.html', context)

def serch_in_list_dict(list_dic, value, total):
    for i in list_dic:
        if i['cource_name'] == value:
            i['count'] += 1
            i['total'] += total
            return True
    return False

def Receive_Money(request):
    current_user = request.user
    current_user.receive_money = 0
    current_user.save()
    return HttpResponseRedirect('/users/profile/')

