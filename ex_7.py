"""
Numărarea caracterelor
Scrieți un program care
 primește un șir de caractere ca intrare
 și numără de câte ori apare un caracter specific (introdus in consola).

 Numarul de caractere trebuie sa fie considerat indiferent daca e majuscula sau minuscula
"""
text = input("Introduce-ti un sir de caractere: ")
print(text.lower().count(input("Introduceti un caracter specific: ")))
