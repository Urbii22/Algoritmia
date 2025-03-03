# # Algoritmia
# ## Práctica 6
# En esta práctica se resolverá el problema de las Torres de Hanoi, con dos añadidos: el número de postes puede ser mayor que 3, los discos pueden estar en cualquiera de los postes.

# En el cuerpo de cada función o método a implementar hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

class Hanoi:
    """Clase para representar las torres de Hanoi."""

    def __init__(self, discos, num_postes=None):
        """
        El parámetro discos es un entero o una secuencia.
        Si es un entero se refiere al número de discos en el primer poste.
        Si es una secuencia, cada elemento indica en qué poste está el disco.
        Los postes se identifican como 1, 2, 3...
        El primer elemento de la secuencia se refiere al disco más pequeño,
        el último al más grande.
        El parámetro num_postes es el número de postes.
        Si num_postes es None, será el máximo de 3 y el mayor valor que aparezca
        en discos
        """

        if isinstance(discos, int):
            discos = [1] * discos # todos los discos en el poste 1
        else:
            discos = list(discos)    
        self._discos = discos
        
        if num_postes is None:
            num_postes = max(3, max(discos))
        
        self._num_postes = num_postes

        # Almacenamos los postes como una lista de listas
        self._postes = [[] for _ in range(num_postes)]
        i = len(discos)
        for d in discos[::-1]:
            self._postes[d - 1].append(i)
            i -= 1

    def __len__(self):
        """Devuelve el número de discos"""
        
        return len(self._discos)

    def mueve(self, origen, destino):
        """Mueve el disco superior del poste origen al poste destino."""
        
        assert 1 <= origen <= self._num_postes
        assert 1 <= destino <= self._num_postes

        poste_origen = self._postes[origen - 1]
        poste_destino = self._postes[destino - 1]
               
        assert len(poste_origen) > 0 # hay discos en el poste origen
        disco = poste_origen[-1]

        # comprobamos si podemos mover el disco:
        assert (len(poste_destino) == 0 # el destino está vacío
                or disco < poste_destino[-1]) # contiene un disco mayor

        # movemos:
        self._discos[disco - 1] = destino
        poste_origen.pop()
        poste_destino.append(disco)
    
    def __str__(self):
        return str(self._discos)
    
    def realiza_movimientos(self, movimientos, imprime=False):
        """
        Realiza varios movimientos, cada movimiento se indica como un par
        (origen, destino).
        """
        
        if imprime:
            self.imprime()
        for origen, destino in movimientos:
            self.mueve(origen, destino)
            if imprime:
                print("\n", origen, "->", destino, sep="")
                self.imprime()


    def imprime(self):        
        """Imprime una representación gráfica de las torres"""

        n = len(self)
        for nivel in range(len(self) - 1, -1, -1):
            for poste in self._postes:
                if nivel >= len(poste):
                    print("|", " " * (n - 1), sep="", end=" ")
                else:
                    disco = poste[nivel]
                    print("X" * disco, " " * (n - disco), sep="", end=" ")
            print()
        for _ in self._postes:
            print("=" * n, sep=" ", end=" ")
        print()
        
    def resuelve(self, destino=None):
        """
        Resuelve el problema, moviendo todos los discos al poste destino,
        partiendo de cualquier configuración inicial.
        Si el argumento destino es None, el poste destino es el último.
        Devuelve una secuencia con los movimientos, cada movimiento es un par
        (origen, destino).
        Si hay más de 3 postes, el resto también se deberían utilizar en algunos 
        casos.
        """
        
        pass