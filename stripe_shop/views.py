from django.conf import settings
from django.shortcuts import redirect
from rest_framework.views import APIView
from django.views.generic import DetailView, TemplateView

from stripe_shop.models import Item

import stripe


stripe.api_key = 'sk_test_51OHxKmG1VxuZMZu8MJE6te8oDBSGLqm1f46p57fqchbs5b9HztN83cVJUEog3xBhnBMmn0V8OTuXfT453bvphFRR00LmooEAYU'


class SessionCreateAPIView(APIView):

    def get(self, request, pk, *args, **kwargs):
        item = Item.objects.get(pk=pk)
        stripe_product = stripe.Product.create(
            name=item.name,
            description=item.description
        )
        price = stripe.Price.create(
            unit_amount=int(item.price*100),
            currency="usd",
            product=stripe_product.id
        )
        session = stripe.checkout.Session.create(
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
            mode="payment",
            line_items=[
                {
                  "price": price.id,
                  "quantity": 1
                }
            ]
        )
        return redirect(session.url)
    

class ItemDetailView(DetailView):
    model = Item


class SuccessView(TemplateView):
    template_name = "stripe_shop/success.html"

class CancelView(TemplateView):
    template_name = "stripe_shop/cancel.html"