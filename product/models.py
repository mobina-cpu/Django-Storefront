from django.db import models


class Category(models.Model):
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


class Brand(models.Model):
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