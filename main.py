import random

#Apu functiot
def hae_sanat():
    with open("*sanat.csv", encoding="utf-8", newline="") as tiedosto:
        teksti = tiedosto.read()

    sanat = teksti.splitlines()
    # sanat = ["linjaauto"]
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

    def arvaus(self, kirjain):
        kirjain = kirjain.lower()

        if kirjain in self.oikeat_kirjaimet or kirjain in self.vaarat_kirjaimet:
            print("Tämä kirjain on arvattu jo")
        elif kirjain in self.oikea_sana.lower():
            OikeaVastaus().handlaa(self, kirjain)
        else:
            VaaraVastaus().handlaa(self, kirjain)

    def suorita(self):
        while self.vaarat_arvaukset < 6:
            naytettava = ""

            for kirjain in self.oikea_sana:
                if kirjain.lower() in self.oikeat_kirjaimet:
                    naytettava += kirjain.lower() + " "
                else:
                    naytettava += "_ "

            print("HIRSIPUU")
            print(naytettava)
            print('_ ' * len(self.oikea_sana))
            
            
            kirjain = input("Anna kirjain : ")
            
            if len(kirjain) == 1:
                self.arvaukset += 1
                self.arvaus(kirjain)
            elif len(kirjain) < 1:
                if kirjain == self.oikea_sana:
                    print("Voitit Pelin, Oot hullu demoni!")
                    break 
                # print("Voit antaa vain yhden kirjaimen kerrallaan!")
                
                
            

class OikeaVastaus:
    def handlaa(self, peli, kirjain):
        peli.oikeat_kirjaimet.append(kirjain)
        print("Oikein!")

class VaaraVastaus:
    def handlaa(self, peli, kirjain):
        peli.vaarat_kirjaimet.append(kirjain)
        peli.vaarat_arvaukset += 1
        print("Väärin!")

testi = Hirsipuu()
testi.suorita()
    
        
