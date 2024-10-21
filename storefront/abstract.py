from django.db import models
from django.utils import timezone

class AbstractModel(models.Model):
    created_at = models.DateTimeField(
        default=timezone.now, null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True
