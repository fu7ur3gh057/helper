from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django_celery_beat.models import PeriodicTask
from django_enum_choices.fields import EnumChoiceField

from other.enums import TimeInterval, TaskStatus, AdvertisingTimeType

User = get_user_model()


class Advertising(models.Model):
    user = models.ForeignKey(User, related_name='advertising_list', on_delete=models.CASCADE)
    object_type = models.ForeignKey(ContentType, related_name='advertising_list', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    type = EnumChoiceField(AdvertisingTimeType, default=AdvertisingTimeType.HOUR)
    expire_datetime = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    canceled = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.object_type} {self.object_id}'


class AdvertisingChecker(models.Model):
    task = models.ForeignKey(PeriodicTask, related_name="advertising_task", on_delete=models.CASCADE)
    interval = EnumChoiceField(TimeInterval, default=TimeInterval.one_min)
    status = EnumChoiceField(TaskStatus, default=TaskStatus.active)
