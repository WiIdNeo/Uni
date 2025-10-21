wert = -5
funktionswert = 0
while wert < 5.1:
    funktionswert = wert * wert
    print("x" + str(wert))
    print ("f(x) = " + str(funktionswert))
    funktionswert = wert*2
    print("f'(x) = " + str(funktionswert))
    print("f''(x) = 2")
    wert+=0.1
    
    
    """
    Ergebnisse teilweise unwahr!
    Iterationsalgorythmus -> Näherungsalgorythmus
    Für wahre Werte Müssen korrekturwerte genutzt werden! Trotzdem nur gerundet!
    
    """