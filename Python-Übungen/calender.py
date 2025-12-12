class event():
    def __init__(self, date, name, place, reminder, reminder_time):
        with open("schedule.txt", "a", encoding="utf-8") as f:
            f.write(f"{date}, {name}, {place}, {reminder}, {reminder_time}\n")
        
        

        
        
        
        
        
        
        # Datei im Lesemodus öffnen
        with open("schedule.txt", "r", encoding="utf-8") as f:
            for zeile in f:
                # Jede Zeile wird nacheinander eingelesen
                print(zeile.strip())  # .strip() entfernt \n am Ende

        