import random
import datetime
import json
import os


def get_imperio(n_planetas):
    if os.path.isfile('imperio.json'):
        imperio = cargar_imperio()
    else:
        imperio = crear_planetas(n_planetas)

    return imperio


def crear_planetas(num_planetas):
    imperio = []
    for i in range(num_planetas):
        planeta = {}
        nombre = input(f'Introduce el nombre del planeta {i + 1}')
        sistema = random.randint(1, 100)
        orbita = random.randint(1, 10)
        recursos = [
            random.randint(1000, 5000),
            random.randint(500, 2500),
            random.randint(100, 500),
        ]
        produccion = [
            [1, 10.0 / 60.0],
            [1, 5.0 / 60.0],
            [1, 1.0 / 60.0],
        ]
        planeta['nombre'] = nombre
        planeta['sistema'] = sistema
        planeta['orbita'] = orbita
        planeta['recursos'] = recursos
        planeta['produccion'] = produccion

        planeta['time_updated'] = datetime.datetime.now().timestamp()

        imperio.append(planeta)

        return imperio


def cargar_imperio():
    with open('imperio.json') as json_file:
        imperio = json.load(json_file)
    return imperio


def guardar_imperio(imperio):
    with open('imperio.json', 'w') as file:
        json.dump(imperio, file)


def actualiza_recursos(imperio):
    for planeta in imperio:
        antes = planeta['time_updated']