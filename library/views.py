from django.shortcuts import render, redirect
from .models import *
def index(request):
    return render(request, "index.html", {})


def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent.")
        else:
            messages.error(request, "Invalid Message")
        return redirect('contact')
    return render(request, "contact.html", {})


def about(request):
    return render(request, "about.html", {})

def service(request):
    return render(request, "service.html", {})

def gallery(request):
    return render(request, "gallery.html", {})

def members(request):
    return render(request, "members.html", {})
