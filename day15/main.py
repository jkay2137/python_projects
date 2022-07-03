# Miles to Km Converter Program 
from tkinter import *

# Constant
KM = 1.6


# Functions
def calculate():
    miles = float(input.get())
    result = miles * KM
    result_label.config(text=result)


# Window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(300, 150)
window.config(padx=20, pady=20)


# User input
input = Entry()
input.grid(row=0, column=1)
input.config(width=10)


# Labels
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to", font=("Arial", 12))
equal_label.grid(row=1, column=0)

result_label = Label(text="0", font=("Arial", 12))
result_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(row=1, column=2)


# Buttons
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)


window.mainloop()