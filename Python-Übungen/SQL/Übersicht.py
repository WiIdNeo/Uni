import mysql.connector

# ------------------------------------------------------------
# 1. Verbindung zur Datenbank herstellen (XAMPP)
# ------------------------------------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = conn.cursor()

# ------------------------------------------------------------
# 2. Neue Datenbank anlegen und auswählen
# ------------------------------------------------------------
cursor.execute("DROP DATABASE IF EXISTS Beispiel")
cursor.execute("CREATE DATABASE Beispiel")
conn.database = "Beispiel"

# ------------------------------------------------------------
# 3. Tabellen erstellen
# ------------------------------------------------------------
cursor.execute("""
CREATE TABLE kategorie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
)
""")

cursor.execute("""
CREATE TABLE einkaufsliste (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produkt VARCHAR(50),
    menge INT,
    preis DECIMAL(5,2),
    kategorie_id INT,
    FOREIGN KEY (kategorie_id) REFERENCES kategorie(id)
)
""")

# ------------------------------------------------------------
# 4. Daten einfügen
# ------------------------------------------------------------
cursor.executemany("INSERT INTO kategorie (name) VALUES (%s)", [
    ("Obst",),
    ("Getränke",),
    ("Backwaren",),
    ("Sonstiges",)
])

cursor.executemany("""
INSERT INTO einkaufsliste (produkt, menge, preis, kategorie_id)
VALUES (%s, %s, %s, %s)
""", [
    ("Äpfel", 5, 2.99, 1),
    ("Milch", 2, 1.19, 2),
    ("Brot", 1, 2.49, 3),
    ("Kaffee", 1, 4.99, 2),
    ("Schokolade", 3, 1.49, 4)
])
conn.commit()

# ------------------------------------------------------------
# 5. SELECT – Daten abfragen
# ------------------------------------------------------------
print("\nAlle Produkte (SELECT *):")
cursor.execute("SELECT * FROM einkaufsliste")
for row in cursor.fetchall():
    print(row)

print("\nNur Produktnamen (SELECT spalte):")
cursor.execute("SELECT produkt FROM einkaufsliste")
for row in cursor.fetchall():
    print(row)

# ------------------------------------------------------------
# 6. WHERE – Bedingungen
# ------------------------------------------------------------
print("\nProdukte mit Preis > 2.00 (WHERE):")
cursor.execute("SELECT produkt, preis FROM einkaufsliste WHERE preis > 2.00")
for row in cursor.fetchall():
    print(row)

# ------------------------------------------------------------
# 7. UPDATE – Daten ändern
# ------------------------------------------------------------
print("\nPreis von Äpfeln ändern (UPDATE):")
cursor.execute("UPDATE einkaufsliste SET preis = 3.49 WHERE produkt = 'Äpfel'")
conn.commit()
cursor.execute("SELECT produkt, preis FROM einkaufsliste WHERE produkt = 'Äpfel'")
print(cursor.fetchall())

# ------------------------------------------------------------
# 8. DELETE – Daten löschen
# ------------------------------------------------------------
print("\nMilch löschen (DELETE):")
cursor.execute("DELETE FROM einkaufsliste WHERE produkt = 'Milch'")
conn.commit()
cursor.execute("SELECT * FROM einkaufsliste")
for row in cursor.fetchall():
    print(row)

# ------------------------------------------------------------
# 9. ORDER BY – Sortieren
# ------------------------------------------------------------
print("\nProdukte nach Preis absteigend sortiert (ORDER BY):")
cursor.execute("SELECT produkt, preis FROM einkaufsliste ORDER BY preis DESC")
for row in cursor.fetchall():
    print(row)

# ------------------------------------------------------------
# 10. GROUP BY – Gruppieren
# ------------------------------------------------------------
print("\nAnzahl Produkte pro Kategorie (GROUP BY):")
cursor.execute("""
SELECT kategorie_id, COUNT(*) AS anzahl
FROM einkaufsliste
GROUP BY kategorie_id
""")
for row in cursor.fetchall():
    print(row)

# ------------------------------------------------------------
# 11. JOIN – Tabellen verbinden
# ------------------------------------------------------------
print("\nProdukte mit Kategorienamen (INNER JOIN):")
cursor.execute("""
SELECT einkaufsliste.produkt, kategorie.name
FROM einkaufsliste
INNER JOIN kategorie ON einkaufsliste.kategorie_id = kategorie.id
""")
for row in cursor.fetchall():
    print(row)

print("\nAlle Kategorien, auch ohne Produkte (LEFT JOIN):")
cursor.execute("""
SELECT kategorie.name, einkaufsliste.produkt
FROM kategorie
LEFT JOIN einkaufsliste ON einkaufsliste.kategorie_id = kategorie.id
""")
for row in cursor.fetchall():
    print(row)

# ------------------------------------------------------------
# 12. Aufräumen
# ------------------------------------------------------------
cursor.execute("DROP DATABASE Beispiel")
cursor.close()
conn.close()

# ------------------------------------------------------------
# SQL-BEFEHLE – SYNTAX-ÜBERSICHT
# ------------------------------------------------------------
# CREATE DATABASE   -> CREATE DATABASE datenbankname;
# CREATE TABLE      -> CREATE TABLE tabellenname (spalte datentyp, ...);
# INSERT INTO       -> INSERT INTO tabellenname (spalte1, spalte2, ...) VALUES (wert1, wert2, ...);
# SELECT            -> SELECT spalte1, spalte2 FROM tabellenname;
# WHERE             -> SELECT spalte FROM tabellenname WHERE bedingung;
# UPDATE            -> UPDATE tabellenname SET spalte = neuer_wert WHERE bedingung;
# DELETE            -> DELETE FROM tabellenname WHERE bedingung;
# ORDER BY          -> SELECT spalte FROM tabellenname ORDER BY spalte [ASC|DESC];
# GROUP BY          -> SELECT spalte, AGGREGATFUNKTION(spalte) FROM tabellenname GROUP BY spalte;
# INNER JOIN        -> SELECT t1.spalte, t2.spalte FROM t1 INNER JOIN t2 ON t1.id = t2.id;
# LEFT JOIN         -> SELECT t1.spalte, t2.spalte FROM t1 LEFT JOIN t2 ON t1.id = t2.id;
