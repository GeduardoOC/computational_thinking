# Computational Thinking

What is this repository about?

    - Learning to solve a problem computationally.
    - Understand the commonalities among all programming languages.
    - Building a foundation for your career as a Computer Scientist.

## What is a programming language

Es un lenguaje formal que, mediante una seria de instrucciones, le permite a un programador escribir un conjunto de ordenes (algoritmos), y de esta forma la computadora devuelva un resultado

- Sintaxis
    - Define la secuencia de los simbolos que esta bien formada
- Semantica estatica
    - Define que enunciados con sintaxis correcta tienen significado
- Semantica
    - Define el significado. **En los lenguajes de programacion solo hay un significado**

### Basic elements of programming languages

Existen lenguajes de Alto nivel y Bajo nivel
> Alto nivel significa que esta disenado para los humanos, se asemeja mucho mas a la forma en que nos comunicamos los humanos.
> Por otro lado Bajo nivel significa que esta optimizado para que una maquina pueda entenderlo, se parece mas a los unos y ceros.

Existen lenguajes Generales y de Dominio especifico
> Los lenguajes Generales tienen todos los primitivos que nos otorga Turing que necesitamos para ejecutar cualquier algoritmo.
> Los lenguajes de Dominio especifico especializados a aplicaciones muy especificas.

Por ultimo tenemos lenguajes Interpretados vs Compilados
> Interpretados significa que mientras corre el programa, despues de cada instruccion, esta instruccion se traduce a lenguajen maquina y la maquina lo puede leer.
> Compilado significa que antes se traduce todo el programa a lenguaje maquina, y despues se entrega a la computadora para que lo compile.


# Enumeración exhaustiva

Es un algoritmo en donde simplemente enumeramos todas la posibilidades **Tambien llamado "adivina y verifica"**, por esto mismo no es el metodo mas eficiente, pero en todo el universo de posibles soluciones, este puede que sea el mas acertado en algun momento.

```py
number = int(input('Escoge un entero: '))

"""Iniciamos respuesta en cero"""
respuesta = 0

"""Mientras respuesta al cuadrado sea menor a number (si es igual es la raiz - si es mayor no es exacta)"""
while respuesta**2 < number:
    print(respuesta)
    respuesta += 1 # Se le suma 1 al valor
    
if respuesta**2 == number:
    print(f'La raiz cuadrada de {number} es {respuesta}')
else:
    print(f'{number} no tiene raiz cuadrada exacta')
```

# Aproximacion de soluciones

Similar a Enumeracion Exhaustiva, pero no necesita una respuesta exacta. Porque hay ocaciones donde la solucion no es exacta y tenemos que da runa respuesta, para esto tenemos algoritmos de aproximacion de soluciones.

> Cuando vamos a aproximar una solucion, tenemos que definir que tan cerca queremos estar de esta solucion, y ha esta diferencia entre la realidad y la solucion la vamos a llamar **Epsilon**

Como siempre en programación debemos hacer un _trade-off_, no podemos ser precisos y rápidos a la vez, por lo tanto cuando nuestro **epsilon** es muy pequeño esto significa que debemos realizar **mas iteraciones** para llegar a la aproximación, lo cual significa sacrificar tiempo. Y por otro lado si queremos que nuestro **tiempo de ejecución** sea lo **mas corto posible** debemos sacrificar la **precisión** aumentando el valor de **epsilon**.

```py
number = int(input("Ingrese un número: "))
epsilon = 0.01  # Definimos un margen de error.
paso = epsilon**2  # Los pasos para buscar la raíz sera igual a epsilon^2
respuesta = 0.0  # Inicializamos una respuesta 0

while abs(respuesta**2 - number) >= epsilon and respuesta <= number:
    print(abs(respuesta**2 - number), respuesta)
    respuesta += paso
    
if abs(respuesta**2 - number) >= epsilon:
    print(f"No se encontró la raíz cuadrada de {number}")
else:
    print(f"La raíz cuadrada de {number} es {respuesta}")
```

# Busqueda Binaria

Uno de los algoritmos mas importante de Computer Science y de los mas eficientes. Cuando utilizamos la busqueda binaria uno de los requisitos es que nuestro conjunto de busqueda tiene que estar ordenado **TIENE QUE EXISTIR UN ORDEN**.

> Es altamente eficiente, pues corta el espacio de búsqueda en dos por cada iteración

Los pasos son los siguientes:

1. Consideramos como segmento inicial de búsqueda a la lista completa.
2. Analizamos el punto medio del segmento (el valor central), si es el valor buscado, devolvemos el índice del punto medio.
3. Si el valor central es mayor al buscado, podemos descartar el segmento que está desde el punto medio hacia la a derecha.
4. Si el valor central es menor al buscado, podemos descartar el segmento que está desde el punto medio hacia la izquierda.
5. Una vez descartado el segmento que no nos interesa, volvemos a analizar el segmento restante, de la misma forma.
6. Si en algún momento el segmento a analizar tiene longitud 0 o negativa significa que el valor buscado no se encuentra en la lista.

```py
number = int(input("Ingrese un número: "))

epsilon = 0.01  # Definimos nuestro margen de error.
bajo = 0.0  # Inicializamos la parte baja de nuestra búsqueda como 0
alto = max(1.0, number)  # Entre el numero que ingresamos y 1 vamos a tomar el mayor valor.
respuesta = (alto + bajo) / 2  # Definimos la mitad entre bajo y alto.


# Mientras el margen de error sea mayor a epsilon.
while abs(respuesta**2 - number) >= epsilon:
    print(f"bajo = {bajo}, alto = {alto}, respuesta = {respuesta}")
    
    # Si ((alto+bajo)/2)^2 es menor a nuestro numero objetivo
    if respuesta**2 < number:

        # Definimos la parte baja de nuestra búsqueda como (alto + bajo)/2
        bajo = respuesta

     # En caso que (alto+bajo)/2 es mayor a nuestro numero objetivo
    else:

         # Definimos la parte alta de nuestra búsqueda como (alto + bajo)/2
        alto = respuesta

    # Luego definimos nuevamente la mitad entre alto y bajo.
    respuesta = (alto + bajo) / 2
    
print(f"La raíz cuadrada de {number} es {respuesta}")
```