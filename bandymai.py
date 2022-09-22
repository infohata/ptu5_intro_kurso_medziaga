# PIRMAS BUDAS su if/else salyga
# print("Dalybos programele")
# sk1 = int(input("iveskite skaiciu: "))
# sk2 = int(input("iveskite skaiciu: "))
# if sk2 == 0:
#     print("negalima dalinti is nulio")
# else:
# print(sk1/sk2)
# print("programa vis dar veikia! iki dabar...")

# ANTRAS BUDAS su try/except/else salyga
print("Dalybos programele")
try:
    sk1 = int(input("iveskite skaiciu: "))
    sk2 = int(input("iveskite skaiciu: "))
    atsakymas = sk1/sk2
except ValueError:
    print("ivestas ne skaicius")
except ZeroDivisionError:
    print("negalima dalinti is nulio")
else:
    print("atsakymas:", atsakymas)
finally:
    print("programa vis dar veikia! iki dabar...")
