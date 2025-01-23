giocatore1 = input("giocatore 1 scegli la tua mossa: ")
giocatore2 = input("giocatore 2 scegli la tua mossa: ")

if ((giocatore1 == "sasso" or giocatore1 == "forbici" or giocatore1 == "carta") and
     (giocatore2 == "sasso" or giocatore2 == "forbici" or giocatore2 == "carta")) :
    if giocatore1 == giocatore2:
        print("Pareggio!!")
    else :
        if ((giocatore1=="sasso" and giocatore2 =="forbici") or
            (giocatore1 == "forbici" and giocatore2 == "carta") or
            (giocatore1 == "carta" and giocatore2 == "sasso")):
            print("Complimenti giocatore1 hai vinto la sfida!")
        else :
            print("Complimenti giocatore2 hai vinto la sfida!")
else :
    print("Hai sbagliato a digitare")
