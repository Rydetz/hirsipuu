import random
import csv

def hae_sanat():
    with open("sanat.csv", encoding="utf-8", newline="") as tiedosto:
        teksti = tiedosto.read()

    sanat = teksti.splitlines()
    return sanat

def Arvattava_sana():
    return random.choice(hae_sanat)


class Hirsipuu:
    def __init__(self):
        self.arvaukset = 0
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

    
        
