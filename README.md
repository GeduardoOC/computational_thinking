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

