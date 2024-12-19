# Online Store - Product Management

This Django-based project is designed to manage products for an online store. It includes features like product categories, multilingual support, image management, pricing, and discounts. The model `Product` holds product-related data such as title, description, category, images, pricing, and discount information.

## Features

- **Multilingual Support**: The project supports translations for product titles and descriptions using the `parler` library, which allows for easy localization.
- **Product Management**: Each product has associated fields such as title, description, price, discount, images, and categories.
- **Image Handling**: Multiple images per product, including the main image and additional images.
- **Dynamic Price Calculation**: The price of the product is dynamically adjusted based on any discounts applied, and the final price (`true_price`) is automatically calculated.
- **Categories**: Products can be associated with categories, making it easier to organize the product catalog.

## Requirements

- **Django 3.x+**
- **django-parler**: For multilingual support.
- **Pillow**: For image handling.
- **SQLite** (default) or any other relational database for production.

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/online-store.git
cd online-store
