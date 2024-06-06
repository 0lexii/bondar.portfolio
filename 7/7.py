import tkinter as tk
from tkinter import messagebox
import random

gehen_forms = {
    "Інфінітив": "gehen",
    "Перша особа однини": "ich gehe",
    "Друга особа однини": "du gehst",
    "Третя особа однини": "er/sie/es geht",
    "Третя особа множини": "sie gehen"
}


def generate_question():
    correct_form = random.choice(list(gehen_forms.keys()))
    correct_answer = gehen_forms[correct_form]

    distractors = []
    while len(distractors) < 3:
        distractor = random.choice(list(gehen_forms.values()))
        if distractor != correct_answer and distractor not in distractors:
            distractors.append(distractor)

    options = [correct_answer] + distractors
    random.shuffle(options)

    question_text = f"Поставте слово 'gehen' у {correct_form.lower()}"

    return question_text, options, correct_answer


def check_answer():
    user_answer = var.get()
    if user_answer == correct_answer:
        messagebox.showinfo("Результат", "Правильно!")
    else:
        messagebox.showinfo("Результат", f"Ні, правильна відповідь: '{correct_answer}'")


root = tk.Tk()
root.title("Бондар Олексій")

frame1 = tk.Frame(root)
frame1.pack(padx=20, pady=20)

label1 = tk.Label(frame1, text="Навчальна інформація про граматику німецької мови:")
label1.pack()

text_info = """
Німецька мова має складну граматику,
але знання її правил допоможе легше вивчити мову.
"""

label_info = tk.Label(frame1, text=text_info)
label_info.pack()

frame2 = tk.Frame(root)
frame2.pack(padx=20, pady=20)

label2 = tk.Label(frame2, text="Тестове запитання:")
label2.pack()

question_text, options, correct_answer = generate_question()

question_label = tk.Label(frame2, text=question_text)
question_label.pack()

var = tk.StringVar()
var.set(None)

for option in options:
    radio = tk.Radiobutton(frame2, text=option, variable=var, value=option)
    radio.pack(anchor="w")

check_button = tk.Button(frame2, text="Відповісти", command=check_answer)
check_button.pack()

root.mainloop()
