orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pare = list(filter(lambda x: x % 2 == 0, orig_list))

lista_impare = list(filter(lambda x: x % 2 != 0, orig_list))

print("Numere pare:", lista_pare)
print("Numere impare:", lista_impare)