from rest_framework import serializers, viewsets

from .models import Device
from .state_provider import create_sensor, get_device_state


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["id", "device_type", "status", "description", "state"]

    state = serializers.SerializerMethodField()

    def get_state(self, obj):
        return get_device_state(obj.pk)

    def create(self, validated_data):
        create_sensor(
            {
                "name": "Living Room Temperature",
                "type": "temperature",
                "location": "Living Room",
                "unit": "°C",
            }
        )
        return super().create(validated_data)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
