from django.contrib import admin
from .models import Supplier, Customer, Category, Product, IncomingOrder, OutgoingOrder

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'city_address', 'date_created')
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'city_address', 'date_created')
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'available_quantity', 'unit_price', 'total_price', 'date_created')
    readonly_fields = ('total_price',)
    list_filter = ('category',)


@admin.register(IncomingOrder)
class IncomingOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'product', 'quantity_supplied', 'product_price', 'total_price', 'date_created')
    readonly_fields = ('total_price',)


@admin.register(OutgoingOrder)
class OutgoingOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'quantity_ordered', 'total_price_before_discount', 'discount', 'total_price_after_discount', 'date_created')
    readonly_fields = ('total_price_before_discount', 'total_price_after_discount')
    list_filter = ('product', 'customer')
