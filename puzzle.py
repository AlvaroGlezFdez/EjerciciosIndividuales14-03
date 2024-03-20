
class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A                               #1      
y = a.z                             #2
print(y(a))                         #3
aa = a()                            #4
print(aa is a())                    #5 
z = aa.y                            #6
print(z(()))                        #7
print(a().y((a,)))                  #8 
print(A.y(aa, (a,z)))               #9
print(aa.y((z,1,'z')))   
print(type(a))           #10



#1:
"""
En esta primera parte simplemente se está nombrando la Clase A en una variable "a"
"""
#2
"""
Aquí se está asignando el método de instancia z perteneciente a la clase A a la variable y
"""
#3
"""
Se imprime la clase A
"""
#4
"""
se está creando una instancia perteneciente a la clase a
"""
#5
"""
aquí imprime false porque aa se refiere a a(), pero no es lo mismo, es decir,
a() crea una instancia y aa se refiere a ella, es lo mismo que en #1, donde pone que 
a = A, pero no es lo mismo, ya que A es una clase y a es una variable que se refiere
a la clase, pero no es una clase
"""
#6
"""
está asignando el método y perteneciente a la variable aa, que se refiere a una
instancia de la clase A,  a una variable z.
"""
#7
"""
anteriormente vimos que z era la variable que representaba el método y
de una instancia perteneciente a la clase A, lo que pasa que se trataba de una
instancia sin argumento, es decir, vacía, por lo que al pasarla por el método y, 
nos devuelve 0, que es la longitud de su argumento.
"""
#8
"""
devuelve 1 ya que se está creando una nueva instancia de la clase A, que consta
de una tupla con 1 solo elemento como argumento, por lo que la longitud
de un elemento es 1
"""
#9
"""
Aquí imprime 2 ya que se está llamando al método y de la clase A y se le está
pasando como argumento una tupla constituida por dos elementos, por lo que 
la longitud de 2 es 2.
"""
#10
"""
Lo mismo que los dos últimos, se está llamando al método y de la case A y le 
está pasando como argumento una tupla formada por 3 elementos, por lo que 
la longitu de 3 es 3,
""" 
