numere_pare = {x for x in range(20) if x % 2 == 0}
print("Primele 10 numere pare:", numere_pare)

text = "inteligenta artificiala"
litere_distincte = {litera for litera in text if litera != " "}
print("Litere distincte:", litere_distincte)

text = "Acesta este un exemplu de set comprehension pentru exercitii"
cuvinte_lungi = {cuvant for cuvant in text.split() if len(cuvant) >= 5}
print("Cuvinte cu cel puțin 5 litere:", cuvinte_lungi)