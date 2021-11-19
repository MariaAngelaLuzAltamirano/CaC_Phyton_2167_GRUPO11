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



