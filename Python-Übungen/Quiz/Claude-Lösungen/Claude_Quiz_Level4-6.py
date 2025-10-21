# Quiz Programm - Level 4-6 (Vollversion)
# Mit Textboxen, Hintergrundbild, Menü, Scoreboard und Speicherfunktion

# ==============================================================================
# SCHRITT 1: Benötigte Module importieren
# ==============================================================================

import random
import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime  # Für Zeitstempel
import json  # Zum Speichern und Laden des Scoreboards
import os   # Zum Prüfen, ob Dateien existieren

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
# SCHRITT 3: Scoreboard-Manager Klasse
# ==============================================================================

class ScoreboardManager:
    """
    Klasse zum Verwalten des Scoreboards
    - Laden von Scores aus Datei
    - Speichern von Scores in Datei
    - Sortieren der Scores
    """
    
    def __init__(self, dateiname="scoreboard.json"):
        """
        Initialisiert den ScoreboardManager
        dateiname: Name der Datei, in der die Scores gespeichert werden
        """
        self.dateiname = dateiname
        self.scores = []  # Liste für alle Scores
        self.lade_scores()  # Beim Start Scores laden
    
    def lade_scores(self):
        """
        Lädt die Scores aus der JSON-Datei
        Falls die Datei nicht existiert, wird eine leere Liste verwendet
        """
        # Prüfen, ob die Datei existiert
        if os.path.exists(self.dateiname):
            try:
                # Datei öffnen im Lese-Modus ('r' = read)
                with open(self.dateiname, 'r', encoding='utf-8') as datei:
                    # JSON-Daten aus der Datei laden
                    self.scores = json.load(datei)
                print(f"✓ {len(self.scores)} Scores erfolgreich geladen")
            except Exception as e:
                # Fehlerbehandlung, falls etwas beim Laden schiefgeht
                print(f"Fehler beim Laden der Scores: {e}")
                self.scores = []
        else:
            # Datei existiert noch nicht - leere Liste verwenden
            print("Keine Scoreboard-Datei gefunden. Starte mit leerem Scoreboard.")
            self.scores = []
    
    def speichere_scores(self):
        """
        Speichert die Scores in die JSON-Datei
        """
        try:
            # Datei öffnen im Schreib-Modus ('w' = write)
            # encoding='utf-8' für Umlaute (ä, ö, ü)
            with open(self.dateiname, 'w', encoding='utf-8') as datei:
                # Daten als JSON in die Datei schreiben
                # indent=4 macht die Datei schön lesbar (formatiert)
                json.dump(self.scores, datei, indent=4, ensure_ascii=False)
            print("✓ Scores erfolgreich gespeichert")
        except Exception as e:
            print(f"Fehler beim Speichern der Scores: {e}")
    
    def fuege_score_hinzu(self, username, score, richtige, gesamt):
        """
        Fügt einen neuen Score zum Scoreboard hinzu
        """
        # Aktuelles Datum und Uhrzeit
        zeitstempel = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        
        # Score-Dictionary erstellen
        score_eintrag = {
            "username": username,
            "score": score,
            "richtige": richtige,
            "gesamt": gesamt,
            "prozent": round((richtige / gesamt) * 100, 1),
            "datum": zeitstempel
        }
        
        # Score zur Liste hinzufügen
        self.scores.append(score_eintrag)
        
        # Nach Score sortieren (höchster zuerst)
        self.scores.sort(key=lambda x: x["score"], reverse=True)
        
        # Nur die Top 20 behalten (optional)
        self.scores = self.scores[:20]
        
        # Scores speichern
        self.speichere_scores()
    
    def hole_scores_formatiert(self):
        """
        Gibt die Scores als formatierten String zurück
        """
        if not self.scores:
            return "Noch keine Einträge im Scoreboard!"
        
        # Header für die Tabelle
        text = "=" * 80 + "\n"
        text += "                          🏆 SCOREBOARD 🏆\n"
        text += "=" * 80 + "\n\n"
        
        # Spaltenüberschriften
        text += f"{'Rang':<6} {'Username':<20} {'Score':<10} {'Richtig':<10} {'%':<8} {'Datum':<20}\n"
        text += "-" * 80 + "\n"
        
        # Jeder Score als Zeile
        for i, score in enumerate(self.scores, 1):
            text += (
                f"{i:<6} "
                f"{score['username']:<20} "
                f"{score['score']:<10} "
                f"{score['richtige']}/{score['gesamt']:<7} "
                f"{score['prozent']:<8.1f} "
                f"{score['datum']:<20}\n"
            )
        
        return text

