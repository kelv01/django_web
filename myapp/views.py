#views

from django.shortcuts import render, redirect

from .models import Order

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



def order_view(request):
    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = Order()
    return render(request, 'order.html', {'form': form})