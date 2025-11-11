treppenstufen = int(input("Wie viele Stufen hat die Treppe?"))
anzahl = 0


if treppenstufen == 0:
    print("Möglichkeiten: 0")
else:
    f = 0
    g = 1
    h = 0
    result = 0
    while f < treppenstufen:
        f+=1
        result = g + h
        h = g
        g = result
    print(f"Möglichkeiten: {result}")

