numere_pare = [x for x in range(0, 101) if x % 2 == 0]
print("Numere pare:", numere_pare)

cuburi = [x**3 for x in range(1, 11)]
print("Cuburile primelor 10 numere:", cuburi)

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comune = [x for x in lista1 if x in lista2]
print("Elemente comune:", comune)