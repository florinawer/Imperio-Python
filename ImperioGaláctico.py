import random
import json
import datetime
import os
import funciones_imperio

num_planetas = 5

imperio = funciones_imperio.get_imperio(num_planetas)

while True:
    print('1.- Resumen')
    print('2.- Salir')
    opcion = input('Seleccione una opcion: ')

    if opcion == '1':
        imperio = funciones_imperio.actualiza_recursos(imperio)























