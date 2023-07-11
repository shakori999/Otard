from django.utils import timezone
from django.contrib import messages

from django.views.generic import ListView, View, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from ecommerce.inventory.models import Product
from .models import *

# Create your views here.

class OrderSummaryView(
        View,
        LoginRequiredMixin,
        PermissionRequiredMixin,
        ):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'order': order
            }
            return render(self.request, 'order/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "you do not have an active order")
            return redirect('/')

class OrderedView(
    ListView,
    LoginRequiredMixin,
    ):
    model = Order
    context_object_name = 'order'
    template_name = 'order/order_list.html'
    # def get(self, *args, **kwargs):
    #     try:
    #         order = Order.objects.get(user=self.request.user, ordered=True)
    #         context = {
    #             'order': order
    #         }
    #         return render(self.request, 'order/ordered_view.html', context)
    #     except ObjectDoesNotExist:
    #         messages.warning(self.request, "you don't have an active order2")
    #         return redirect('/')

class OrderedDetailView(
        DeleteView):
    model = Order
    context_object_name = 'order'
    template_name = 'order/order_detail.html'

@login_required(login_url='/accounts/login')
def add_to_cart(request, pk):
    item = get_object_or_404(Product, id=pk)
    items, created= OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            items.quantity += 1
            items.save()
            messages.info(request, "this item was updated to your cart")
        else:
            order.items.add(items)
            messages.info(request, "this item was added to your cart")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user,
            ordered_date=ordered_date
            )
        order.items.add(items)
        messages.info(request, "this item was added to your cart")
    return redirect("order_summary")

@login_required(login_url='/accounts/login')
def remove_from_cart(request, pk):
    item = get_object_or_404(Product, id=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
        )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "this item was removed to your cart")
            return redirect("order_summary")
        else:
            messages.info(request, "this item was not in your cart")
            return redirect("book_detail", pk=pk)
    else:
        messages.info(request, "you don't have an active order")
        return redirect("book_detail", pk=pk)
    
@login_required(login_url='/accounts/login')
def remove_single_item_from_cart(request, pk):
    item = get_object_or_404(Product, id=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("order_summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("book_detail", pk=pk)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("book_detail", pk=pk)
