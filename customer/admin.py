from django.contrib import admin

from .models import (
    Customer,
    Address
)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'purchase_type',
        'phone_number',
        'company',
        'work_experience',
        'representative'
    ]
    readonly_fields_for_retails = [
        'company',
        'work_experience',
        'representative',
    ]

    list_filter = ['purchase_type']

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.purchase_type == 'retail':
            return self.readonly_fields_for_retails
        return []


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'customer',
        'state',
        'city',
        'zone',
        'street',
        'postal_code',
        'is_default'
    ]
    search_fields = [
        'state__name',
        'city__name',
        'zone__name',
        'postal_code'
    ]
    list_filter = [
        'state',
        'city',
        'zone',
        'is_default'
    ]

    fieldsets = (
        (None, {
            'fields': [
                'customer',
                'state',
                'city',
                'zone'
            ]
        }),
        ('Address Details', {
            'fields': [
                'street',
                'address_line',
                'postal_code',
                'is_default'
            ]
        }),
    )