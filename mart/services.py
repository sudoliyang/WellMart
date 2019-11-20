from django.db import transaction
from mart.models import Order
from mart.decorators import is_vip, is_in_stock


@is_vip
@transaction.atomic
@is_in_stock
def create_order(form, product):
    order = form.save(commit=False)

    order.price = order.product.price
    order.shop_id = order.product.shop_id
    order.save()

    product.stock_pcs -= order.qty
    product.save()


@transaction.atomic
def delete_order(pk):
    order = Order.objects.select_for_update().select_related().get(pk=pk)
    product = order.product

    product.stock_pcs += order.qty

    product.save()
    order.delete()
