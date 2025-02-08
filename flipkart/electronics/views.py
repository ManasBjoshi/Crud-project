from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Product
from .forms import ProductForm
# Create your views here.


def home(request):
    data=""
    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ProductForm()
        data = Product.objects.all()
    form = ProductForm() 
    return render(request,'electronics/home.html',{'data':data,'form':form})
    