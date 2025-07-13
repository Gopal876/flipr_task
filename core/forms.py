from django import forms
from .models import ContactFormEntry, NewsletterSubscriber

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormEntry
        fields = ['name', 'email', 'mobile', 'city']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
