from tkinter import *

window = Tk()  # This creates a window object


def km_to_meters():
    meter = int(e1_value.get()) * 1000
    t1.insert(END, meter)


e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)  # Entry: It provides Textbox
e1.grid(row=0, column=0)

# Button: It provides Button
b1 = Button(window, text="Execute", command=km_to_meters)
# Grid: Provides proper alignment on the basis of Row and Column passed
b1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)  # Text: It provides Textarea
t1.grid(row=0, column=2)

window.mainloop()  # This prevents the window from auto closing
