import mysql.connector
import time

kürzel = ["APS", "ORS", "KIS", "ANS", "SJS", "RJS", "BRS", "GFS", "BNS"]
warenkorb = []
user_name = ""
geld = 10000
einkaufsliste = []


def show_warenkorb():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS warenkorb (
        id INT AUTO_INCREMENT PRIMARY KEY,
        kuerzel VARCHAR(4),
        anzahl INT 
    )
    """)
    # ❌ vorher: print(cursor.execute(...)) → execute gibt None zurück
    # ✅ fetchall() verwenden, um Ergebnisse zu holen
    cursor.execute("SELECT * FROM warenkorb")
    print(cursor.fetchall())

    mode = input("Was möchtest du tun?\nB: Kaufen\nE: Shop verlassen\nG: Dinge aus dem Warenkorb entfernen\n")
    if mode == "G":
        waren_hinzufügen()
    else:
        menue(mode)


def show_bestand():
    cursor.execute("SELECT * FROM bestand")
    print(cursor.fetchall())  # ❌ vorher: print(cursor.execute(...))

    mode = input("Was möchtest du tun?\nB: Kaufen\nE: Shop verlassen\n")
    if mode == "B":
        waren_hinzufügen()
    else:
        menue(mode)


def show_Einkaufsliste():
    if einkaufsliste:  # ❌ vorher: try/except unnötig
        for item in einkaufsliste:
            print(item)
    else:
        print("Die Einkaufsliste ist leer!")

    mode = input("Was möchtest du tun?\n\nK: Warenkorb sehen\nB: Bestand sehen\nE: Shop verlassen\n")
    menue(mode)


def waren_hinzufügen():
    tabelle_bereinigen()
    ware = input("Gib den Kürzel der Ware an, um die es geht: ")
    anzahl = int(input("Wie oft wollen Sie den Artikel hinzufügen (negative Werte für das Entfernen): "))

    # ❌ vorher: Parameter falsch übergeben
    cursor.execute("SELECT anzahl FROM warenkorb WHERE kuerzel = %s", (ware,))
    warenkorb_plus = cursor.fetchall()

    # ❌ vorher: x = 0; for i in range(len(x)) → x war int, nicht iterierbar
    x = sum([row[0] for row in warenkorb_plus]) if warenkorb_plus else 0

    neue_anzahl = x + anzahl
    cursor.execute("UPDATE warenkorb SET anzahl = %s WHERE kuerzel = %s", (neue_anzahl, ware))
    conn.commit()  # ❗ Änderungen müssen gespeichert werden


def tabelle_bereinigen():
    for k in kürzel:
        cursor.execute("SELECT anzahl FROM warenkorb WHERE kuerzel = %s", (k,))
        y = cursor.fetchall()
        x = sum([row[0] for row in y]) if y else 0

        cursor.execute("DELETE FROM warenkorb WHERE kuerzel = %s", (k,))
        if x > 0:
            cursor.execute("INSERT INTO warenkorb (kuerzel, anzahl) VALUES (%s, %s)", (k, x))
    conn.commit()


def main_loop():
    while True:
        mode = input("K: Warenkorb\nB: Bestand\nL: Einkaufsliste\nE: Shop verlassen\n")
        mode = menue(mode)
        if mode == 0:
            break


def shop_verlassen():
    x = input("Zur Kasse gehen? y/N\n")
    if x == "y":
        cursor.execute("""
            SELECT warenkorb.anzahl, produkt_eigenschaften.preis 
            FROM produkt_eigenschaften 
            JOIN warenkorb ON produkt_eigenschaften.kuerzel = warenkorb.kuerzel
        """)
        h = cursor.fetchall()

        gesamtkosten = 0
        for row in h:
            gesamtkosten += row[0] * row[1]  # ❌ vorher: h[[0],[i]] → falsche Indexierung

        x = input(f"Wollen Sie {gesamtkosten} Eurocent bezahlen? y/N\n")
        if x == "y":
            if geld >= gesamtkosten:
                cursor.execute("SELECT kundennr FROM kunden WHERE name = %s", (user_name,))
                kunden_nr = cursor.fetchone()[0]

                for row in h:
                    datum = int(time.time())
                    cursor.execute(
                        "INSERT INTO kaeufe (kundennr, datum, produkt, anzahl) VALUES (%s, %s, %s, %s)",
                        (kunden_nr, datum, row[1], row[0])
                    )
                conn.commit()
    else:
        print("Auf Wiedersehen " + str(user_name))
        cursor.execute("DROP TABLE warenkorb")  # ❌ vorher: DROP warenkorb


def menue(mode):
    if mode == "K":
        show_warenkorb()
    elif mode == "B":
        show_bestand()
    elif mode == "L":
        show_Einkaufsliste()
    elif mode == "E":
        shop_verlassen()
        return 0
    else:
        print("Bitte mache eine gültige Eingabe!")
        main_loop()


# Start des Programmes
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Shop")  # ❌ vorher: CREATE IF NOT EXISTS DATABASE
conn.database = "Shop"

while True:
    user_name = input("Wie ist dein Name? ")
    cursor.execute("SELECT kundennr FROM kunden WHERE name = %s", (user_name,))
    check_kunde = cursor.fetchall()

    if not check_kunde:
        cursor.execute("SELECT COUNT(*) FROM kunden")
        nr = cursor.fetchone()[0] + 1
        cursor.execute("INSERT INTO kunden (kundennr, name) VALUES (%s, %s)", (nr, user_name))
        conn.commit()
    else:
        cursor.execute("SELECT * FROM kaeufe WHERE kundennr = %s ORDER BY datum DESC", (check_kunde[0][0],))
        last_purch = cursor.fetchone()
        if last_purch:
            c = input(f"Hast du zuletzt {last_purch} gekauft? y/N\n")
            if c == "y":
                break
        else:
            break

print("Gib deine Einkaufsliste ein, Format: [Anzahl][Objekt], Zeile für Zeile.\nWenn du fertig bist, Enter leer!")
while True:
    item = input()
    if item == "":
        break
    einkaufsliste.append(item)

main_loop()
print("Auf Wiedersehen " + str(user_name))
