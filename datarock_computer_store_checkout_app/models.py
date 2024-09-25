from django.db import models

class Product(models.Model):
    # Defining product SKUs and corresponding names
    SKU_CHOICES = [
        ('ipd', 'Super iPad'),
        ('mbp', 'MacBook Pro'),
        ('atv', 'Apple TV'),
        ('vga', 'VGA adapter'),
    ]
    
    sku = models.CharField(max_length=3, choices=SKU_CHOICES, unique=True)  # SKU code for the product
    name = models.CharField(max_length=100)  # Name of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product

    def __str__(self):
        return self.name  # String representation of the product
