"""Declaraţi o variabilă price, de tip int, care va reţine preţul unui produs citit de la tastatură.

* Calculaţi cât va reprezenta 30% din preţul iniţial şi salvaţi valoarea în variabila reducere
*	Scădeţi din preţul iniţial valoarea reducerii, calculate la pasul precedent. Salvaţi valoarea în variabila preţ_final
* Creaţi o variabilă nouă pret_100_lei, şi salvaţi în această variabilă cât va fi preţul iniţial minus 100 lei
* Afişaţi la final ambele preturi.

"""

x = int(input("Pret produs: "))
variabila_redus = x * 30 / 100
y = variabila_redus
pret_final = x - y
print("Pret final: ", y)
pret_100_lei = x - 100
print("Preţul iniţial minus 100 lei: ", pret_100_lei)

