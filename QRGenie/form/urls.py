from django.contrib import admin
from django.urls import path, include
from form import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    path('form', views.generate_qr_code, name = 'generate_qr_code'),
    path('form1', views.form1, name = 'form1')
    # path('abc', views.abc, name = 'abc')
]