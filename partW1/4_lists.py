#creation
c = True
lista = ["a", 'b', 1, c, 1.000054]
print(lista)
print(lista[0])
print(lista[-2])
print(lista[1:3])
#concatenation
lista = lista + lista
print(lista)
lista = 2 * lista
print(lista)
#replace list elements
lista[1] = False
print(lista)
#add element to the end of list
lista = [False]
lista.append(True)
print(lista)
lista[0:2] = []
#lista[0:5] = []
print(lista)
lista = ["a", 'b', 1, c, 1.000054]
lista[:] = []
print(lista)
#count list elements
print(len(lista))
lista = ["a", 'b', 1, c, 1.000054]
print(len(lista))
#list of lists
lista1 = ["a", 'b', 1, c, 1.000054]
lista2 = [True, False]
lista3 = [lista1, lista2]
print(lista3)