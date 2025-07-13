from django.shortcuts import render, redirect
from .models import Project, Client
from .forms import ContactForm, NewsletterForm

def home(request):
    projects = Project.objects.all()
    clients = Client.objects.all()
    contact_form = ContactForm()
    newsletter_form = NewsletterForm()

    if request.method == 'POST':
        if 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                return redirect('/')
        elif 'newsletter_submit' in request.POST:
            newsletter_form = NewsletterForm(request.POST)
            if newsletter_form.is_valid():
                newsletter_form.save()
                return redirect('/')

    return render(request, 'core/home.html', {
        'projects': projects,
        'clients': clients,
        'contact_form': contact_form,
        'newsletter_form': newsletter_form,
    })
