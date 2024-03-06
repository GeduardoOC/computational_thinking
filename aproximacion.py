number = int(input("Ingrese un número: "))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - number) >= epsilon and respuesta <= number:
    print(abs(respuesta**2 - number), respuesta)
    respuesta += paso
    
if abs(respuesta**2 - number) >= epsilon:
    print(f"No se encontró la raíz cuadrada de {number}")
else:
    print(f"La raíz cuadrada de {number} es {respuesta}")