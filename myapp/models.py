from django.db import models

# Create your models here.

class Order(models.Model):
    DRINK_CHOICES = (
        ('espresso', 'espresso'),
        ('latte', 'latte'),
        ('cappuccino', 'Cappuccino'),
        ('americano', 'Americano'),
        ('cocacola', 'Cocacola'),
        ('sprite', 'Sprite'),
        ('fanta', 'Fanta'),
        ('milkshake', 'Milkshake'),
        ('mango_juice', 'Mango Juice'),
        ('passion_juice', 'Passion Juice'),
       
    )

    SIZE_CHOICES = (
        ('small', 'small'),
        ('medium', 'medium'),
        ('large', 'large'),
    )


    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    drink_type = models.CharField(max_length=50, choices=DRINK_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES) 
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.drink_type} - {self.size}"
    
    def get_drink_type(self):
        return dict(self.DRINK_CHOICES).get(self.drink_type)
    
    def get_size_display(self):
        return dict(self.SIZE_CHOICES).get(self.size)
    








