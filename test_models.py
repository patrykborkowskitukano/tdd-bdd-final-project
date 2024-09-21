# tests/test_models.py

from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):

    def setUp(self):
        # Create a sample product to use in tests
        self.product = Product.objects.create(
            name='Test Product',
            price=19.99,
            description='A test product for unit testing.'
        )

    def test_update_product(self):
        # Fetch the product from the database
        product = Product.objects.get(id=self.product.id)

        # Update the product details
        product.name = 'Updated Product'
        product.price = 29.99
        product.description = 'An updated description for the test product.'
        product.save()

        # Fetch the updated product
        updated_product = Product.objects.get(id=self.product.id)

        # Assert that the updates were successful
        self.assertEqual(updated_product.name, 'Updated Product')
        self.assertEqual(updated_product.price, 29.99)
        self.assertEqual(updated_product.description, 'An updated description for the test product.')
