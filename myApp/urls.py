from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('apointment/', views.apointment, name='apointment'),
    path('doctors/', views.doctors, name="doctors"),
    path('services/', views.services, name='services'),

]