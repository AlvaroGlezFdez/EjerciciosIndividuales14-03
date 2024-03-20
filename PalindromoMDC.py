# Creación de una clase Palíndromo

class Palindromo:
    #contructor de clase

    def __init__(self,CadenaDeTexto):
        self.CadenaDeTexto = CadenaDeTexto
    
    
    @classmethod
        
     # Creción del método de clase que comprueba las dos cadenas de texto
        
    def esPalindromo(cls,cadena):
        if cadena == cadena[::-1]:
            return True
        else:
            return False
    
#crear un input que pida la cadena al usuario y la convierta en una cadena unida y en mayusculas
my_input ="".join((input("Ingrese una cadena de texto:")).upper().split())

    
Palindromo.esPalindromo(my_input)





    












