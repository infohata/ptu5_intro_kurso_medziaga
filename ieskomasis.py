sarasas = [77, 13, 69, 42, 21, 23, 777, 314, 88, 12, 9]
ieskomasis = int(input("Įveskite skaičių: "))
for skaicius in sarasas:
    print(skaicius, end=", ")
    if skaicius == ieskomasis:
        print("RADAU!")
        break
else:
    print("skaičius nerastas")
print("...THE END...")
