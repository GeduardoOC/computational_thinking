number = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < number:
    print(respuesta)
    respuesta += 1
    
if respuesta**2 == number:
    print(f'La raiz cuadrada de {number} es {respuesta}')
else:
    print(f'{number} no tiene raiz cuadrada exacta')