def teilbar_durch_2(x):
    return int(x[-1]) % 2 == 0

def teilbar_durch_3(x):
    z = 0
    for i in range(len(x)):
        z += int(x[i])
    return z % 3 == 0

def teilbar_durch_4(x):
    y = x[-2:] if len(x) >= 2 else x
    return int(y) % 4 == 0

def teilbar_durch_5(x):
    y = int(x[-1])
    if y == 5 or y == 0:
        return True
    else:
        return False
    
def teilbar_durch_6():
    if teil_2 == True and teil_3 == True:
        return True
    else: 
        return False

def teilbar_durch_7(x):
    z = int(x)
    print(f"Starte mit: {z}")
    
    while abs(z) > 7:
        letzte = z % 10
        rest = z // 10
        z = rest - 2 * letzte
    if z == 0 or z == 7 or z == -7:
        return True
    else:
        return False


def teilbar_durch_8(x):
    y = x[-3:] if len(x) >= 2 else x
    return int(y) % 8 == 0

def teilbar_durch_9(x):
    z = 0
    for i in range(len(x)):
        z += int(x[i])
    return z % 9 == 0


while True:
    x = input("Gib eine Ganzzahl ein!\n")

    teil_2 = teilbar_durch_2(x)
    teil_3 = teilbar_durch_3(x)
    teil_4 = teilbar_durch_4(x)
    teil_5 = teilbar_durch_5(x)
    teil_6 = teilbar_durch_6()
    teil_7 = teilbar_durch_7(x)
    teil_8 = teilbar_durch_8(x)
    teil_9 = teilbar_durch_9(x)


    print("Teilbar durch 2:", teil_2)
    print("Teilbar durch 3:", teil_3)
    print("Teilbar durch 4:", teil_4)
    print("Teilbar durch 5:", teil_5)
    print("Teilbar durch 6:", teil_6)
    print("Teilbar durch 7:", teil_7)
    print("Teilbar durch 8:", teil_8)
    print("Teilbar durch 9:", teil_9)
