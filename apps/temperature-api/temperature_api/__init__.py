import datetime
import random

from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

def formatted_now():
    ftime = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
    if ftime.endswith('+0000'):
        ftime = ftime[:-5] + 'Z'

    return ftime

@app.get("/temperature/")
async def get_by_location(location: str):
    temp = random.uniform(-50, 50)
    return JSONResponse(
        {
            "Value": temp,
            "Unit": "°C",
            "Timestamp": formatted_now(),
            "Location": location,
            "Status": "on",
            "SensorId": "00000000-0000-0000-0000-000000000001",
            "SensorType": "temperature",
            "Description": "temparature sensor",
        }
    )


@app.get("/temperature/{id}")
async def get_by_id(id: int):
    temp = random.uniform(-50, 50)
    return JSONResponse(
        {
            "Value": temp,
            "Unit": "°C",
            "Timestamp": formatted_now(),
            "Location": "...",
            "Status": "on",
            "SensorId": id,
            "SensorType": "temperature",
            "Description": "temparature sensor",
        }
    )
