import time

import pwn

from app.core.training_programs.training_common import create_file_name, start_training
from app.hardware import gpio_interface
from app.utils.reader import get_content
from app.utils.text_directions import Files

FILE_CORE_NAME = "FIST_TRAINING"


def testSensor(test_information, sensor_interface):
    startTime = time.time()
    while time.time() - startTime < 3:
        test_information.status(
            f"sensor voltage: {(sensor_interface.voltage):.3f}\nsensor analog: {sensor_interface.value}"
        )
        time.sleep(0.2)
    test_information.success("Prueba terminada")


def fistTrain():
    sensorValidator = get_content(Files.sensorValidation.value)
    print(sensorValidator)
    instructions = {
        "relaxed_hand": "relaja tu mano y los musculos del brazo testeado",
        "fist_formation": "Cierra lentamente tu mano en un puño. Mantén la muñeca en una posición neutral.",
        "fist_hold": "Mantén la posición del puño, manteniendo todos los dedos y el pulgar firmemente cerrados.",
        "fist_release": "Abre lentamente tu mano, comenzando por liberar el pulgar y luego estirando los dedos para formar una palma abierta.",
        "open_palm": "Mantén tu mano en una posición de palma abierta, con los dedos y el pulgar extendidos pero relajados.",
        "fist_to_open_palm": "Haz la transición de un puño a una palma abierta abriendo lentamente los dedos y estirando la mano.",
        "open_palm_to_fist": "Haz la transición de una palma abierta a un puño cerrando lentamente los dedos y el pulgar para formar un puño firme.",
    }

    exercises = [
        {
            "name": "Relaxed Hand",
            "instructions": "relaxed_hand",
            "duration": 5,
        },
        {
            "name": "Transition to Fist",
            "instructions": "fist_formation",
            "duration": 5,
        },
        {"name": "Fist", "instructions": "fist_hold", "duration": 10},
        {
            "name": "Transition to Relaxed Hand",
            "instructions": "fist_to_open_palm",
            "duration": 5,
        },
    ]
    try:
        # getting interface
        interface = gpio_interface.get_interface()
        test_information = pwn.log.progress("Sensor data")

        # This is for testing purposes
        testSensor(test_information, interface)
        start_training(exercises, instructions, FILE_CORE_NAME)

    except Exception as e:
        print("no interface detected")
        raise e
