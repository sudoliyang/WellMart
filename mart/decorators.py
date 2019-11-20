from django.core.exceptions import PermissionDenied, SuspiciousOperation
from mart.models import Product


def is_delete_method(func):
    def check_and_call(request, *args, **kwargs):
        data = request.POST
        method = data.get('method', '').lower()
        if method != "delete":
            raise SuspiciousOperation
        return func(request, *args, **kwargs)
    return check_and_call


def is_vip(func):
    def check_and_call(form, product):
        is_vip = form.cleaned_data.get("is_vip")
        if product.vip and not is_vip:
            raise PermissionDenied
        return func(form, product)
    return check_and_call


def is_in_stock(func):
    def check_and_call(form, product):
        pk = product.pk
        product = Product.objects.select_for_update().get(pk=pk)
        qty = form.cleaned_data.get("qty")
        if not (qty <= product.stock_pcs):
            raise ValueError
        return func(form, product)
    return check_and_call
