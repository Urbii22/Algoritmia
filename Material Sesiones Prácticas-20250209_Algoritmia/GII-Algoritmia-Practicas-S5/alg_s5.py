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
        pass
            

    def __len__(self):
        """Devuelve el número de subconjuntos en la partición."""
        pass

    def numero(self, k=None):
        """
        Devuelve el número de elementos del subconjunto al que pertenece el 
        elemento k. 
        Si k es None devuelve el número de elementos.
        """
        pass
        

    def __getitem__(self, k):
        """
        Devuelve el subconjunto al que pertenece el elemento k.
        El subconjunto se identifica mediante uno de sus elementos.
        """
        pass


    def __iter__(self):
        """
        Devuelve un iterador sobre los subconjuntos.
        Cada subconjunto se identifica mediante uno de sus elementos.
        """
        pass
    
    def une(self, a, b):
        """Une los subconjuntos a los que pertencen a y b."""
        
        pass

# Sugerencia: Implementar con las diveras técncias de unión-pertenencia vistas en clase y probar los tiempos de ejecución.

def kruskal(grafo):
    """
    Dado un grafo devuelve otro grafo con el árbol expandido mínimo,
    utilizando el algoritmo de Kruskal.
    Los grafos son diccionario donde las claves son arcos (pares de nodos) y los
    valores son el peso de los arcos.
    """
    
    pass

# Sugerencia: Prueba a implementar Kruskal para un grafo que esté en formato de matriz de adyacencia.

# Sugerencia: Compara los tiempos de ejecución del algoritmo de Kruskal con los del algormitmo de Prim.