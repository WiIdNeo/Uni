b = [[1, 2],[0, 1],[4, 0]]
a = [[3, 2, 1],[1, 0, 2]]
ergebnis = "Die Matrizen sind nicht Multiplizierbar"
print(a[1])
if len(a) == len(b[0]):
    erg_1x1 = a[1[1]] * b[1[1]] + a[2[1]] * b[1[2]] + a[3[1]] * b[1[3]]
    erg_1x2 = a[1[2]] * b[2[1]] + a[2[2]] * b[2[2]] + a[3[2]] * b[2[3]]
    erg_2x1 = a[1[1]] * b[1[1]] + a[2[1]] * b[1[2]] + a[3[1]] * b[1[3]]
    erg_2x2 = a[1[2]] * b[2[1]] + a[2[1]] * b[2[2]] + a[3[1]] * b[2[3]]
    ergebnis = [[erg_1x1, erg_1x2],[erg_2x1, erg_2x2]]
    
print(ergebnis)


