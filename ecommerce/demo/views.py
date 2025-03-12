from django.shortcuts import render
from ecommerce.inventory import models
from django.db.models import Count
from django.contrib.postgres.aggregates import ArrayAgg
def cetegories(request):
    data = models.Category.objects.all()
    return render(request, 'index.html' , {"categories": data})

def products(request, category):
    data = models.Product.objects.filter(category__slug=category).values("id","name", "slug", "category__name", "product__store_price")
    return render(request, 'products.html', {"products": data})

def product_detail(request, slug):
    filter_arguments = []
    if request.GET:
        for value in request.GET.values():
            filter_arguments.append(value)
        data = models.ProductInventory.objects.filter(product__slug=slug).filter(
            attribute_values__attribute_value__in=filter_arguments
        ).annotate(
            num_tags=Count('attribute_values')
        ).filter(
            num_tags=len(filter_arguments)
        ).values(
            "id", "product__name", "upc", "retail_price", "product_inventory__units"
        ).annotate(filed_a=ArrayAgg("attribute_values__attribute_value")).get()
    else:
        data = models.ProductInventory.objects.filter(product__slug=slug).filter(
            is_default=True
        ).values(
            "id", "product__name", "upc", "retail_price", "product_inventory__units"
        ).annotate(filed_a=ArrayAgg("attribute_values__attribute_value")).get()
        print(data)
    prdct_attribute_values = models.ProductInventory.objects.filter(product__slug=slug).distinct().values(
        "attribute_values__product_attribute__name", "attribute_values__attribute_value"
    )

    product_attributes = models.ProductTypeAttribute.objects.filter(
         product_type__product_type__product__slug=slug
    ).distinct().values("product_attribute__name")
    return render(request, 'product_detail.html', {
        "product": data, 
        "product_attributes": product_attributes,
        "prdct_attribute_values": prdct_attribute_values
        })