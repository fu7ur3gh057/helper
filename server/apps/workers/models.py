from django.db import models
from django.contrib.auth import get_user_model

from apps.common.models import UUIDTimeStampedModel
from apps.services.models import Service
from other.enums import Cities

User = get_user_model()


class Company(UUIDTimeStampedModel):
    name = models.CharField(max_length=255)


class Worker(UUIDTimeStampedModel):
    user = models.OneToOneField(User, related_name="worker", on_delete=models.CASCADE)
    company = models.OneToOneField(Company, related_name='worker', on_delete=models.CASCADE, null=True)
    is_company = models.BooleanField(default=True)
    work_experience = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=False)
    city = models.CharField(max_length=255, choices=Cities.choices(), default=Cities.BAKU)
    # Минимальная цена за выезд
    departure_amount = models.IntegerField(null=True)
    # Работает по договору
    contractual = models.BooleanField(default=False)
    # services
    services = models.ManyToManyField(Service, related_name='workers')

    def __str__(self):
        if self.is_company:
            return self.company.name
        else:
            return self.user.get_full_name


class WorkerInfo(models.Model):
    worker = models.OneToOneField(Worker, related_name='info', on_delete=models.CASCADE)
    image = models.FileField(upload_to='workers/image', blank=True)
    phone = models.CharField(blank=True, null=True, max_length=100)
    whatsapp = models.CharField(blank=True, null=True, max_length=100)
    telegram = models.CharField(blank=True, null=True, max_length=100)

# TODO Geolocation, Gallery models
