wort_inp = input("Welche Buchstabenkombination, möchtest du analysieren?\n")
alphabet = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L","m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]
umschreiber = ["Ä", "ä", "Ö", "ö", "Ü", "ü", "ß"]
umschreiber_zu = ["a", "e", "o", "e", "u", "e", "s", "s"]
geordnet = []
wort = list(wort_inp)
for i in range(len(umschreiber)-1):
    for j in range(len(umschreiber)-1):
        try:    
            if wort.index(umschreiber[i]) != None:
                wort[wort.index(umschreiber[i])] = ""
                wort.append(umschreiber_zu[i])
                wort.append(umschreiber_zu[i+1])
            else: break
        except: continue
        


for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        try: 
            if wort.index(alphabet[i]) != None:
                wort[wort.index(alphabet[i])] = ""
                geordnet.append(alphabet[i])
            else: break
        except: continue
        
        
print(f"Die Buchstaben nach dem Alphabet geordnet ergeben {geordnet}")



