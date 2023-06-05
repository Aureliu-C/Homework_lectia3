"""
Înlocuiți un subșir de caractere
Scrieți un program care primește o propoziție, un subșir de caractere țintă
și un subșir de caractere de înlocuire ca intrare (din consola)
și înlocuiește toate aparițiile subșirului de caractere țintă cu subșirul de caractere de înlocuire.
"""

text = input("Scrie o propozitie: ")
sir_de_inlocuit = text.replace(input("ce cuvint doresti sa inlocuesti ? :"), input("cu ce cuvint ai dori sa inlocuesti?: "))

print(sir_de_inlocuit)