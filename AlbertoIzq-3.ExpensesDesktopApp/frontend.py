from tkinter import *
import backend

MONTH = list(range(1, 13))
MONTH.insert(0, "")

DAY = list(range(1, 32))
DAY.insert(0, "")

CATEGORY = [
"",
"Restaurant",
"Bar",
"Supermarket",
"Transport",
"Other"
]

def get_selected_row(event):
    try:
        global selected_tuple # You create a global variable that can be used outside of the function
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)

        # Update entry fields with selected row in listbox
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        month_text.set(selected_tuple[2])
        day_text.set(selected_tuple[3])
        category_text.set(selected_tuple[4])
        e5.delete(0, END)
        e5.insert(END, selected_tuple[5])
        e6.delete(0, END)
        e6.insert(END, selected_tuple[6])
    except IndexError:
        pass

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
    view_command() # To see how the added entry was in fact added

def delete_command():
    backend.delete(selected_tuple[0])
    view_command() # To see how the deleted selection was in fact deleted

def update_command():
    backend.update(selected_tuple[0], year_text.get(), month_text.get(), day_text.get(), category_text.get(), value_text.get(), concept_text.get())
    view_command() # To see how the deleted selection was in fact deleted

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
o1 = OptionMenu(window, month_text, *MONTH)
o1.configure(width = 2)
o1.grid(row = 0, column = 3)

day_text = StringVar()
o2 = OptionMenu(window, day_text, *DAY)
o2.configure(width = 2)
o2.grid(row = 0, column = 5)

category_text = StringVar()
o3 = OptionMenu(window, category_text, *CATEGORY)
o3.configure(width = 12)
o3.grid(row = 0, column = 7)

value_text = StringVar()
e5 = Entry(window, textvariable = value_text, width = 15)
e5.grid(row = 0, column = 9)

concept_text = StringVar()
e6 = Entry(window, textvariable = concept_text, width = 84)
e6.grid(row = 1, column = 1, columnspan = 9)


list1 = Listbox(window, height = 6, width = 60)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 8)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 8, rowspan = 6)

list1.bind('<<ListboxSelect>>', get_selected_row)


b1 = Button(window, text = "View All", width = 12, command = view_command)
b1.grid(row = 2, column = 9)

b2 = Button(window, text = "Search entry", width = 12, command = search_command)
b2.grid(row = 3, column = 9)

b3 = Button(window, text = "Add entry", width = 12, command = add_command)
b3.grid(row = 4, column = 9)

b4 = Button(window, text = "Update selected", width = 12, command = update_command)
b4.grid(row = 5, column = 9)

b5 = Button(window, text = "Delete selected", width = 12, command = delete_command)
b5.grid(row = 6, column = 9)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 9)

window.mainloop()