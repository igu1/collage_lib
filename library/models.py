from django.db import models
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm


class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(max_length=2048, upload_to='gallery')
    def __str__(self):
        return self.name
    
    
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name
    
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']
    
class NumberOfBooks(models.Model):
    count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if NumberOfBooks.objects.exists() and self.pk is None:
            alert_message = "Only one instance of Number Of Book is allowed."
            return HttpResponseRedirect(reverse("admin:index") + f"?alert={alert_message}")
        return super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        if NumberOfBooks.objects.exists():
            return NumberOfBooks.objects.first()
        return NumberOfBooks.objects.create()

    def __str__(self):
        return f"Books: {self.count}"

    class Meta:
        verbose_name_plural = "Number Of Books"
        
class Quote(models.Model):
    quote = models.CharField(default="Discover the magic of books at our library, where imagination knows no bounds", blank=True, max_length=2048)

    def save(self, *args, **kwargs):
        if Quote.objects.exists() and self.pk is None:
            alert_message = "Only one instance of Quote is allowed."
            return HttpResponseRedirect(reverse("admin:index") + f"?alert={alert_message}")
        return super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        if Quote.objects.exists():
            return Quote.objects.first()
        return Quote.objects.create()

    def __str__(self):
        return f"Quote: {self.quote}"

    class Meta:
        verbose_name_plural = "Main Page Quote"
        
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')
    def __str__(self):
        return self.title