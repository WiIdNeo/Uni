# Quiz Programm - Level 3
# Quiz mit grafischer Benutzeroberfläche (GUI) mit Tkinter

# ==============================================================================
# SCHRITT 1: Benötigte Module importieren
# ==============================================================================

import random
import tkinter as tk  # tkinter ist das Standard-GUI-Modul von Python
from tkinter import messagebox  # Für Popup-Fenster (z.B. Endergebnis)

# ==============================================================================
# SCHRITT 2: Fragen und Antworten definieren
# ==============================================================================

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
# SCHRITT 3: Quiz-Klasse erstellen (Objektorientierte Programmierung)
# ==============================================================================

# Eine Klasse ist wie ein Bauplan für ein Objekt
# Hier erstellen wir eine Klasse für unser Quiz-Programm
class QuizApp:
    
    def __init__(self, root):
        """
        Constructor (Konstruktor) - wird beim Erstellen des Quiz-Objekts aufgerufen
        root: Das Hauptfenster von Tkinter
        """
        
        # ==============================================================================
        # SCHRITT 4: Instanzvariablen initialisieren
        # ==============================================================================
        
        # self. bedeutet, dass diese Variablen zur Klasse gehören
        # und in allen Methoden der Klasse verfügbar sind
        
        self.root = root
        self.root.title("Python Quiz-Show - Level 3")  # Fenstertitel
        self.root.geometry("700x500")  # Fenstergröße (Breite x Höhe)
        self.root.configure(bg="#2C3E50")  # Hintergrundfarbe (dunkelblau)
        
        # Fragen vorbereiten (kopieren und mischen)
        self.fragen = fragen.copy()
        random.shuffle(self.fragen)  # Zufällige Reihenfolge
        
        # Spielvariablen
        self.aktuelle_frage_index = 0  # Bei welcher Frage sind wir?
        self.score = 0  # Punktestand
        self.richtige_antworten = 0  # Anzahl richtiger Antworten
        self.punkte_pro_frage = 100
        
        # Diese Variable speichert, welche Antwort aktuell richtig ist
        self.richtige_antwort = ""
        
        # Diese Variable speichert alle aktuellen Antwortmöglichkeiten
        self.antwortmoeglichkeiten = []
        
        # ==============================================================================
        # SCHRITT 5: GUI-Elemente erstellen
        # ==============================================================================
        
        # Titel-Label (Überschrift)
        self.titel_label = tk.Label(
            root,
            text="🎯 Python Quiz-Show 🎯",
            font=("Arial", 24, "bold"),
            bg="#2C3E50",  # Hintergrundfarbe
            fg="#ECF0F1"   # Textfarbe (hellgrau)
        )
        self.titel_label.pack(pady=20)  # pack() fügt das Element zum Fenster hinzu
        # pady = Padding (Abstand) oben und unten
        
        # Frame (Container) für den Fortschritt
        fortschritt_frame = tk.Frame(root, bg="#2C3E50")
        fortschritt_frame.pack(pady=10)
        
        # Label für Fragennummer
        self.fragen_label = tk.Label(
            fortschritt_frame,
            text="Frage 1 von 10",
            font=("Arial", 12),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        self.fragen_label.pack(side=tk.LEFT, padx=20)
        
        # Label für aktuellen Score
        self.score_label = tk.Label(
            fortschritt_frame,
            text="Score: 0 Punkte",
            font=("Arial", 12, "bold"),
            bg="#2C3E50",
            fg="#F39C12"  # Orange
        )
        self.score_label.pack(side=tk.LEFT, padx=20)
        
        # Frame für die Frage
        frage_frame = tk.Frame(root, bg="#34495E", relief=tk.RAISED, bd=2)
        frage_frame.pack(pady=20, padx=30, fill=tk.BOTH)
        
        # Label für die Frage selbst
        self.frage_text = tk.Label(
            frage_frame,
            text="",
            font=("Arial", 16, "bold"),
            bg="#34495E",
            fg="#ECF0F1",
            wraplength=600,  # Textumbruch bei 600 Pixeln
            justify=tk.CENTER,
            pady=20
        )
        self.frage_text.pack()
        
        # ==============================================================================
        # SCHRITT 6: Antwort-Buttons erstellen
        # ==============================================================================
        
        # Frame für die Antwort-Buttons
        self.button_frame = tk.Frame(root, bg="#2C3E50")
        self.button_frame.pack(pady=20)
        
        # Wir erstellen 4 Buttons für die 4 Antwortmöglichkeiten
        # Diese speichern wir in einer Liste, um später darauf zugreifen zu können
        self.antwort_buttons = []
        
        for i in range(4):
            # lambda mit i=i ist wichtig! Sonst würden alle Buttons den gleichen Wert haben
            # command gibt an, welche Funktion beim Klick aufgerufen wird
            button = tk.Button(
                self.button_frame,
                text="",
                font=("Arial", 12),
                bg="#3498DB",  # Blau
                fg="white",
                width=50,
                height=2,
                relief=tk.RAISED,
                bd=3,
                cursor="hand2",  # Hand-Cursor beim Hover
                command=lambda i=i: self.pruefe_antwort(i)  # Funktion beim Klick
            )
            button.pack(pady=5)
            self.antwort_buttons.append(button)  # Button zur Liste hinzufügen
        
        # ==============================================================================
        # SCHRITT 7: Erste Frage laden
        # ==============================================================================
        
        self.naechste_frage()
    
    # ==============================================================================
    # SCHRITT 8: Methode zum Laden der nächsten Frage
    # ==============================================================================
    
    def naechste_frage(self):
        """
        Lädt die nächste Frage und aktualisiert alle GUI-Elemente
        """
        
        # Prüfen, ob noch Fragen übrig sind
        if self.aktuelle_frage_index >= len(self.fragen):
            self.zeige_endergebnis()
            return
        
        # Aktuelle Frage holen
        frage_dict = self.fragen[self.aktuelle_frage_index]
        
        # Fragentext aktualisieren
        self.frage_text.config(text=frage_dict["frage"])
        
        # Fortschritt aktualisieren
        self.fragen_label.config(
            text=f"Frage {self.aktuelle_frage_index + 1} von {len(self.fragen)}"
        )
        
        # ==============================================================================
        # SCHRITT 9: Antwortmöglichkeiten vorbereiten und mischen
        # ==============================================================================
        
        # Alle Antworten sammeln
        self.antwortmoeglichkeiten = frage_dict["falsch"].copy()
        self.antwortmoeglichkeiten.append(frage_dict["richtig"])
        
        # In zufälliger Reihenfolge mischen
        random.shuffle(self.antwortmoeglichkeiten)
        
        # Richtige Antwort speichern (für den Vergleich später)
        self.richtige_antwort = frage_dict["richtig"]
        
        # ==============================================================================
        # SCHRITT 10: Button-Texte aktualisieren
        # ==============================================================================
        
        # Jeden Button mit einer Antwortmöglichkeit beschriften
        for i, button in enumerate(self.antwort_buttons):
            button.config(
                text=self.antwortmoeglichkeiten[i],
                bg="#3498DB",  # Zurück zur Standardfarbe (Blau)
                state=tk.NORMAL  # Button aktivieren
            )
    
    # ==============================================================================
    # SCHRITT 11: Methode zur Überprüfung der Antwort
    # ==============================================================================
    
    def pruefe_antwort(self, button_index):
        """
        Wird aufgerufen, wenn der User auf einen Antwort-Button klickt
        button_index: Index des geklickten Buttons (0-3)
        """
        
        # Gewählte Antwort ermitteln
        gewaehlte_antwort = self.antwortmoeglichkeiten[button_index]
        
        # Alle Buttons deaktivieren (damit man nicht mehrfach klicken kann)
        for button in self.antwort_buttons:
            button.config(state=tk.DISABLED)
        
        # ==============================================================================
        # SCHRITT 12: Antwort auswerten und visuelles Feedback geben
        # ==============================================================================
        
        # Prüfen, ob die Antwort richtig ist
        if gewaehlte_antwort.strip().lower() == self.richtige_antwort.strip().lower():
            # RICHTIG!
            self.antwort_buttons[button_index].config(bg="#27AE60")  # Grün
            self.score += self.punkte_pro_frage
            self.richtige_antworten += 1
            self.score_label.config(text=f"Score: {self.score} Punkte")
        else:
            # FALSCH!
            self.antwort_buttons[button_index].config(bg="#E74C3C")  # Rot
            
            # Richtige Antwort grün markieren
            for i, antwort in enumerate(self.antwortmoeglichkeiten):
                if antwort.strip().lower() == self.richtige_antwort.strip().lower():
                    self.antwort_buttons[i].config(bg="#27AE60")  # Grün
        
        # ==============================================================================
        # SCHRITT 13: Nach 2 Sekunden zur nächsten Frage
        # ==============================================================================
        
        # after() führt eine Funktion nach einer bestimmten Zeit aus (in Millisekunden)
        # 2000 ms = 2 Sekunden
        self.aktuelle_frage_index += 1
        self.root.after(2000, self.naechste_frage)
    
    # ==============================================================================
    # SCHRITT 14: Endergebnis anzeigen
    # ==============================================================================
    
    def zeige_endergebnis(self):
        """
        Zeigt das Endergebnis in einem Popup-Fenster an
        """
        
        max_punkte = len(self.fragen) * self.punkte_pro_frage
        prozent = (self.score / max_punkte) * 100
        
        # Bewertung ermitteln
        if prozent == 100:
            bewertung = "🏆 PERFEKT! Du bist ein Quiz-Champion!"
        elif prozent >= 80:
            bewertung = "⭐ Ausgezeichnet! Sehr gute Leistung!"
        elif prozent >= 60:
            bewertung = "👍 Gut gemacht! Solides Wissen!"
        elif prozent >= 40:
            bewertung = "📚 Nicht schlecht, aber da geht noch was!"
        else:
            bewertung = "💪 Weiter üben! Beim nächsten Mal klappt's besser!"
        
        # Endergebnis-Text erstellen
        ergebnis_text = f"""
QUIZ BEENDET!

Richtige Antworten: {self.richtige_antworten} von {len(self.fragen)}
Gesamtpunktzahl: {self.score} von {max_punkte} Punkten
Das entspricht {prozent:.1f}%

{bewertung}

Danke fürs Mitspielen!
        """
        
        # Popup-Fenster mit dem Ergebnis anzeigen
        messagebox.showinfo("Endergebnis", ergebnis_text)
        
        # Fenster schließen
        self.root.destroy()

# ==============================================================================
# SCHRITT 15: Hauptprogramm starten
# ==============================================================================

if __name__ == "__main__":
    # Hauptfenster erstellen
    root = tk.Tk()
    
    # Quiz-App erstellen (initialisiert das gesamte GUI)
    app = QuizApp(root)
    
    # Mainloop starten - wartet auf User-Interaktionen (Klicks, etc.)
    # Das Programm läuft so lange, bis das Fenster geschlossen wird
    root.mainloop()