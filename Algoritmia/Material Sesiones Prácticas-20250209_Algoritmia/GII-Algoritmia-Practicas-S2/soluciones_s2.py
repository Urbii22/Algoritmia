from math import log


def generador_recurrencia(coeficientes, funcion_adicional, iniciales):
    """
    Generador de valores de acuerdo a una recurrencia:
    F(n) = coeficientes[0]*F(n-1) + coeficientes[1]*F(n-2) + ...
         + funcion_adicional(n)
    Los valores iniciales son F(0) = iniciales[0], F(1) = iniciales[1],...
    Los valores que se generan son F(0), F(1), F(2),...
    Se deben generar los valores de uno en uno, no hay que devolver varios.
    Debe generar valores indefinidamente, no hay que poner límites.
    Aunque sea una recurrencia, los valores *no* deben calcularse recursivamente.
    """
    seq = list(iniciales)
    # Emitir los valores iniciales
    for v in seq:
        yield v

    orden = len(coeficientes)
    n = orden
    while True:
        # Cálculo iterativo del siguiente valor sin llamar a ninguna función auxiliar
        valor = 0
        for i in range(orden):
            valor += coeficientes[i] * seq[n - 1 - i]
        valor += funcion_adicional(n)
        seq.append(valor)
        yield valor
        n += 1


class RecurrenciaMaestra:
    """
    Representa una recurrencia del tipo T(n) = aT(n//b) + n^k, donde la división es entera.
    Además de los métodos indicados, deben funcionar los operadores:
        ==, !=,
        str() con la representación 'aT(n/b)+n^k',
        [] para obtener T(n).
    """

    def __init__(self, a, b, k, inicial=0):
        """
        Constructor: se guardan los parámetros de la recurrencia y se inicializa T(0)=inicial.
        """
        self.a = a
        self.b = b
        self.k = k
        self.inicial = inicial
        # Se almacenan los valores calculados de T(n)
        self._valores = [inicial]

    def metodo_maestro(self):
        """
        Retorna una cadena con la complejidad según el método maestro, en el formato:
        "O(n^x)" o "O(n^x*log(n))", donde x es un número.
        Se evita el uso de funciones auxiliares para comparar reales.
        """
        # Calcular x = log_b(a)
        if self.a > 0 and self.b > 1:
            x = log(self.a, self.b)
        else:
            x = 0
        # Usamos una tolerancia pequeña para la comparación entre k y x
        tol = 1e-9
        if self.k < x - tol:
            return f"O(n^{x})"
        elif abs(self.k - x) <= tol:
            return f"O(n^{self.k}*log(n))"
        else:
            return f"O(n^{self.k})"

    def __iter__(self):
        """
        Generador que produce los valores T(0), T(1), T(2), ... de forma iterativa.
        No se utilizan métodos auxiliares para el cálculo.
        """
        # Primero se entregan los valores ya calculados
        for valor in self._valores:
            yield valor
        n = len(self._valores)
        while True:
            indice = n // self.b  # División entera
            # Calcular T(n) = a * T(n//b) + n^k sin funciones auxiliares
            valor = self.a * self._valores[indice] + (n ** self.k)
            self._valores.append(valor)
            yield valor
            n += 1

    def __getitem__(self, n):
        """
        Permite obtener T(n) usando la notación objeto[n].
        Se calcula iterativamente hasta llegar al valor solicitado.
        """
        while len(self._valores) <= n:
            indice = len(self._valores) // self.b
            valor = self.a * self._valores[indice] + ((len(self._valores)) ** self.k)
            self._valores.append(valor)
        return self._valores[n]

    def __str__(self):
        """
        Representación en cadena: 'aT(n/b)+n^k'.
        """
        return f"{self.a}T(n/{self.b})+n^{self.k}"

    def __eq__(self, other):
        if not isinstance(other, RecurrenciaMaestra):
            return NotImplemented
        return (self.a == other.a and self.b == other.b and
                self.k == other.k and self.inicial == other.inicial)

    def __ne__(self, other):
        eq = self.__eq__(other)
        if eq is NotImplemented:
            return NotImplemented
        return not eq


