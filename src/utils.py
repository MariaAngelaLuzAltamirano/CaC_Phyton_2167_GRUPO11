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
