from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
def index(request):
    context = {
        'numberic_data': NumericData.objects.all(),
        'main_quote': Quote.objects.all().first(),
        'quotes': Quote.objects.all(),
        'gallery': Gallery.objects.filter(main=True)[:6],
    }
    return render(request, "index.html", context)


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
    return render(request, "gallery.html", {
        'gallery': Gallery.objects.all(),
    })

def members(request):
    return render(request, "members.html", {
        'main': Member.objects.filter(main=True).first(),
        'members': Member.objects.filter(main=False).all(),
    })
