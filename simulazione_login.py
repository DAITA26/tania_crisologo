class ValidateLogin(Exception):
    pass

collezione_dati = {"pippo" : "marianna", "topolino": "tania", "minnie":"lucia", "paperina" : "aferdita"}

user = ""
password= ""

stop = False
while not stop:
    try:
        user = input("Inserire nome utente")
        if user not in collezione_dati.keys():
            raise ValidateLogin("Utente non trovato")
        else:
            stop = True
            print("Nome utente corretto")
            #raise Va

    except ValidateLogin as ex:
        print (ex)
    else:
        while password != collezione_dati[user]:
            try:
                password = input ("Inserire password")
                if password == collezione_dati[user]:
                #password specifica
                    stop= True
                    raise ValidateLogin("Password trovata, accesso consentito!")
                else:
                    raise ValidateLogin("Password non trovata")
            except ValidateLogin as ex:
                 print(ex)



#con username e password

#dal file dobbiamo prelevare la collezione di utenti (solo username)
#mettendola dentro una variabile

#il programma chiede all'utente se vuole fare login o signup

#terza opzione: modificare la password

#poi viene richiesto lo username e la password

#se l'utente ha richiesto il login
#controllo la validità dello username:esiste nella collezione di utenti
# - se esiste, controllare la sua password sia uguale a quella inserita
    #password corretta: login autorizzato
    #password sbagliata: "password non valida"
# - se NON esiste, lanciare un errore "user non valido"

#Se l'utente ha richiesto il signup
#controllo se lo username:è già utilizzato: esiste nella collezione di utenti
# - se è un nuovo utente: bisogna aggiungere username e password all'elenco utenti e aggiornare il file
# - se l'utente si è registrato in precedenza: lanciare un"iscrizione non valida"

# se l'utente ha richiesto di modificare la password
#...