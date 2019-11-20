import django_tables2 as tables
from .models import Order, Product


class ProductTable(tables.Table):
    class Meta:
        orderable = False
        model = Product
        template_name = "django_tables2/bootstrap4.html"


class OrderTable(tables.Table):
    class Meta:
        orderable = False
        model = Order
        template_name = "django_tables2/bootstrap4.html"

    delete = tables.TemplateColumn(
        '''
        <form action="/order/{{record.id}}/" method="post">
            {% csrf_token %}
            <input type="hidden" name="method" value="DELETE">
            <button type="submit" class="btn btn-danger btn-xs">delete</button>
        </form>
        ''',
        orderable=False,
        verbose_name=''
    )
