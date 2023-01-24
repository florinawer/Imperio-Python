import datetime
import os
import random
import json


def get_imperio(n_planetas=10):
    if os.path.isfile('imperio.json'):
        imperio = cargar_imperio()
    else:
        imperio = crear_imperio(n_planetas)

    return imperio


def crear_imperio(n_planetas):
    imperio = []
    for i in range(n_planetas):
        planeta = {}
        nombre = input(f'Nombre del planeta {i + 1}:')
        sistema = random.randint(1, 100)
        orbita = random.randint(1, 10)
        recursos = [
            random.randint(1000, 5000),  # metal
            random.randint(500, 2500),  # cristal
            random.randint(100, 500),  # uranio
        ]
        produccion = [
            [1, 10.0 / 60.0],  # nivel, producción (metal)
            [1, 5.0 / 60.0],  # nivel, producción (cristal)
            [1, 1.0 / 60.0],  # nivel, producción (uranio)
        ]

        planeta['nombre'] = nombre
        planeta['sistema'] = sistema
        planeta['orbita'] = orbita
        planeta['recursos'] = recursos
        planeta['produccion'] = produccion

        # tiempo en segundos (desde 1/1/1970)
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
    """
    :param imperio: El imperio (lista de panetas)
    :return: el imperio con los recursos actualizados
    """
    for planeta in imperio:
        antes = planeta["time_updated"]
        ahora = datetime.datetime.now().timestamp()
        delta = ahora - antes
        for i, recurso in enumerate(['Metal', 'Cristal', 'Uranio']):
            # recursos actuales = recursos antes + producción * tiempo_transcurrido
            recursos_antes = planeta["recursos"][i]
            mina = planeta["produccion"][i]
            recursos_ahora = recursos_antes + mina[1] * delta

            # Actualiza el recurso
            planeta["recursos"][i] = recursos_ahora
            planeta["time_updated"] = ahora

    return imperio


def imprime_resumen(imperio):
    for planeta in imperio:
        print(f'Nombre: {planeta["nombre"]}')
        print(f'Sistema: {planeta["sistema"]}')
        print(f'Órbita: {planeta["orbita"]}')
        print('Recursos: ')

        for i, recurso in enumerate(['Metal', 'Cristal', 'Uranio']):
            recursos = planeta["recursos"][i]
            print(f'{recurso}: {recursos:.2f}')

        print('Producción: ')
        print(f'Metal: Nivel {planeta["produccion"][0][0]}, '
              f'Producción {planeta["produccion"][0][1]:.2f}/seg')
        print(f'Cristal: Nivel {planeta["produccion"][1][0]}, '
              f'Producción {planeta["produccion"][1][1]:.2f}/seg')
        print(f'Uranio: Nivel {planeta["produccion"][2][0]}, '
              f'Producción {planeta["produccion"][2][1]:.2f}/seg')
        print()