l import math


#BUSQUEDA LINEAL
def linear_search(number1, list1):
  number_in_list = False
  if number1 in list1:
    number_in_list = True
  return number_in_list



#BUSQUEDA BINARIA
def findInList (number, list1):
  #Si es una lista vacía el número no está acá
  if len(list1) == 0:
    return False
  #Obtengo el medio redondeado para abajo
  middle_index = math.floor((len(list1)/2))
  #Si el elemento del medio del array es el que busco, terminé
  if number == list1[middle_index]:
    return True
  else:
    #Como es una lista ordenada, el número potencialmente se encuentra antes o después
    if number > list1[middle_index]:
      #Repito la búsqueda del número en la segunda mitad
      return False or findInList(number, list1[middle_index:len(list1)-1])
    #Repito la búsqueda del número en la primera mitad
    return False or findInList(number, list1[0:middle_index])
