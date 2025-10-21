poss = [[0, 0], [0, 1], [1, 0], [1, 1]]
poss_neg = [0, 1]


print("Konjunktion:")
for i in range(len(poss)):
    k = poss[i]
    g = k[0] * k[1] 
    print(str(k[0]) + ", " + str(k[1]) + " -> " + str(g))
    i+=1

print("\n\nDisjunktion: ")
i = 0
for i in range(len(poss)):
    k = poss[i]
    g = k[0] + k[1]
    try:
        g = g/g
    except ZeroDivisionError:
        g = 0
    print(str(k[0]) + ", " + str(k[1]) + " -> " + str(int(g)))
    i+=1

print("\n\nAntivalenz: ")
i = 0
for i in range(len(poss)):
    k = poss[i]
    g = k[0] - k[1]
    if g < 0:
        g = g*(-1)
    print(str(k[0]) + ", " + str(k[1]) + " -> " + str(int(g)))
    i+=1
    
print("\n\nAmbivalenz")
i = 0
for i in range(len(poss)):
    k = poss[i]
    g = k[0] - k[1]
    if g < 0:
        g = g*(-1)
    g = g-1
    if g < 0:
        g = g*(-1)
    print(str(k[0]) + ", " + str(k[1]) + " -> " + str(int(g)))
    i+=1
    
print("\n\nNegation")
i = 0
for i in range(len(poss_neg)):
    k = poss_neg[i]
    g = k - 1
    if g < 0:
        g = g*(-1)
    print(str(k) + " -> " + str(int(g)))
    
