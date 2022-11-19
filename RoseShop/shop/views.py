import stripe
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Item, Price
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        domain = "http://127.0.0.1:8000"  # change in production

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card', 'p24', 'blik'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': request.POST['quantity'],
                },
            ],
            mode='payment',
            success_url=domain + '/?success=true',
            cancel_url=domain + '/?success=false',
        )
        return redirect(checkout_session.url)


class Index(View):
    def get(self, request):
        highlighted = Item.objects.all().filter(highlighted=True)
        return render(request, "index.html", {"items": highlighted})


class ItemDetails(View):
    def get(self, request, item_id):
        item_ = get_object_or_404(Item, id=item_id)
        prices = Price.objects.filter(item=item_)
        remaining_units = item_.total_units-item_.sold_units

        images = [item_.image_one, item_.image_two, item_.image_three]

        return render(request, "item.html", {"item": item_, "remaining_units": remaining_units, "price": prices[0], 'images': images})


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

# ERRORS


def page_not_found(request, exception, *args, **kwargs):
    response = render(request, 'errors/404.html')
    response.status_code = 404
    return response


def general_error_view(request, *args, **kwargs):
    response = render(request, 'errors/500.html')
    response.status_code = 500
    return response


def permission_denied_view(request, exception, *args, **kwargs):
    response = render(request, 'errors/403.html')
    response.status_code = 403
    return response


def bad_request_view(request, exception, *args, **kwargs):
    response = render(request, 'errors/400.html')
    response.status_code = 400
    return response