"""Scrieţi un program care citeşte de la tastatură de 3 ori timpul în care un sportiv aleargă proba de 100 metri (numărul de secunde).
Apoi afişaţi la ecran timpul mediu (media aritmetică a celor 3 încercări) în secunde."""

x1 = float(input("1 incercare: "))
x2 = float(input("2 incercare: "))
x3 = float(input("3 incercare: "))

timp_mediu = (x1 + x2 + x3) / 3
print("Timp mediu: ", timp_mediu)