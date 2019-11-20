from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from mart.models import Product, Order
from mart.forms import OrderForm
from mart.tables import ProductTable, OrderTable
from mart.decorators import is_delete_method
from mart import services

"""
    請設計以下API功能
      i. 加入訂單,訂單成立需檢查是否符合vip身份,並確認商品庫存數量(身份和庫存檢查限用decorator實作)
      ii. 刪除訂單(庫存檢查限用decorator實作) 備註:加入訂單時,若小於可購買量,前端需提示貨源不足 / 刪除訂單,庫存從0變回有值則提示
          商品到貨
      iii. 請設計一排程,根據訂單記錄算出各個館別的
                  1.總銷售金額
                  2.總銷售數量
                  3.總訂單數量
                  備註:輸出方式不限(ex: slack通知,email通知,生成csv,...)
      iv. 根據訂單記錄計算出最受用戶歡迎的商品前三名(根據商品銷售量)
"""

def index(request):
    products = Product.objects.all().order_by('pk')
    orders = Order.objects.all().order_by('pk')
    hot_products = Product.objects.hot_product()
    top_three_product = hot_products[:3]

    context = {
        "product_table": ProductTable(products),
        "order_table": OrderTable(orders),
        "form": OrderForm(),
        "top_three_product": top_three_product
    }
    return render(request, "index.html", context)


# View Function
@require_http_methods(["POST"])
def create_order(request):
    form = OrderForm(request.POST or None, request.FILES or None)
    if not form.is_valid():
        messages.add_message(request, messages.ERROR, '訂單內容有誤')
        return redirect('index')

    try:
        product = form.cleaned_data.get("product")
        services.create_order(form, product)
    except PermissionDenied as e:
        messages.add_message(request, messages.WARNING, '此商品僅限 VIP 購買')
    except ValueError as e:
        messages.add_message(request, messages.WARNING, '貨源不足')
    except Exception as e:
        messages.add_message(request, messages.ERROR, '操作發生錯誤，請聯繫客服')
    else:
        messages.add_message(request, messages.SUCCESS, '訂單成立')

    return redirect('index')


@require_http_methods(["POST"])
@is_delete_method
def delete_order(request, pk):
    try:
        order = Order.objects.select_related().get(pk=pk)
        product = order.product
        is_product_back_to_active = product.stock_pcs <= 0 and order.qty >= 1
        services.delete_order(pk)
    except ObjectDoesNotExist as e:
        messages.add_message(request, messages.ERROR, '訂單不存在')
    except Exception as e:
        messages.add_message(request, messages.ERROR, '操作發生錯誤，請聯繫客服')
    else:
        messages.add_message(request, messages.INFO, '訂單已刪除')
        if is_product_back_to_active:
            messages.add_message(request, messages.SUCCESS, '商品已到貨')


    return redirect('index')
