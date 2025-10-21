import tkinter
import random
import time

fragen = [ 
    "Wie hoch ist der K2?", 
    "Wie lang ist der Nil?", 
    "Welches war das größte Reich aller Zeiten?", 
    "Wie viele Länder gibt es auf der Welt (Stand 2024)?", 
    "Wie alt ist das älteste zur Zeit lebende Tier (Stand 2024)?",
    "Wie alt ist die älteste Pflanze der Welt?", 
    "Wie groß ist die Sahara?",
    "Wie heißt die größte Wüste der Welt?",
    "Wie alt ist der Old Tjikko?",
    "Wann kam die Wii U heraus?"
]

antworten = [
    ["8611m", "8848m", "8741m", "8563m"], 
    ["6650km", "6700km", "6600km", "6500m"], 
    ["British Empire", "Mongolisches Reich", "Römisches Imperium", "Sowjetunion"],
    ["195", "197", "189", "192"],
    ["Riesenschwämme", "Galapagosschildkröte", "Grönlandhai", "Quahog-Muschel"],
    ["bis zu 100.000 Jahre", "bis zu 80.000 Jahre", "bis zu 10.000 Jahre", "bis zu 500 Jahre"], 
    ["9.000.000km²", "9.500.000km²", "8.500.000km²", "8.000.000km²"],
    ["Antarktis", "Sahara", "Namib", "Arabische Wüste"],
    ["9.950 Jahre", "8.940 Jahre", "3.720 Jahre", "4.970 Jahre"], 
    ["2012", "2013", "2011", "2014"]
]

# ------------------------------
# Variablen für Spielstand
# ------------------------------
score = 0
correct_val = 10   # Punkte für richtige Antwort
wrong_val = 0      # Punkte für falsche Antwort
gestellte_fragen = []  # Liste der bereits gestellten Fragen
j = None           # Index der aktuellen Frage
global start_time
global end_time
nTime = 0


wind0w = tkinter.Tk()
wind0w.title("Quiz")
wind0w.geometry("800x500")


# Alle Widgets im Fenster löschen
def clear_window():
    for widget in wind0w.winfo_children():
        widget.destroy()

# Hauptmenü anzeigen
def show_menu():
    clear_window()
    tkinter.Label(wind0w, text="Hauptmenü", font=("Arial", 20)).pack(pady=20)
    tkinter.Button(wind0w, text="Quiz starten", command=show_quiz).pack(pady=10)
    tkinter.Button(wind0w, text="Scoreboard", command=show_scoreboard).pack(pady=10)

# Neue Frage auswählen, die noch nicht gestellt wurde
def get_question():
    global j
    j = random.randint(0, len(fragen)-1)
    while fragen[j] in gestellte_fragen:
        j = random.randint(0, len(fragen)-1)
    gestellte_fragen.append(fragen[j])
    return fragen[j]

# Antwortmöglichkeiten zur aktuellen Frage holen
def get_answer():
    return antworten[j]

# Antwort prüfen
def check_answer(is_correct, start_time):
    global score, nTime   # <--- nTime hier global machen
    clear_window()
    if is_correct:
        score += correct_val
        tkinter.Label(wind0w, text="Richtig!", fg="green", font=("Arial", 16)).pack(pady=10)
    else:
        score += wrong_val
        tkinter.Label(wind0w, text="Falsch!", fg="red", font=("Arial", 16)).pack(pady=10)

    end_time = time.time()
    nTime = nTime + (end_time - start_time)   # jetzt funktioniert es

    # Wichtig: show_scoreboard darf nicht sofort aufgerufen werden,
    # sondern als Callback übergeben werden:
    if len(gestellte_fragen) < len(fragen):
        wind0w.after(1000, show_quiz)
    else:
        wind0w.after(1000, lambda: show_scoreboard(nTime))


# Eine Quizfrage anzeigen
def show_quiz():
    start_time = time.time()
    clear_window()
    tkinter.Button(wind0w, text="Zurück zum Menü", command=show_menu).pack(pady=5)

    current_question = get_question()
    tkinter.Label(wind0w, text=current_question, font=("Arial", 14)).pack(pady=20)

    x = get_answer()
    order = list(range(4))
    random.shuffle(order)  # Antworten mischen

    # Antwort-Buttons erzeugen
    for idx in order:
        ans = x[idx]
        is_correct = (idx == 0)  # Nur Index 0 ist korrekt
        tkinter.Button(
            wind0w,
            text=ans,
            width=30,
            command=lambda c=is_correct: check_answer(c, start_time)
        ).pack(pady=5)

# Endscreen mit Score
def show_scoreboard(nTime):
    clear_window()
    add_to_score_board(nTime)
    tkinter.Button(wind0w, text="Scoreboard anzeigen", command=lambda: (save_score(nTime), load_score_board())).pack(pady=10)

# Scoreboard laden und anzeigen
def load_score_board():
    clear_window()
    try:
        with open("C:/Users/User/Documents/Studium/Python-Übungen/Quiz/score_board.txt", "r", encoding="utf-8") as file:
            zeilen = file.readlines()

        eintraege = []
        for zeile in zeilen:
            if "|" in zeile:
                parts = zeile.strip().split("|")
                if len(parts) == 4:
                    name = parts[0].strip()
                    try:
                        score_wert = float(parts[3])   # jetzt float statt int
                        eintraege.append((name, score_wert))
                    except ValueError:
                        continue


        # Sortieren nach Score
        eintraege.sort(key=lambda x: x[1], reverse=True)

        tkinter.Label(wind0w, text="Scoreboard", font=("Arial", 18)).pack(pady=10)
        for name, score_wert in eintraege:
            tkinter.Label(wind0w, text=f"{name} | Score: {score_wert}", font=("Arial", 14)).pack()

    except FileNotFoundError:
        tkinter.Label(wind0w, text="Keine Scoreboard-Datei gefunden.", font=("Arial", 14)).pack(pady=10)

# Score speichern
def save_score(nTime):
    name = user_name.get()
    if name.strip():
        with open("C:/Users/User/Documents/Studium/Python-Übungen/Quiz/score_board.txt", "a", encoding="utf-8") as file:
            file.write(f"{name}|{score}|{nTime:.2f}|{score/nTime:.2f}\n")


# Eingabe für Namen + Score speichern
def add_to_score_board(nTime):
    global user_name
    tkinter.Label(wind0w, text="Wer spielt?", font=("Arial", 16)).pack(pady=10)
    user_name = tkinter.Entry(wind0w)
    user_name.pack(pady=5)
    tkinter.Label(wind0w, text=f"Dein Score: {score}", font=("Arial", 16)).pack(pady=10)

    # Button 1: Speichern + zurück ins Menü
    tkinter.Button(wind0w, text="Zurück zum Menü", command=lambda: (save_score(nTime), show_menu())).pack(pady=10)

show_menu()
wind0w.mainloop()
