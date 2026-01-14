from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category, ShippingAddress, Wishlist


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_sale', 'size_type']
    list_filter = ['category', 'is_sale', 'size_type']
    search_fields = ['name']


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_order_id', 'user', 'phone', 'city', 'state', 'get_order_total', 'get_order_status', 'date_added']
    list_filter = ['state', 'order__complete', 'date_added']
    search_fields = ['phone', 'address', 'city', 'user__username']
    readonly_fields = ['user', 'order', 'phone', 'address', 'city', 'state', 'country', 'date_added', 'get_order_items']
    
    fieldsets = (
        ('Customer Info', {
            'fields': ('user', 'phone')
        }),
        ('Shipping Address', {
            'fields': ('address', 'city', 'state', 'country')
        }),
        ('Order Details', {
            'fields': ('order', 'get_order_items', 'date_added')
        }),
    )
    
    def get_order_id(self, obj):
        return f"Order #{obj.order.id}" if obj.order else "-"
    get_order_id.short_description = 'Order'
    
    def get_order_total(self, obj):
        if obj.order:
            return f"{obj.order.get_order_total} DA"
        return "-"
    get_order_total.short_description = 'Total'
    
    def get_order_status(self, obj):
        if obj.order:
            return "✓ Complete" if obj.order.complete else "⏳ Pending"
        return "-"
    get_order_status.short_description = 'Status'
    
    def get_order_items(self, obj):
        if obj.order:
            items = obj.order.orderitem_set.all()
            if items:
                html = '<table style="width:100%; border-collapse: collapse;">'
                html += '<tr style="background:#f0f0f0;"><th style="padding:8px; text-align:left;">Product</th><th style="padding:8px;">Size</th><th style="padding:8px;">Qty</th><th style="padding:8px;">Price</th></tr>'
                for item in items:
                    html += f'<tr><td style="padding:8px;">{item.product.name}</td><td style="padding:8px; text-align:center;">{item.size or "-"}</td><td style="padding:8px; text-align:center;">{item.quantity}</td><td style="padding:8px; text-align:right;">{item.get_total} DA</td></tr>'
                html += f'<tr><td colspan="3" style="padding:8px;">Subtotal</td><td style="padding:8px; text-align:right;">{obj.order.get_cart_total} DA</td></tr>'
                html += f'<tr><td colspan="3" style="padding:8px;">Shipping</td><td style="padding:8px; text-align:right;">{obj.order.shipping_cost} DA</td></tr>'
                html += f'<tr style="background:#f0f0f0; font-weight:bold;"><td colspan="3" style="padding:8px;">Total</td><td style="padding:8px; text-align:right;">{obj.order.get_order_total} DA</td></tr>'
                html += '</table>'
                return format_html(html)
        return "-"
    get_order_items.short_description = 'Order Items'

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date_added']
    list_filter = ['date_added']
    search_fields = ['user__username', 'product__name']