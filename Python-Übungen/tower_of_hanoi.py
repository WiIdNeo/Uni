# ======= Deine Stack-Klasse (unverändert) =======
class Stack():  # 3-hoher Stack -> für höheren Stack einfach höheren Stack erstellen
    def __init__(self, x, y, z, a):
        self.positions = [x, y, z]
        self.current_stack_height = a

# ======= Hilfsfunktionen & Druck =======
def stack_printer():
    print(f"\nA: {StackA.positions} \n\nB: {StackB.positions} \n\nC: {StackC.positions}\n")

# sichere Abfrage der obersten Scheibe (None, falls leer)
def top(stack):
    if stack.current_stack_height > 0:
        return stack.positions[stack.current_stack_height - 1]
    return None

# prüft, ob ein Zug von from_stack nach to_stack legal ist
def can_move(from_stack, to_stack):
    if from_stack.current_stack_height == 0:
        return False
    if to_stack.current_stack_height == 0:
        return True
    return top(from_stack) < top(to_stack)

# generischer Move, verwendet von A_auf_C etc. -> Minimale Änderungen in den Original-Funktionen
def move_disk(from_stack, to_stack, from_name, to_name):
    disk = from_stack.positions[from_stack.current_stack_height - 1]
    print(f"{from_name}({disk} auf {to_name})")
    to_stack.positions[to_stack.current_stack_height] = disk
    to_stack.current_stack_height += 1
    from_stack.positions[from_stack.current_stack_height - 1] = 0
    from_stack.current_stack_height -= 1
    stack_printer()

def where_is_2():
    if 2 in StackA.positions:
        return "A"
    elif 2 in StackB.positions:
        return "B"
    else:
        return "C"

def where_is_1():
    if 1 in StackA.positions:
        return "A"
    elif 1 in StackB.positions:
        return "B"
    else:
        return "C"
    
def where_is_0():
    is0 = []
    if all(x == 0 for x in StackA.positions):
        is0.append("A")
    if all(x == 0 for x in StackB.positions):
        is0.append("B")
    if all(x == 0 for x in StackC.positions):
        is0.append("C")
    return is0

# ======= Deine benannten Bewegungsfunktionen (erhalten, verwenden move_disk intern) =======
def A_auf_C():
    move_disk(StackA, StackC, "A", "C")

def A_auf_B():
    move_disk(StackA, StackB, "A", "B")

def B_auf_C():
    move_disk(StackB, StackC, "B", "C")

def B_auf_A():
    move_disk(StackB, StackA, "B", "A")

def C_auf_B():
    move_disk(StackC, StackB, "C", "B")

def C_auf_A():
    move_disk(StackC, StackA, "C", "A")

# ======= Initialisierung (dein Startzustand) =======
StackA = Stack(3, 2, 1, 3)
StackB = Stack(0, 0, 0, 0)
StackC = Stack(0, 0, 0, 0)

# Druck vor Beginn
stack_printer()

# ======= Heuristische Hauptschleife (dein "Erraten"-Stil, aber deterministisch) =======
# Erklärung: wir probieren in jeder Iteration eine feste Reihenfolge von möglichen legalen Zügen.
# Diese Reihenfolge ist bewusst so gewählt, dass sie für 3-Scheiben-Hanoi zum Ziel führt,
# ohne Rekursion - ideal als Übung für heuristische Suche.
move_count = 0
MAX_MOVES = 100  # Sicherheitsgrenze, falls doch etwas schiefgeht

while StackC.current_stack_height < 3 and move_count < MAX_MOVES:
    move_count+=1
    moved = False

    # Sonderfall-Block aus deiner Version: wenn die größte Scheibe schon auf C an der Basis liegt,
    # dann unbedingt versuchen, die verbleibenden Scheiben (2,1) nachzuziehen.
    # In der Originalversion blieb das Programm hier hängen, weil nach diesem Block kein "continue"
    # kam und die Schleifenlogik durcheinander geriet. Hier behandeln wir den Sonderfall robust:
    if StackC.positions[0] == 3:
        if where_is_2() == "A" and top(StackA) == 2 and can_move(StackA, StackC):
            A_auf_C()
            continue
        elif where_is_2() == "B" and top(StackB) == 2 and can_move(StackB, StackC):
            B_auf_C()
            continue
        elif where_is_2() == "C":
            # 2 ist schon auf C, jetzt 1 nachziehen
            if where_is_1() == "A" and top(StackA) == 1 and can_move(StackA, StackC):
                A_auf_C()
                continue
            elif where_is_1() == "B" and top(StackB) == 1 and can_move(StackB, StackC):
                B_auf_C()
                continue

                
        
        if StackC.current_stack_height == 3:
            break

    # Allgemeine heuristische Reihenfolge (erkennbar aus deiner Vorlage)
    if can_move(StackA, StackC):
        A_auf_C()
        continue
    elif can_move(StackA, StackB):
        A_auf_B()
        continue
    elif where_is_1() == "A":
            x = where_is_0()
            if "B" in x:
                A_auf_B()
                continue
            elif "C" in x:
                A_auf_C()

    elif where_is_1() == "B":
            x = where_is_0()
            if "A" in x:
                B_auf_A()
                continue
            elif "C" in x:
                B_auf_C()
                continue

    elif where_is_1() == "C":
            x = where_is_0()
            if "B" in x:
                C_auf_B()
                continue
            elif "A" in x:
                C_auf_A()
                continue
                   
    if where_is_1() == "A":
        x = where_is_2()
        if "B" in x:
            A_auf_B()
            continue
        elif "C" in x:
            A_auf_C()
            continue

    elif where_is_1() == "B":
        x = where_is_2()
        if "A" in x:
            B_auf_A()
            continue
        elif "C" in x:
            B_auf_C()
            continue

    elif where_is_1() == "C":
        x = where_is_2()
        if "B" in x:
            C_auf_B()
            continue
        elif "A" in x:
            C_auf_A()
            continue
      
    

# Endzustand / Info
if StackC.current_stack_height == 3:
    print(f"\n Ziel erreicht in {move_count} Zügen. Finale Stacks:")
else:
    print(f"\n Nicht gelöst nach {move_count} Zügen (Sicherheitsabbruch).")

stack_printer()
