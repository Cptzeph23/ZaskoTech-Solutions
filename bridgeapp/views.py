from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def terms(request):
    return render(request, 'T&C.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def team(request):
    return render(request, 'team.html')

def website(request):
    return render(request, 'website.html')

def ecommerce(request):
    return render(request, 'ecommerce.html')

def mobileApp(request):
    return render(request, 'mobileApp.html')

def customSystems(request):
    return render(request, 'customSystems.html')

def booking(request):
    return render(request, 'booking.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def newsletter(request):
    return render(request, 'newsletter.html')
















