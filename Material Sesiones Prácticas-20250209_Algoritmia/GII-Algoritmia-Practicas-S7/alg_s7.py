# # Algoritmia
# ## Práctica 7
# En esta práctica se resolverá el problema de ordenación Divide y Vencerás

# En el cuerpo de cada función o método a implementar hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

# NO se deberá utilizar el método sort de las listas de Python. Se deberán implementar los algoritmos de ordenación.

def ordena(sequencia, key_function=lambda x:x, reverse=False, tipo="mergesort"):
    """
    Ordena la secuencia dada.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    El parámetro tipo indica el algoritmo de ordenación a usar. Puede ser "mergesort" o "quicksort".
    """
    if tipo == "mergesort":
        mergesort(sequencia, key_function, reverse)
    elif tipo == "quicksort":
        quicksort(sequencia, key_function, reverse)
    else:
        raise ValueError("Tipo de ordenación no válido")
    
def mergesort(sequencia, key_function, reverse):
    """
    Ordena la secuencia dada con el algoritmo mergesort.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.
    """
    pass

def quicksort(sequencia, key_function, reverse):
    """
    Ordena la secuencia dada con el algoritmo quicksort.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    Puedes utilizar el método de partición que quieras.
    """
    pass


# Sugerencia: Prueba los tiempos de los distitnos algoritmos de ordenación, así como sus variantes.

# Sugerencia: Comprueba formalmente y experimentalmente los tiempos de ordenación de los algoritmos para conjuntos ya ordenados, conjuntos ordenados en orden inverso y conjuntos aleatorios.

# Sugerencia: Prueba los tiempos comparando tu implementación con la del Timsort incluida en la función sorted de Python.