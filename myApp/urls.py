from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('apointment/', views.apointment, name='apointment'),
    path('doctors/', views.doctors, name="doctors"),
    path('services/', views.services, name='services'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    
    #Mpesa API urls
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),


]