from django.contrib import admin

from .models import Customer


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
