def fak(x):
    if x == 0:
        return 1
    else:
        print(f"{x}\n")
        x = x * fak(x-1)
        return x

x = int(input("Enter an integer "))
y = fak(x)
print(f"{y}")
with open("fak.txt", "w") as file:
    file.write(str(y))
    

        