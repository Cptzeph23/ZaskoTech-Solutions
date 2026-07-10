from django.http import JsonResponse
from django.shortcuts import render
from .models import Contact, NewsLetter

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
    if request.method == 'POST':
        email_address = request.POST.get('email', '').strip()
        
        if not email_address:
            return JsonResponse({'error': 'Email field cannot be empty.'}, status=400)
            
        if NewsLetter.objects.filter(email=email_address).exists():
            return JsonResponse({'error': 'This email is already subscribed!'}, status=400)
            
        try:
            subscriber = NewsLetter(email=email_address)
            subscriber.save()
            return JsonResponse({'success': True}, status=200)
        except Exception as e:
            return JsonResponse({'error': 'Failed! Check your email address.'}, status=500)
            
    return JsonResponse({'error': 'Invalid request.'}, status=400)
















