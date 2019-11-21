import csv
import json
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Sum, Count
from django.db.models import F
from mart.models import Product, Order


class Command(BaseCommand):
    help = 'Generate sales report'

    def handle(self, *args, **options):
        q = Order.objects.order_by('shop_id').values("shop_id").annotate(
            total_qty=Sum('qty'),
            count=Count('pk'),
            total_amount=Sum(F('price') * F('qty')) )

        data = q[::1]
        if len(data) < 0:
            self.stdout.write(self.style.SUCCESS('No data'))
            return

        headers = data[0].keys()
        with open("report.csv", "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(headers)
            for line in data:
                writer.writerow(line.values())

        self.stdout.write(self.style.SUCCESS('Successfully generated'))
