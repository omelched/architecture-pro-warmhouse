import datetime
import random

from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/temperature/")
async def create_item(location: str):
    temp = random.uniform(-50, 50)
    return JSONResponse(
        {
            "Value": temp,
            "Unit": "°C",
            "Timestamp": datetime.datetime.now().timestamp(),
            "Location": location,
            "Status": "on",
            "SensorId": "00000000-0000-0000-0000-000000000001",
            "SensorType": "temperature",
            "Description": "temparature sensor",
        }
    )
