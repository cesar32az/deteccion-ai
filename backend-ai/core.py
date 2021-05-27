import cv2
import numpy as np
import pathlib
from pathlib import Path


def deteccion(file):
    #dir = pathlib.Path().parent.absolute()
    dir = '/home/julio/umg/inteligencia-artificial/proyecto-final-ai/backend-ai/upload'
    img_path = f'{dir}/{file.filename}'
    print(img_path)

    print(file.filename)
    return 'Gato'
    
