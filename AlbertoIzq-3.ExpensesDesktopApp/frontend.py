from tkinter import *
import backend

def view_command(): # Wrapper function
    list1.delete(0, END) # Firstly you have to delete the list
    for row in backend.view():
        list1.insert(END, row) # Every new row is inserted at the end of the list box

def search_command():
    list1.delete(0, END)
    for row in backend.search(year_text.get(), month_text.get(), day_text.get(), category_text.get(), value_text.get(), concept_text.get()):
        list1.insert(END, row) # Every new row is inserted at the end of the list box

def add_command():
    backend.insert(year_text.get(), month_text.get(), day_text.get(), category_text.get(), value_text.get(), concept_text.get())
    list1.delete(0, END)
    list1.insert(END, (year_text.get(), month_text.get(), day_text.get(), category_text.get(), value_text.get(), concept_text.get()))



window = Tk()

window.title("Expenses manager")

l1 = Label(window, text = "Year")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Month")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Day")
l3.grid(row = 0, column = 4)

l4 = Label(window, text = "Category")
l4.grid(row = 0, column = 6)

l5 = Label(window, text = "Value [€]")
l5.grid(row = 0, column = 8)

l6 = Label(window, text = "Concept")
l6.grid(row = 1, column = 0)


year_text = StringVar()
e1 = Entry(window, textvariable = year_text, width = 4)
e1.grid(row = 0, column = 1)

month_text = StringVar()
e2 = Entry(window, textvariable = month_text, width = 2)
e2.grid(row = 0, column = 3)

day_text = StringVar()
e3 = Entry(window, textvariable = day_text, width = 2)
e3.grid(row = 0, column = 5)

category_text = StringVar()
e3 = Entry(window, textvariable = category_text)
e3.grid(row = 0, column = 7)

value_text = StringVar()
e4 = Entry(window, textvariable = value_text, width = 15)
e4.grid(row = 0, column = 9)

concept_text = StringVar()
e5 = Entry(window, textvariable = concept_text, width = 76)
e5.grid(row = 1, column = 1, columnspan = 9)


list1 = Listbox(window, height = 6, width = 60)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 8)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 8, rowspan = 6)


b1 = Button(window, text = "View All", width = 12, command = view_command)
b1.grid(row = 2, column = 9)

b2 = Button(window, text = "Search entry", width = 12, command = search_command)
b2.grid(row = 3, column = 9)

b3 = Button(window, text = "Add entry", width = 12, command = add_command)
b3.grid(row = 4, column = 9)

b4 = Button(window, text = "Update selected", width = 12)
b4.grid(row = 5, column = 9)

b5 = Button(window, text = "Delete selected", width = 12)
b5.grid(row = 6, column = 9)

b6 = Button(window, text = "Close", width = 12)
b6.grid(row = 7, column = 9)

window.mainloop()