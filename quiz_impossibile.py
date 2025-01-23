import random
lista_domande = ("gelato","animali","città","zodiaco")
gelati = {"A":"cioccolato","B":"pistacchio","C":"nocciola","d":"limone"}
animali = {"A":"cane","B":"gatto","C":"giraffa","D":"leone"}
citta = {"A" : "Tokyo","B" : "Dubai","C":"Toronto","D":"Singapur"}
zodiaco = {"A":"Ariete","B":"Leone","C":"Cancro","D":"leo"}

opzioni = (gelati,animali,citta,zodiaco)
numero_domanda = 0
risposte_corrette = []
risposte_utente = []
scelte_pc = ("A","B","C","D")
conteggio = 0

for domanda in lista_domande:
    print(f"A che {domanda} sto pensando?")
    risposta = input(f"scegli tra:{opzioni[numero_domanda]}").strip().upper()
    numero_domanda += 1
    risposte_utente.append(risposta)
    risposta_giusta = random.randint(0,3)
    print(scelte_pc[risposta_giusta])
    risposte_corrette.append(scelte_pc[risposta_giusta])
    if scelte_pc[risposta_giusta] == risposta:
       conteggio += 1
       print("Hai indovinato!")
    else:
        print(f"Hai sbagliato! La risposta giusta era {scelte_pc[risposta_giusta]}")


print(risposte_corrette)
print(risposte_utente)

percentuale_giusta = (conteggio/4)*100
print(f"Ne hai azzeccate il {percentuale_giusta} % ")
print(f"Hai sbagliato di un {(100-percentuale_giusta)} % ")