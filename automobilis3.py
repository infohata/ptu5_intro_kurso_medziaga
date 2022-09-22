class Automobilis():
    def __init__(self, metai, modelis, kuro_tipas, kuro_bakas=40, degalai=0, dugnas=0):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        self.kuro_bakas = kuro_bakas
        self.dugnas = dugnas
        self.degalai = degalai
        self._informacija()

    @property
    def degalai(self):
        return self.__degalai

    @degalai.setter
    def degalai(self, naujas_kiekis):
        if naujas_kiekis < self.dugnas:
            print("kuro bake negali būti neigiamas kiekis degalų")
        elif naujas_kiekis > self.kuro_bakas:
            print(f"kuro bake negali būti daugiau negu {self.kuro_bakas} degalų")
        else:
            self.__degalai = naujas_kiekis

    def vaziuoti(self):
        if self.degalai > self.dugnas:
            self.degalai -= 1
            print("Važiuoja")
        else:
            self.stoveti()

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self, kiekis=20):
        if (self.kuro_bakas - self.dugnas) - (self.degalai - self.dugnas) < kiekis:
            print(f"Negalima perpildyti bako ({self.kuro_bakas}), kuriame dar yra {self.degalai}")
        else:
            self.degalai += kiekis
            print(f"Įpilta {kiekis} degalų")

    def _informacija(self):
        print("Metai:", self.metai, "Modelis:", self.modelis, "Tipas:", self.kuro_tipas)


class Elektromobilis(Automobilis):
    def __init__(self, metai, modelis, kuro_tipas, kuro_bakas=480, degalai=400, dugnas=340):
        super().__init__(metai, modelis, kuro_tipas, kuro_bakas, degalai, dugnas)

    def pildyti_degalu(self, kiekis=60):
        super().pildyti_degalu(kiekis)
        print("Baterija įkrauta")

    # def vaziuoti(self):
    #     print("Elektra ", end="")
    #     super().vaziuoti()

    def vaziuoti_automonomiškai(self):
        print("Autonomiškai ", end="")
        self.vaziuoti()

# bandymai
toyota = Automobilis(2015, "Toyota Avensis", "Dyzelinas", degalai=5)
tesla = Elektromobilis(2018, "Telsla Model S", "Elektra")

for km in range(61):
    tesla.vaziuoti_automonomiškai()
    print(tesla.degalai)
tesla.pildyti_degalu()
for km in range(5):
    tesla.vaziuoti_automonomiškai()
    print(tesla.degalai)

# tesla.pildyti_degalu()
# tesla.vaziuoti_automonomiškai()
