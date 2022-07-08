# accounts/urls.py
from django.urls import path

from .views import SignUpView
from .views import Profile, Receive_Money


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", Profile, name="profile"),
    path("profile/receive_money", Receive_Money, name="receive_money"),
]