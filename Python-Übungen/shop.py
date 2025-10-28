warenbestand = [["Kürzel", "Name", "Verfügbare Anzahl", "Preis in Eurocent"],
                ["TTK", "Tischtenniskelle", 5, 500],
                ["TTB", "Tischtennisbälle", 20, 99],
                ["TTK", "Tischtennisplatte", 2, 10000]]
warenkorb = []
user_name = ""

user_name = input("Wie ist dein Name?")
while True:
    #Shop Loop
    mode = input("K: Wahrenkorp, \nB: Bestand\n")
    if mode == "K":
        i = 0
        while i < len(warenkorb):
            print(warenkorb[i])
            i+=1
            
    elif mode == "B":
        i = 0
        while i < len(warenbestand):
            print(warenbestand[i])
            i+=1
    else:
        print("Bitte mache eine Gültige Eingabe!")
        continue

    break
print("Aus Wiedersehen " + str(user_name))

