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