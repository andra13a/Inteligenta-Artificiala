import random

print("Bine ai venit la Loteria Python!")
print("Alege 6 numere între 1 și 49")

numere_alese = []

for i in range(1,7):
    numar = int(input( f"Numarul {i}: "))
    while numar < 1 or numar > 49:
        numar = int(input(f"Invalid! Alege un numar intre 1 si 49 pentru pozitia {i}: "))
    numere_alese.append(numar)

numere_extrase = random.sample(range(1,50),6)
ghicite = list(set(numere_alese).intersection(set(numere_extrase)))


print(f"Numere extrase: {numere_extrase}")
print(f"Ai ghicit {len(ghicite)} numere: {ghicite}")

if len(ghicite) == 6:
    print("Ai castigat MARELE PREMIU!")
elif len(ghicite) >=3:
    print("Felicitari! Ai castigat un premiu mic!")
else:
    print("Mai incearca, data viitoare va fi cu noroc!")