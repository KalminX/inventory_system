# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Supplier, Customer, Product, Category, IncomingOrder, OutgoingOrder
from .forms import SupplierForm, CustomerForm, ProductForm, CategoryForm, IncomingOrderForm, OutgoingOrderForm


class NamedModelMixin:
    object_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_name'] = self.object_name or self.model.__name__
        return context


# Supplier Views
class SupplierListView(NamedModelMixin, ListView):
    model = Supplier
    template_name = 'list.html'  # Use the generic table template
    object_name = 'Supplier'


class SupplierCreateView(NamedModelMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'form.html'
    success_url = reverse_lazy('supplier-list')
    object_name = 'Supplier'

class SupplierUpdateView(NamedModelMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'form.html'
    success_url = reverse_lazy('supplier-list')
    object_name = 'Supplier'

class SupplierDeleteView(NamedModelMixin, DeleteView):
    model = Supplier
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('supplier-list')
    object_name = 'Supplier'


# Customer Views
class CustomerListView(NamedModelMixin, ListView):
    model = Customer
    template_name = 'list.html'
    object_name = 'Customer'


class CustomerCreateView(NamedModelMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'form.html'
    success_url = reverse_lazy('customer-list')
    object_name = 'Customer'

class CustomerUpdateView(NamedModelMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'form.html'
    success_url = reverse_lazy('customer-list')
    object_name = 'Customer'

class CustomerDeleteView(NamedModelMixin, DeleteView):
    model = Customer
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('customer-list')
    object_name = 'Customer'


# Product Views
class ProductListView(NamedModelMixin, ListView):
    model = Product
    template_name = 'list.html'
    object_name = 'Product'

class ProductCreateView(NamedModelMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'form.html'
    success_url = reverse_lazy('product-list')
    object_name = 'Product'

class ProductUpdateView(NamedModelMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'form.html'
    success_url = reverse_lazy('product-list')
    object_name = 'Product'

class ProductDeleteView(NamedModelMixin, DeleteView):
    model = Product
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('product-list')
    object_name = 'Product'


# Category Views
class CategoryListView(NamedModelMixin, ListView):
    model = Category
    template_name = 'list.html'
    object_name = 'Category'

class CategoryCreateView(NamedModelMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'form.html'
    success_url = reverse_lazy('category-list')
    object_name = 'Category'

class CategoryUpdateView(NamedModelMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'form.html'
    success_url = reverse_lazy('category-list')
    object_name = 'Category'

class CategoryDeleteView(NamedModelMixin, DeleteView):
    model = Category
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('category-list')
    object_name = 'Category'


# IncomingOrder Views
class IncomingOrderListView(NamedModelMixin, ListView):
    model = IncomingOrder
    template_name = 'list.html'
    object_name = 'IncomingOrder'

class IncomingOrderCreateView(NamedModelMixin, CreateView):
    model = IncomingOrder
    form_class = IncomingOrderForm
    template_name = 'form.html'
    success_url = reverse_lazy('incomingorder-list')
    object_name = 'Incoming Order'

class IncomingOrderUpdateView(NamedModelMixin, UpdateView):
    model = IncomingOrder
    form_class = IncomingOrderForm
    template_name = 'form.html'
    success_url = reverse_lazy('incomingorder-list')
    object_name = 'Incoming Order'

class IncomingOrderDeleteView(NamedModelMixin, DeleteView):
    model = IncomingOrder
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('incomingorder-list')
    object_name = 'Incoming Order'


# OutgoingOrder Views
class OutgoingOrderListView(ListView):
    model = OutgoingOrder
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = sum(order.total_price for order in context['object_list'])
        context['total_outgoing_price'] = total
        context['show_total_price'] = True
        context['object_name'] = 'OutgoingOrder'  # ✅ Add this line (singular, camel case)
        return context


class OutgoingOrderCreateView(NamedModelMixin, CreateView):
    model = OutgoingOrder
    form_class = OutgoingOrderForm
    template_name = 'form.html'
    success_url = reverse_lazy('outgoingorder-list')
    object_name = 'Outgoing Order'

class OutgoingOrderUpdateView(NamedModelMixin, UpdateView):
    model = OutgoingOrder
    form_class = OutgoingOrderForm
    template_name = 'form.html'
    success_url = reverse_lazy('outgoingorder-list')
    object_name = 'Outgoing Order'

class OutgoingOrderDeleteView(NamedModelMixin, DeleteView):
    model = OutgoingOrder
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('outgoingorder-list')
    object_name = 'Outgoing Order'