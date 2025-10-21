# Quiz Programm - Level 2
# Quiz mit zufälliger Fragenreihenfolge und Multiple-Choice-Antworten

# ==============================================================================
# SCHRITT 1: Benötigte Module importieren
# ==============================================================================

# random-Modul wird für Zufallsauswahl und Mischen von Listen benötigt
import random

# ==============================================================================
# SCHRITT 2: Fragen, richtige Antworten und Falschantworten erstellen
# ==============================================================================

# Jetzt verwenden wir ein erweitertes Format:
# - "frage": Die Quizfrage
# - "richtig": Die richtige Antwort
# - "falsch": Liste mit falschen Antworten für Multiple Choice

fragen = [
    {
        "frage": "Was ist die Hauptstadt von Deutschland?",
        "richtig": "Berlin",
        "falsch": ["München", "Hamburg", "Köln"]
    },
    {
        "frage": "Wie viele Bundesländer hat Deutschland?",
        "richtig": "16",
        "falsch": ["12", "18", "14"]
    },
    {
        "frage": "In welchem Jahr fiel die Berliner Mauer?",
        "richtig": "1989",
        "falsch": ["1990", "1985", "1991"]
    },
    {
        "frage": "Welcher Planet ist der Sonne am nächsten?",
        "richtig": "Merkur",
        "falsch": ["Venus", "Mars", "Erde"]
    },
    {
        "frage": "Wie viele Minuten hat eine Stunde?",
        "richtig": "60",
        "falsch": ["50", "100", "75"]
    },
    {
        "frage": "Was ist die chemische Formel für Wasser?",
        "richtig": "H2O",
        "falsch": ["CO2", "O2", "H2SO4"]
    },
    {
        "frage": "Wer schrieb 'Faust'?",
        "richtig": "Goethe",
        "falsch": ["Schiller", "Kafka", "Brecht"]
    },
    {
        "frage": "Wie viele Spieler hat eine Fußballmannschaft auf dem Feld?",
        "richtig": "11",
        "falsch": ["10", "12", "9"]
    },
    {
        "frage": "In welchem Kontinent liegt Ägypten?",
        "richtig": "Afrika",
        "falsch": ["Asien", "Europa", "Südamerika"]
    },
    {
        "frage": "Wie viele Seiten hat ein Würfel?",
        "richtig": "6",
        "falsch": ["8", "4", "12"]
    }
]

# ==============================================================================
# SCHRITT 3: Fragen in zufälliger Reihenfolge mischen
# ==============================================================================

# random.shuffle() mischt die Liste direkt (in-place)
# WICHTIG: Wir machen eine Kopie der Liste, um das Original nicht zu verändern
fragen_gemischt = fragen.copy()  # Kopie erstellen
random.shuffle(fragen_gemischt)   # Kopie mischen

# Jetzt ist fragen_gemischt in zufälliger Reihenfolge!
# Dadurch kommt jede Frage nur einmal vor und keine Frage wird doppelt gestellt.

# ==============================================================================
# SCHRITT 4: Score-System initialisieren
# ==============================================================================

score = 0
punkte_pro_frage = 100
richtige_antworten = 0

# ==============================================================================
# SCHRITT 5: Begrüßung
# ==============================================================================

print("=" * 60)
print("Willkommen bei der Python Quiz-Show!")
print("Level 2 - Multiple Choice mit Zufallsreihenfolge")
print("=" * 60)
print(f"\nEs warten {len(fragen_gemischt)} Fragen auf dich.")
print(f"Für jede richtige Antwort gibt es {punkte_pro_frage} Punkte.")
print("Wähle die richtige Antwort durch Eingabe der Nummer (1-4).")
print("\nViel Erfolg!\n")
print("=" * 60)

# ==============================================================================
# SCHRITT 6: Durch alle Fragen iterieren
# ==============================================================================

