import tkinter as tk
import random
import time

def move_button():
    global counter
    counter += 1
    new_x = random.randint(0, 650)
    new_y = random.randint(0, 650)
    button.place(x=new_x, y=new_y)

    needed_time = time.time() - start_time
    lab.config(text=f"Time: {needed_time:.2f} s    Buttons clicked: {counter}    Buttons per Time: {counter/needed_time:.2f}")

start_time = time.time()
counter = 0
root = tk.Tk()
root.title("Click the red button")
root.geometry("900x900")
button = tk.Button(root, text="     ", bg="red", command=move_button)
button.place(x=100, y=100)
lab = tk.Label(root, text="Time: 0.00 s    Buttons clicked: 0    Buttons per Time: 0.00")
lab.pack()

root.mainloop()



