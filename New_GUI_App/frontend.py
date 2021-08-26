from tkinter import *
import backend

window = Tk()  # This creates a window object
window.wm_title('BookStore') #Gives title to the window

def get_selected_row(event):
    try:
        global selected_tuple
        index = list.curselection()[0]
        selected_tuple = list.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list.delete(0, END)
    data = backend.view()
    if len(data) > 0:
        for row in data:
            list.insert(END, row)
    else:
        list.insert(END, 'No data available!!')


def search_command():
    list.delete(0, END)
    data = backend.search(e1_title.get(), e2_author.get(),
                          e3_year.get(), e4_isbn.get())
    if len(data) > 0:
        for row in data:
            list.insert(END, row)
    else:
        list.insert(END, 'No data found!!')


def add_command():
    backend.insert(e1_title.get(), e2_author.get(),
                   e3_year.get(), e4_isbn.get())
    list.delete(0, END)
    data = backend.view()
    if len(data) > 0:
        for row in data:
            list.insert(END, row)
    else:
        list.insert(END, 'No data available!!')


def delete_command():
    list.delete(0, END)
    backend.delete(selected_tuple[0])
    data = backend.view()
    if len(data) > 0:
        for row in data:
            list.insert(END, row)
    else:
        list.insert(END, 'No data found!!')


def update_command():
    list.delete(0, END)
    backend.update(selected_tuple[0], e1_title.get(),
                   e2_author.get(), e3_year.get(), e4_isbn.get())
    data = backend.view()
    if len(data) > 0:
        for row in data:
            list.insert(END, row)
    else:
        list.insert(END, 'No data found!!')


l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

e1_title = StringVar()
e1 = Entry(window, textvariable=e1_title)  # Entry: It provides Textbox
e1.grid(row=0, column=1)

e2_author = StringVar()
e2 = Entry(window, textvariable=e2_author)  # Entry: It provides Textbox
e2.grid(row=0, column=3)

e3_year = StringVar()
e3 = Entry(window, textvariable=e3_year)  # Entry: It provides Textbox
e3.grid(row=1, column=1)

e4_isbn = StringVar()
e4 = Entry(window, textvariable=e4_isbn)  # Entry: It provides Textbox
e4.grid(row=1, column=3)

list = Listbox(window, height=6, width=35)
list.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list.configure(yscrollcommand=sb1.set)
sb1.configure(command=list.yview)

list.bind('<<ListboxSelect>>', get_selected_row)

# Button: It provides Button
viewBTN = Button(window, text="View All", width=12, command=view_command)
# Grid: Provides proper alignment on the basis of Row and Column passed
viewBTN.grid(row=2, column=3)

searchBTN = Button(window, text="Search", width=12, command=search_command)
searchBTN.grid(row=3, column=3)

addBTN = Button(window, text="Add", width=12, command=add_command)
addBTN.grid(row=4, column=3)

updateBTN = Button(window, text="Update", width=12, command=update_command)
updateBTN.grid(row=5, column=3)

deleteBTN = Button(window, text="Delete", width=12, command=delete_command)
deleteBTN.grid(row=6, column=3)

closeBTN = Button(window, text="Close", width=12, command=window.destroy)
closeBTN.grid(row=7, column=3)


window.mainloop()  # This prevents the window from auto closing
