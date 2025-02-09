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
    
    pass

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
        
        pass
        
    def metodo_maestro(self):
        """
        Devuelve una cadena con el tiempo de la recurrencia de acuerdo al 
        método maestro. La salida está en el formato "O(n^x)" o "O(n^x*log(n))",
        siendo x un número.
        """
        
        pass
       
    def __iter__(self):
        """
        Generador de valores de la recurrencia: T(0), T(1), T(2), T(3)..., 
        indefinidamente.
        Aunque sea una recurrencia, los valores *no* deben calcularse 
        recursivamente.
        """
        
        pass     