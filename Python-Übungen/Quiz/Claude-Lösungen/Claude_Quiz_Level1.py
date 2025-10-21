# Quiz Programm - Level 1
# Ein interaktives Quiz mit 10 Fragen, Antwort-Auswertung und Score-System

# ==============================================================================
# SCHRITT 1: Fragen und Antworten erstellen
# ==============================================================================

# Wir verwenden eine Liste (Array) mit Dictionaries (Wörterbüchern).
# Jedes Dictionary enthält eine Frage und die richtige Antwort.
# Dies macht es einfach, Fragen und Antworten zusammenzuhalten.

fragen = [
    {
        "frage": "Was ist die Hauptstadt von Deutschland?",
        "antwort": "Berlin"
    },
    {
        "frage": "Wie viele Bundesländer hat Deutschland?",
        "antwort": "16"
    },
    {
        "frage": "In welchem Jahr fiel die Berliner Mauer?",
        "antwort": "1989"
    },
    {
        "frage": "Welcher Planet ist der Sonne am nächsten?",
        "antwort": "Merkur"
    },
    {
        "frage": "Wie viele Minuten hat eine Stunde?",
        "antwort": "60"
    },
    {
        "frage": "Was ist die chemische Formel für Wasser?",
        "antwort": "H2O"
    },
    {
        "frage": "Wer schrieb 'Faust'?",
        "antwort": "Goethe"
    },
    {
        "frage": "Wie viele Spieler hat eine Fußballmannschaft auf dem Feld?",
        "antwort": "11"
    },
    {
        "frage": "In welchem Kontinent liegt Ägypten?",
        "antwort": "Afrika"
    },
    {
        "frage": "Wie viele Seiten hat ein Würfel?",
        "antwort": "6"
    }
]

# ==============================================================================
# SCHRITT 2: Score-System initialisieren
# ==============================================================================

# Wir verwenden ein realistisches Score-System wie in echten Quizshows:
# - Richtige Antwort: +100 Punkte
# - Falsche Antwort: 0 Punkte (keine Punktabzug, um fair zu bleiben)
# - Am Ende wird die Gesamtpunktzahl und der Prozentsatz angezeigt

score = 0  # Variable für die Gesamtpunktzahl
punkte_pro_frage = 100  # Punkte für jede richtige Antwort
richtige_antworten = 0  # Zähler für richtige Antworten

# ==============================================================================
# SCHRITT 3: Begrüßung und Spielstart
# ==============================================================================

print("=" * 60)
print("Willkommen bei der Python Quiz-Show!")
print("=" * 60)
print(f"\nEs warten {len(fragen)} Fragen auf dich.")
print(f"Für jede richtige Antwort gibt es {punkte_pro_frage} Punkte.")
print("Bei der Groß-/Kleinschreibung wird nicht unterschieden.")
print("\nViel Erfolg!\n")
print("=" * 60)

# ==============================================================================
# SCHRITT 4: Durch alle Fragen iterieren
# ==============================================================================

# enumerate() gibt uns sowohl den Index (i) als auch das Element (frage_dict)
# Index startet bei 0, deshalb fügen wir +1 hinzu für die Anzeige
for i, frage_dict in enumerate(fragen):
    
    # Anzeige der Fragennummer (i+1, weil wir bei 1 starten wollen, nicht bei 0)
    print(f"\nFrage {i + 1} von {len(fragen)}:")
    print(frage_dict["frage"])
    
    # ==============================================================================
    # SCHRITT 5: User-Input entgegennehmen
    # ==============================================================================
    
    # input() wartet auf die Eingabe des Users und speichert sie in einer Variable
    user_antwort = input("Deine Antwort: ")
    
    # ==============================================================================
    # SCHRITT 6: Antwort auswerten
    # ==============================================================================
    
    # Wir vergleichen die Antworten case-insensitive (Groß-/Kleinschreibung egal)
    # .strip() entfernt Leerzeichen am Anfang und Ende
    # .lower() wandelt alles in Kleinbuchstaben um
    
    if user_antwort.strip().lower() == frage_dict["antwort"].strip().lower():
        # Antwort ist richtig!
        print("✓ Richtig! 🎉")
        score += punkte_pro_frage  # Punkte zur Gesamtsumme hinzufügen
        richtige_antworten += 1     # Zähler für richtige Antworten erhöhen
        print(f"Du hast {punkte_pro_frage} Punkte verdient!")
    else:
        # Antwort ist falsch
        print(f"✗ Leider falsch. Die richtige Antwort wäre: {frage_dict['antwort']}")
        print("Keine Punkte diesmal.")
    
    # Aktuellen Zwischenstand anzeigen
    print(f"Aktueller Score: {score} Punkte")
    print("-" * 60)

# ==============================================================================
# SCHRITT 7: Endergebnis anzeigen
# ==============================================================================

print("\n" + "=" * 60)
print("QUIZ BEENDET!")
print("=" * 60)

# Berechnung des Prozentsatzes
max_punkte = len(fragen) * punkte_pro_frage
prozent = (score / max_punkte) * 100

# Endergebnis ausgeben
print(f"\nDein Endergebnis:")
print(f"Richtige Antworten: {richtige_antworten} von {len(fragen)}")
print(f"Gesamtpunktzahl: {score} von {max_punkte} Punkten")
print(f"Das entspricht {prozent:.1f}%")

# ==============================================================================
# SCHRITT 8: Bewertung ausgeben (wie in einer echten Quizshow)
# ==============================================================================

print("\nBewertung:")
if prozent == 100:
    print("🏆 PERFEKT! Du bist ein Quiz-Champion!")
elif prozent >= 80:
    print("⭐ Ausgezeichnet! Sehr gute Leistung!")
elif prozent >= 60:
    print("👍 Gut gemacht! Solides Wissen!")
elif prozent >= 40:
    print("📚 Nicht schlecht, aber da geht noch was!")
else:
    print("💪 Weiter üben! Beim nächsten Mal klappt's besser!")

print("=" * 60)
print("\nDanke fürs Mitspielen!")
print("=" * 60)