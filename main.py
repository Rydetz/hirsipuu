import random

#Apufunktiot
def hae_sanat():
    with open("sanat.csv", "r", encoding="utf-8") as tiedosto:
        sanat = []

        for rivi in tiedosto:
            sana = rivi.strip()
            if sana: 
                sanat.append(sana)

    return sanat

def arvattava_sana():
    return random.choice(hae_sanat())


#Pelin luokat
class Hirsipuu:
    def __init__(self):
        self.arvaukset = 0
        self.vaarat_arvaukset = 0
        self.oikea_sana = arvattava_sana()
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
            return

        self.arvaukset += 1

        if kirjain in self.oikea_sana.lower():
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
            
            print(*self.vaarat_kirjaimet, sep=", ")
            
            kirjain = input("Arvaa kirjain tai sana: ").strip().lower()
            
            if len(kirjain) == 0:
                print("Kokeilisit nyt edes jotain?") #jos inputti jää tyhjäksi
                continue

            if not kirjain.isalpha(): #tollanen tuli vastaa ja on aika hyvätäs, checkkaa onko kaikki kirjaimia. ei salli numeroit
                print("Käytä vain kirjaimia!")
                continue

            if len(kirjain) == 1: #Jos arvaa kirjainta
                self.arvaus(kirjain)

                if set(self.oikea_sana.lower()) <= set(self.oikeat_kirjaimet):
                    print(f"Oikea sana: {self.oikea_sana.lower()}")
                    print("Voitit Pelin, GG!")
                    print(f"Arvausten määrä: {self.arvaukset}")
                    return

            elif len(kirjain) > 1: #Jos arvaa sanaa
                if kirjain in self.vaarat_kirjaimet:
                    print("Tämä sana on jo arvattu")
                    continue

                self.arvaukset += 1

                if kirjain == self.oikea_sana.lower():
                    print(f"Oikea sana: {self.oikea_sana.lower()}")
                    print("Voitit Pelin, GG!")
                    print(f"Arvausten määrä: {self.arvaukset}")
                    return
                else:
                    self.vaara_vastaus(kirjain)
                
        #kun looppi ei pyöri enää eli vääriä vastauksia on liikaa
        print("Hävisit pelin!")
        self.piirra_hirsipuu()
        print(naytettava)     
        print('‾ ' * len(self.oikea_sana))        
        print(self.oikea_sana)
        print(f"Arvausten määrä: {self.arvaukset}")


testi = Hirsipuu()
testi.suorita()
