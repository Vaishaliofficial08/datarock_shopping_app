# datarock_computer_store_checkout_app/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class CheckoutTests(TestCase):
    def setUp(self):
        """Set up the test client for making API requests."""
        self.client = APIClient()  # Initialize the API client for testing


    def test_three_for_two_apple_tv(self):
        """
        Test the 3-for-2 deal on Apple TVs.
        If 3 Apple TVs are purchased, the price should reflect buying 2.
        """
        response = self.client.post('/checkout/', {"items": ["atv", "atv", "atv"]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check if the response is OK
        self.assertEqual(response.data['total'], 219.00)  # Expected total for 3 Apple TVs

    def test_super_ipad_bulk_discount(self):
        """
        Test the bulk discount on Super iPads.
        If more than 4 Super iPads are purchased, the price should be $499.99 each.
        """
        response = self.client.post('/checkout/', {'items': ['ipd', 'ipd', 'ipd', 'ipd', 'ipd']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check if the response is OK
        self.assertEqual(response.data['total'], 2499.95)  # Expected total for 5 iPads

    def test_macbook_pro_with_vga(self):
        """
        Test purchasing a MacBook Pro with a free VGA adapter.
        The total should be the price of the MacBook Pro alone.
        """
        response = self.client.post('/checkout/', {'items': ['mbp', 'vga']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check if the response is OK
        self.assertEqual(response.data['total'], 1399.99)  # Expected total for MacBook Pro

    def test_combined_purchase(self):
        """
        Test a combined purchase scenario.
        This test checks if multiple items work together in a single transaction.
        """
        response = self.client.post('/checkout/', {
            'items': ['atv', 'ipd', 'mbp', 'vga', 'atv', 'atv', 'ipd', 'ipd', 'ipd', 'ipd']
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check if the response is OK
        self.assertEqual(response.data['total'], 4118.94)  # Expected total for the combined purchase

    def test_empty_cart(self):
        """
        Test the behavior when an empty cart is submitted.
        This test checks if the API handles empty submissions gracefully.
        """
        response = self.client.post('/checkout/', {'items': []})
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check if the response is OK
        self.assertEqual(response.data['total'], 0.00)  # Expected total for an empty cart

