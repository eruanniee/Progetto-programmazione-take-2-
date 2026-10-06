import re 
import pandas as pd
# carica la libreria Pandas e le dà il soprannome pd
df = pd.read_csv("repubblica.csv")
# apre il file repubblica.csv e lo trasforma in un DataFrame
# il risultato è salvato in nella variabile df
# tutto il contenuto del CSV è caricato dentro df
print(df.columns)
#df.columns è un attributo del DataFrame che contiene l'elenco dei nomi delle sue colonne

def tokenizza(t):
    return re.findall(r"\w+", str(t).lower())
# definisco cosa fa la funzione tokenizza 
# str(t) prende qualunque valore del testo in una cella e lo trasforma in una stringa di testo
# lower() trasforma tutte le lettere maiuscole in minuscole
# senza lower, parole identiche ma scritte diversamente verrebbero trattate come token distinti
df["token"] = df["full_text"].apply(tokenizza) 
# il risultato è salavato in una colonna nuova chiamata token
# il DataFrame ha un colonna in più
# questa riga tokenizza l'intero dataset, non solo il primo articolo
print(df["full_text"].iloc[0])   # il testo originale del primo articolo
print(df["token"].iloc[0])       # la sua versione tokenizzata
# iloc[0] serve a selezionare una riga specifica del DataFrame, 
# indicandola per posizione numerica, partendo da 0 e non da 1
# è solo una prova per vedere cosa succede
print(len(df))                      # quante righe ha il dataset in totale
print(df["token"].notna().sum())    # quante di quelle righe hanno un valore in "token"
#questo mi serve per avere la conferma che la tokenizzazione è avvenuta per tutte le celle del testo
from collections import Counter 
# conto le occorrenze per capire se ha senso fare la ricerca su quei paesi
all_tokens = []
for lista in df["token"]:       # prendi ogni riga della colonna "token"
    for tok in lista:           # e di quella riga esamina ogni parola
    # la colonna token è una lista di liste
    # per arrivare alle singole parole bisogna prima entrare in ogni articolo
    # poi dentro di esso scorrere ogni parola
        all_tokens.append(tok)
        # contiene tutte le parole di tutti gli articoli in un'unica lista semplice
        # non più divisa per articolo)
occorrenze = Counter(all_tokens)

print(occorrenze["siria"]) #6489  
print(occorrenze["afghanistan"]) #1603
print(occorrenze["iraq"]) # 3707
print(occorrenze["sudan"]) #1598
print(occorrenze["libia"]) #4322
print(occorrenze["siriano"]) #1745
print(occorrenze["siriana"]) #933
print(occorrenze["siriani"]) #1798
print(occorrenze["siriane"]) #392
print(occorrenze["afghano"]) #130
print(occorrenze["afghana"]) #94
print(occorrenze["afghani"]) #162
print(occorrenze["afghane"]) #65
print(occorrenze["iracheno"]) #890
print(occorrenze["irachena"]) #393
print(occorrenze["iracheni"]) #487
print(occorrenze["irachene"]) #402
print(occorrenze["sudanese"]) #173
print(occorrenze["sudanesi"]) #202
print(occorrenze["libico"]) #761
print(occorrenze["libica"]) #830
print(occorrenze["libici"]) #571
print(occorrenze["libiche"]) #598
print(occorrenze["2014"]) #9426

#co-occorrenze per un'analisi semantica
