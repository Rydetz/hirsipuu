import random
import csv

def hae_sanat():
    with open("sanat.csv", encoding="utf-8", newline="") as tiedosto:
        teksti = tiedosto.read()

    sanat = teksti.split(";")
    return sanat

def Arvattava_sana():
    return random.choice(hae_sanat)


class Hirsipuu:
    def __init__(self)
        self.arvaukset = 0
        self.oikea_sana = Arvattava_sana()
        self.vaarat_kirjaimet = []

    
        
