import threading
import time
from datetime import datetime

import pwn
from adafruit_ads1x15.analog_in import AnalogIn
from pwnlib.log import Progress

from app.hardware.gpio_interface import get_interface
from app.utils.text_directions import Files


def start_training(exercises, instructions, main_file_name):
    save_data_route = Files.fileDirection.value + create_file_name(main_file_name)
    print(
        "Realiza los ejercicios de forma calmada y tomate tu tiempo para transisionar entre posiciones"
    )
    interface = get_interface()

    train_data = pwn.log.progress("Info")
    train_data.status("Vamos a empezar!")
    time.sleep(3)
    count_down(5, train_data)
    train_data.success("Sigue las instruciones")
    for exercise in exercises:
        run_exercise(exercise, instructions, interface, save_data_route)


def run_exercise(exercise, instructions, interface, save_data_route):
    instruction = str(instructions[exercise["instructions"]])
    # print(instruction)
    user_instructions = threading.Thread(
        target=show_instruction, args=(instruction, exercise["duration"])
    )
    user_instructions.start()

    capture_data = threading.Thread(
        target=save_training_data,
        args=(
            interface,
            save_data_route,
            exercise["instructions"],
            exercise["duration"],
        ),
    )
    capture_data.start()

    capture_data.join()
    user_instructions.join()


def save_training_data(sensor: AnalogIn, filename: str, running_instruction, duration):
    """
    this will take the data from the sensor and will save it in the specified route
    """
    file_mode = "a" if file_exists(filename) else "w"
    start_time = time.time()
    with open(filename, file_mode) as f:
        while time.time() - start_time < duration:
            f.write(f"{running_instruction}, {sensor.value},{sensor.voltage}\n")


def file_exists(filename):
    """
    Helper function to check if a file exists
    """
    try:
        with open(filename, "r"):
            return True
    except FileNotFoundError:
        return False


def show_instruction(instruction, duration):
    print(f"\n{instruction}")
    remaining_time = pwn.log.progress("Remaining time")
    count_down(duration, remaining_time)
    remaining_time.success("Vamos a la siguiente prueba")
    time.sleep(2)


def count_down(start, log: Progress):
    while start > 0:
        log.status(start)
        start = start - 1
        time.sleep(1)


def create_file_name(main_name: str) -> str:
    # Obtener la fecha y hora actual
    now = datetime.now()

    # Formatear la fecha y hora según el formato especificado
    formatted_date = now.strftime("%d_%m_%Y_%H_%M")

    # Construir el nombre del archivo
    filename = f"{main_name}_{formatted_date}.txt"

    return filename
