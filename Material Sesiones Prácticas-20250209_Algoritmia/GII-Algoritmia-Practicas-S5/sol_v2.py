# # Algoritmia
# ## Práctica 5

# En esta práctica se implementan las estructuras unión pertenencia y el algoritmo de Kruskal.

# En el cuerpo de cada función o método a implementar hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

class Particion:
    """
    Clase que implementa una partición de un conjunto en subconjuntos disjuntos.
    Una partición se corresponde con una estructura Unión-Pertenencia.
    """

    def __init__(self, iterable):
        """
        Crea una partición con los elementos del iterable.
        Inicialmente cada elemento forma un subconjunto.
        """
        self.padre = {elem: elem for elem in iterable}
        self.tamano = {elem: 1 for elem in iterable}
        self.total_elementos = len(self.padre)
            

    def __len__(self):
        """Devuelve el número de subconjuntos en la partición."""
        return len({self[elem] for elem in self.padre})

    def numero(self, k=None):
        """
        Devuelve el número de elementos del subconjunto al que pertenece el 
        elemento k. 
        Si k es None devuelve el número   de elementos.
        """
        if k is None:
            return self.total_elementos
        return self.tamano[self[k]]
        

    def __getitem__(self, k):
        """
        Devuelve el subconjunto al que pertenece el elemento k.
        El subconjunto se identifica mediante uno de sus elementos.
        """
        if self.padre[k] != k:
            self.padre[k] = self[self.padre[k]]  # Path compression
        return self.padre[k]


    def __iter__(self):
        """
        Devuelve un iterador sobre los subconjuntos.
        Cada subconjunto se identifica mediante uno de sus elementos.
        """
        representantes = set()
        for elem in self.padre:
            rep = self[elem]
            if rep not in representantes:
                representantes.add(rep)
                yield rep
    
    def une(self, a, b):
        """Une los subconjuntos a los que pertencen a y b."""
        a_rep = self[a]
        b_rep = self[b]
        
        if a_rep == b_rep:
            return  # Already in same subset
        
        # Union by size
        if self.tamano[a_rep] < self.tamano[b_rep]:
            self.padre[a_rep] = b_rep
            self.tamano[b_rep] += self.tamano[a_rep]
        else:
            self.padre[b_rep] = a_rep
            self.tamano[a_rep] += self.tamano[b_rep]

# Sugerencia: Implementar con las diveras técncias de unión-pertenencia vistas en clase y probar los tiempos de ejecución.

def kruskal(grafo):
    """
    Dado un grafo devuelve otro grafo con el árbol expandido mínimo,
    utilizando el algoritmo de Kruskal.
    Los grafos son diccionario donde las claves son arcos (pares de nodos) y los
    valores son el peso de los arcos.
    """
    # Extract all unique nodes from the graph
    nodos = set()
    for arco in grafo:
        nodos.add(arco[0])
        nodos.add(arco[1])
    
    # Create a partition of nodes
    p = Particion(nodos)
    
    # Sort edges by weight
    arcos_ordenados = sorted(grafo.items(), key=lambda x: x[1])
    
    # Result tree
    arbol = {}
    
    # Process edges in ascending order of weight
    for arco, peso in arcos_ordenados:
        u, v = arco
        # Check if adding this edge would create a cycle
        if p[u] != p[v]:
            arbol[arco] = peso
            p.une(u, v)
    
    return arbol

# Sugerencia: Prueba a implementar Kruskal para un grafo que esté en formato de matriz de adyacencia.

# Sugerencia: Compara los tiempos de ejecución del algoritmo de Kruskal con los del algormitmo de Prim.