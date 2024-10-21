from django.contrib import admin

from .models import (
    Customer,
    Address
)


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


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
    inlines = [AddressInline]

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.purchase_type == 'retail':
            return self.readonly_fields_for_retails
        return []


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'customer',
        'Province',
        'city',
        'zone',
        'street',
        'postal_code',
        'is_default'
    ]
    search_fields = [
        'Province__name',
        'city__name',
        'postal_code'
    ]
    list_filter = [
        'Province',
        'city',
        'zone',
        'is_default'
    ]

    fieldsets = (
        (None, {
            'fields': [
                'customer',
                'Province',
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