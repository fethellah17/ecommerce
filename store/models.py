from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    SIZE_TYPE_CHOICES = [
        ('none', 'No Size'),
        ('clothing', 'Clothing (XS, S, M, L, XL, 2XL)'),
        ('shoe', 'Shoe (36, 37, 38, 39, 40, 41, 42, 43)'),
    ]
    
    CLOTHING_SIZES = ['XS', 'S', 'M', 'L', 'XL', '2XL']
    SHOE_SIZES = ['36', '37', '38', '39', '40', '41', '42', '43']
    
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    static_image = models.CharField(max_length=200, blank=True, help_text='Static image filename (e.g., shirt.jpg)')
    description = models.TextField(blank=True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    size_type = models.CharField(max_length=20, choices=SIZE_TYPE_CHOICES, default='none', help_text='Select size type for this product')
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        if self.image:
            try:
                return self.image.url
            except:
                pass
        if self.static_image:
            return f'/static/images/{self.static_image}'
        return '/static/images/1.png'
    
    @property
    def has_sizes(self):
        return self.size_type != 'none'
    
    def get_sizes_list(self):
        if self.size_type == 'clothing':
            return self.CLOTHING_SIZES
        elif self.size_type == 'shoe':
            return self.SHOE_SIZES
        return []
    
    def get_size_label(self):
        if self.size_type == 'clothing':
            return 'Size'
        elif self.size_type == 'shoe':
            return 'EU Size'
        return ''


from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def get_order_total(self):
        return self.get_cart_total + self.shipping_cost


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    size = models.CharField(max_length=10, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        size_str = f" ({self.size})" if self.size else ""
        return f"{self.quantity} x {self.product.name}{size_str}"

    @property
    def get_total(self):
        if self.product.is_sale and self.product.sale_price:
            return self.product.sale_price * self.quantity
        return self.product.price * self.quantity


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200, default='Algeria')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.address} - {self.phone}"

    class Meta:
        verbose_name_plural = 'Shipping Addresses'


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

    class Meta:
        unique_together = ('user', 'product')
        verbose_name_plural = 'Wishlists'
