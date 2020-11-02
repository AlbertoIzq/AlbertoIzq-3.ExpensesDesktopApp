from tkinter import *
from backend import Database

database = Database("expenses.db") # database object is an instance of Database class

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

class Window(object):
    """Class to store window object"""

    def __init__(self, window):

        self.window = window
        self.window.title("Expenses manager")

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

        self.year_text = StringVar()
        self.e1 = Entry(window, textvariable = self.year_text, width = 4)
        self.e1.grid(row = 0, column = 1)

        self.month_text = StringVar()
        self.o1 = OptionMenu(window, self.month_text, *MONTH)
        self.o1.configure(width = 2)
        self.o1.grid(row = 0, column = 3)

        self.day_text = StringVar()
        self.o2 = OptionMenu(window, self.day_text, *DAY)
        self.o2.configure(width = 2)
        self.o2.grid(row = 0, column = 5)

        self.category_text = StringVar()
        self.o3 = OptionMenu(window, self.category_text, *CATEGORY)
        self.o3.configure(width = 12)
        self.o3.grid(row = 0, column = 7)

        self.value_text = StringVar()
        self.e5 = Entry(window, textvariable = self.value_text, width = 15)
        self.e5.grid(row = 0, column = 9)

        self.concept_text = StringVar()
        self.e6 = Entry(window, textvariable = self.concept_text, width = 84)
        self.e6.grid(row = 1, column = 1, columnspan = 9)

        self.list1 = Listbox(window, height = 6, width = 60)
        self.list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 8)

        sb1 = Scrollbar(window)
        sb1.grid(row = 2, column = 8, rowspan = 6)
 
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        b1 = Button(window, text = "View All", width = 12, command = self.view_command)
        b1.grid(row = 2, column = 9)

        b2 = Button(window, text = "Search entry", width = 12, command = self.search_command)
        b2.grid(row = 3, column = 9)

        b3 = Button(window, text = "Add entry", width = 12, command = self.add_command)
        b3.grid(row = 4, column = 9)

        b4 = Button(window, text = "Update selected", width = 12, command = self.update_command)
        b4.grid(row = 5, column = 9)

        b5 = Button(window, text = "Delete selected", width = 12, command = self.delete_command)
        b5.grid(row = 6, column = 9)

        b6 = Button(window, text = "Close", width = 12, command = window.destroy)
        b6.grid(row = 7, column = 9)

    def get_selected_row(self, event):
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)

            # Update entry fields with selected row in listbox
            self.e1.delete(0, END)
            self.e1.insert(END, self.selected_tuple[1])
            self.month_text.set(self.selected_tuple[2])
            self.day_text.set(self.selected_tuple[3])
            self.category_text.set(self.selected_tuple[4])
            self.e5.delete(0, END)
            self.e5.insert(END, self.selected_tuple[5])
            self.e6.delete(0, END)
            self.e6.insert(END, self.selected_tuple[6])
        except IndexError:
            pass

    def view_command(self): # Wrapper function
        self.list1.delete(0, END) # Firstly you have to delete the list
        for row in database.view():
            self.list1.insert(END, row) # Every new row is inserted at the end of the list box

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.year_text.get(), self.month_text.get(), self.day_text.get(), self.category_text.get(),
                                   self.value_text.get(), self.concept_text.get()):
            self.list1.insert(END, row) # Every new row is inserted at the end of the list box

    def add_command(self):
        database.insert(self.year_text.get(), self.month_text.get(), self.day_text.get(), self.category_text.get(), self.value_text.get(),
                        self.concept_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.year_text.get(), self.month_text.get(), self.day_text.get(), self.category_text.get(),
                                self.value_text.get(), self.concept_text.get()))
        self.view_command() # To see how the added entry was in fact added

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.view_command() # To see how the deleted entry was in fact deleted

    def update_command(self):
        database.update(self.selected_tuple[0], self.year_text.get(), self.month_text.get(), self.day_text.get(), self.category_text.get(),
                        self.value_text.get(), self.concept_text.get())
        self.view_command() # To see how the updated entry was in fact updated

window = Tk()
Window(window)
window.mainloop()