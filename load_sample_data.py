import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ecommerce'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product, Category

# Create categories
clothing, _ = Category.objects.get_or_create(name='Clothing')
electronics, _ = Category.objects.get_or_create(name='Electronics')
accessories, _ = Category.objects.get_or_create(name='Accessories')
books, _ = Category.objects.get_or_create(name='Books')

# Create products using existing static images
products_data = [
    {'name': 'Classic T-Shirt', 'price': 29.99, 'category': clothing, 'is_sale': True, 'sale_price': 19.99},
    {'name': 'Running Shoes', 'price': 89.99, 'category': clothing, 'is_sale': False},
    {'name': 'Premium Headphones', 'price': 149.99, 'category': electronics, 'is_sale': True, 'sale_price': 99.99},
    {'name': 'Smart Watch', 'price': 199.99, 'category': accessories, 'is_sale': False},
    {'name': 'Programming Book', 'price': 49.99, 'category': books, 'is_sale': False},
    {'name': 'Source Code Guide', 'price': 39.99, 'category': books, 'is_sale': True, 'sale_price': 29.99},
]

for data in products_data:
    Product.objects.get_or_create(
        name=data['name'],
        defaults={
            'price': data['price'],
            'category': data['category'],
            'is_sale': data['is_sale'],
            'sale_price': data.get('sale_price'),
        }
    )

print(f"Created {Product.objects.count()} products in {Category.objects.count()} categories")
