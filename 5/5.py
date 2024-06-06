import sqlite3
from tkinter import *
from tkinter import ttk


def on_cell_select(event):
    selected_cell = event.widget
    row, col = int(selected_cell.grid_info()["row"]), int(selected_cell.grid_info()["column"])

    selected_word = word_list[row][col]
    translation = word_list[row][-1]

    label_translation.config(text=f"{selected_word} - {translation}")


main = Tk()
main.geometry("1200x850")
main.title("Бондар Олексій, прикладна лінгвістика")

tabs = ttk.Notebook(main)
tab1 = ttk.Frame(tabs, width=1200, height=800)
tab2 = ttk.Frame(tabs, width=1200, height=800)
tabs.add(tab1, text="Словник")
tabs.add(tab2, text="Про автора")
tabs.grid()

cb_categories = ttk.Combobox(tab1)
cb_categories.configure(font="Colibri, 11", values=["food", "color", "clothes", "transport", "jobs"])
cb_categories.place(relx=0.5, rely=0)

label_translation = Label(tab1, font=("Arial", 12), text="")
label_translation.place(relx=0.75, rely=0.05, anchor=W)

conn = sqlite3.connect(r"dictionary.db")
curs = conn.cursor()
curs.execute("SELECT * from vocab Order by german")
word_list = []

for i in range(50):
    word_list.append(curs.fetchone())
    for j in range(8):
        e = Entry(tab1, width=11)
        e.insert(0, word_list[i][j])
        e.grid(row=i, column=j)
        e.bind("<Button-1>", on_cell_select)

y_scroll = Scrollbar(tab1, orient=VERTICAL)
y_scroll.grid(row=0, column=8, rowspan=50, sticky=N + S)
x_scroll = Scrollbar(tab1, orient=HORIZONTAL)
x_scroll.grid(row=50, column=0, columnspan=8, sticky=E + W)

canvas = Canvas(tab1, yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
canvas.grid(row=0, column=0, rowspan=50, columnspan=8, sticky=N + E + S + W)

y_scroll.config(command=canvas.yview)
x_scroll.config(command=canvas.xview)

table_frame = Frame(canvas)
canvas.create_window((0, 0), window=table_frame, anchor="nw")

for i in range(50):
    for j in range(8):
        e = Entry(table_frame, width=11)
        e.insert(0, word_list[i][j])
        e.grid(row=i, column=j)
        e.bind("<Button-1>", on_cell_select)

table_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

label_name = Label(tab2, font=("Arial", 16, "bold"),
                   text="Роботу виконав студент 4 курсу "

                        "спеціальності 'Прикладна (комп'ютерна) лінгвістика та англійська мова' "

                        "Бондар Олексій Олегович",
                   wraplength=300, justify="center")

label_name.place(relx=0.5, rely=0.5, anchor=CENTER)

main.mainloop()
