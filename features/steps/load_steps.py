# features/steps/load_steps.py

from behave import given, when, then
from django.test.client import Client
from service.models import Product
import json

client = Client()

@given('the following products exist')
def step_impl(context):
    for row in context.table:
        Product.objects.create(
            name=row['name'],
            price=row['price'],
            description=row['description'],
            category=row['category'],
            is_available=row['is_available'] == 'true'
        )

@when('I request to read the product with id "{product_id}"')
def step_impl(context, product_id):
    context.response = client.get(f'/product/{product_id}/')

@then('I should receive the product details for "{product_name}"')
def step_impl(context, product_name):
    response_data = json.loads(context.response.content)
    assert response_data['name'] == product_name

@when('I update the product with id "{product_id}" with new name "{new_name}"')
def step_impl(context, product_id, new_name):
    context.response = client.post(f'/product/update/{product_id}/', json.dumps({'name': new_name}), content_type='application/json')

@then('the product name should be updated to "{new_name}"')
def step_impl(context, new_name):
    response_data = json.loads(context.response.content)
    assert response_data['message'] == 'Product updated successfully'
    updated_product = Product.objects.get(id=1)  # Assuming ID is known for simplicity
    assert updated_product.name == new_name

@when('I delete the product with id "{product_id}"')
def step_impl(context, product_id):
    context.response = client.post(f'/product/delete/{product_id}/')

@then('the product should no longer exist')
def step_impl(context):
    assert context.response.status_code == 204
    with context.assertRaises(Product.DoesNotExist):
        Product.objects.get(id=1)

@when('I request to list all products')
def step_impl(context):
    context.response = client.get('/products/')

@then('I should see a list of all products')
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert len(response_data) > 0

@when('I search for products in category "{category}"')
def step_impl(context, category):
    context.response = client.get('/products/category/', {'category': category})

@then('I should see products belonging to category "{category}"')
def step_impl(context, category):
    response_data = json.loads(context.response.content)
    for product in response_data:
        assert product['category'] == category
