from django.db import models


from apps.common.models import UUIDTimeStampedModel
from apps.services.models import Service
from other.enums import Cities, OrderStatus
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(UUIDTimeStampedModel):
    customer = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    budget = models.FloatField(blank=False, null=False)
    services = models.ManyToManyField(Service, related_name='orders', null=True)
    city = models.CharField(max_length=255, choices=Cities.choices(), default="Baku")
    status = models.CharField(max_length=255, choices=OrderStatus.choices(), default="Considered")
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# TODO Order Image model
