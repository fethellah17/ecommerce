import os
import sys
import django

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ecommerce'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product

# Update products with size types
size_updates = {
    'Classic T-Shirt': 'clothing',
    'Running Shoes': 'shoe',
}

for name, size_type in size_updates.items():
    try:
        product = Product.objects.get(name=name)
        product.size_type = size_type
        product.save()
        print(f"Updated {name} with size_type: {size_type}")
    except Product.DoesNotExist:
        print(f"Product {name} not found")

print("Done!")
