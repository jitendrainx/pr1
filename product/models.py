from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    descriptin = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,related_name="products",on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title