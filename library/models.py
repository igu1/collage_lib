from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Member(models.Model):
    name = models.CharField(max_length=100)
    main = models.BooleanField(default=False)
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
    
class NumericData(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name}: {self.count}"

    class Meta:
        verbose_name_plural = "NumericDatas"
        
class Quote(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = ProcessedImageField(upload_to='quote',
                                           processors=[ResizeToFill(200, 300)],
                                           format='PNG',
                                           options={'quality': 100}, null=True)                                
    quote = models.CharField(default="No Quote Given", blank=True, max_length=2048)

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
    image = ProcessedImageField(upload_to='gallery',
                                           format='PNG',
                                           options={'quality': 50}, null=True)
    main = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Gallery"