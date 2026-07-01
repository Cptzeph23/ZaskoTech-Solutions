from django.urls import path
from . import views, admin
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('T&C/', views.terms, name='terms'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('team/', views.team, name='team'),

]
