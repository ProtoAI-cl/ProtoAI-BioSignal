import asyncio

from app.api.api import run_api
from app.core.training_programs.fist_training import fistTrain
from app.core.training_programs.index_Training import indexTrain
from app.core.websocket.websocket_handler import send_data
from app.hardware.pin_handler import PinHandler
from app.utils.reader import get_content
from app.utils.text_directions import Files
from resources.ascii import projectName


def menu():
    print(projectName.project_name, end="\n\n")
    print("selecciona una opcion de funcionamiento", end="\n")

    print(get_content(Files.menu.value))
    user_response = input("Tu respuesta: ")
    if user_response == "1":
        fistTrain()
    elif user_response == "2":
        indexTrain()
    elif user_response == "3":
        asyncio.run(send_data())
    elif user_response == "4":
        run_api()
