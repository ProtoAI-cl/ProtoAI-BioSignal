import time
from random import random

import websockets

# from app.hardware.gpio_interface import get_interface


async def send_data():
    uri = "ws://localhost:8765"
    # sensor = get_interface()
    async with websockets.connect(uri) as websocket:
        while True:
            # voltage = sensor.value
            # sensor_value = sensor.voltage
            voltage = random()
            sensor_value = random()
            await websocket.send(f"{sensor_value},{voltage}")

            response = await websocket.recv()
            print(f"response: {response}")

            time.sleep(0.2)
