"""
 Extrageți un subșir de caractere
Scrieți un program care primește un șir de caractere ca intrare și extrage un subșir specific din acesta,
 bazat pe pozițiile de început și sfârșit definite de utilizator.
"""

text = input("Introduceti un sir de caractere: ")
x = int(input("Introduceti 1 pozitie: "))
y = int(input("Introduceti 2 pozitie: "))
subsir = text[x:y]
print(subsir)


