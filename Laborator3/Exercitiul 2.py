def genereaza_factura(nume_client, **kwargs):
    print("Factura pentru:", nume_client)

    total = 0

    for produs, pret in kwargs.items():
        print(produs, ":", pret, "lei")
        total += pret

    print("Total de plata:", total, "lei")

genereaza_factura("Ana",paine=5,lapte=7,oua=10)