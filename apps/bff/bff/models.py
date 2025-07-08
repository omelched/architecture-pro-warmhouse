from django.db import models
from django.utils import timezone

class DeviceType(models.Model):
    nams = models.CharField()


# Create your models here.
class Device(models.Model):
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, null=True)
    status = models.CharField()
    description = models.CharField()


class DeviceStateProperty(models.Model):
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, null=True)
    name = models.CharField()


class DeviceStateLedger(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='state')
    state_property = models.ForeignKey(DeviceStateProperty, on_delete=models.CASCADE)
    serialized_value = models.CharField()
