
cuvinte_pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
cuvinte_negative = ["urat", "prost", "groaznic", "dezamagitor"]

comentariu = input("Introduceti comentariul: ").lower().strip()

este_pozitiv = False
este_negativ = False

for cuvant in cuvinte_pozitive:
    if cuvant in comentariu:
        este_pozitiv = True

for cuvant in cuvinte_negative:
    if cuvant in comentariu:
        este_negativ = True

if este_pozitiv:
    print("Comentariu pozitiv!")
elif este_negativ:
    print("Comentariu negativ!")
else:
    print("Comentariu neutru.")