# ==============================================================================
# SCHRITT 4: Hauptanwendung mit Menü
# ==============================================================================

class QuizApp:
    
    def __init__(self, root):
        """
        Initialisiert die Quiz-Anwendung
        """
        self.root = root
        self.root.title("Python Quiz-Show - Level 4-6")
        self.root.geometry("800x600")
        
        # Scoreboard-Manager initialisieren
        self.scoreboard = ScoreboardManager()
        
        # Username für das aktuelle Spiel (wird beim Start abgefragt)
        self.username = ""
        
        # ==============================================================================
        # SCHRITT 5: Hintergrundbild (Level 4)
        # ==============================================================================
        
        # Da wir kein echtes Bild haben, erstellen wir einen farbigen Hintergrund
        # In der echten Anwendung würde man hier ein Bild laden:
        # self.bg_image = tk.PhotoImage(file="hintergrund.png")
        # self.background_label = tk.Label(root, image=self.bg_image)
        
        # Für dieses Beispiel: Canvas mit Farbverlauf-Simulation
        self.canvas = tk.Canvas(root, width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Gradient-Effekt simulieren (von oben nach unten dunkler werdend)
        for i in range(60):
            # Berechne Farbe (von hell nach dunkel)
            color_value = 50 - i  # Von 50 runter zu -10
            if color_value < 0:
                color_value = 0
            hex_color = f"#{30+color_value:02x}{45+color_value:02x}{60+color_value:02x}"
            
            # Rechteck zeichnen
            self.canvas.create_rectangle(
                0, i*10, 800, (i+1)*10,
                fill=hex_color,
                outline=hex_color
            )
        
        # ==============================================================================
        # SCHRITT 6: Startmenü anzeigen (Level 5)
        # ==============================================================================
        
        self.zeige_startmenu()
    
    def zeige_startmenu(self):
        """
        Zeigt das Startmenü mit Buttons für verschiedene Optionen
        """
        # Alle vorherigen Widgets löschen (falls vorhanden)
        for widget in self.root.winfo_children():
            if widget != self.canvas:
                widget.destroy()
        
        # Container-Frame für das Menü (auf dem Canvas platziert)
        menu_frame = tk.Frame(self.canvas, bg="#2C3E50", relief=tk.RAISED, bd=5)
        self.canvas.create_window(400, 300, window=menu_frame)
        
        # Titel
        titel = tk.Label(
            menu_frame,
            text="🎯 Python Quiz-Show 🎯",
            font=("Arial", 28, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1",
            pady=20
        )
        titel.pack()
        
        # Untertitel
        untertitel = tk.Label(
            menu_frame,
            text="Level 4-6 - Vollversion",
            font=("Arial", 14),
            bg="#2C3E50",
            fg="#BDC3C7"
        )
        untertitel.pack(pady=(0, 30))
        
        # Button: Spiel starten
        start_button = tk.Button(
            menu_frame,
            text="🎮 Spiel Starten",
            font=("Arial", 14, "bold"),
            bg="#27AE60",
            fg="white",
            width=25,
            height=2,
            cursor="hand2",
            command=self.frage_username
        )
        start_button.pack(pady=10)
        
        # Button: Scoreboard anzeigen
        scoreboard_button = tk.Button(
            menu_frame,
            text="🏆 Scoreboard",
            font=("Arial", 14, "bold"),
            bg="#3498DB",
            fg="white",
            width=25,
            height=2,
            cursor="hand2",
            command=self.zeige_scoreboard
        )
        scoreboard_button.pack(pady=10)
        
        # Button: Beenden
        exit_button = tk.Button(
            menu_frame,
            text="❌ Beenden",
            font=("Arial", 14, "bold"),
            bg="#E74C3C",
            fg="white",
            width=25,
            height=2,
            cursor="hand2",
            command=self.root.destroy
        )
        exit_button.pack(pady=10)
    
    def frage_username(self):
        """
        Fragt den Usernamen ab, bevor das Spiel startet
        """
        # Alle vorherigen Widgets löschen
        for widget in self.root.winfo_children():
            if widget != self.canvas:
                widget.destroy()
        
        # Container-Frame
        username_frame = tk.Frame(self.canvas, bg="#2C3E50", relief=tk.RAISED, bd=5)
        self.canvas.create_window(400, 300, window=username_frame)
        
        # Titel
        titel = tk.Label(
            username_frame,
            text="Willkommen beim Quiz!",
            font=("Arial", 20, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1",
            pady=20
        )
        titel.pack()
        
        # Beschreibung
        beschreibung = tk.Label(
            username_frame,
            text="Bitte gib deinen Namen ein:",
            font=("Arial", 14),
            bg="#2C3E50",
            fg="#BDC3C7"
        )
        beschreibung.pack(pady=(0, 20))
        
        # ==============================================================================
        # SCHRITT 7: Textbox für Username-Eingabe (Level 4)
        # ==============================================================================
        
        # Entry-Widget = Einzeilige Textbox
        self.username_entry = tk.Entry(
            username_frame,
            font=("Arial", 16),
            width=25,
            justify=tk.CENTER,
            relief=tk.SOLID,
            bd=2
        )
        self.username_entry.pack(pady=10)
        self.username_entry.focus()  # Fokus auf die Textbox setzen
        
        # Enter-Taste zum Bestätigen
        self.username_entry.bind('<Return>', lambda e: self.starte_quiz())
        
        # Button zum Starten
        start_button = tk.Button(
            username_frame,
            text="Los geht's!",
            font=("Arial", 14, "bold"),
            bg="#27AE60",
            fg="white",
            width=20,
            height=2,
            cursor="hand2",
            command=self.starte_quiz
        )
        start_button.pack(pady=20)
        
        # Zurück-Button
        zurueck_button = tk.Button(
            username_frame,
            text="Zurück",
            font=("Arial", 12),
            bg="#95A5A6",
            fg="white",
            width=20,
            cursor="hand2",
            command=self.zeige_startmenu
        )
        zurueck_button.pack(pady=10)
    
    def starte_quiz(self):
        """
        Startet das Quiz, nachdem der Username eingegeben wurde
        """
        # Username aus der Textbox holen
        self.username = self.username_entry.get().strip()
        
        # Validierung: Username darf nicht leer sein
        if not self.username:
            messagebox.showwarning("Achtung", "Bitte gib einen Namen ein!")
            return
        
        # Wenn Username zu lang ist, kürzen
        if len(self.username) > 20:
            self.username = self.username[:20]
        
        # Quiz initialisieren
        self.initialisiere_quiz()
    
    def initialisiere_quiz(self):
        """
        Bereitet das Quiz vor und zeigt die erste Frage
        """
        # Spielvariablen zurücksetzen
        self.fragen = fragen.copy()
        random.shuffle(self.fragen)
        self.aktuelle_frage_index = 0
        self.score = 0
        self.richtige_antworten = 0
        self.punkte_pro_frage = 100
        
        # Alle vorherigen Widgets löschen
        for widget in self.root.winfo_children():
            if widget != self.canvas:
                widget.destroy()
        
        # ==============================================================================
        # SCHRITT 8: Quiz-GUI aufbauen
        # ==============================================================================
        
        # Container-Frame für das Quiz
        self.quiz_frame = tk.Frame(self.canvas, bg="#2C3E50")
        self.canvas.create_window(400, 300, window=self.quiz_frame)
        
        # Header mit Username und Score
        header_frame = tk.Frame(self.quiz_frame, bg="#34495E", relief=tk.RAISED, bd=2)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Username anzeigen
        username_label = tk.Label(
            header_frame,
            text=f"Spieler: {self.username}",
            font=("Arial", 14, "bold"),
            bg="#34495E",
            fg="#ECF0F1",
            padx=20,
            pady=10
        )
        username_label.pack(side=tk.LEFT)
        
        # Fragennummer
        self.fragen_label = tk.Label(
            header_frame,
            text="Frage 1 von 10",
            font=("Arial", 12),
            bg="#34495E",
            fg="#ECF0F1",
            padx=20,
            pady=10
        )
        self.fragen_label.pack(side=tk.LEFT, expand=True)
        
        # Score
        self.score_label = tk.Label(
            header_frame,
            text="Score: 0",
            font=("Arial", 14, "bold"),
            bg="#34495E",
            fg="#F39C12",
            padx=20,
            pady=10
        )
        self.score_label.pack(side=tk.RIGHT)
        
        # Frage-Frame
        frage_frame = tk.Frame(self.quiz_frame, bg="#2C3E50")
        frage_frame.pack(pady=20)
        
        # Frage-Text
        self.frage_text = tk.Label(
            frage_frame,
            text="",
            font=("Arial", 16, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1",
            wraplength=700,
            justify=tk.CENTER,
            pady=20
        )
        self.frage_text.pack()
        
        # ==============================================================================
        # SCHRITT 9: Textboxen für Antworten (Level 4)
        # ==============================================================================
        
        # Container für Antworten
        antwort_frame = tk.Frame(self.quiz_frame, bg="#2C3E50")
        antwort_frame.pack(pady=20)
        
        # 4 Textboxen mit Buttons
        self.antwort_entries = []
        self.antwort_buttons = []
        
        for i in range(4):
            # Frame für eine Zeile (Textbox + Button)
            row_frame = tk.Frame(antwort_frame, bg="#2C3E50")
            row_frame.pack(pady=5)
            
            # Nummer-Label (1, 2, 3, 4)
            nummer_label = tk.Label(
                row_frame,
                text=f"{i+1}.",
                font=("Arial", 14, "bold"),
                bg="#2C3E50",
                fg="#ECF0F1",
                width=2
            )
            nummer_label.pack(side=tk.LEFT, padx=5)
            
            # Textbox (Entry) - nur lesbar, zeigt die Antwort an
            entry = tk.Entry(
                row_frame,
                font=("Arial", 12),
                width=40,
                state='readonly',  # Nur lesbar
                readonlybackground="white",
                relief=tk.SOLID,
                bd=2
            )
            entry.pack(side=tk.LEFT, padx=5)
            self.antwort_entries.append(entry)
            
            # Button zum Auswählen
            button = tk.Button(
                row_frame,
                text="Auswählen",
                font=("Arial", 12, "bold"),
                bg="#3498DB",
                fg="white",
                width=12,
                cursor="hand2",
                command=lambda idx=i: self.pruefe_antwort(idx)
            )
            button.pack(side=tk.LEFT, padx=5)
            self.antwort_buttons.append(button)
        
        # Erste Frage laden
        self.naechste_frage()
    
    def naechste_frage(self):
        """
        Lädt die nächste Frage
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
        
        # Antwortmöglichkeiten vorbereiten
        self.antwortmoeglichkeiten = frage_dict["falsch"].copy()
        self.antwortmoeglichkeiten.append(frage_dict["richtig"])
        random.shuffle(self.antwortmoeglichkeiten)
        self.richtige_antwort = frage_dict["richtig"]
        
        # Textboxen und Buttons aktualisieren
        for i in range(4):
            # Textbox mit normaler Methode aktualisieren
            self.antwort_entries[i].config(state='normal')
            self.antwort_entries[i].delete(0, tk.END)
            self.antwort_entries[i].insert(0, self.antwortmoeglichkeiten[i])
            self.antwort_entries[i].config(state='readonly', readonlybackground="white")
            
            # Button zurücksetzen
            self.antwort_buttons[i].config(bg="#3498DB", state=tk.NORMAL)
    
    def pruefe_antwort(self, button_index):
        """
        Prüft die ausgewählte Antwort
        """
        gewaehlte_antwort = self.antwortmoeglichkeiten[button_index]
        
        # Alle Buttons deaktivieren
        for button in self.antwort_buttons:
            button.config(state=tk.DISABLED)
        
        # Antwort prüfen und Feedback geben
        if gewaehlte_antwort.strip().lower() == self.richtige_antwort.strip().lower():
            # RICHTIG
            self.antwort_buttons[button_index].config(bg="#27AE60")
            self.antwort_entries[button_index].config(readonlybackground="#27AE60")
            self.score += self.punkte_pro_frage
            self.richtige_antworten += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            # FALSCH
            self.antwort_buttons[button_index].config(bg="#E74C3C")
            self.antwort_entries[button_index].config(readonlybackground="#E74C3C")
            
            # Richtige Antwort markieren
            for i, antwort in enumerate(self.antwortmoeglichkeiten):
                if antwort.strip().lower() == self.richtige_antwort.strip().lower():
                    self.antwort_buttons[i].config(bg="#27AE60")
                    self.antwort_entries[i].config(readonlybackground="#27AE60")
        
        # Nächste Frage nach 2 Sekunden
        self.aktuelle_frage_index += 1
        self.root.after(2000, self.naechste_frage)
    
    def zeige_endergebnis(self):
        """
        Zeigt das Endergebnis und speichert den Score
        """
        max_punkte = len(self.fragen) * self.punkte_pro_frage
        prozent = (self.score / max_punkte) * 100
        
        # Score zum Scoreboard hinzufügen
        self.scoreboard.fuege_score_hinzu(
            self.username,
            self.score,
            self.richtige_antworten,
            len(self.fragen)
        )
        
        # Bewertung
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
        
        # Endergebnis-Text
        ergebnis_text = f"""
QUIZ BEENDET!

Spieler: {self.username}

Richtige Antworten: {self.richtige_antworten} von {len(self.fragen)}
Gesamtpunktzahl: {self.score} von {max_punkte} Punkten
Das entspricht {prozent:.1f}%

{bewertung}

Dein Score wurde im Scoreboard gespeichert!
        """
        
        messagebox.showinfo("Endergebnis", ergebnis_text)
        
        # Zurück zum Menü
        self.zeige_startmenu()
    
    def zeige_scoreboard(self):
        """
        Zeigt das Scoreboard in einem neuen Fenster
        """
        # Neues Fenster erstellen
        scoreboard_window = tk.Toplevel(self.root)
        scoreboard_window.title("🏆 Scoreboard")
        scoreboard_window.geometry("900x600")
        scoreboard_window.configure(bg="#2C3E50")
        
        # Titel
        titel = tk.Label(
            scoreboard_window,
            text="🏆 SCOREBOARD 🏆",
            font=("Arial", 24, "bold"),
            bg="#2C3E50",
            fg="#F39C12"
        )
        titel.pack(pady=20)
        
        # ScrolledText für das Scoreboard (mehrzeilige Textbox mit Scrollbar)
        text_widget = scrolledtext.ScrolledText(
            scoreboard_window,
            font=("Courier", 11),  # Courier = monospace Font für Tabellen
            width=100,
            height=25,
            bg="#ECF0F1",
            fg="#2C3E50",
            relief=tk.SOLID,
            bd=2
        )
        text_widget.pack(padx=20, pady=10)
        
        # Scoreboard-Text einfügen
        scoreboard_text = self.scoreboard.hole_scores_formatiert()
        text_widget.insert(tk.END, scoreboard_text)
        text_widget.config(state=tk.DISABLED)  # Nur lesbar
        
        # Schließen-Button
        close_button = tk.Button(
            scoreboard_window,
            text="Schließen",
            font=("Arial", 12, "bold"),
            bg="#E74C3C",
            fg="white",
            width=20,
            cursor="hand2",
            command=scoreboard_window.destroy
        )
        close_button.pack(pady=10)

# ==============================================================================
# SCHRITT 10: Hauptprogramm starten
# ==============================================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()