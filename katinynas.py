# Parašyti veikiančią programą katinynui:
# - sukurti klasę Kate, kuri turėtų atributus katės vardui, spalvai, amžiui ir kojų kiekiui.
# -- katė turi sugebėti miauksėti ir bėgti, judinant kojas ir žiūrint kur bėga.
# -- senstant katės pradeda eiti, o pasenus - tik šliaužti.
# - programa turi leisti įvesti katę.
# - esant bent vienai katei, programa turi leisti parodyti kačių sąrašą.
# - esant bent vienai katei, programa turi leisti pavedžioti pasirinktą katę
#   (katė turi bėgti, ir miaukti tiek, kiek turi metų).
# - išsaugoti katinyno katalogą pickle faile
import pickle

class Kate:
    def __init__(self, vardas, spalva="juoda", amzius=0, kojos=4):
        self.vardas = vardas
        self.spalva = spalva
        self.amzius = amzius
        self.kojos = kojos

    def __str__(self):
        return f"{self.vardas}, {self.amzius} metu, {self.kojos}-kojis, spalva: {self.spalva}"

    def _judinti_kojas(self):
        pass

    def _ziureti_kur_begi(self):
        pass

    def miaukseti(self, zinute="miau ", kartai=1):
        print(zinute * kartai)

    def begti(self):
        self._judinti_kojas()
        self._ziureti_kur_begi()
        if self.amzius > 15:
            print("sliauziu")
        elif self.amzius > 12:
            print("einu")
        else:
            print("begu")

def ivesti():
    vardas = input("Vardas: ")
    spalva = input("Spalva (juodas): ")
    if not len(spalva):
        spalva = "juodas"
    try:
        amzius = int(input("Amzius (0): "))
    except ValueError:
        amzius = 0
    try:
        kojos = int(input("Kojos (4): "))
    except ValueError:
        kojos = 4
    nauja_kate = Kate(vardas, spalva, amzius, kojos)
    return nauja_kate   #galima tiesiai kviesti Kates objekto sukurima

def rodyti_kataloga(kates):
    for numeris, kate in enumerate(kates):
        print(numeris+1, kate, hex(id(kate)))

def vedzioti(kate):
    print(kate.vardas)
    kate.begti()
    kate.miaukseti(kartai=kate.amzius)

def issaugoti(kates):
    with open("Naujas/kates.pkl", "wb") as failas:
        pickle.dump(kates, failas)
    print(f"{len(kates)} kates issaugotos sekmingai")

def atidaryti():
    with open("Naujas/kates.pkl", "rb") as failas:
        kates = pickle.load(failas)
    return kates

try:
    kates = atidaryti()
except FileNotFoundError as error:
    print(error.__class__, error)
    kates = []

while True:
    # programos meniukas
    print("Katinynas")
    print(" 1 - ivesti")
    if len(kates):
        print(" 2 - rodyti kataloga")
        print(" 3 - vedzioti kate")
        print(" 4 - issaugoti")
    # veiksmo nuskaitymas ir apdorojimas
    veiksmas = input("betkas kitas - iseiti\nPasirinkite: ")
    if veiksmas == "1":
        # ivedimas
        kates.append(ivesti())
    elif len(kates) and veiksmas == "2":
        # katalogo rodymas
        rodyti_kataloga(kates)
    elif len(kates) and veiksmas == "3":
        # vedziojimas
        try:
            numeris = int(input(f"pasirinkite kate nuo 1 iki {len(kates)}: " ))
        except ValueError:
            print("Ivestas ne skaicius")
        else:
            if numeris >= 1 and numeris <= len(kates):
                vedzioti(kates[numeris-1])
            else:
                print("Neteisingas skaicius, arba per didelis, arba per mazas")
    elif len(kates) and veiksmas == "4":
        issaugoti(kates)
    else:
        print("iki!")
        break
