from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class NewsLetter(models.Model):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email    


class BookingRequest(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'New'
        REVIEWING = 'reviewing', 'Reviewing'
        SCHEDULED = 'scheduled', 'Scheduled'
        CLOSED = 'closed', 'Closed'

    name = models.CharField(max_length=100)
    company = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    service = models.CharField(max_length=120)
    project_type = models.CharField(max_length=120, blank=True)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    budget = models.CharField(max_length=120, blank=True)
    preferred_contact = models.CharField(max_length=30, default='WhatsApp')
    message = models.TextField()
    consent = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.service}'
    
