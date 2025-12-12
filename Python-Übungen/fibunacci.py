import sys

x = int(sys.argv[1])   #Programm-Übergabe-Parameter, zum Programmaufruf
if x == 0:
    with open("fib.txt", "w") as file:
        file.write(0)
else:
    f = 0
    g = 1
    h = 0
    result = 0
    with open("fib.txt", "w") as file:
        file.write(f"1\n")
    while f < (x-1):
        f+=1
        result = g + h
        h = g
        g = result
        with open("fib.txt", "a") as file:
            file.write(f"{result}\n")
            
            
            
        