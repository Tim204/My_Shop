from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm
from coupons.models import Coupon


@require_POST
def cart_add(request, product_id):
    """Adds products to the cart or updates existing products"""
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])

    return HttpResponseRedirect(reverse('cart:cart_detail'))


@require_POST
def cart_remove(request, product_id):
    """Removes items from cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return HttpResponseRedirect(reverse('cart:cart_detail'))


def cart_detail(request):
    """Displays the cart and it's items"""
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'override': True}
        )
    coupon_apply_form = CouponApplyForm()
    coupon = Coupon.objects.filter(active=True)
    context = {
        'cart': cart,
        'coupon_apply_form': coupon_apply_form,
        'coupons': coupon,
    }
    return render(request, 'cart/detail.html', context)
