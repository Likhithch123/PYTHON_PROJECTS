
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repitition = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer",fg=RED)
    canvas.itemconfig(timer_text, text="00:00")
    tick_mark_label.config(text="")
    global repitition
    repitition=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

from math import floor
from tkinter import *
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

def count_down(count):
    global repitition
    global timer
    count_min = floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"


    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)

    else:
        start_button_clicked()
        mark = ""
        work_sessions=floor(repitition/2)
        for _ in range(work_sessions):
            mark += "✔"
        tick_mark_label.config(text=mark)

timer_label=Label(text="Timer",font=(FONT_NAME, 35, "bold"),fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(row=0,column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="../python-projects/PROJECT-28/tomato.png")
canvas.create_image(100,105,image=tomato_image)
timer_text=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

# count_down(5)

def start_button_clicked():
    global repitition
    repitition+=1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repitition %8 == 0:
        timer_label.config(text="Long Break",fg=RED)
        count_down(long_break_sec)    
    elif repitition%2 == 0:
        timer_label.config(text="Short Break",fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work",fg=GREEN)
        count_down(work_sec)

    # count_down(5 * 60)

start_button=Button(text="Start",highlightthickness=0, command=start_button_clicked)


start_button.grid(row=2,column=0)
reset_button=Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)
tick_mark_label=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME, 15, "bold"))
tick_mark_label.grid(row=3,column=1)
window.mainloop()