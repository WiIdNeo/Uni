# ========================================
# Mathematischer Rechner - Level 6
# ========================================
# Ziel:
# - Basis-Operationen auf mehrere Zahlen erweitern
# - Robuste Fehlerbehandlung & saubere Fehlermeldungen
# ========================================

# ------------------------------
# 1️⃣ Basisoperationen
# ------------------------------

def addieren(*zahlen):
    """Addiert beliebig viele Zahlen."""
    ergebnis = 0
    for z in zahlen:
        ergebnis += z
    return ergebnis

def subtrahieren(*zahlen):
    """Subtrahiert alle nachfolgenden Zahlen von der ersten Zahl."""
    if len(zahlen) == 0:
        return "Fehler: Keine Zahlen eingegeben!"
    ergebnis = zahlen[0]
    for z in zahlen[1:]:
        ergebnis -= z
    return ergebnis

def multiplizieren(*zahlen):
    """Multipliziert beliebig viele Zahlen."""
    if len(zahlen) == 0:
        return "Fehler: Keine Zahlen eingegeben!"
    ergebnis = 1
    for z in zahlen:
        ergebnis *= z
    return ergebnis

def dividieren(*zahlen):
    """Teilt die erste Zahl nacheinander durch die weiteren Zahlen."""
    if len(zahlen) == 0:
        return "Fehler: Keine Zahlen eingegeben!"
    ergebnis = zahlen[0]
    for z in zahlen[1:]:
        if z == 0:
            return "Fehler: Division durch 0 ist nicht erlaubt!"
        ergebnis /= z
    return ergebnis

# ------------------------------
# 2️⃣ Erweiterte Funktionen
# ------------------------------

def potenz(a, b):
    """Berechnet a hoch b."""
    try:
        return a ** b
    except Exception:
        return "Fehler bei der Potenzberechnung!"

def wurzel(a):
    """Berechnet die Quadratwurzel von a."""
    if a < 0:
        return "Fehler: Wurzel aus negativer Zahl ist nicht definiert!"
    return a ** 0.5

def fakultät(a):
    """Berechnet die Fakultät von a."""
    if a < 0 or not float(a).is_integer():
        return "Fehler: Fakultät nur für ganze, positive Zahlen!"
    ergebnis = 1
    for i in range(1, int(a) + 1):
        ergebnis *= i
    return ergebnis

def modulo(a, b):
    """Berechnet a % b."""
    if b == 0:
        return "Fehler: Division durch 0 ist nicht erlaubt!"
    return a % b

def fibonacci(n):
    """Berechnet die ersten n Fibonacci-Zahlen."""
    if n <= 0:
        return "Fehler: Bitte eine positive Zahl eingeben!"
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def durchschnitt(*zahlen):
    """Berechnet den Durchschnitt von beliebig vielen Zahlen."""
    if len(zahlen) == 0:
        return "Fehler: Keine Zahlen eingegeben!"
    summe = sum(zahlen)
    return summe / len(zahlen)

def ist_primzahl(n):
    """Prüft, ob n eine Primzahl ist."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primzahlen_bis_n(n):
    """Berechnet alle Primzahlen bis n."""
    prims = []
    for i in range(2, n+1):
        if ist_primzahl(i):
            prims.append(i)
    return prims

# ------------------------------
# 3️⃣ Hauptprogramm
# ------------------------------

def eingabe_zahlen():
    """Liest beliebig viele Zahlen vom Benutzer ein, getrennt durch Komma."""
    while True:
        text = input("Gib die Zahlen ein (durch Komma getrennt, z. B. 1,2,3): ")
        try:
            zahlen = [float(x.strip()) for x in text.split(",")]
            if len(zahlen) == 0:
                print("❌ Fehler: Du musst mindestens eine Zahl eingeben.")
                continue
            return zahlen
        except ValueError:
            print("❌ Fehler: Bitte nur gültige Zahlen eingeben!")

weiter = "ja"

while weiter.lower() == "ja":
    print("\nWillkommen zum Level 6 Rechner!")
    print("Operationen:")
    print("+  → Addition")
    print("-  → Subtraktion")
    print("*  → Multiplikation")
    print("/  → Division")
    print("^  → Potenz")
    print("√  → Wurzel")
    print("!  → Fakultät")
    print("%  → Modulo")
    print("fib → Fibonacci")
    print("avg → Durchschnitt")
    print("prime → Primzahl ja/nein")
    print("primes → Primzahlen bis n")

    operation = input("\nWelche Operation möchtest du durchführen? ")

    erlaubte_ops = ["+", "-", "*", "/", "^", "√", "!", "%", "fib", "avg", "prime", "primes"]
    if operation not in erlaubte_ops:
        print("❌ Ungültige Eingabe! Bitte wähle eine der angegebenen Optionen.")
        continue

    try:
        # Basisoperationen mit beliebig vielen Zahlen
        if operation in ["+", "-", "*", "/"]:
            zahlen = eingabe_zahlen()
            if operation == "+":
                ergebnis = addieren(*zahlen)
            elif operation == "-":
                ergebnis = subtrahieren(*zahlen)
            elif operation == "*":
                ergebnis = multiplizieren(*zahlen)
            elif operation == "/":
                ergebnis = dividieren(*zahlen)

        elif operation == "^":
            a = float(input("Basis a: "))
            b = float(input("Exponent b: "))
            ergebnis = potenz(a, b)

        elif operation == "√":
            a = float(input("Zahl: "))
            ergebnis = wurzel(a)

        elif operation == "!":
            a = float(input("Ganze Zahl: "))
            ergebnis = fakultät(a)

        elif operation == "%":
            a = float(input("a: "))
            b = float(input("b: "))
            ergebnis = modulo(a, b)

        elif operation == "fib":
            n = int(input("Anzahl Fibonacci-Zahlen: "))
            ergebnis = fibonacci(n)

        elif operation == "avg":
            zahlen = eingabe_zahlen()
            ergebnis = durchschnitt(*zahlen)

        elif operation == "prime":
            n = int(input("Zahl: "))
            ergebnis = f"{n} ist {'eine Primzahl' if ist_primzahl(n) else 'keine Primzahl'}."

        elif operation == "primes":
            n = int(input("Obere Grenze: "))
            ergebnis = primzahlen_bis_n(n)

        print("✅ Ergebnis:", ergebnis)

    except Exception as e:
        print("⚠️ Unerwarteter Fehler:", e)

    weiter = input("\nMöchtest du eine weitere Berechnung durchführen? (ja/nein): ")

print("Programm beendet. Auf Wiedersehen!")
