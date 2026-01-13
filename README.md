# Django Ecommerce Store

A full-featured ecommerce web application built with Django, featuring product management, user authentication, shopping cart, wishlist, and checkout functionality with Algeria-specific features.

## Features

### 🛍️ Core Ecommerce Features
- **Product Catalog**: Browse products with categories and search functionality
- **Product Details**: Detailed product pages with image zoom functionality
- **Shopping Cart**: Add/remove items, quantity management
- **Checkout Process**: Complete order processing with shipping information
- **User Authentication**: Login, signup, and user management
- **Wishlist/Favorites**: Save favorite products for later

### 🇩🇿 Algeria-Specific Features
- **58 Wilayas Support**: Complete list of Algerian provinces
- **Municipality Integration**: Dynamic city selection based on wilaya
- **Delivery Pricing**: Wilaya-based shipping costs (400-1200 DA)
- **Algerian Dinar (DA)**: Local currency throughout the application

### 👕 Product Management
- **Size Variants**: Support for clothing sizes (XS-2XL) and shoe sizes (36-43)
- **Sale System**: Products can be marked on sale with discounted prices
- **Category Filtering**: Filter products by category or sale status
- **Image Management**: Product images with zoom functionality

### 🎨 User Interface
- **Responsive Design**: Mobile-friendly interface
- **Modern UI**: Clean, professional design
- **Interactive Elements**: Smooth hover effects and transitions
- **Visual Feedback**: Clear indication of user actions

## Technology Stack

- **Backend**: Django 6.0.1
- **Database**: SQLite3 (development)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 4.4.1 + Custom CSS
- **Icons**: SVG icons for modern look

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/fethellah17/Ecom.git
   cd Ecom
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
ecommerce/
├── ecommerce/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/              # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   ├── urls.py         # URL patterns
│   ├── forms.py        # Django forms
│   ├── admin.py        # Admin configuration
│   └── templates/      # HTML templates
├── static/             # Static files (CSS, JS, images)
├── media/              # User uploaded files
└── manage.py           # Django management script
```

## Models

### Core Models
- **Product**: Product information with pricing and categories
- **Category**: Product categorization
- **Order**: Customer orders
- **OrderItem**: Individual items in orders
- **ShippingAddress**: Delivery information
- **Wishlist**: User favorite products

## Usage

### For Customers
1. **Browse Products**: Visit the store to see available products
2. **Add to Cart**: Click "Buy" to add products to cart
3. **Manage Wishlist**: Click heart icons to save favorites
4. **Checkout**: Complete purchase with shipping information
5. **Account Management**: Create account for order history

### For Administrators
1. **Access Admin Panel**: Use superuser credentials
2. **Manage Products**: Add/edit products and categories
3. **Process Orders**: View and manage customer orders
4. **User Management**: Handle customer accounts

## Customization

### Adding New Wilayas/Cities
Edit the `DELIVERY_PRICES` and wilaya choices in `forms.py`

### Modifying Pricing
Update delivery costs in the `DELIVERY_PRICES` dictionary

### Styling Changes
Modify `static/css/main.css` for custom styling

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support or questions, please open an issue on GitHub.

---

**Made with ❤️ for the Algerian market**