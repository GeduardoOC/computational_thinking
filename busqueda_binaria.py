number = int(input("Ingrese un número: "))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, number)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - number) >= epsilon:
    print(f"bajo = {bajo}, alto = {alto}, respuesta = {respuesta}")
    if respuesta**2 < number:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo) / 2
    
print(f"La raíz cuadrada de {number} es {respuesta}")