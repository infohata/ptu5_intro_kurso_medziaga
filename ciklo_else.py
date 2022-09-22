ivestas = int(input("Įveskite skaičių: "))
for skaicius in range(1, ivestas+1):
    print(skaicius)
    if skaicius == 5:
        print("nutraukiam cikla")
        break
else:
    print("ciklas nebuvo nutrauktas")
