from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
# Create your models here.
class Category(MPTTModel):
    name = models.CharField(verbose_name=_("Category Name"), max_length=150)
    slug = models.SlugField(max_length=200, verbose_name=_("category safe URL"))
    is_active = models.BooleanField(default=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        verbose_name=_("parent of category")
    )

    class MPTTMeta:
        order_insertion_by = ["name"]
    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    web_id = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_("product website ID")
    )
    name = models.CharField(max_length=255, verbose_name=_("product name"))
    slug = models.SlugField(_("product safe URL"), max_length=300)
    description = models.TextField(_("product description"))
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(_("product visibility"), default=True)
    created_at = models.DateTimeField(_("date product created"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("date product last updated"), auto_now=True)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(_("type of a product"), max_length=255, unique=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("brand name"))

    def __str__(self):
        return self.name

class ProductInventory(models.Model):
    sku = models.CharField(max_length=50, unique=True, verbose_name=_("stock keeping unit"))
    upc = models.CharField(max_length=12, unique=True, verbose_name=_("universal product code"))
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.PROTECT,
        related_name="product_type"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="product"
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name="brand"
    )
    
    is_active = models.BooleanField(default=True, verbose_name=_("product visibility"))
    retail_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_("recomended retail price"),
        error_messages={
            "name":{
                "max_length": _("the price must be between 0 to 999.99")
            }
        }
    )
    store_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_("recomended retail price"),
        error_messages={
            "name":{
                "max_length": _("the price must be between 0 to 999.99")
            }
        }
    )
    sale_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_("recomended retail price"),
        error_messages={
            "name":{
                "max_length": _("the price must be between 0 to 999.99")
            }
        }
    )
    weight = models.FloatField(_("Product weight"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name