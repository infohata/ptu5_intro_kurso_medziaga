# 1
# Sukurti norimą sąrašą ir žodyną ir juose:
# - Atspausdinti vieną norimą įrašą
# - Pridėti įrašą
# - Ištrinti įrašą
# - pakeisti įrašą
# Išbandyti kitas sąrašų ir žodynų funkcijas: clear(), index(), insert(), remove...

# 2
# Parašyti programą, kuri:

# Leistų vartotojui įvesti skaičių.
# Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
# Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
# Patarimas: Naudoti ciklą while, sąlygą if, break

sarasas = [1, 2, 3]
print("pradinis sarasas", sarasas)
sarasas.pop() # trina paskutini elementa
print("pratrintas sarasas", sarasas)
sarasas.clear()
print("isvalytas sarasas", sarasas)

zodynas = {"oras": "geras", "temperatura": 39}
print("pradinis zodynas", zodynas)
del zodynas["oras"]
print("pratrintas zodynas", zodynas)
zodynas.clear()
print("isvalytas zodynas", zodynas)
