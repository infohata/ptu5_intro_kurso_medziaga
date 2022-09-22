import pickle

def perziura():
    try:
        with open('Naujas/zmones.pkl', 'rb') as failas:
            zmones = pickle.load(failas)
    except Exception as e:
        print('nepavyko nuskaityti failo, klaida:', e)
        return []
    else:
        for zmogus in zmones:
            print(zmogus)
        return zmones

def irasymas(zmones):
    # Įvedame naujo žmogaus vardą
    vardas = input("Įveskite naujo žmogaus vardą: ")
    # Pridedame naują vardą į sąrašą
    zmones.append(vardas)
    # Išsaugome atnaujintą sąrašą į pickle failą
    with open('Naujas/zmones.pkl', 'wb') as failas:
        pickle.dump(zmones, failas)
    # Grąžiname atnaujintą sąrašą
    return zmones

# Programėlės karkasas
zmones = []
while True:
    veiksmas = input("Žmonių katalogas:\n 1 - peržiūrėti\n 2 - įrašyti\n bet kas kitas - išeiti\nPasirinkite veiksmą:")
    if veiksmas == "1":
        zmones = perziura()
    elif veiksmas == "2":
        zmones = irasymas(zmones)
    else:
        print('Programa baigta!')
        break
