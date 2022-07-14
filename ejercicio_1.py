#Matias tapia
#Prueba 3

import random
import numpy as np

def escribir_numeros_random(cantidad):
  with open('./numeros_prueba.txt', 'w', encoding="utf-8") as file:
    for x in range(cantidad):
      numero_aleatorio = random.randint(100, 1000)
      file.write(str(numero_aleatorio))
      file.write("\n")

def leer_archivo():
    numeros = []
    numeros_impar = []
    with open('./numeros_prueba.txt', 'r') as file:
        for linea in file:
            numeros.append(int(linea))
    for numero in numeros:
      if(numero%2 != 0):
        numeros_impar.append(numero)
    return numeros,numeros_impar

def dimension_lista(lista):
    dimension = np.array(lista)
    print("La dimension de la lista es de: " + str(dimension.ndim))

def main():
  escribir_numeros_random(20)
  numeros = []
  numeros_par = []
  numeros,numeros_impar = leer_archivo()
  #print("el documento 'numeros_prueba.txt' contiene la siguiente lista de numeros" + str(numeros))
  print("la lista final es " + str(numeros_impar))
  dimension_lista(numeros_impar)

#Punto de entrada
if __name__ == "__main__":
    main()
