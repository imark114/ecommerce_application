import pytest
from django.core.management import call_command

@pytest.fixture
def creat_admin_user(django_user_model):
    return django_user_model.objects.create_superuser("rakib", "ark@gmail.com", "114")

@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_product_fixture.json")
        call_command("loaddata", "db_type_fixture.json")
        call_command("loaddata", "db_brand_fixture.json")
        call_command("loaddata", "db_product_inventory_fixture.json")
        call_command("loaddata", "db_media_fixture.json")
        call_command("loaddata", "db_stock_fixture.json")
        call_command("loaddata", "db_product_attribute.json")
        call_command("loaddata", "db_product_attribute_value.json")