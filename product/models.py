from django.db import models
from storefront.abstract import AbstractModel


class Category(AbstractModel):
    name = models.CharField(
        max_length=255, unique=True
    )
    slug = models.SlugField(
        max_length=255, unique=True
    )
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL
    )
    description = models.TextField(
        max_length=500, null=True, blank=True
    )
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class Brand(AbstractModel):
    name = models.CharField(
        max_length=255, unique=True
    )
    slug = models.SlugField(
        max_length=255, unique=True
    )
    description = models.TextField(
        max_length=500, null=True, blank=True
    )
    logo = models.ImageField(
        upload_to='media/brands/', null=True, blank=True
    )

    def __str__(self):
        return self.name


class Attribute(AbstractModel):
    title = models.CharField(
        max_length=250
    )
    code_name = models.CharField(
        max_length=250
    )

    def __str__(self):
        return self.title


class AttributeGroup(AbstractModel):
    title = models.CharField(
        max_length=250
    )
    attributes = models.ManyToManyField(
        Attribute, related_name='attribute_groups'
    )

    def __str__(self):
        return self.title


class Product(AbstractModel):
    STATUS_IS_ACTIVE = 1
    STATUS_IS_NOT_ACTIVE = 2
    STATUS_CHOICES = [
        (STATUS_IS_ACTIVE, 'فعال'),
        (STATUS_IS_NOT_ACTIVE, 'غیر فعال'),
    ]

    name = models.CharField(
        max_length=250
    )
    description = models.TextField(
        null=True, blank=True
    )
    inventory = models.IntegerField(
        default=0
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES, default=STATUS_IS_ACTIVE
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand, null=True, blank=True, on_delete=models.SET_NULL
    )
    attribute_group = models.ManyToManyField(
        AttributeGroup
    )

    def __str__(self):
        return self.name


class ProductAttribute(AbstractModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='attributes'
    )
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE
    )
    value = models.CharField(
        max_length=250
    )

    def __str__(self):
        return f"{self.product.name} - {self.attribute.title}: {self.value}"


class ProductImage(AbstractModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images'
    )
    image = models.ImageField(
        upload_to='media/products/', null=True, blank=True
    )
    is_primary = models.BooleanField(
        default=True
    )
    description = models.TextField(
        max_length=500, null=True, blank=True
    )
