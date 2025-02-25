# # Algoritmia
# ## Práctica 5

# En esta práctica se implementan las estructuras unión pertenencia y el algoritmo de Kruskal.

# En el cuerpo de cada función o método a implementar hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.


# todo esto lo ha hecho copilot solo, wow
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
        self.parent = {}
        self.rank = {}
        self.size = {}
        for x in iterable:
            self.parent[x] = x
            self.rank[x] = 0
            self.size[x] = 1
            
    def _find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self._find(self.parent[x])
        return self.parent[x]

    def __len__(self):
        """Devuelve el número de subconjuntos en la partición."""
        return sum(1 for x in self.parent if self.parent[x] == x)

    def numero(self, k=None):
        """
        Devuelve el número de elementos del subconjunto al que pertenece el 
        elemento k. 
        Si k es None devuelve el número total de elementos.
        """
        if k is None:
            return len(self.parent)
        root = self._find(k)
        return self.size[root]

    def __getitem__(self, k):
        """
        Devuelve el subconjunto al que pertenece el elemento k.
        El subconjunto se identifica mediante uno de sus elementos (el representante).
        """
        return self._find(k)

    def __iter__(self):
        """
        Devuelve un iterador sobre los subconjuntos.
        Cada subconjunto se identifica mediante uno de sus elementos representante.
        """
        seen = set()
        for x in self.parent:
            rep = self._find(x)
            if rep not in seen:
                seen.add(rep)
                yield rep

    def une(self, a, b):
        """Une los subconjuntos a los que pertenecen a y b."""
        rootA = self._find(a)
        rootB = self._find(b)
        if rootA == rootB:
            return
        # Unión por rango
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
            self.size[rootB] += self.size[rootA]
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
            self.size[rootA] += self.size[rootB]


def kruskal(grafo):
    """
    Dado un grafo devuelve otro grafo con el árbol expandido mínimo,
    utilizando el algoritmo de Kruskal.
    Los grafos son diccionario donde las claves son arcos (pares de nodos) y los
    valores son el peso de los arcos.
    """
    # Obtener todos los nodos presentes en el grafo
    nodos = set()
    for (u, v) in grafo.keys():
        nodos.add(u)
        nodos.add(v)

    particion = Particion(nodos)
    # Ordenar las aristas por peso
    aristas_ordenadas = sorted(grafo.items(), key=lambda x: x[1])
    arbol = {}

    for (u, v), peso in aristas_ordenadas:
        if particion._find(u) != particion._find(v):
            particion.une(u, v)
            arbol[(u, v)] = peso

    return arbol