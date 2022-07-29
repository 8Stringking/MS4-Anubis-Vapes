from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LR26WK7ad8LPnXB49WAYkIFeR8pjjD5bmZae0IiS7MWjnYx7B6kepU7z9M90ZNf94PAzJFqBd2pcFACdoHY7uxL00zPiO1ckz'
    }

    return render(request, template, context)
