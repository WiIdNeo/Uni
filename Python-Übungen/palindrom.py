
def checker(x):
    for i in range(len(x)):
        if x[i] != x[-(i+1)]:
            return False
    return True    

x = input("Gib ein Wort an, dass du prüfen möchtest: ")

print(checker(x))


