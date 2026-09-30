import random

#Apufunktiot
def hae_sanat():
    with open("sanat.csv", "r", encoding="utf-8") as tiedosto:
        teksti = tiedosto.read()

    sanat = teksti.splitlines()
    return sanat

def Arvattava_sana():
    return random.choice(hae_sanat())


#Pelin luokat
class Hirsipuu:
    def __init__(self):
        self.arvaukset = 0
        self.vaarat_arvaukset = 0
        self.oikea_sana = Arvattava_sana()
        self.oikeat_kirjaimet = []
        self.vaarat_kirjaimet = []
        
    def oikea_vastaus(self, kirjain):
        self.oikeat_kirjaimet.append(kirjain)
        print("Oikein!")

    def vaara_vastaus(self, arvaus):
        self.vaarat_kirjaimet.append(arvaus)
        self.vaarat_arvaukset += 1
        print("Väärin!")
        
        
    #Hirsipuun rakenne
    def piirra_hirsipuu(self):
        base = [
            "  +---+",
            "  |  | ",
            "     | ",
            "      |",
            "      |",
            "     | ",
            "========="
        ]
        
        #Kehon osat
        osat = [
            (2, 2, "O."),  #Pää
            (3, 3, "|"),   #Vartalo
            (3, 2, "/"),   #Vasen käsi
            (3, 4, "\\"),  #Oikea käsi
            (4, 2, "/"),   #Vasen jalka
            (4, 4, "\\")   #Oikea jalka
        ]

        rivit = []
        for rivi in base:
            rivit.append(list(rivi))

        for i in range(self.vaarat_arvaukset):
            rivin_numero, kohta, merkki = osat[i]
            rivit[rivin_numero][kohta] = merkki

        for rivi in rivit:
            print("".join(rivi))
            

    def arvaus(self, kirjain):
        kirjain = kirjain.lower()

        if kirjain in self.oikeat_kirjaimet or kirjain in self.vaarat_kirjaimet:
            print("Tämä kirjain on arvattu jo!")
        elif kirjain in self.oikea_sana.lower():
            self.oikea_vastaus(kirjain)
        else:
            self.vaara_vastaus(kirjain)
            

    def suorita(self):
        while self.vaarat_arvaukset < 6:
            naytettava = ""

            for kirjain in self.oikea_sana:
                if kirjain.lower() in self.oikeat_kirjaimet:
                    naytettava += kirjain.lower() + " "
                else:
                    naytettava += "  "

            print("HIRSIPUU")
            self.piirra_hirsipuu()
            print(naytettava)
            print('‾ ' * len(self.oikea_sana)) #Merkataan sanan kirjainten määrät viivalla
            
            if len(self.vaarat_kirjaimet) > 0:
                print(*self.vaarat_kirjaimet, sep=", ")
            
            kirjain = input("Arvaa kirjain tai sana: ")
            
            if len(kirjain) == 1: #Jos arvaa kirjainta
                self.arvaukset += 1
                self.arvaus(kirjain)
                if set(self.oikea_sana.lower()) <= set(self.oikeat_kirjaimet):
                    print("Voitit Pelin, GG!")
                    print(self.oikea_sana.lower())        
                    return
                
            elif len(kirjain) > 1: #Jos arvaa sanaa
                if kirjain.lower() == self.oikea_sana.lower():
                    print("Voitit Pelin, GG!")
                    print(self.oikea_sana.lower())       
                    return
                else:
                    self.vaara_vastaus(kirjain.lower())
            else:
                print("Kokeilisit nyt edes jotain?") #jos inputti jää tyhjäksi
                
        #kun looppi ei pyöri enää eli vääriä vastauksia on liikaa
        print("Hävisit pelin!")
        self.piirra_hirsipuu()
        print(naytettava)     
        print('‾ ' * len(self.oikea_sana))        
        print(self.oikea_sana)


testi = Hirsipuu()
testi.suorita()
