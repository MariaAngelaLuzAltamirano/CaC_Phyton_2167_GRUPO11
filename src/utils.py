def contarPares(n):
    """ Funcion que cuenta pares hasta n """
    contador = [] # Es un array vacio...
    for i in range(n):
        if (i % 2) == 0:
            contador.append(i)

    return contador

# Si son iguales... devuelve 0
# Si a es mayor que b... devuelve 1
# Si a es menor que b... devuelve -1
def comparoLista( a, b):

  sizeA = len(a)
  sizeB = len(b)
  comparasion = 0

  if sizeA < sizeB:
    comparasion = -1
  elif sizeA > sizeB:
    comparasion = 1

  return comparasion

# 4- Escribir una funcion que reciba un string con nombre y apellido y devuelva un string con el nombre y apellido
#pero con capitalizacion(primera letra mayuscula)

def mayusculaNombreApellido(nombreApellido):
  resultado = nombreApellido.title()
  return resultado

# 5- Escribir una funcion que reciba N numeros, los cuales representan la puntuacion de un concurso, y 
# esta devuelve la puntuacion del subcampeon. (ejemplo de ingreso de datos... [2,6,10,10,7,5,6], debe devolver 7)

def subcampeon (puntaje):
  puntaje.sort(reverse=True)
  maximo = max(puntaje)
  i=0
  while maximo == puntaje[i]:
    i=i+1
  return puntaje [i]


# 3- Los strings son inmutables, escribir una funcion que reciba un string, un indice y una letra a modificar de ese string y 
# que devuelve el string modificado.


def stringInmutables (string, indice, letra):

  letraAcambiar = string[indice]
  stringFinal = string.replace(letraAcambiar, letra)

  return stringFinal


# 2- Escribir una funcion que reciba un string y devuelva un string con la primera letra en mayuscula y el resto en minuscula

def uppercaseToLowercase(string):
    newString = ""

    if len(string) > 100:
        return "String mayor a 100 caracteres"
    else:
        for i in range(len(string)):
            if string[i].isupper():
                newString += string[i].lower()
            else:
                newString += string[i].upper()
                
	return newString

#Ejercicios con clases
#1 - Crear una clase que represente un numero complejo. Tenga 4 metodos que permita las operaciones matematicas basicas (+,-,*,/).
class numero_complejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario
#--------------------------Getter y Setter------------------------------------
    def getreal(self):
        return self.real
    
    def getimaginario(self):
        return self.imaginario

    def setreal(self, real):
        self.real = real
    
    def setimaginario(self, imaginario):
        self.imaginario = imaginario
        
    def __str__(self):
        if self.imaginario < 0:
            return "{} - {}i".format(self.real, abs(self.imaginario))
        else:
            return "{} + {}i".format(self.real, self.imaginario)

#----------------------------Metodos------------------------------------------
    def suma(c1,c2):
        a = c1.getreal()    #obtengo los valores de los atributos
        c = c2.getreal()    #tambien puede ser c = c2.real
        b = c1.getimaginario() 
        d = c2.getimaginario()
        aux = numero_complejo((a+c),(b+d))
        return aux

    def resta(c1, c2):
        a = c1.getreal() 
        c = c2.getreal()
        b = c1.getimaginario() 
        d = c2.getimaginario()
        aux = numero_complejo((a-c),(b-d))
        return aux

    def mul(c1, c2):
        a = c1.getreal() 
        c = c2.getreal()
        b = c1.getimaginario() 
        d = c2.getimaginario()
        aux = numero_complejo (((a*c) - (b*d)), ((a*d) + (b*c)))
        return aux
        
    def div(c1, c2):
        a = c1.getreal() 
        c = c2.getreal()
        b = c1.getimaginario() 
        d = c2.getimaginario()
        aux = (((a*c) + (b*d)) / ((c*c) + (d*d))), (((b*c) - (a*d)) / ((c*c) + (d*d)))
        return aux

c1 = numero_complejo(1.0,1.0)
c2 = numero_complejo(2.0,2.0)

print("Para los siguientes numeros complejos: ")
print("c1 = ",c1)
print("c2 = ",c2)

print("\nEl resultado de la operaciones son:\n")
c3 = numero_complejo.suma(c1,c2)
print("Suma")
print("c3 = ",c3)

c3 = numero_complejo.resta(c1,c2)
print("\nResta")
print("c3 = ",c3)

c3 = numero_complejo.mul(c1,c2)
print("\nMultiplicación")
print("c3 = ",c3)

c3 = numero_complejo.div(c1,c2)
print("\nDivision")
print("c3 = ",c3)