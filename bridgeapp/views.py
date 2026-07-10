from email.message import Message

from django.http import JsonResponse
from django.shortcuts import redirect, render
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
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        # Basic safety validation check
        if not all([name, email, subject, message]):
            return JsonResponse({'error': 'All fields are required.'}, status=400)

        try:
            mymessage = Contact(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            mymessage.save()
            return JsonResponse({'success': True}, status=200)
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while saving your message.'}, status=500)
            
    else:
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
















