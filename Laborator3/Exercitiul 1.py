def joaca_rps():
    reguli = {
        "piatra": "foarfeca",
        "foarfeca": "hartie",
        "hartie": "piatra"
    }

    optiuni = ["piatra", "hartie", "foarfeca"]

    while True:
        j1 = input("Jucator 1 (piatra/hartie/foarfeca): ").lower()
        j2 = input("Jucator 2 (piatra/hartie/foarfeca): ").lower()

        if j1 not in optiuni or j2 not in optiuni:
            print("Alegere invalida! Incearca din nou.")
            continue

        if j1 == j2:
            print("Egalitate!")
        else:
            if reguli[j1] == j2:
                print("Felicitari! Jucatorul 1 a castigat!")
            else:
                print("Felicitari! Jucatorul 2 a castigat!")

        rejucare = input("Doresti sa mai joci? (da/nu): ").lower()

        if rejucare != "da":
            print("La revedere!")
            break

joaca_rps()