from django.shortcuts import render

# Create your views here.
def main (request):
    return render(request, 'main.html')

def about (request):
    return render(request, 'about.html')

def login (request):
    return render(request, 'login.html')

def order (request):
    return render(request, 'order.html')

def contact (request):
    return render(request, 'contact.html')

