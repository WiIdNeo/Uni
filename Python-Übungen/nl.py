k = 0
z = 0.5
sum = 0

for k in range(1, 100, 1):
    sum = sum-(z**k / k * (-1)**k)
    
print(sum)

