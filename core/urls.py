# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.SupplierListView.as_view(), name='supplier-list'),
    path('suppliers/create/', views.SupplierCreateView.as_view(), name='supplier-create'),
    path('suppliers/<int:pk>/edit/', views.SupplierUpdateView.as_view(), name='supplier-edit'),
    path('suppliers/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier-delete'),

    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/create/', views.CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<int:pk>/edit/', views.CustomerUpdateView.as_view(), name='customer-edit'),
    path('customers/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer-delete'),

    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-edit'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),

    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category-edit'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    path('incomingorders/', views.IncomingOrderListView.as_view(), name='incomingorder-list'),
    path('incomingorders/create/', views.IncomingOrderCreateView.as_view(), name='incomingorder-create'),
    path('incomingorders/<int:pk>/edit/', views.IncomingOrderUpdateView.as_view(), name='incomingorder-edit'),
    path('incomingorders/<int:pk>/delete/', views.IncomingOrderDeleteView.as_view(), name='incomingorder-delete'),

    path('outgoingorders/', views.OutgoingOrderListView.as_view(), name='outgoingorder-list'),
    path('outgoingorders/create/', views.OutgoingOrderCreateView.as_view(), name='outgoingorder-create'),
    path('outgoingorders/<int:pk>/edit/', views.OutgoingOrderUpdateView.as_view(), name='outgoingorder-edit'),
    path('outgoingorders/<int:pk>/delete/', views.OutgoingOrderDeleteView.as_view(), name='outgoingorder-delete'),
]