for i, frage_dict in enumerate(fragen_gemischt):
    
    print(f"\nFrage {i + 1} von {len(fragen_gemischt)}:")
    print(frage_dict["frage"])
    print()  # Leerzeile für bessere Lesbarkeit
    
    # ==============================================================================
    # SCHRITT 7: Antwortmöglichkeiten vorbereiten und mischen
    # ==============================================================================
    
    # Wir erstellen eine Liste mit ALLEN Antwortmöglichkeiten
    # Dabei kopieren wir die falschen Antworten mit .copy(), um das Original nicht zu verändern
    antwortmoeglichkeiten = frage_dict["falsch"].copy()
    
    # Die richtige Antwort zur Liste hinzufügen
    antwortmoeglichkeiten.append(frage_dict["richtig"])
    
    # WICHTIG: Jetzt mischen wir die Antworten in zufälliger Reihenfolge!
    # Dadurch steht die richtige Antwort nicht immer an der gleichen Position
    random.shuffle(antwortmoeglichkeiten)
    
    # Nach dem Mischen ist garantiert:
    # - Jede Antwort kommt genau 1x vor (keine Duplikate)
    # - Die richtige Antwort ist an einer zufälligen Position
    
    # ==============================================================================
    # SCHRITT 8: Antwortmöglichkeiten anzeigen
    # ==============================================================================
    
    # Wir zeigen alle Antworten mit Nummern an (1, 2, 3, 4)
    for j, antwort in enumerate(antwortmoeglichkeiten):
        # j startet bei 0, deshalb +1 für die Anzeige (1, 2, 3, 4)
        print(f"{j + 1}. {antwort}")
    
    print()  # Leerzeile
    
    # ==============================================================================
    # SCHRITT 9: User-Input entgegennehmen und validieren
    # ==============================================================================
    
    # Endlosschleife für die Eingabe, bis eine gültige Nummer eingegeben wird
    while True:
        user_input = input("Deine Antwort (1-4): ")
        
        # Prüfen, ob die Eingabe eine Zahl ist
        if user_input.isdigit():
            user_wahl = int(user_input)  # String in Zahl umwandeln
            
            # Prüfen, ob die Zahl im gültigen Bereich liegt (1-4)
            if 1 <= user_wahl <= len(antwortmoeglichkeiten):
                break  # Gültige Eingabe! Schleife verlassen
            else:
                print(f"Bitte gib eine Zahl zwischen 1 und {len(antwortmoeglichkeiten)} ein.")
        else:
            print("Bitte gib eine gültige Zahl ein.")
    
    # ==============================================================================
    # SCHRITT 10: Antwort auswerten
    # ==============================================================================
    
    # user_wahl ist 1-4, aber Listen starten bei Index 0
    # Deshalb müssen wir -1 rechnen
    gewaehlte_antwort = antwortmoeglichkeiten[user_wahl - 1]
    
    # Vergleich der gewählten Antwort mit der richtigen Antwort
    # case-insensitive mit .lower() und ohne Leerzeichen mit .strip()
    if gewaehlte_antwort.strip().lower() == frage_dict["richtig"].strip().lower():
        print("\n✓ Richtig! 🎉")
        score += punkte_pro_frage
        richtige_antworten += 1
        print(f"Du hast {punkte_pro_frage} Punkte verdient!")
    else:
        print(f"\n✗ Leider falsch. Die richtige Antwort wäre: {frage_dict['richtig']}")
        print("Keine Punkte diesmal.")
    
    print(f"Aktueller Score: {score} Punkte")
    print("-" * 60)

# ==============================================================================
# SCHRITT 11: Endergebnis anzeigen
# ==============================================================================

print("\n" + "=" * 60)
print("QUIZ BEENDET!")
print("=" * 60)

max_punkte = len(fragen_gemischt) * punkte_pro_frage
prozent = (score / max_punkte) * 100

print(f"\nDein Endergebnis:")
print(f"Richtige Antworten: {richtige_antworten} von {len(fragen_gemischt)}")
print(f"Gesamtpunktzahl: {score} von {max_punkte} Punkten")
print(f"Das entspricht {prozent:.1f}%")

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