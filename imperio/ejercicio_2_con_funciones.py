import funciones_imperio


PLANETAS = 5

imperio = funciones_imperio.get_imperio(PLANETAS)

while True:
    # 1 muestra menú principal
    print('1.- Resumen')
    print('2.- Salir')
    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        imperio = funciones_imperio.actualiza_recursos(imperio)
        funciones_imperio.imprime_resumen(imperio)

    elif opcion == '2':
        imperio = funciones_imperio.actualiza_recursos(imperio)
        funciones_imperio.guardar_imperio(imperio)
        break
    else:
        print('Opción incorrecta!!!!!!')
