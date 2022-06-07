from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from coupons.forms import CouponApplyForm
from .models import OrderItem
from cart.cart import Cart
from .forms import OrderCreateForm
from .tasks import order_created

# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
             # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    
    coupon_apply_form = CouponApplyForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form, 'coupon_apply_form': coupon_apply_form})
