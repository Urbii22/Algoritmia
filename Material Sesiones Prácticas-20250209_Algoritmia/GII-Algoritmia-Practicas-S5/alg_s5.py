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
        Inicialmente, cada elemento forma un subconjunto.
        """

        self.padre = {elem: elem for elem in iterable}
        self.tam = {elem: 1 for elem in iterable}
        self.rango = {elem: 0 for elem in iterable}

    def __len__(self):
        """Devuelve el número de subconjuntos en la partición."""
        return sum(1 for elem in self.padre if self.padre[elem] == elem)

    def numero(self, k=None):
        """
        Devuelve el número de elementos del subconjunto al que pertenece el 
        elemento k. 
        Si k es None devuelve el número de elementos.
        """
        if k is None:
            return sum(self.tam[rep] for rep in self.padre if rep == self.padre[rep])
        else:
            rep = self.__getitem__(k)
        return self.tam[rep]

        

    def __getitem__(self, k): #obtenemos la clase del objeto
        """
        Devuelve el subconjunto al que pertenece el elemento k.
        El subconjunto se identifica mediante uno de sus elementos.
        """
        if self.padre[k] != k:
            self.padre[k] = self.__getitem__(self.padre[k])

        return self.padre[k]


    def __iter__(self):
        """
        Devuelve un iterador sobre los subconjuntos.
        Cada subconjunto se identifica mediante uno de sus elementos.
        """
        return (elem for elem in self.padre if elem == self.padre[elem])

    
    def une(self, a, b):
        """Une los subconjuntos a los que pertencen a y b."""
        
        a_rep = self.__getitem__(a)
        b_rep = self.__getitem__(b)

        if a_rep == b_rep:
            return a_rep

        if self.rango[a_rep] < self.rango[b_rep]:
            self.padre[a_rep] = b_rep
            self.tam[b_rep] += self.tam[a_rep]

        elif self.rango[a_rep] > self.rango[b_rep]:
            self.padre[b_rep] = a_rep
            self.tam[a_rep] += self.tam[b_rep]

        else:
            # En caso de igualdad, eliges uno y actualizas el rango
            self.padre[b_rep] = a_rep
            self.tam[a_rep] += self.tam[b_rep]
            self.rango[a_rep] += 1

# Sugerencia: Implementar con las diveras técncias de unión-pertenencia vistas en clase y probar los tiempos de ejecución.
def kruskal(grafo):
    """
    Dado un grafo devuelve otro grafo con el árbol expandido mínimo,
    utilizando el algoritmo de Kruskal.
    Los grafos son diccionario donde las claves son arcos (pares de nodos) y los
    valores son el peso de los arcos.
    """

    nodos = set()
    for (u, v) in grafo:
        nodos.add(u)
        nodos.add(v)

    p = Particion(nodos)

    arcos_ordenados=sorted(grafo.items(), key=lambda x: x[1])

    arbol = {}
    for (u, v) , peso in arcos_ordenados:
        if p.__getitem__(u) != p.__getitem__(v):
            p.une(u, v)
            arbol[u, v] = peso
# Sugerencia: Prueba a implementar Kruskal para un grafo que esté en formato de matriz de adyacencia.

# Sugerencia: Compara los tiempos de ejecución del algoritmo de Kruskal con los del algormitmo de Prim.