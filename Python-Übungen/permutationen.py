import itertools

text = input("Gib die Zeichenkette ein: ")

for perm in itertools.permutations(text):
    print("".join(perm))
