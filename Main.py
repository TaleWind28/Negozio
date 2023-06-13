from Module import * #importa tutto il contenuto della directory

i=1;a=[];giocatori=[]#p array di Player

#Aggiunta dei Player all'array p con i punteggi in base alle tappe disputate
tappe.AddTappe(giocatori)

#Creazione array d'appoggio per ordinare i punteggi
for x in giocatori:
    a.append(x.punteggio)

#Ordinamento decrescente dei punteggi
a.sort(reverse= True)

#Stampa della Classifica
with open('Negozio/Classifica.txt','w') as f:
    for y in a:
        for x in giocatori:
            if not x.printed and x.punteggio == y:
                f.write(stampa.Printing(x,i))
                if i<giocatori.__len__():
                    f.write('\n')
                x.printed = True
                i+=1
