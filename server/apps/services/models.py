from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Service(MPTTModel):
    name = models.CharField(max_length=255, blank=False, null=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
