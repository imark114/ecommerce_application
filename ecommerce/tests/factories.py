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