from tkinter import *
from tkinter import ttk
import sqlite3

main = Tk()
main.geometry("600x600")
main.title("Бондар Олексій, прикладна лінгвістика")

label_result = Label(main, font=("Arial", 16), bg="lightgray", text="")
label_result.grid(row=15, column=1, pady=10)

conn = sqlite3.connect(r"pol_lab02.s3db")
curs = conn.cursor()
curs.execute("SELECT plD FROM tnoun WHERE plD LIKE 'D%'")
result = curs.fetchone()[0]
label_result.configure(text=result)

for i in range(13):
    label_num = Label(main, text=str(i + 1), font=('Colibri', 11), bd=1, relief="solid")
    label_num.grid(row=i, column=0, padx=3, pady=3)
    for j in range(3):
        e = Entry(main, width=10, font=('Colibri', 11), bd=1, relief="solid")
        e.grid(row=i, column=j + 1, padx=3, pady=3)


def get_n_nouns():
    conn = sqlite3.connect(r"pol_lab02.s3db")
    curs = conn.cursor()
    curs.execute("SELECT id, sgN, plD from tnoun LIMIT 13")
    noun_list1 = []
    for i in range(13):
        noun_list1.append(curs.fetchone())
        for j in range(3):
            e = Entry(main, width=10, font=('Colibri', 11), bd=1, relief="solid")
            e.insert(0, noun_list1[i][j])
            e.grid(row=i, column=j + 1, padx=3, pady=3)


cb_nouns = ttk.Combobox(main, font=("Arial", 11), state="readonly")
cb_nouns.grid(row=14, column=2, padx=10, pady=10)


def combobox():
    conn = sqlite3.connect(r"pol_lab02.s3db")
    curs = conn.cursor()
    curs.execute("SELECT sgN from tnoun WHERE sgN LIKE 'D%'")
    noun_list = curs.fetchall()
    cb_nouns.configure(values=noun_list)


combobox()

button = Button(main, text="Велика кнопка", font=("Colibri", 11), command=lambda: [get_n_nouns(), combobox()])
button.grid(row=14, column=1, pady=10)
main.mainloop()
