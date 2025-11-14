def get_grid():
    print("Enter your Mambo line-wise. Pay attention to relations between sigle elements!\n Enter empty fields using 0, one color using 1 and the other using 2\n \
        If there is a = relation use 4, if it is an X-ralation use 5 and if there is no relation use 3.?n \
            Also pay attention: every second line is only for realations! Use 6 for those no relation and no number!!!")
    for row_idx in range(11):
        while True:
            line = input(f"Zeile {row_idx + 1}: ").strip().replace(" ", "")
            if len(line) != 11:
                print("Bitte genau 11 Zeichen eingeben!")
                continue
            row = []
            valid = True
            for ch in line:
                if ch in "0.":
                    row.append(None)
                elif ch.isdigit() and 1 <= int(ch) <= 9:
                    row.append(int(ch))
                else:
                    print("Nur Ziffern 1–6 erlaubt!")
                    valid = False
                    break
            if valid:
                grid.append(row)
                break
    return grid
    
def solve_grid():
    # Leere Zellen in Kandidatenlisten umwandeln
    for i in range(11):
        for j in range(11):
            if grid[i][j] is None:
                grid[i][j] = list(range(1, 3))

    changed = True
    while changed:
        print(grid)
        changed = False
        for i in range(11):
            for j in range(11):
                if isinstance(grid[i][j], int):
                    num = grid[i][j]

                    # Zeile
                    for y in range(11):
                        ...
                    # Spalte
                    for x in range(11):
                        ...
                elif isinstance(grid[i][j], list) and len(grid[i][j]) == 1:
                    ...

    return grid


def guess_solve():
    ...
    
def check_grid():
    ...

def print_grid(grid):
    for i, row in enumerate(grid):
        line = []
        for j, x in enumerate(row):
            val = x if isinstance(x, int) else 0
            line.append(val)
        print(line)
    print()

grid = []
get_grid()
solved = False
while solved == False:
    solve_grid()