
tari_risc = ["Coreea de Nord", "Siria", "Iran"]
contor_suspecte = 0
tranzactii_efectuate = 0

print(" *** SISTEM DE MONITORIZARE BANCARA ***")

while contor_suspecte < 3:
    print(f"\nIntroducere Tranzactia #{tranzactii_efectuate + 1}:")

    suma = float(input("Suma tranzactiei (RON): "))
    tara = input("Tara de origine: ").strip().capitalize()

    tranzactii_efectuate += 1
    este_problema = False

    if tara in tari_risc:
        print(f"Tranzactie: {suma} RON din {tara} -> Frauduloasa (tara cu risc ridicat)")
        contor_suspecte += 1
        este_problema = True
    elif suma > 10000:
        print(f"Tranzactie: {suma} RON din {tara} -> Suspicioasa (suma mare)")
        contor_suspecte += 1
        este_problema = True
    else:
        print(f"Tranzactie: {suma} RON din {tara} -> Sigura")

    if este_problema:
        print(f"Atentie! Ai {contor_suspecte} tranzactii suspecte detectate.")

print("\n" + "!" * 30)
print(f"{contor_suspecte} tranzactii suspecte detectate! CONT BLOCAT.")
print("Va rugam sa contactati banca pentru deblocare.")