
# DATAROCK Computer Store Checkout System
## Overview

Welcome to the Computer Store Checkout System! This modular Python application is designed to facilitate the checkout process for a computer store. 
It manages various products, each with unique pricing rules, and allows for flexible pricing strategies.
 The application is built using Django and Django REST Framework, ensuring maintainability and scalability.

## Features

- **Product Management**: Handles multiple products with distinct pricing rules.
- **Flexible Pricing**: Easily modify pricing strategies and apply discounts.
- **Checkout Process**: Scan items and calculate totals seamlessly.
- **Unit Tests**: Comprehensive test suite to validate functionality.

## Products

The current catalog includes:

| SKU | Name            | Price   |
|-----|----------------|---------|
| ipd | Super iPad     | $549.99 |
| mbp | MacBook Pro    | $1399.99|
| atv | Apple TV       | $109.50 |
| vga | VGA Adapter     | $30.00  |

## Pricing Rules

- **Apple TV (atv)**: Buy 3, pay for 2 (3-for-2 deal).
- **Super iPad (ipd)**: Bulk discount at $499.99 each when purchasing more than 4.
- **MacBook Pro (mbp)**: Includes a free VGA adapter with each purchase.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL (optional, for database)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Vaishaliofficial08/datarock_shopping_app.git
   
Install dependencies:
pip install -r requirements.txt

Run migrations:
python manage.py migrate

Start the server:
python manage.py runserver
Access the API at http://127.0.0.1:8000/checkout/

Usage
To calculate the total for purchased items, make a POST request to the /checkout/ endpoint with the following JSON payload:

json
{
  "items": ["atv", "ipd", "mbp"]
}

Example Requests
3-for-2 Apple TV Deal:

Request:
{
  "items": ["atv", "atv", "atv"]
}
Expected Response:
{
  "total": 219.00
}

Bulk Discount on Super iPads:

Request:
{
  "items": ["ipd", "ipd", "ipd", "ipd", "ipd"]
}
Expected Response:
{
  "total": 2499.95
}


Running Tests
To run the unit tests, use the following command:
python manage.py test


Contact
For any inquiries, please contact:

Name: Vaishali
GitHub: Vaishaliofficial08

Thanks !! I really enjoyed creating this app. Happy TEsting !!


