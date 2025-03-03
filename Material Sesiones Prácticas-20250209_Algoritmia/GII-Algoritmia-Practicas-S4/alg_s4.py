# # Algoritmia
# ## Práctica 4

# El objetivo de esta práctica es trabajar con grafos.
# Se pide la implementación de las funciones que aparecen a continuación. 

# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada. 

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

# El grafo se puede representar como un diccionario de diccionarios o como una matriz de adyacencia.
# Para esta práctica se usará la representación de diccionario de diccionarios.

# NOTA: Los grafos son dirigidos y pesados.

grafo_de_ejemplo = {
        'a': {'b': 1, 'c': 2},
        'b': {'a': 3, 'd': 6},
        'c': {'a': 5, 'b': 2},
        'd': {}
    }

# Funciones genéricas de grafos
def numero_nodos(grafo):
    """Número de nodos en el grafo"""
    
    pass


def numero_arcos(grafo):
    """Número de arcos en el grafo"""
    
    pass


def peso_total(grafo):
    """Suma de los pesos de los arcos del grafo"""
    
    pass


def arco(grafo, origen, destino):
    """
    Si hay un arco de origen a destino, devuelve su peso. 
    Si no hay, devuelve None.
    """
    
    pass


# Operaciones de modificación

def inserta_nodo(grafo, nodo):
    """
    Inserta el nodo en el grafo.
    Si ya estaba, no se modifica.
    Devuelve el propio grafo."""
    
    pass


def inserta_arco(grafo, origen, destino, peso=1):
    """
    Inserta el arco en el grafo.
    Si ya estaba se actualiza el peso.
    Devuelve el propio grafo.
    """
    
    pass

# Operaciones de consulta
def grado(grafo, nodo, salida=True):
    """
    Devuelve el grado de salida o entrada de un nodo del grafo.
    Estos grados son el número de arcos que salen o llegan al nodo.
    """
    
    pass


def pesos_adyacentes(grafo, nodo, salida=True):
    """
    Devuelve la suma de los pesos de los arcos adyacentes al nodo, 
    de salida o entrada.
    """
    
    pass

def coste_camino(grafo, camino):
    """
    Devuelve el coste del camino en el grafo.
    El camino viene dado como una secuencia de nodos.
    Si esa secuencia no forma un camino, devuelve None.
    """
    
    pass

###################
# Habiendo creado las funciones anteriores, se pide implementar los siguientes métodos:

def prim(grafo, inicial=None):
    """
    Implementa el algoritmo de Prim para obtener el árbol de expansión mínima de un grafo. Devuelve en el formato del grafo el árbol.

    Se recuerda que un árbol es un grafo sin bucles y conectado.

    El grafo que se va a recibir siempre será conexo y sin direcciones.
    """

    pass


def dijkstra(grafo, inicial):
    """
    Implementa el algoritmo de Dijkstra
    Devuelve un diccionario con la distancia mínima desde el nodo inicial a cada uno de los nodos del grafo.
    """

    pass


def obten_camino_minimo(inicial, final, caminos_pre_calculados):
    """
    Devuelve el camino mínimo entre dos nodos, a partir de la información obtenida con Dijkstra.
    Si no hay camino, devuelve None.
    """

    pass