from django.shortcuts import render

def home(request):
    return render(request, 'sneakers_brand/home.html')

def about(request):
    return render(request, 'sneakers_brand/about.html')


def contact(request):
    return render(request, 'sneakers_brand/contact.html')