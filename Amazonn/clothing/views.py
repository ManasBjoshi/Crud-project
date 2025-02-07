from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    prod = Product.objects.all()
    return render(request,'clothing/home.html',{"prod":prod})
 