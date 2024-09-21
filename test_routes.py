# tests/test_routes.py

from django.test import TestCase, Client
from django.urls import reverse
from .models import Product

class ProductRoutesTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name='Test Product',
            price=19.99,
            description='A test product.',
            category='Electronics',
            is_available=True
        )

    def test_update_product(self):
        response = self.client.post(reverse('product-update', args=[self.product.id]), {
            'name': 'Updated Product',
            'price': 29.99,
            'description': 'Updated description.',
            'category': 'Gadgets',
            'is_available': False
        })
        self.assertEqual(response.status_code, 200)
        updated_product = Product.objects.get(id=self.product.id)
        self.assertEqual(updated_product.name, 'Updated Product')

    def test_delete_product(self):
        response = self.client.post(reverse('product-delete', args=[self.product.id]))
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=self.product.id)

    def test_list_products(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_list_products_by_name(self):
        response = self.client.get(reverse('product-list-by-name'), {'name': 'Test Product'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_list_products_by_category(self):
        response = self.client.get(reverse('product-list-by-category'), {'category': 'Electronics'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.category)

    def test_list_products_by_availability(self):
        response = self.client.get(reverse('product-list-by-availability'), {'is_available': True})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, str(self.product.is_available))
