from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    cart[product_id_str] = cart.get(product_id_str, 0) + 1
    request.session['cart'] = cart
    return redirect('/cart')

def delete_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    new_amount = cart.get(product_id_str, 1) - 1
    if new_amount > 0:
        cart[product_id_str] = new_amount
    else:
        del cart[product_id_str]
    request.session['cart'] = cart
    return redirect('/cart')
    

def cart_detail(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_products = []
    for product in products:
        cart_products.append({
            'product': product,
            'quantity': cart[str(product.id)]
        })

    return render(request, 'shop/cart.html', {'cart_products': cart_products})


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')

