# ## Algoritmia
# ### Práctica 2
# El objetivo de esta práctica es trabajar con recurrencias


# Se pide la implementación de las funciones que aparecen a continuación. 
#
# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada. 
#
# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

# Importaciones
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
    yield from seq

    orden = len(coeficientes)
    n = orden

    while True:
        valor = 0
        for i in range(orden):
            valor += coeficientes[i] * seq[n - 1 - i]
        valor += funcion_adicional(n)
        seq.append(valor)
        yield valor
        n += 1



class RecurrenciaMaestra: 
    """
    Clase que representa una recurrencia de las que se consideran en el 
    teorema maestro, de la forma T(n)=aT(n/b)+n^k. Se interpreta que en n/b
    la división es entera.
    Además de los métodos que aparecen a continuación, tienen que funcionar 
    los siguientes operadores: 
        ==, !=,
        str(): la representación como cadena debe ser 'aT(n/b)+n^k'
        []: el parámetro entre corchetes es el valor de n para calcular T(n).
    """
    
    def __init__(self, a, b, k, inicial = 0):
        """
        Constructor de la clase, los parámetros a, b, y k son los que
        aparecen en la fórmula aT(n/b)+n^k. El parámetro inicial es el valor
        para T(0).
        """

        self.a = a
        self.b = b
        self.k = k
        self.inicial = inicial


        
    def metodo_maestro(self):
        """
        Devuelve una cadena con el tiempo de la recurrencia de acuerdo al 
        método maestro. La salida está en el formato "O(n^x)" o "O(n^x*log(n))",
        siendo x un número.
        """
        if self.a > 0 and self.b > 1:
            x = log(self.a, self.b)
        else:
            x = 0

        if self.a < self.b ** self.k :
            return f"O(n^{x})"
        elif self.a == self.b ** self.k:
            return f"O(n^{self.k}*log(n))"
        elif self.a > self.b ** self.k:
            return f"O(n^{self.k})"



       
    def __iter__(self):
        """
        Generador de valores de la recurrencia: T(0), T(1), T(2), T(3)..., 
        indefinidamente.
        Aunque sea una recurrencia, los valores *no* deben calcularse 
        recursivamente.
        """
    pass

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

    def __str__(self):
        return f"{self.a}T(n/{self.b})+n^{self.k}"


    def __getitem__(self, item):

        pass