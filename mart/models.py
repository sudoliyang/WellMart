from django.db import models
from mart.managers import ProductManager


class Product(models.Model):
    """
        1. product_id: 商品id
        2. stock_pcs: 商品庫存數量
        3. price: 商品單價
        4. shop_id : 商品所屬館別
        5. vip (boolean) : True => VIP限定/ False =>無限制購買對象
    """
    product_id = models.AutoField(primary_key=True)
    stock_pcs = models.IntegerField()
    price = models.IntegerField()
    shop_id = models.CharField(max_length=255)
    vip = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        return f"{self.product_id}"


class Order(models.Model):
    """
        1. id: 訂單id
        2. product_id: 商品id
        3. qty: 購買數量
        4. price: 商品單價
        5. shop_id: 商品所屬館別
    """
    # id = django auto handle
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.IntegerField()
    price = models.IntegerField()
    shop_id = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self._id}"
