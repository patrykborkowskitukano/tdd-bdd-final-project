# service/routes.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json

@csrf_exempt
def read_product(request, product_id):
    """Read a single product by ID."""
    product = get_object_or_404(Product, id=product_id)
    data = {
        'id': product.id,
        'name': product.name,
        'price': str(product.price),
        'description': product.description,
        'category': product.category,
        'is_available': product.is_available,
    }
    return JsonResponse(data)

@csrf_exempt
def update_product(request, product_id):
    """Update a product by ID."""
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        data = json.loads(request.body)
        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        product.description = data.get('description', product.description)
        product.category = data.get('category', product.category)
        product.is_available = data.get('is_available', product.is_available)
        product.save()
        return JsonResponse({'message': 'Product updated successfully'})

@csrf_exempt
def delete_product(request, product_id):
    """Delete a product by ID."""
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return HttpResponse(status=204)

def list_all_products(request):
    """List all products."""
    products = Product.objects.all()
    data = [{'id': p.id, 'name': p.name, 'price': str(p.price), 'description': p.description,
             'category': p.category, 'is_available': p.is_available} for p in products]
    return JsonResponse(data, safe=False)

def list_products_by_name(request):
    """List products filtered by name."""
    name = request.GET.get('name')
    products = Product.objects.filter(name__icontains=name)
    data = [{'id': p.id, 'name': p.name, 'price': str(p.price), 'description': p.description,
             'category': p.category, 'is_available': p.is_available} for p in products]
    return JsonResponse(data, safe=False)

def list_products_by_category(request):
    """List products filtered by category."""
    category = request.GET.get('category')
    products = Product.objects.filter(category__icontains=category)
    data = [{'id': p.id, 'name': p.name, 'price': str(p.price), 'description': p.description,
             'category': p.category, 'is_available': p.is_available} for p in products]
    return JsonResponse(data, safe=False)

def list_products_by_availability(request):
    """List products filtered by availability."""
    is_available = request.GET.get('is_available') == 'true'
    products = Product.objects.filter(is_available=is_available)
    data = [{'id': p.id, 'name': p.name, 'price': str(p.price), 'description': p.description,
             'category': p.category, 'is_available': p.is_available} for p in products]
    return JsonResponse(data, safe=False)
