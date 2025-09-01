from celery import shared_task
from product.models import *

@shared_task
def create_bulk_product(n):
            category = Category.objects.first()
            if not category:
                category = Category.objects.create(name="Default")
            
            product = []
            
            for _ in range(n):
                product.append(Product(
                    category=category,
                    title=f"auto-generate{_}",
                    price = 100.00,
                    status = True,
                    descriptin = f"auto-description-{_}"
                ))
            Product.objects.bulk_create(product)
        