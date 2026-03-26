preturi = [100, 200, None, 50, None, 400]

preturi_valide = list(filter(lambda x: x is not None, preturi))
preturi_redus = list(map(lambda x: x * 0.9, preturi_valide))

print("Preturi originale (valide):", preturi_valide)
print("Preturi dupa reducere 10%:", preturi_redus)