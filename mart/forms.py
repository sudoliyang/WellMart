from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from mart.models import Order, Product


class OrderForm(ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                     empty_label="Select Product")
    is_vip = forms.BooleanField(required=False)
    qty = forms.IntegerField(min_value=1)

    class Meta:
        model = Order
        fields = ['product', 'qty', 'customer_id', 'is_vip']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.form_action = 'order'
        self.helper.field_template = 'bootstrap4/layout/inline_field.html'
        self.helper.add_input(Submit('submit', 'add'))
