from django.http import QueryDict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Checkout(APIView):
    PRODUCT_PRICES = {
        'ipd': 549.99,  # Super iPad
        'mbp': 1399.99,  # MacBook Pro
        'atv': 109.50,   # Apple TV
        'vga': 30.00     # VGA adapter
    }

    def post(self, request):
        if isinstance(request.data, QueryDict):
            items = request.data.getlist('items')  # Extract list from QueryDict
        else:
            items = request.data.get('items', [])  # Extract directly from JSON payload
        total = self.calculate_total(items)
        return Response({'total': total}, status=status.HTTP_200_OK)

    def calculate_total(self, items):
        item_counts = {sku: items.count(sku) for sku in self.PRODUCT_PRICES.keys()}
        total = 0  # Initialize total price
        
        # Calculate total price with discounts
        for sku, quantity in item_counts.items():
            if sku == 'atv':
                # 3 for 2 deal on Apple TV
                total += (quantity // 3) * 2 * self.PRODUCT_PRICES['atv'] + (quantity % 3) * self.PRODUCT_PRICES['atv']
            elif sku == 'ipd':
                # Bulk discount on Super iPads
                total += (499.99 * quantity) if quantity > 4 else (549.99 * quantity)
            elif sku == 'mbp':
                # Price of MacBook Pro
                total += 1399.99 * quantity
                # VGA adapter is free with MacBook Pro
                total += 0.00 * quantity
            elif sku == 'vga':
                # VGA adapter is free with MacBook Pro; no action needed here
                continue
        
        return total  # Return the calculated total price