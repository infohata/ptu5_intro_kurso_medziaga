# Parašyti programą, kuri su eilute "Zen of Python" darytų šiuos veiksmus:​
# Atspausdintų paskutinį antro žodžio simbolį​
# Atspausdintų pirmą trečio žodžio simbolį​
# Atspausdintų tik pirmą žodį​
# Atspausdintų tik paskutinį žodį​
# Atspausdintų visą frazę atbulai​
# Atskirtų žodžius ir juos atspausdintų​
# Žodį "Python" pakeistų į "Programming" ir atspausdintų naują sakinį​
# Patarimas: naudoti string karpymo įrankius, funkcijas split(), replace()​

# Programoje išbandyti daugiau string funkcijų:
# upper()
# casefold()
# capitalize()
# count()
# find()
# ir t.t.
zodis = "Zen of Python, dar keletas besikartojanciu raidziu"
# zodzio_pozicija = zodis.find("e")
# print(zodzio_pozicija)
# dar_viena_pozicija = zodis.find("e", zodzio_pozicija+1)
# print(dar_viena_pozicija)
# dar_viena_pozicija = zodis.find("e", dar_viena_pozicija+1)
# print(dar_viena_pozicija)
# neranda = zodis.find("X")
# print(neranda)
print("swap:", zodis.swapcase())
print("title:", zodis.title())
print("upper:", zodis.upper())
print("islower:", zodis.casefold().islower())

# Parašyti programą, kuri:
# Leistų įvesti pirmą skaičių
# Leistų įvesti antrą skaičių
# Paklaustų, kokį matematinį veiksmą reiktų atliktų
# Atspausdintų rezultatą: pasirinktų skaičių suma, daugybą ar pan.
# Patarimas: naudoti input(), if, print
