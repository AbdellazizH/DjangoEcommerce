from django.shortcuts import render, get_object_or_404

from store.models import Product


# Create your views here.
def home(request):
    product = Product.objects.all()

    context = {'product': product}
    return render(request, 'store/home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {'product': product}
    return render(request, 'store/product_detail.html', context)
