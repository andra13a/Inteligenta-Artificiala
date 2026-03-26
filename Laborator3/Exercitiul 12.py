patrate = {x: x**2 for x in range(1, 11)}
print("Numere și pătratele lor:", patrate)

text = "programare"
litere_count = {litera: text.count(litera) for litera in set(text)}
print("Numărul de apariții ale fiecărei litere:", litere_count)

divizori = {x: [i for i in range(1, x+1) if x % i == 0] for x in range(1, 11)}
print("Primele 10 numere și divizorii lor:", divizori)

