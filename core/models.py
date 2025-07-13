from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(default="https://source.unsplash.com/600x400/?project")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    designation = models.CharField(max_length=100)
    image = models.URLField(default="https://source.unsplash.com/100x100/?person")

    def __str__(self):
        return self.name

class ContactFormEntry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

