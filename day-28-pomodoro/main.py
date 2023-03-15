from math import floor
from os import path
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
DIRNAME = path.dirname(__file__)
CHECK_EMOJI = "✔️"

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global reps
    if timer:
        window.after_cancel(timer)
        reps = 0
        interval_checks.config(text="")
        label.config(text="Timer", fg=GREEN)
        canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps == 8:
        label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        if reps == 8:
            label.config(text="Done!", fg=GREEN)
            if timer:
                window.after_cancel(timer)
        else:
            start_timer()
            marks = ""
            for _ in range(floor(reps / 2)):
                marks += CHECK_EMOJI
            interval_checks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
label.grid(row=0, column=1)

tomato_img = PhotoImage(file=f"{DIRNAME}/tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    103, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

start_button = Button(
    text="Start", bg="white", highlightthickness=0, command=start_timer
)
start_button.grid(row=2, column=0)

reset_button = Button(
    text="Reset", bg="white", highlightthickness=0, command=reset_timer
)
reset_button.grid(row=2, column=2)

interval_checks = Label(text="", fg=GREEN, background=YELLOW, font=(FONT_NAME, 24))
interval_checks.grid(row=3, column=1)

window.mainloop()
