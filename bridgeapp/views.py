import logging
import threading
import json
import urllib.error
import urllib.request
from datetime import date
from datetime import time as time_cls

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import BookingRequest, Contact, NewsLetter

logger = logging.getLogger(__name__)


def _send_resend_email(*, subject, text, to):
    if not settings.RESEND_API_KEY:
        logger.warning('Resend API key is missing; skipping outbound email.')
        return

    payload = {
        'from': settings.DEFAULT_FROM_EMAIL,
        'to': [to] if isinstance(to, str) else list(to),
        'subject': subject,
        'text': text,
    }

    request = urllib.request.Request(
    'https://api.resend.com/emails',
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Authorization': f'Bearer {settings.RESEND_API_KEY}',
        'Content-Type': 'application/json',
        'User-Agent': 'ByteBridge-Technologies/1.0 (+https://cukcu.org)',
        'Accept': 'application/json',
    },
    method='POST',
)

    try:
        with urllib.request.urlopen(request, timeout=settings.RESEND_TIMEOUT) as response:
            payload = response.read().decode('utf-8', errors='replace').strip()
            if payload:
                logger.info('Resend accepted email: %s', payload)
    except urllib.error.HTTPError as exc:
        details = exc.read().decode('utf-8', errors='replace') if exc.fp else ''
        logger.error('Resend rejected email request with HTTP %s: %s', exc.code, details)
        raise RuntimeError(f'Resend API returned HTTP {exc.code}: {details}') from exc


def _send_booking_notifications(booking_request, email_body, email, phone, name):
    try:
        _send_resend_email(
            subject=f'Booking request: {booking_request.service}'[:200],
            text=(
                'A new booking request has been submitted.\n\n'
                f'{email_body}\n\n'
                f'Status: {booking_request.get_status_display()}\n'
                f'Reply to: {email} / {phone}'
            ),
            to=settings.BOOKING_NOTIFICATION_EMAIL,
        )
    except Exception:
        logger.exception('Booking was saved, but the notification email failed.')

    if getattr(settings, 'BOOKING_COPY_TO_CUSTOMER', False):
        try:
            _send_resend_email(
                subject='We received your booking request',
                text=(
                    f'Hi {name},\n\n'
                    'Thanks for booking with ByteBridge Technologies. We have received your request and will get back to you shortly.\n\n'
                    f'Your request summary:\n{email_body}\n\n'
                    'If you need urgent help, you can reply to this email or call us directly on +254703297902.'
                ),
                to=email,
            )
        except Exception:
            logger.exception('Booking was saved, but the customer copy email failed.')

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
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        company = request.POST.get('company', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        service = request.POST.get('service', '').strip()
        project_type = request.POST.get('project_type', '').strip()
        preferred_date = request.POST.get('date', '').strip()
        preferred_time = request.POST.get('time', '').strip()
        budget = request.POST.get('budget', '').strip()
        preferred_contact = request.POST.get('contact_preference', 'WhatsApp').strip() or 'WhatsApp'
        message = request.POST.get('message', '').strip()
        consent = request.POST.get('consent', '').strip()

        if not all([name, email, phone, service, preferred_date, preferred_time, message, consent]):
            return HttpResponse('Please complete all required booking fields.', status=400)

        try:
            validate_email(email)
        except ValidationError:
            return HttpResponse('Please enter a valid email address.', status=400)

        try:
            requested_date = date.fromisoformat(preferred_date)
        except ValueError:
            return HttpResponse('Please choose a valid booking date.', status=400)

        try:
            requested_time = time_cls.fromisoformat(preferred_time)
        except ValueError:
            return HttpResponse('Please choose a valid booking time.', status=400)

        if requested_date < date.today():
            return HttpResponse('Please choose a future booking date.', status=400)

        subject = f'Booking request: {service}'[:200]
        details = [
            f'Name: {name}',
            f'Company: {company}' if company else None,
            f'Email: {email}',
            f'Phone: {phone}',
            f'Service: {service}',
            f'Project type: {project_type}' if project_type else None,
            f'Preferred date: {preferred_date}',
            f'Preferred time: {preferred_time}',
            f'Budget: {budget}' if budget else None,
            f'Preferred contact: {preferred_contact}',
            '',
            'Project notes:',
            message,
        ]
        email_body = '\n'.join([line for line in details if line is not None])

        try:
            booking_request = BookingRequest.objects.create(
                name=name,
                email=email,
                company=company,
                phone=phone,
                service=service,
                project_type=project_type,
                preferred_date=requested_date,
                preferred_time=requested_time,
                budget=budget,
                preferred_contact=preferred_contact,
                message=message,
                consent=bool(consent),
            )
        except Exception:
            logger.exception('Failed to save booking request.')
            return HttpResponse('We could not save your booking right now. Please try again.', status=500)

        threading.Thread(
            target=_send_booking_notifications,
            args=(booking_request, email_body, email, phone, name),
        ).start()

        return HttpResponse('OK')

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




