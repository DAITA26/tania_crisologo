class StringaDiTesto:
    lista_consonanti = ("B", "C", "D", "F", "G", "H", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "Z", "K")
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    def separa_consonanti(self, cognome):
        contatore = 0
        parola = ""
        for lettera in cognome:
            for consonante in StringaDiTesto.lista_consonanti:
                if lettera == consonante:
                    contatore = contatore+1
                    parola = parola + lettera
                    #print(lettera)
                    break
            if contatore == 3:
                break

        return parola

class Data_di_nascita:
    mesi = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F",
            7: "G", 8: "H", 9: "I", 10: "L", 11: "M", 12: "P"}
    def __init__(self,giorno, mese, anno, sesso):
        self.giorno = giorno
        self.mese = mese
        self.anno = anno
        self.sesso = sesso

    def calcola_giorno(self, giorno, sesso):
        if sesso == "FEMMINA":
            giorno= int(giorno)+40

        return str(giorno)


    def calcola_anno(self, anno):
        return anno[2]+anno[3]

    def calcola_mese(self,mese):
        return Data_di_nascita.mesi[int(mese)]

class Comune_di_nascita:
    comuni = {"ROMA": "H501",
        "MILANO": "F205",
        "NAPOLI": "F839",
        "TORINO": "L219",
        "VENEZIA": "Z404",
        "PERU" : "Z611"}
    def __init__(self,comune):
        self.comune=comune

    def scegli_comune(self, comune):
        return Comune_di_nascita.comuni[comune]

user1= StringaDiTesto(input("Scrivi il tuo nome: ").upper(), input("Scrivi il tuo cognome: ").upper())
user2=Data_di_nascita(input("Giorno di nascita: "), input("Scrivi il mese: "), input("Anno di nascita: "), input("Sesso: ").upper())
user3=Comune_di_nascita(input("Luogo di nascita: ").upper())

print(user1.separa_consonanti(user1.cognome) + user1.separa_consonanti(user1.nome) +user2.calcola_anno(user2.anno)+user2.calcola_mese(user2.mese)+user2.calcola_giorno(user2.giorno,user2.sesso) +user3.scegli_comune(user3.comune) )











