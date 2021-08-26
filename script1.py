from tkinter import *

window = Tk()


def convert():
    gram = float(t1_value.get()) * 1000
    pound = float(t1_value.get()) * 2.20462
    ounces = float(t1_value.get()) * 35.274

    l2.delete('1.0', END)
    # l2.delete("1.0", END)  # Deletes the content of the Text box from start to END
    l2.insert(END, gram)

    l3.delete('1.0', END)
    l3.insert(END, pound)

    l4.delete('1.0', END)
    l4.insert(END, ounces)


l1 = Label(window, text='Kg')
l1.grid(row=0, column=0)

t1_value = StringVar()
t1 = Entry(window, textvariable=t1_value)
t1.grid(row=0, column=1)

b1 = Button(window, text='Convert', command=convert)
b1.grid(row=0, column=2)

l2 = Text(window, height=1, width=20)
l2.grid(row=1, column=0)

l3 = Text(window, height=1, width=20)
l3.grid(row=1, column=1)

l4 = Text(window, height=1, width=20)
l4.grid(row=1, column=2)

window.mainloop()  # This prevents the window from auto closing
