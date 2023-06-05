"""Utilizatorul va introduce un șir de caractere in consola.
* Calculați și afișați numarul total de litere în șirului de caractere
* Calculați și afișați numarul de vocale în șirul de caractere
* Calculați și afișați numarul de consoane în șirul de caractere

Note: Indiferent daca e majuscula sau minusucula litera

"""

text = input("Introduceti un text: ")
nr_de_litere = len(text)

vocale = ["a","e","i","o","u","A","E","I","U","O"]
count = 0
for i in text:
 if i in vocale:
   count+=1

consoane = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
count1 = 0
for i in text.upper():
 if i in consoane:
   count1+=1

print("Nr de litetre: ",nr_de_litere)
print("Nr. de vocale in sir: ", count)
print("Nr. de consoane: ",count1)
