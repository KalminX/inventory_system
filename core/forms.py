# forms.py
from django import forms
from .models import Supplier, Customer, Category, Product, IncomingOrder, OutgoingOrder


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class IncomingOrderForm(forms.ModelForm):
    class Meta:
        model = IncomingOrder
        fields = ['supplier', 'product', 'quantity_supplied', 'product_price']


class OutgoingOrderForm(forms.ModelForm):
    class Meta:
        model = OutgoingOrder
        fields = ['customer', 'product', 'quantity_ordered', 'discount']
