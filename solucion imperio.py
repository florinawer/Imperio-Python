import random
import datetime

imperio = []
for i in range(5):
    planeta = {}
    nombre = (f'Introduce el nombre del planeta {i+1}')
    sistema = random.randint(1, 100)
    orbita = random.randint(1, 10)
    recursos = [random.randint(1000, 5000), #metal
                random.randint(500, 2500), #cristal
                random.randint(100, 500)] #uranio
    produccion = [[1, 10.0/60.0], #prod metal
                  [1, 5.0/60.0], #prod cristal
                  [1, 1.0/60.0]] #prod uranio
    planeta['Nombre'] = nombre
    planeta['Sistema'] = sistema
    planeta['Orbita'] = orbita
    planeta['Recursos'] = recursos
    planeta['Produccion'] = produccion
