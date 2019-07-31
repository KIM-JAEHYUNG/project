from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User


# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products_html':products})
    
    
def register(request):
    return render(request, 'register.html')
    
    
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        product = Product.objects.create(title = title,description = description,price = price,image = image)
        return redirect('app:product')
    return render(request, 'app/register.html')
    

def login(request):
    return render(request, 'login.html')