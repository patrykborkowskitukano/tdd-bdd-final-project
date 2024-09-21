# factories.py

import factory
from faker import Faker

# Initialize Faker
fake = Faker()

class Product:
    """A simple Product class to demonstrate the factory."""
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class ProductFactory(factory.Factory):
    """Factory for creating fake Product instances."""
    class Meta:
        model = Product

    name = factory.LazyAttribute(lambda x: fake.word().capitalize())
    price = factory.LazyAttribute(lambda x: round(fake.random_number(digits=5) * 0.01, 2))
    description = factory.LazyAttribute(lambda x: fake.sentence())

# Example usage
if __name__ == "__main__":
    # Generate a single fake product
    product = ProductFactory()
    print(f"Name: {product.name}, Price: {product.price}, Description: {product.description}")

    # Generate a list of fake products
    products = ProductFactory.create_batch(5)
    for i, prod in enumerate(products, start=1):
        print(f"Product {i}: Name: {prod.name}, Price: {prod.price}, Description: {prod.description}")
