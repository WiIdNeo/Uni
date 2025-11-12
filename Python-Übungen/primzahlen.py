y = int(input("Bis zu welcher Zahl sollen die Primzahlen ausgegeben werden?\n"))
class num():
    def __init__(self, i):
        self.numb = i
        self.is_prime_num = True
        

if y == 0 or y == 1:
    print("Keine Primzahlen vorhanden")
else:
    print("\n\n\nPrimzahlen: \n\n")
    for i in range(2, y+1, 1):
        x = num(i)
        for j in range(2, int(i/2)+1, 1):
            if x.numb % j == 0:
                x.is_prime_num = False
                break
        if x.is_prime_num == False:
            continue
        else:
            print(f"{x.numb}")
            continue
            
    