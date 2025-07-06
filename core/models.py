from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# ========== Supplier & Customer ==========

class Supplier(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18)])
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    city_address = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18)])
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    city_address = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# ========== Category ==========

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# ========== Product ==========

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    available_quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        return self.available_quantity * self.unit_price

# ========== Incoming Orders ==========

class IncomingOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity_supplied = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    product_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Incoming Order #{self.id}"

    def save(self, *args, **kwargs):
        # If the object is new, add stock
        if self._state.adding:
            self.product.available_quantity += self.quantity_supplied
            self.product.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.product.available_quantity -= self.quantity_supplied
        self.product.save()
        super().delete(*args, **kwargs)

    @property
    def total_price(self):
        return self.quantity_supplied * self.product_price

# ========== Outgoing Orders ==========

class OutgoingOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity_ordered = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00,
                                   validators=[MinValueValidator(0), MaxValueValidator(100)])
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Outgoing Order #{self.id}"

    def clean(self):
        if self.quantity_ordered > self.product.available_quantity:
            raise ValidationError(
                f"Not enough stock for {self.product.name}. Only {self.product.available_quantity} available."
            )

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.full_clean()
            self.product.available_quantity -= self.quantity_ordered
            self.product.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.product.available_quantity += self.quantity_ordered
        self.product.save()
        super().delete(*args, **kwargs)

    @property
    def total_price_before_discount(self):
        return self.quantity_ordered * self.product.unit_price

    @property
    def total_price_after_discount(self):
        return self.total_price_before_discount * (1 - self.discount / 100)
    
    @property
    def total_price(self):
        return self.product.unit_price * self.quantity_ordered - self.discount
