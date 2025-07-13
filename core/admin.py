from django.contrib import admin
from .models import Project, Client, ContactFormEntry, NewsletterSubscriber

admin.site.register(Project)
admin.site.register(Client)
admin.site.register(ContactFormEntry)
admin.site.register(NewsletterSubscriber)

