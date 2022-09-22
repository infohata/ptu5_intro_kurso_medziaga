while True:
    try:
        skaicius = float(input("Iveskite skaiciu:"))
    except ValueError:
        print("bandykite dar..")
    else:
        break
