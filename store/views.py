from django.shortcuts import render

from store.models import Product


# Create your views here.
def home(request):
    product = Product.objects.all()

    context = {'product': product}
    return render(request, 'store/home.html', context)
