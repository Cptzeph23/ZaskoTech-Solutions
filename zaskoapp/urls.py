from django.urls import path
from . import views, admin
from django.contrib import admin
urlpatterns = [
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap'),
    path('sitemaps.xml', views.sitemap_xml, name='sitemaps'),
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('T&C/', views.terms, name='terms'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('team/', views.team, name='team'),
    path('website/', views.website, name='website'),
    path('ecommerce/', views.ecommerce, name='ecommerce'),
    path('mobileApp/', views.mobileApp, name='mobileApp'),
    path('customSystems/', views.customSystems, name='customSystems'),
    path('booking/', views.booking, name='booking'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('newsletter/', views.newsletter, name='newsletter'),

]
