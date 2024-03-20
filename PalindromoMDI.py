
# Creación de una clase Palíndromo

class Palindromo:
    #contructor de clase con su atributo 
    def __init__(self,CadenaDeTexto):
        self.CadenaDeTexto = CadenaDeTexto


    #método de instancia
    def test(self):
        if self.CadenaDeTexto == self.CadenaDeTexto[::-1]:
            return True
        else:
            return False
        

    #creación del método para borrar/destruir instancias
    def __del__(self):
        print ((self.CadenaDeTexto).upper())
  


my_input =Palindromo("".join((input("Ingrese una cadena de texto:")).upper().split()))



print(Palindromo.test(my_input))