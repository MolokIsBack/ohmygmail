# Tutto parte dal fatto che gmail non tiene conto del punto(.) nella parte di indirizzo email prima di 
# @gmail.com . Se il tuo indirizzo è mario.rossi@gmail.com, riceverai correttamente le email anche se viene 
# inviata a marioross.i@gmail.com, m.a.r.ior.ossi@gmail.com etc... L'unica limitazione è quella di non usare
# il punto all'inizio o alla fine. Da questo è nata l'idea di uno script python per generare tutte le email
# a disposizione, partendo dal proprio indirizzo gmail, e le scrivesse in un file .txt. 
# E tu conoscevi questo trucchetto?

indirizzo_email = input("Inserisci la parte del tuo indirizzo gmail che si trova prima di @gmail.com senza punti. \nSe la tua email abituale è mario.rossi@gmail.com inserisci solo mariorossi \n")
provider_email = "@gmail.com"
punto = "."

# creo la funzione per generare tutte le combo trovata su 
# https://blog.enterprisedna.co/how-to-generate-all-combinations-of-a-list-in-python/
# con questa funzione in pratica andrò a crearmi tutte le combinazioni di n elementi (la lunghezza di indirizzo_email)
# presi a 1 a 1, a 2, a 3, a 4 etc... fino a len(indirizzo_email)-1 . -1 perchè il punto non posso metterlo alla fine
def combinations(original_list):
    # The number of subsets is 2^n
    num_subsets = 2 ** len(original_list)
    
    # Create an empty list to hold all the subsets
    subsets = []
    
    # Iterate over all possible subsets
    for subset_index in range(num_subsets):
        # Create an empty list to hold the current subset
        subset = []
        # Iterate over all elements in the original list
        for index in range(len(original_list)):
            # Check if index bit is set in subset_index
            if (subset_index & (1 << index)) != 0:
                # If the bit is set, add the element at this index to the current subset
                subset.append(original_list[index])
        # Add the current subset to the list of all subsets
        subsets.append(subset)

    return subsets

# Uso la funzione per generare tutte le combo e per avere quindi tutte le posizioni dopo le quali devo aggiungere il punto
lst = []
for i in range(1,len(indirizzo_email)):
    lst.append(i)
# Adesso creo la lista che conterrà tutte le combinazioni
lst_finale =combinations(lst) 

# Il core dello script. Vado a scorrere tutti gli elementi della lista combo (lst_finale)

# dichiaro una lista vuota che conterrà le parti centrali delle email
parti_email = []

# dichiaro una lista vuota che conterrà tutte le email che man mano genererò
lista_email =[]

# inizio a scorrere tutti gli elementi della lst_finale partendo dal secondo (posizione 1) perchè il primo è vuoto 
# (bug della funzione che non ho voglia di correggere tanto non influisce)

for i in range (1,len(lst_finale)):
    # Ci sono 2 casi possibili. Elemento con lunghezza 1 e quindi solo un punto e 2 parti di email. 
    # Oppure lunghezza > 1 e quindi più punti e più parti di email
    if len(lst_finale[i]) == 1:
        parte_iniziale = indirizzo_email[:lst_finale[i][0]] + "."
        parte_finale= indirizzo_email[lst_finale[i][0]:]
        email_finale = parte_iniziale + parte_finale + provider_email
        # ogni email creata la scrivo nella lista
        lista_email.append(email_finale)
    if len(lst_finale[i]) > 1:
        parte_iniziale = indirizzo_email[:lst_finale[i][0]] + "."
        parte_finale= indirizzo_email[lst_finale[i][-1]:]
        # questo serve per creare le parti centrali dell'email
        for k in range (1,len(lst_finale[i])):
            parte_email= indirizzo_email[lst_finale[i][k-1]:lst_finale[i][k]]
            parte_email = parte_email+"."
            parti_email.append(parte_email)
        parti_unite_email = ''.join(parti_email)
        email_finale = parte_iniziale + parti_unite_email + parte_finale + provider_email
        # anche qui scrivo nella lista ogni email finita
        lista_email.append(email_finale)
        # cancello la lista parti_email perchè mi serve solo da appoggio per ogni elemento dove occorre creare parti centrali
        parti_email.clear()

# qui mi creo il file con nome indirizzo_email.txt e gli scrivo dentro tutti gli indirizzi email uno per riga
file = open(indirizzo_email+".txt", "w")
for i in range(0,len(lista_email)):
    file.write(lista_email[i]+ "\n")
file.close()

# Stampo alcune info utili
print("______________________________________")
print ("\nLo sapevi che hai",len(lst_finale)-1,"indirizzi email che puoi utilizzare? Li trovi tutti nel file",indirizzo_email +".txt", "che ho creato per te")
print("______________________________________")
print("\nInvia una mail utilizzando come destinatario uno degli indirizzi che troverai nel file. \nGuarda chi riceverà l'email... \nImmagina in quanti modi li potrai usare: \n - per aprire più account su un sito senza dover creare nuovamente una mail; \n - potrai decidere di 'sacrificare' un indirizzo per le iscrizioni alle newsletter o allo spam in generale, dopodichè ti basterà \n   bloccare tutte le email destinate a quell'indirizzo tramite un filtro gmail e non vedrai più email seccatura; \n - etc... spazio alla fantasia per altri utilizzi ;-)")




