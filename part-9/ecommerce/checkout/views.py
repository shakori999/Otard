from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from .forms import CheckoutForm
from django.contrib import messages
from .models import *
from ecommerce.order.models import * 

# Create your views here.


class CheckoutPageView(View):
    
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        user = get_user_model()
        context = {
            'form': form,
            'user': user
        }
        return render(self.request, 'checkout/checkout-page.html', context)

    def post(self, *args, **kwargs):
        user = self.request.user
        form = CheckoutForm(self.request.POST or None)
        order = Order.objects.get(user=self.request.user, ordered=False)
        try:
            if form.is_valid():
                name = form.cleaned_data.get('name')
                phone = form.cleaned_data.get('number')
                address = form.cleaned_data.get('street_address')
                address_2 = form.cleaned_data.get('apartment_address')

                order_items = order.items.all()
                order_items.update(ordered=True)
                for item in order_items:
                    item.save()

                order.ordered = True
                order.name = name
                order.phone_number = phone
                order.address = address
                order.address_2 = address_2
                order.save()

                # TODO: add redirect to the selected payment option
                messages.warning(self.request, 'تم استلام طلبك بنجاح سيتم التواصل مع باقرب وقت')
                return redirect('/')
            messages.warning(self.request, 'Faild checkout')
            return redirect('checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "you do not have an active order")
            return redirect('order_summary')
