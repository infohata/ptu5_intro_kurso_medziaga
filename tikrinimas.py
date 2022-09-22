skaicius = int(input("Įveskite skaičių: "))
# jeigu sąlyga:
if skaicius > 0:
    # vykdomas blokas, jeigu atitinka sąlygą
    print(f"skaičius {skaicius} yra teigiamas")
# jeigu ne, tada kita sąlyga
elif skaicius < 0:
    # vykdomas blokas, jeigu atitinka sąlygą
    print(f"skaičius {skaicius} yra neigiamas")
# jeigu vistiek ne, tada kitas blokas
else:
    print("Įvestas nulis")
