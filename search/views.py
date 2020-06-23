from django.shortcuts import render
from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})