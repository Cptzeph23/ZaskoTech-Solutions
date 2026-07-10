from .models import Contact, NewsLetter
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']



        
