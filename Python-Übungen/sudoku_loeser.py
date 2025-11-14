import copy

# ------------------------------------------------------
# Sudoku-Solver (logisch + rekursiv raten)
# Stark kommentierte Version für Lernzwecke
# ------------------------------------------------------

def print_grid(grid):
    """
    Gibt das Sudoku in lesbarer Form aus.
    Leere Zellen (Kandidatenlisten) werden als 0 dargestellt.
    """
    for i, row in enumerate(grid):
        line = []
        for j, x in enumerate(row):
            val = x if isinstance(x, int) else 0
            line.append(val)
        print(line)
    print()


def get_block_indices(i, j):
    """
    Liefert alle (x, y)-Koordinaten des 3x3-Blocks, in dem die Zelle (i,j) liegt.
    """
    bi, bj = 3 * (i // 3), 3 * (j // 3)
    return [(x, y) for x in range(bi, bi + 3) for y in range(bj, bj + 3)]


def input_sudoku():
    """
    Liest ein Sudoku vom Nutzer ein.
    Leere Zellen: 0 oder '.'
    """
    grid = []
    print("Bitte gib dein Sudoku ein (9 Zeilen, 9 Zahlen pro Zeile, Leerfelder mit 0 oder .):\n")
    for row_idx in range(9):
        while True:
            line = input(f"Zeile {row_idx + 1}: ").strip().replace(" ", "")
            if len(line) != 9:
                print("Bitte genau 9 Zeichen eingeben!")
                continue
            row = []
            valid = True
            for ch in line:
                if ch in "0.":
                    row.append(None)
                elif ch.isdigit() and 1 <= int(ch) <= 9:
                    row.append(int(ch))
                else:
                    print("Nur Ziffern 1–9 oder 0/Punkt für leer erlaubt!")
                    valid = False
                    break
            if valid:
                grid.append(row)
                break
    return grid


def solve_sudoku(grid):
    """
    Logische Eliminierung:
    - Jede leere Zelle bekommt Kandidaten [1-9]
    - Solange sich etwas ändert:
        - Feste Zahlen eliminieren aus Zeile/Spalte/Block
        - Zellen mit nur einem Kandidaten fixieren
    """
    # Leere Zellen in Kandidatenlisten umwandeln
    for i in range(9):
        for j in range(9):
            if grid[i][j] is None:
                grid[i][j] = list(range(1, 10))

    changed = True
    while changed:
        print(grid)
        changed = False
        for i in range(9):
            for j in range(9):
                if isinstance(grid[i][j], int):
                    num = grid[i][j]

                    # Zeile
                    for y in range(9):
                        if isinstance(grid[i][y], list) and num in grid[i][y]:
                            grid[i][y].remove(num)
                            changed = True
                    # Spalte
                    for x in range(9):
                        if isinstance(grid[x][j], list) and num in grid[x][j]:
                            grid[x][j].remove(num)
                            changed = True
                    # Block
                    for (x, y) in get_block_indices(i, j):
                        if isinstance(grid[x][y], list) and num in grid[x][y]:
                            grid[x][y].remove(num)
                            changed = True

                elif isinstance(grid[i][j], list) and len(grid[i][j]) == 1:
                    grid[i][j] = grid[i][j][0]
                    changed = True

    return grid


def is_valid(grid, i, j, num):
    """
    Prüft, ob num in Zeile, Spalte, Block an Position (i,j) platziert werden darf.
    """
    if num in [grid[i][y] for y in range(9) if isinstance(grid[i][y], int)]:
        return False
    if num in [grid[x][j] for x in range(9) if isinstance(grid[x][j], int)]:
        return False
    for x, y in get_block_indices(i, j):
        if isinstance(grid[x][y], int) and grid[x][y] == num:
            return False
    return True


def guess_solve(grid):
    """
    Rekursives Raten:
    - Findet die Zelle mit den wenigsten Kandidaten
    - Probiert jeden Kandidaten aus
    - Rekursiv lösen, bis Sudoku vollständig ist
    """
    # Logisches Lösen zuerst
    grid = solve_sudoku(copy.deepcopy(grid))

    # Prüfen, ob fertig
    if all(isinstance(grid[i][j], int) for i in range(9) for j in range(9)):
        return grid

    # Finde die Zelle mit den wenigsten Kandidaten
    min_len = 10
    cell = None
    for i in range(9):
        for j in range(9):
            if isinstance(grid[i][j], list) and 1 <= len(grid[i][j]) < min_len:
                min_len = len(grid[i][j])
                cell = (i, j)

    if cell is None:
        return None  # Kein Kandidat gefunden → keine Lösung

    i, j = cell
    for num in grid[i][j]:
        if is_valid(grid, i, j, num):
            new_grid = copy.deepcopy(grid)
            new_grid[i][j] = num
            result = guess_solve(new_grid)
            if result is not None:
                return result

    return None  # Keine Lösung gefunden


# ------------------------------------------------------
# PROGRAMMAUFRUF
# ------------------------------------------------------

if __name__ == "__main__":
    grid = input_sudoku()
    print("\nStarte Lösung...\n")
    solved = guess_solve(grid)
    if solved is None:
        print("Keine Lösung gefunden!")
    else:
        print("Ergebnis:")
        print_grid(solved)
