from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    WHOLESALER = 'wholesaler'
    RETAIL = 'retail'

    PURCHASE_TYPE_CHOICES = [
        (WHOLESALER, 'عمده'),
        (RETAIL, 'تکی')
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    purchase_type = models.CharField(
        max_length=10 , choices=PURCHASE_TYPE_CHOICES, null=True
    )
    phone_number = models.CharField(
        max_length=11, unique=True, null=True
    )

    # only for wholesalers
    company = models.CharField(
        max_length=255, blank=True, null=True
    )
    work_experience = models.CharField(
        max_length=255, blank=True, null=True
    )
    representative = models.CharField(
        max_length=100, blank=True, null=True
    )

    def __str__(self):
        return self.user.username


class State(models.Model):
    name = models.CharField(
        max_length=255
    )


class City(models.Model):
    name = models.CharField(
        max_length=255
    )
    state = models.ForeignKey(
        State, on_delete=models.CASCADE
    )


class Zone(models.Model):
    name = models.CharField(
        max_length=255
    )
    state = models.ForeignKey(
        State, on_delete=models.CASCADE
    )


class Address(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE
    )
    state = models.ForeignKey(
        State, on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        City, on_delete=models.CASCADE
    )
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE
    )
    street = models.CharField(
        max_length=255
    )
    address_line = models.CharField(
        max_length=225
    )
    postal_code = models.CharField(
        max_length=10
    )
    is_default = models.BooleanField(
        default=True
    )

