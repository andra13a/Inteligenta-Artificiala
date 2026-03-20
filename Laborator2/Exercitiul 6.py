print("Bine ai venit in Padurea Magica!")
print("Aventura ta incepe acum...\n")

inventar = []

directie = input("Alegi directia (stanga/dreapta): ").lower()

if directie == "stanga":
    print("\nMergi pe o poteca intunecata...")

    actiune = input("Intalnesti un lup! Fugi sau lupti? ")

    if actiune == "lupti":
        print("Ai invins lupul!")
        inventar.append("blana de lup")
    else:
        print("Ai fugit si ai scapat!")

    print("\nContinui drumul si gasesti o lada misterioasa...")
    print("In ea gasesti o lampa magica!")
    inventar.append("lampa magica")

    dorinta = input("Vrei sa o folosesti? (da/nu): ")

    if dorinta == "da":
        print("Geniul iti ofera o moneda de aur!")
        inventar.append("moneda de aur")
    else:
        print("Pastrezi lampa pentru mai tarziu.")

    print("\nMai departe gasesti o pestera...")
    actiune2 = input("Intri sau pleci? ")

    if actiune2 == "intri":
        print("Gasesti o sabie de foc!")
        inventar.append("sabie de foc")
    else:
        print("Eviti pericolul si mergi mai departe.")

elif directie == "dreapta":
    print("\nAjungi la un lac magic...")

    print("Pe marginea lacului gasesti o sabie de gheata!")
    inventar.append("sabie de gheata")

    actiune = input("Apare un zmeu! Lupti sau fugi? ")

    if actiune == "lupti":
        if "sabie de gheata" in inventar:
            print("Ai invins zmeul!")
            inventar.append("comoara rara")
        else:
            print("Nu ai arma! Ai pierdut!")
    else:
        print("Ai fugit!")

    print("\nDupa lupta gasesti un saculet...")
    print("In el sunt monede de aur!")
    inventar.append("moneda de aur")

    actiune2 = input("Mergi mai departe sau te intorci? ")

    if actiune2 == "mergi":
        print("Gasesti o lampa magica abandonata!")
        inventar.append("lampa magica")
    else:
        print("Te intorci in siguranta.")

else:
    print("Directie invalida!")

print("\nAventura s-a incheiat!")
print(f"Inventarul tau: {inventar}")