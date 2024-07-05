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

def signup (request):
    return render(request, 'signup.html')

def order (request):
    return render(request, 'order.html')

def contact (request):
    return render(request, 'contact.html')


#//FIXME: add order confirmation and caculate price ...
def order_view(request):
    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
           order = form.save(commit=False)
           order.price = calculate_price(order.drink_type, order.size)
           order.save()
           send_order_confirmation(
               name=order.name,
               phone=order.phone,
               email=order.email,
               drink_type=order.drink_type,
               size=order.size,
               price=order.price
           )
        return redirect('main')
    else:
        form = Order()
    return render(request, 'order.html', {'form': form}) 