"""marketing_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from course import views as courseView
from users import views as userView

from django.views.static import serve
from django.conf.urls import url 

urlpatterns = [
    path("", courseView.home, name="home", ),
    path('<str:ref_course>/<str:ref_user>', userView.add_promotion),
    path('admin/', admin.site.urls),
    path("accounts/profile/", userView.Profile, name="profile"),
    path("users/", include("users.urls")),
    path("users/", include("django.contrib.auth.urls")),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
