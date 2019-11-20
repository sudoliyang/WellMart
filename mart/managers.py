from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce


class ProductManager(models.Manager):

    def hot_product(self):
        return self.annotate(total=Coalesce(Sum('order__qty'), 0)).order_by(
            '-total')
