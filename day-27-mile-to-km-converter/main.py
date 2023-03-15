from tkinter import *

FONT = ("Arial", 14, "normal")


def calculate():
    miles = float(miles_input.get())
    km_value.config(text=str(miles * 1.609))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(row=1, column=0)

km_value = Label(text="0", font=FONT)
km_value.grid(row=1, column=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
