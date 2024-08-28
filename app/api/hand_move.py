import asyncio

from app.hardware.pin_handler import PinHandler
from app.utils.hand_model import Hand


def hand_handler(instructions):
    # {"engine": "upper_thumb", "value": 0},
    # {"engine": "lower_thumb", "value": 0.5},
    # {"engine": "index_finger", "value": 0.8},
    # {"engine": "middle_finger", "value": 1},
    # {"engine": "ring_finger", "value": 0},
    # {"engine": "pinky_finger", "value": 0}
    # instructions = instructions.split("\n")

    upper_thumb = Hand.upperThumb.value
    lower_thumb = Hand.lowerThumb.value
    index_finger = Hand.indexFinger.value
    middle_finger = Hand.middleFinger.value
    ring_finger = Hand.ringFinger.value

    hand = {
        upper_thumb: 17,
        lower_thumb: 18,
        index_finger: 19,
        middle_finger: 20,
        ring_finger: 21,
    }

    gpio_handler = PinHandler(17)
    try:
        for i in instructions:
            gpio_handler.setPin(hand[i["engine"]])
            gpio_handler.set_servo_position(parse_data(i["value"]))
            gpio_handler.stop()

    except Exception as e:
        raise e
    finally:
        gpio_handler.cleanGPIO()


def parse_data(data):
    max = 89
    if data <= 1 and data >= 0:
        return int(max * data)
    else:
        return 0
