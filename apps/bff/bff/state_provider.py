import requests
from django.utils import timezone


def create_sensor(sensor_data: dict):
    return requests.post("http://smarthome-app:8080/api/v1/sensors/", json=sensor_data)


def get_device_state(device_id: int):
    return [
        {"timestamp": timezone.now().isoformat(), "property_name": key, "value": value}
        for key, value in requests.get(
            f"http://smarthome-app:8080/api/v1/sensors/{device_id}"
        )
        .json()
        .items()
    ]
