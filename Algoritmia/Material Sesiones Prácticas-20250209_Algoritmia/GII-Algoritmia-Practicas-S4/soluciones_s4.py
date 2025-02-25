import heapq

# ================================
# Funciones genéricas de grafos
# ================================

def numero_nodos(grafo):
    """Número de nodos en el grafo"""
    return len(grafo)

def numero_arcos(grafo):
    """Número de arcos en el grafo"""
    return sum(len(grafo[nodo]) for nodo in grafo)

def peso_total(grafo):
    """Suma de los pesos de los arcos del grafo"""
    return sum(sum(grafo[nodo].values()) for nodo in grafo)

def arco(grafo, origen, destino):
    """
    Si hay un arco de origen a destino, devuelve su peso. 
    Si no hay, devuelve None.
    """
    if origen in grafo and destino in grafo[origen]:
        return grafo[origen][destino]
    return None

# ====================================
# Operaciones de modificación del grafo
# ====================================

def inserta_nodo(grafo, nodo):
    """
    Inserta el nodo en el grafo.
    Si ya estaba, no se modifica.
    Devuelve el propio grafo.
    """
    if nodo not in grafo:
        grafo[nodo] = {}
    return grafo

def inserta_arco(grafo, origen, destino, peso=1):
    """
    Inserta el arco en el grafo.
    Si ya estaba se actualiza el peso.
    Devuelve el propio grafo.
    """
    inserta_nodo(grafo, origen)
    inserta_nodo(grafo, destino)
    grafo[origen][destino] = peso
    return grafo

# ====================================
# Operaciones de consulta sobre el grafo
# ====================================

def grado(grafo, nodo, salida=True):
    """
    Devuelve el grado de salida o entrada de un nodo del grafo.
    Estos grados son el número de arcos que salen o llegan al nodo.
    """
    if salida:
        return len(grafo.get(nodo, {}))
    else:
        count = 0
        for origen in grafo:
            if nodo in grafo[origen]:
                count += 1
        return count

def pesos_adyacentes(grafo, nodo, salida=True):
    """
    Devuelve la suma de los pesos de los arcos adyacentes al nodo, 
    de salida o entrada.
    """
    if salida:
        return sum(grafo.get(nodo, {}).values())
    else:
        total = 0
        for origen in grafo:
            if nodo in grafo[origen]:
                total += grafo[origen][nodo]
        return total

def coste_camino(grafo, camino):
    """
    Devuelve el coste del camino en el grafo.
    El camino viene dado como una secuencia de nodos.
    Si esa secuencia no forma un camino, devuelve None.
    """
    if not camino or len(camino) < 2:
        return 0  # Camino vacío o de un solo nodo
    coste = 0
    for i in range(len(camino)-1):
        p = arco(grafo, camino[i], camino[i+1])
        if p is None:
            return None
        coste += p
    return coste

# =======================
# Algoritmos sobre grafos
# =======================

def prim(grafo, inicial=None):
    """
    Implementa el algoritmo de Prim para obtener el árbol de expansión mínima de un grafo.
    Devuelve en el formato del grafo el árbol.
    
    Se asume que el grafo es conexo, no dirigido y sin bucles.
    """
    if not grafo:
        return {}
    
    if inicial is None:
        inicial = next(iter(grafo))
    
    # Inicializamos el MST con todos los nodos, sin arcos
    mst = {nodo: {} for nodo in grafo}
    visitados = {inicial}
    # Cola de prioridad: (peso, origen, destino)
    cola = []
    for destino, peso in grafo[inicial].items():
        heapq.heappush(cola, (peso, inicial, destino))
    
    while cola and len(visitados) < len(grafo):
        peso, origen, destino = heapq.heappop(cola)
        if destino in visitados:
            continue
        # Se añade el arco al árbol (se agrega en ambas direcciones, ya que el grafo es no dirigido)
        mst[origen][destino] = peso
        mst[destino][origen] = peso
        visitados.add(destino)
        for siguiente, p in grafo[destino].items():
            if siguiente not in visitados:
                heapq.heappush(cola, (p, destino, siguiente))
    return mst

def dijkstra(grafo, inicial):
    """
    Implementa el algoritmo de Dijkstra.
    Devuelve un diccionario donde para cada nodo se asocia una tupla (predecesor, distancia mínima)
    desde el nodo inicial.
    """
    distancias = {nodo: float('inf') for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    distancias[inicial] = 0
    
    cola = [(0, inicial)]
    while cola:
        d, nodo_actual = heapq.heappop(cola)
        if d > distancias[nodo_actual]:
            continue
        for vecino, peso in grafo[nodo_actual].items():
            nueva_dist = d + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_dist, vecino))
    
    # Se construye el diccionario resultado: cada nodo se asocia a (predecesor, distancia)
    return {nodo: (predecesores[nodo], distancias[nodo]) for nodo in grafo}

def obten_camino_minimo(inicial, final, caminos_pre_calculados):
    """
    Devuelve el camino mínimo entre dos nodos, a partir de la información obtenida con Dijkstra.
    Se asume que 'caminos_pre_calculados' es un diccionario en el que cada nodo se asocia a una tupla
    (predecesor, distancia). Si no hay camino, devuelve None.
    
    Además, si el diccionario no corresponde al nodo inicial proporcionado 
    (es decir, el valor asociado a 'inicial' no es (None, 0)), se lanza una excepción.
    """
    if caminos_pre_calculados.get(inicial) != (None, 0):
        raise Exception("El diccionario de caminos no corresponde al nodo inicial proporcionado.")
    
    camino = []
    nodo = final
    while nodo is not None:
        camino.append(nodo)
        if nodo == inicial:
            break
        nodo = caminos_pre_calculados.get(nodo, (None,))[0]
    if camino[-1] != inicial:
        return None
    camino.reverse()
    return camino

# ================================
# Ejemplo de grafo (no se utiliza en testing)
# ================================

grafo_de_ejemplo = {
    'a': {'b': 1, 'c': 2},
    'b': {'a': 3, 'd': 6},
    'c': {'a': 5, 'b': 2},
    'd': {}
}

