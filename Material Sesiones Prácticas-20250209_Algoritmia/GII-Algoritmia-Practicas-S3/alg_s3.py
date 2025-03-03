# # Algoritmia
# ## Práctica 3

# El objetivo de esta práctica es trabajar con los algoritmos de la mochila y dar la vuelta. 

# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada. 

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.


def dar_la_vuelta(cambio, valores_monedas):
    """
    Se recibe una cantidad de dinero y una lista de monedas. Se devuelve un generador de las monedas que se necesitan para dar ese cambio de forma que se minimice el número de monedas.

    Se han de devolver las monedas de mayor a menor valor.

    Nota: Para evitar el problema de los decimales en python se puede usar la función round() para redondear a dos decimales.
    """
    monedas = sorted (valores_monedas, reverse = True)

    while round(cambio, 2) > 0:
        for elem in monedas:
           while elem <= round(cambio, 2):
                yield elem
                cambio =round(cambio, 2) - elem



# Implementa dar la vuelta utilizando las recomendaciones de la diapositiva 5 de la presentación del tema 2 y comprueba si es más rápido que la implementación básica.


def algoritmo_mochila_voraz(objetos, peso_soportado):     #MUY POSIBLE EXAMEN
    """
    Se recibe un diccionario de objetos, cada elemento del diccionario es una tupla (peso, valor)
    y una variable numérica, peso_soportado.
    Seleccionar las claves de los objetos cuya suma del peso no sea mayor que el peso soportado y se 
    maximice el valor usando un algoritmo voraz. Los objetos no pueden partirse.
    """

    ratios = sorted(objetos.items(), key=lambda item: item[1][1] / item[1][0], reverse=True)

    peso_actual = 0
    seleccion = []

    for clave, (peso, valor) in ratios:
        if peso + peso_actual <= peso_soportado:
            seleccion.append(clave)
            peso_actual += peso

    return seleccion


"""
SI QUISIERA PARTIR OBJETOS:

objetos = sorted (objetos.items(), key = lambda x: x[1][1] / x[1][0], reverse = True
peso = 0
candidatos= {k:0 for k in candidatos}
for k, (p,v) in objetos:
    if peso + p <= peso_soportado:
        candidatos[k] = 1
        peso +=p
        valor +=v
    else:
        candidatos[k] = (peso_soportado - peso) /p
        peso += (peso_soportado -peso)
        break # imposible que quede mas espacio, mochila llena
return candidatos
    
"""





"""
Diferncias entre Alg optimo y aproximado.
OPTIMO: Encuentra maximo o minimo GLOBAL
APROXIMADO: Encuentra maximo o minimo LOCAL
"""
