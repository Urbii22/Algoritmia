# # Algoritmia
# ## Práctica 3

# El objetivo de esta práctica es trabajar con los algoritmos de la mochila y dar la vuelta.

# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.


def dar_la_vuelta(cambio, valores_monedas):
    """
    Se recibe una cantidad de dinero y una lista de monedas. Se devuelve un generador
    de las monedas que se necesitan para dar ese cambio de forma que se minimice el número de monedas.
    Se han de devolver las monedas de mayor a menor valor.
    Nota: Para evitar el problema de los decimales en python se puede usar la función round() para redondear a dos decimales.
    """
    # Ordenar las monedas de mayor a menor valor
    monedas = sorted(valores_monedas, reverse=True)

    while round(cambio, 2) > 0:
        for moneda in monedas:
            # Si la moneda cabe en el cambio restante
            if moneda <= round(cambio, 2):
                yield moneda
                cambio = round(cambio - moneda, 2)
                break
        else:
            # Si ninguna moneda cabe, significa que no se puede dar el cambio exacto
            raise ValueError("No es posible dar la vuelta exacta con las monedas disponibles")


# Implementa dar la vuelta utilizando las recomendaciones de la diapositiva 5 de la presentación del tema 2 y comprueba si es más rápido que la implementación básica.


def algoritmo_mochila_voraz(objetos, peso_soportado):
    """
    Se recibe un diccionario de objetos, donde cada elemento es una tupla (peso, valor),
    y una variable numérica peso_soportado.
    Se deben seleccionar las claves de los objetos cuya suma del peso no sea mayor que
    el peso soportado y se maximice el valor usando un algoritmo voraz. Los objetos no pueden partirse.
    """
    # Calcular el ratio valor/peso para cada objeto y ordenarlos de mayor a menor
    ratios = sorted(objetos.items(), key=lambda item: item[1][1] / item[1][0], reverse=True)

    peso_actual = 0
    seleccion = []

    for clave, (peso, valor) in ratios:
        if peso_actual + peso <= peso_soportado:
            seleccion.append(clave)
            peso_actual += peso

    return seleccion
