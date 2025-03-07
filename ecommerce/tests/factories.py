import factory
import pytest
from faker import Faker
from pytest_factoryboy import register
from ecommerce.inventory import models

fake = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category
    
    name = fake.lexify(text="cat_name_????")
    slug = fake.lexify(text= "cat_slug_????")

register(CategoryFactory)

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    web_id = factory.Sequence(lambda n: "web_id_%d" % n)
    slug = fake.lexify(text="prod_slug_??????")
    name = fake.lexify(text="prod_name_??????")
    description = fake.text()
    is_active = True
    created_at = "2021-09-04 22:14:18.279092"
    updated_at = "2021-09-04 22:14:18.279092"

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        if extracted:
            for cat in extracted:
                self.category.add(cat)
register(ProductFactory)

class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductType
    
    name = factory.Sequence(lambda n: "type_%d" % n)

register(ProductTypeFactory)

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand
    name = factory.Sequence(lambda n: "brand_%d" % n)
register(BrandFactory)

class ProductInventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductInventory
    
    sku = factory.Sequence(lambda n: "sku_%d" % n)
    upc = factory.Sequence(lambda n: "sku_%d" % n)
    product_type = factory.SubFactory(ProductTypeFactory)
    product = factory.SubFactory(ProductFactory)
    brand = factory.SubFactory(BrandFactory)
    is_active = 1
    retail_price = 97
    store_price = 92
    sale_price = 46
    weight = 987

register(ProductInventoryFactory)

class MediaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Media
    product_inventory = factory.SubFactory(ProductInventoryFactory)
    image = "images/default.png"
    alt_text = "a default image solid color"
    is_feature = True

register(MediaFactory)

class StockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Stock
    product_inventory = factory.SubFactory(ProductInventoryFactory)
    units = 2
    units_sold = 100
register(StockFactory)

class ProductAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductAttribute
    name = factory.Sequence(lambda n : "attribute_name_%d" % n)
    description = factory.Sequence(lambda n : "description_%d" % n)

register(ProductAttributeFactory)

class ProductAttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductAttributeValue
    product_attribute = factory.SubFactory(ProductAttributeFactory)
    attribute_value = fake.lexify(text="attribute_value_??????")

register(ProductAttributeValueFactory)