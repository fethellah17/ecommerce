import os
import sys
import django

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ecommerce'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product

# Map products to existing static images
image_map = {
    'Classic T-Shirt': 'shirt.jpg',
    'Running Shoes': 'shoes.jpg',
    'Premium Headphones': 'headphones.jpg',
    'Smart Watch': 'watch.jpg',
    'Programming Book': 'book.jpg',
    'Source Code Guide': 'sourcecode.jpg',
}

for name, image in image_map.items():
    try:
        product = Product.objects.get(name=name)
        product.static_image = image
        product.save()
        print(f"Updated {name} with {image}")
    except Product.DoesNotExist:
        print(f"Product {name} not found")

print("Done!")
