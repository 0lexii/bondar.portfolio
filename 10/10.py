import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import PhotoImage, END

test_questions = {
    "Das Präsens": [
        ("Оберіть дієслово у формі Präsens", ["spiele", "spielte", "gespielt", "spielen"], 0, "single"),
        ("Оберіть дієслово у формі Präsens, 1 особи однини", ["spiele", "spielst", "spielt", "spielen"], 0,
         "single"),
        ("Оберіть дієслова НЕ у формі Präsens", ["spiele", "spielte", "gespielt", "spielen", "gesehen"], [1, 2, 4],
         "multiple"),
        ("Оберіть дієслова НЕ у формі Präsens, 2 особи множини", ["spielt", "spieltet", "spielten", "gespielt"],
         [1, 2, 3], "multiple"),
        ("Вставте пропущене слово: Er ___ zum Fußballtraining", ["geht", "ging", "gegangen", "gehts"], 0, "single"),
        ("Вставте пропущене слово: Das ___ Oleg!", ["ist", "war", "wird", "sein"], 0, "single"),
        ("Впишіть пропущене слово: Ich ___ (грати) jeden Tag.", "", "spiele", "text"),
        ("Впишіть пропущене слово: Sie ___ (бачити) den Film.", "", "sieht", "text"),
        ("Перекладіть речення: Я граю у футбол.", "", "Ich spiele Fußball.", "translation"),
        ("Перекладіть речення: Вона дивиться фільм.", "", "Sie sieht den Film.", "translation"),
    ],
    "Das Präteritum": [
        ("Оберіть дієслово у формі Präteritum", ["spielte", "spielen", "gespielt", "spiele"], 0, "single"),
        ("Оберіть дієслово у формі Präteritum, 1 особи однини", ["spielte", "spieltest", "spielten", "spieltet"], 0,
         "single"),
        ("Оберіть дієслова НЕ у формі Präteritum", ["spielte", "spielen", "gespielt", "spiele", "gesehen"],
         [1, 2, 4],
         "multiple"),
        ("Оберіть дієслова НЕ у формі Präteritum, 2 особи множини", ["spielte", "spielten", "spielen", "gespielt"],
         [1, 2, 3], "multiple"),
        ("Вставте пропущене слово: Er ___ gestern Fußball.", ["spielte", "spielt", "spielen", "gespielt"], 0,
         "single"),
        ("Вставте пропущене слово: Das ___ gestern passiert.", ["ist", "war", "wird", "sein"], 1, "single"),
        ("Впишіть пропущене слово: Ich ___ (читати) ein Buch gestern.", "", "las", "text"),
        ("Впишіть пропущене слово: Sie ___ (піти) на роботу.", "", "ging", "text"),
        ("Перекладіть речення: Ми грали у футбол вчора.", "", "Wir spielten gestern Fußball.", "translation"),
        ("Перекладіть речення: Вони читали цю книгу.", "", "Sie lasen dieses Buch.", "translation")
    ],
    "Perfekt": [
        ("Оберіть дієслово у формі Perfekt", ["gespielt", "spiele", "spielte", "spielen"], 0, "single"),
        ("Оберіть дієслово у формі Perfekt, 1 особи однини",
         ["habe gespielt", "hast gespielt", "hat gespielt", "haben gespielt"], 0,
         "single"),
        ("Оберіть дієслова НЕ у формі Perfekt", ["gespielt", "spiele", "spielte", "spielen", "gesehen"], [1, 2, 4],
         "multiple"),
        ("Оберіть дієслова НЕ у формі Perfekt, 2 особи множини", ["gespielt", "spielen", "gesehen", "spiele"],
         [1, 2, 3], "multiple"),
        ("Вставте пропущене слово: Ich ___ schon im Urlaub.", ["bin gewesen", "war", "bin", "bin geworden"], 0,
         "single"),
        ("Вставте пропущене слово: Sie ___ das Buch gelesen.", ["hat", "hatte", "habe", "hatten"], 0, "single"),
        ("Впишіть пропущене слово: Ich ___ (подивитися) цей фільм.", "", "habe gesehen", "text"),
        ("Впишіть пропущене слово: Wir ___ (зробити) домашнє завдання.", "", "haben gemacht", "text"),
        ("Перекладіть речення: Я вже бачив цей фільм.", "", "Ich habe diesen Film schon gesehen.", "translation"),
        ("Перекладіть речення: Вони вже зробили свою роботу.", "", "Sie haben ihre Arbeit schon gemacht.",
         "translation")
    ],
    "Plusquamperfekt": [
        ("Оберіть дієслово у формі Plusquamperfekt", ["gespielt", "spielte", "habe gespielt", "hatte gespielt"], 3,
         "single"),
        ("Оберіть дієслово у формі Plusquamperfekt, 1 особи однини",
         ["habe gespielt", "hattest gespielt", "hatte gespielt", "hatten gespielt"], 0,
         "single"),
        ("Оберіть дієслова НЕ у формі Plusquamperfekt",
         ["gespielt", "spielte", "hatte gespielt", "spielen", "gesehen"], [1, 2, 4],
         "multiple"),
        ("Оберіть дієслова НЕ у формі Plusquamperfekt, 2 особи множини",
         ["hatte gespielt", "spielte", "gesehen", "spielen"], [1, 2, 3], "multiple"),
        ("Вставте пропущене слово: Sie ___ schon im Kino gewesen.", ["waren", "war", "haben", "hatten"], 0,
         "single"),
        ("Вставте пропущене слово: Ich ___ bereits gegessen.", ["hatte", "war", "bin", "haben"], 0, "single"),
        ("Впишіть пропущене слово: Wir ___ (почути) die Nachrichten.", "", "hatten gehört", "text"),
        ("Впишіть пропущене слово: Ihr ___ (повернутися) nach Hause.", "", "waret nach Hause gekommen", "text"),
        ("Перекладіть речення: Вони вже бачили цей фільм.", "", "Sie hatten diesen Film schon gesehen.",
         "translation"),
        ("Перекладіть речення: Я вже чув цю новину.", "", "Ich hatte diese Nachricht schon gehört.", "translation")
    ],
    "Futur I": [
        ("Оберіть дієслово у формі Futur I", ["werde spielen", "spielst", "wirst spielen", "spielen"], 0, "single"),
        ("Оберіть дієслово у формі Futur I, 1 особи однини",
         ["werde spielen", "wirst spielen", "wird spielen", "spielen"], 0,
         "single"),
        ("Оберіть дієслова НЕ у формі Futur I",
         ["werde spielen", "werden spielen", "wird spielen", "spielt", "gespielt"], [2, 3],
         "multiple"),
        ("Оберіть дієслова НЕ у формі Futur I, 2 особи множини",
         ["werdet spielen", "werdet", "werdet spiele", "werden spielen"], [1, 2, 3], "multiple"),
        ("Вставте пропущене слово: Morgen ___ wir ins Kino gehen.", ["werden", "wird", "wirst", "werdet"], 0,
         "single"),
        ("Вставте пропущене слово: Du ___ es sicherlich schaffen.", ["wirst", "werdest", "wird", "werde"], 0,
         "single"),
        ("Впишіть пропущене слово: Ich ___ (вивчати) Deutsch lernen.", "", "werde Deutsch lernen", "text"),
        ("Впишіть пропущене слово: Ihr ___ (мандрувати) nach Deutschland.", "", "werdet nach Deutschland reisen",
         "text"),
        ("Перекладіть речення: Ми будемо грати у футбол.", "", "Wir werden Fußball spielen.", "translation"),
        ("Перекладіть речення: Ви будете вивчати німецьку мову.", "", "Ihr werdet Deutsch lernen.", "translation")
    ],
    "Futur II": [
        ("Оберіть дієслово у формі Futur II",
         ["werde gespielt haben", "wirst gespielt haben", "werden gespielt haben", "spielen"], 0, "single"),
        ("Оберіть дієслово у формі Futur II, 1 особи однини",
         ["werde gespielt haben", "wirst gespielt haben", "wird gespielt haben", "gespielt haben"], 0,
         "single"),
        ("Оберіть дієслова НЕ у формі Futur II",
         ["werde gespielt haben", "wirst gespielt haben", "werden gespielt haben", "spielen", "gespielt haben"],
         [3, 4],
         "multiple"),
        ("Оберіть дієслова НЕ у формі Futur II, 2 особи множини",
         ["werdet gespielt haben", "werdet spielen", "werdet", "gespielt haben"], [1, 2, 3], "multiple"),
        ("Вставте пропущене слово: Morgen ___ sie das Buch schon gelesen haben.",
         ["werden", "wird", "wirst", "werdet"], 0, "single"),
        ("Вставте пропущене слово: Du ___ alles erreicht haben.", ["wirst", "werdest", "wird", "werde"], 0,
         "single"),
        ("Впишіть пропущене слово: Ich ___ (вивчати) Deutsch gelernt haben.", "", "werde Deutsch gelernt haben",
         "text"),
        ("Впишіть пропущене слово: Ihr ___ (мандрувати) nach Deutschland gereist sein.", "",
         "werdet nach Deutschland gereist sein", "text"),
        ("Перекладіть речення: Ми будемо грати у футбол.", "", "Wir werden Fußball spielen.", "translation"),
        ("Перекладіть речення: Ви будете вивчати німецьку мову.", "", "Ihr werdet Deutsch lernen.", "translation")
    ]
}


def create_main_window():
    ctk.set_appearance_mode("Light")  
    ctk.set_default_color_theme("blue")  

    root = ctk.CTk()  
    root.title("Deutschify")
    root.geometry("400x500")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    tabview = ctk.CTkTabview(master=frame)
    tabview.pack(fill="both", expand=True)

    login_tab = tabview.add("Увійти")
    register_tab = tabview.add("Реєстрація")

    create_login_ui(login_tab, root)
    create_register_ui(register_tab)

    return root


def create_login_ui(parent, root):
    login_label = ctk.CTkLabel(master=parent, text="Вхід", font=ctk.CTkFont(size=24, weight="bold"))
    login_label.pack(pady=12, padx=10)

    email_entry = ctk.CTkEntry(master=parent, placeholder_text="Електронна адреса")
    email_entry.pack(pady=12, padx=10)

    password_entry = ctk.CTkEntry(master=parent, placeholder_text="Пароль", show="*")
    password_entry.pack(pady=12, padx=10)

    login_button = ctk.CTkButton(master=parent, text="Увійти",
                                 command=lambda: handle_login(email_entry, password_entry, root))
    login_button.pack(pady=12, padx=10)


def create_register_ui(parent):
    register_label = ctk.CTkLabel(master=parent, text="Реєстрація", font=ctk.CTkFont(size=24, weight="bold"))
    register_label.pack(pady=12, padx=10)

    reg_email_entry = ctk.CTkEntry(master=parent, placeholder_text="Електронна адреса")
    reg_email_entry.pack(pady=12, padx=10)

    reg_password_entry = ctk.CTkEntry(master=parent, placeholder_text="Пароль", show="*")
    reg_password_entry.pack(pady=12, padx=10)

    reg_confirm_password_entry = ctk.CTkEntry(master=parent, placeholder_text="Підтвердити пароль", show="*")
    reg_confirm_password_entry.pack(pady=12, padx=10)

    register_button = ctk.CTkButton(master=parent, text="Зареєструватись", command=lambda: print("Register clicked"))
    register_button.pack(pady=12, padx=10)

    try:
        google_image = Image.open("7123025_logo_google_g_icon.png")
        google_image = google_image.resize((20, 20), Image.Resampling.LANCZOS)
        google_icon = ImageTk.PhotoImage(google_image)

        google_button = ctk.CTkButton(master=parent, image=google_icon, text="Зареєструватись з Google",
                                      compound="left",
                                      command=lambda: print("Google Register clicked"))
        google_button.pack(pady=12, padx=10)
    except FileNotFoundError:
        print("Google icon file not found. Please check the file path.")


def handle_login(email_entry, password_entry, login_window):
    email = email_entry.get()
    password = password_entry.get()

    if email == "user@gmail.com" and password == "123123":
        messagebox.showinfo("Deutschify", "Вітаємо у Deutschify!")
        login_window.destroy()
        open_home_window()
    else:
        messagebox.showerror("Deutschify", "Неправильна електронна адреса або пароль.")


def open_home_window():
    home_window = ctk.CTk()
    home_window.title("Deutschify")

    screen_width = home_window.winfo_screenwidth()
    screen_height = home_window.winfo_screenheight()

    home_window.geometry(f"{screen_width}x{screen_height}")

    tabview = ctk.CTkTabview(master=home_window)
    tabview.pack(fill="both", expand=True)

    theory_tab = tabview.add("Теоретичний матеріал")
    practice_tab = tabview.add("Тестування")
    settings_tab = tabview.add("Налаштування")

    create_theory_ui(theory_tab)
    create_practice_ui(practice_tab)
    create_settings_ui(settings_tab)

    home_window.mainloop()


def create_theory_ui(parent):
    topics = ["Тема 1. Das Präsens", "Тема 2. Das Präteritum", "Тема 3. Perfekt", "Тема 4. Plusquamperfekt",
              "Тема 5. Futur I", "Тема 6. Futur II"]
    content = {
        "Тема 1. Das Präsens": """ 
            Теперішній час (Das Präsens) - це час, який вказує на події, що відбуваються в даний момент часу  
            або взагалі сталися. Він також використовується для вираження загальних фактів та регулярних  
            подій. У німецькій мові теперішній час утворюється за допомогою закінчення дієслова, яке змінюється  
            в залежності від особи та числа. 
 
            Наприклад: 
 
            - ich spiele (я граю) 
            - du spielst (ти граєш) 
            - er/sie/es spielt (він/вона/воно грає) 
            - wir spielen (ми граємо) 
            - ihr spielt (ви граєте) 
            - sie/Sie spielen (вони грають) 
 
            Також варто відзначити, що деякі німецькі дієслова мають неправильні форми у теперішньому часі. 
 
            КОН’ЮГАЦІЯ ТЕПЕРІШНЬОГО ЧАСУ: РЕГУЛЯРНІ ДІЄСЛОВА 
 
            """,
        "Тема 2. Das Präteritum": """ 
            Минулий час (Das Präteritum) - це час, який використовується для опису дій або подій, що відбулися в минулому.  
            Він часто використовується в письмовій мові, особливо в літературі, розповідях та описах. 
 
            Наприклад: 
 
            - ich spielte (я грав) 
            - du spieltest (ти грав) 
            - er/sie/es spielte (він/вона/воно грав) 
            - wir spielten (ми грали) 
            - ihr spieltet (ви грали) 
            - sie/Sie spielten (вони грали) 
 
            Для неправильних дієслів форми Präteritum можуть значно відрізнятися від стандартних. Ось деякі приклади: 
 
            - ich war (я був) 
            - du warst (ти був) 
            - er/sie/es war (він/вона/воно був) 
            - wir waren (ми були) 
            - ihr wart (ви були) 
            - sie/Sie waren (вони були) 
 
            - ich hatte (я мав) 
            - du hattest (ти мав) 
            - er/sie/es hatte (він/вона/воно мав) 
            - wir hatten (ми мали) 
            - ihr hattet (ви мали) 
            - sie/Sie hatten (вони мали) 
 
            Präteritum часто використовується в офіційних письмових текстах, новинах, історіях та романах. 
 
            КОН’ЮГАЦІЯ — РЕГУЛЯРНІ ДІЄСЛОВА 
 
            """,
        "Тема 3. Perfekt": """ 
        Завершений час (Perfekt) - це час, який використовується для опису дій або подій, що відбулися в минулому,  
        але мають зв'язок з теперішнім часом. Він часто використовується в розмовній мові. 
 
        Наприклад: 
 
        - ich habe gespielt (я грав) 
        - du hast gespielt (ти грав) 
        - er/sie/es hat gespielt (він/вона/воно грав) 
        - wir haben gespielt (ми грали) 
        - ihr habt gespielt (ви грали) 
        - sie/Sie haben gespielt (вони грали) 
 
        Зауважте, що для утворення Perfekt використовується допоміжне дієслово (haben або sein) та причастя минулого часу основного дієслова. 
 
        УТВОРЕННЯ PERFEKT 
 
        """,
        "Тема 4. Plusquamperfekt": """ 
        Передминулий час (Plusquamperfekt) - це час, який використовується для опису дій або подій, що відбулися до іншої події в минулому. 
 
        Наприклад: 
 
        - ich hatte gespielt (я грав) 
        - du hattest gespielt (ти грав) 
        - er/sie/es hatte gespielt (він/вона/воно грав) 
        - wir hatten gespielt (ми грали) 
        - ihr hattet gespielt (ви грали) 
        - sie/Sie hatten gespielt (вони грали) 
 
        Зауважте, що для утворення Plusquamperfekt використовується допоміжне дієслово (haben або sein) в Präteritum та причастя минулого часу основного дієслова. 
 
        УТВОРЕННЯ PLUSQUAMPERFEKT 
 
        """,
        "Тема 5. Futur I": """ 
        Майбутній час I (Futur I) - це час, який використовується для опису дій або подій, що відбудуться в майбутньому, або для вираження припущень. 
 
        Наприклад: 
 
        - ich werde spielen (я буду грати) 
        - du wirst spielen (ти будеш грати) 
        - er/sie/es wird spielen (він/вона/воно буде грати) 
        - wir werden spielen (ми будемо грати) 
        - ihr werdet spielen (ви будете грати) 
        - sie/Sie werden spielen (вони будуть грати) 
 
        Зауважте, що для утворення Futur I використовується допоміжне дієслово werden та інфінітив основного дієслова. 
 
        УТВОРЕННЯ FUTUR I 
 
        """,
        "Тема 6. Futur II": """ 
        Майбутній час II (Futur II) - це час, який використовується для опису дій або подій, які будуть завершені в майбутньому. 
 
        Наприклад: 
 
        - ich werde gespielt haben (я буду грав) 
        - du wirst gespielt haben (ти будеш грав) 
        - er/sie/es wird gespielt haben (він/вона/воно буде грав) 
        - wir werden gespielt haben (ми будемо грали) 
        - ihr werdet gespielt haben (ви будете грали) 
        - sie/Sie werden gespielt haben (вони будуть грали) 
 
        Зауважте, що для утворення Futur II використовується допоміжне дієслово werden, причастя минулого час 
 
        УТВОРЕННЯ FUTUR II 
 
        """
    }

    frame = ctk.CTkFrame(master=parent)
    frame.pack(fill="both", expand=True)

    button_frame = ctk.CTkFrame(master=frame)
    button_frame.pack(side="left", fill="y")

    content_frame = ctk.CTkFrame(master=frame)
    content_frame.pack(side="right", fill="both", expand=True)

    content_text = tk.Text(master=content_frame, wrap="word", font=("Helvetica", 12), state="disabled")
    content_text.pack(pady=20, padx=20, fill="both", expand=True)

    for topic in topics:
        button = ctk.CTkButton(master=button_frame, text=topic,
                               command=lambda t=topic: display_content(t, content, content_text))
        button.pack(pady=5, padx=5, fill="x")


def display_content(topic, content, text_widget):
    text_widget.config(state="normal")
    text_widget.delete(1.0, "end")

    text_widget.insert("insert", content[topic])

    if topic == "Тема 1. Das Präsens":
        image = PhotoImage(file="regular verbs.png")

        text_widget.image_create(END, image=image)

        text_widget.image = image

    if topic == "Тема 2. Das Präteritum":
        image = PhotoImage(file="praterium.png")

        text_widget.image_create(END, image=image)

        text_widget.image = image

    if topic == "Тема 3. Perfekt":
        image = PhotoImage(file="perfekt.png")

        text_widget.image_create(END, image=image)

        text_widget.image = image

    if topic == "Тема 4. Plusquamperfekt":
        image = PhotoImage(file="plusquamperfekt.png")

        text_widget.image_create(END, image=image)

        text_widget.image = image

    if topic == "Тема 5. Futur I":
        image = PhotoImage(file="futur1.png")

        text_widget.image_create(END, image=image)

        text_widget.image = image

    if topic == "Тема 6. Futur II":
        image = PhotoImage(file="futur2.png")

        text_widget.image_create(END, image=image)

        text_widget.image = image

    text_widget.config(state="disabled")


def create_practice_ui(parent):
    label = ctk.CTkLabel(parent, text="Оберіть тему для тестування", font=ctk.CTkFont(size=20, weight="bold"))
    label.pack(pady=20)

    test_topics = ["Das Präsens", "Das Präteritum", "Perfekt", "Plusquamperfekt", "Futur I", "Futur II"]

    for topic in test_topics:
        button = ctk.CTkButton(parent, text=topic, command=lambda t=topic: open_test_window(t))
        button.pack(pady=10)


def change_language(value):
    language_var.set(value)


def create_settings_ui(parent):
    label = ctk.CTkLabel(parent, text="Налаштування", font=ctk.CTkFont(size=20, weight="bold"))
    label.pack(pady=20)

    theme_frame = ctk.CTkFrame(parent)
    theme_frame.pack(pady=10, padx=20, anchor="w")

    theme_label = ctk.CTkLabel(theme_frame, text="Тема:", font=ctk.CTkFont(size=14))
    theme_label.pack(side="left")

    def toggle_theme():
        current_theme = theme_var.get()
        if current_theme == "світла":
            root.configure(bg="white")
        elif current_theme == "темна":
            root.configure(bg="black")

    theme_var = ctk.BooleanVar(value=True)  
    theme_switch = ctk.CTkSwitch(theme_frame, variable=theme_var, command=toggle_theme)
    theme_switch.pack(side="left")

  
    def logout():
        if messagebox.askyesno("Підтвердження", "Ви впевнені, що хочете вийти з акаунту?"):
            parent.destroy()

    logout_button = ctk.CTkButton(parent, text="Вийти з акаунту", command=logout)
    logout_button.pack(pady=20)


def open_test_window(topic=""):
    global test_questions

    test_window = ctk.CTkToplevel()
    test_window.geometry("800x600")
    test_window.title(f"Тестування: {topic}")

    canvas = ctk.CTkCanvas(test_window)
    scrollbar = ctk.CTkScrollbar(test_window, orientation="vertical", command=canvas.yview)
    scrollable_frame = ctk.CTkFrame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    questions = test_questions.get(topic, [])
    responses = []

  
    def submit_test():
        score = 0
        for idx, response in enumerate(responses):
            q_index, user_answer, q_type = response
            correct_answer = questions[q_index][2]

            if q_type == "single":
                if int(user_answer.get()) == correct_answer:
                    score += 1
            elif q_type == "multiple":
                correct_answers = set(correct_answer)
                user_answers = set([i for i, var in enumerate(user_answer) if var.get() == 1])
                if user_answers == correct_answers:
                    score += 1
            elif q_type == "text":
                if user_answer.get().strip().lower() == correct_answer.lower():
                    score += 1
            elif q_type == "translation":
                if user_answer.get().strip().lower() == correct_answer.lower():
                    score += 1

        percentage = (score / len(questions)) * 100
        result_message = f"Ви відповіли правильно на {score} з {len(questions)} питань. Ваш результат: {percentage:.2f}%. "

        if percentage >= 100:
            result_message += "Відмінно!"
        elif percentage >= 80:
            result_message += "Добре!"
        elif percentage >= 60:
            result_message += "Задовільно."
        else:
            result_message += "Не здано."

        result_label = ctk.CTkLabel(test_window, text=result_message, font=ctk.CTkFont(size=18, weight="bold"))
        result_label.pack(pady=20)

        if percentage >= 60:
            return_button = ctk.CTkButton(test_window, text="Повернутись в основне вікно", command=test_window.destroy)
            return_button.pack(pady=10)
        else:
            retry_button = ctk.CTkButton(test_window, text="Повторити спробу",
                                         command=lambda: [test_window.destroy(), open_test_window(topic)])
            retry_button.pack(pady=10)
            review_button = ctk.CTkButton(test_window, text="Повторити матеріал",
                                          command=lambda: [test_window.destroy(),
                                                           tabview.select("Теоретичний матеріал")])
            review_button.pack(pady=10)

    for i, (question, options, answer, q_type) in enumerate(questions):
        q_frame = ctk.CTkFrame(scrollable_frame)
        q_frame.pack(fill="both", pady=10, padx=10)

        q_label = ctk.CTkLabel(q_frame, text=f"{i + 1}. {question}", font=ctk.CTkFont(size=16))
        q_label.pack(anchor="w", pady=5)

        if q_type == "single":
            answer_var = ctk.StringVar()
            for opt in options:
                rb = ctk.CTkRadioButton(q_frame, text=opt, variable=answer_var, value=options.index(opt))
                rb.pack(anchor="w", padx=20)
            responses.append((i, answer_var, q_type))

        elif q_type == "multiple":
            answer_vars = []
            for opt in options:
                cb_var = ctk.IntVar()
                cb = ctk.CTkCheckBox(q_frame, text=opt, variable=cb_var)
                cb.pack(anchor="w", padx=20)
                answer_vars.append(cb_var)
            responses.append((i, answer_vars, q_type))

        elif q_type == "text":
            answer_entry = ctk.CTkEntry(q_frame)
            answer_entry.pack(anchor="w", padx=20)
            responses.append((i, answer_entry, q_type))

        elif q_type == "translation":
            answer_entry = ctk.CTkEntry(q_frame)
            answer_entry.pack(anchor="w", padx=20)
            responses.append((i, answer_entry, q_type))

    submit_button = ctk.CTkButton(scrollable_frame, text="Завершити тестування", command=submit_test)
    submit_button.pack(pady=20)


root = create_main_window()
root.mainloop()

if __name__ == "__main__":
    root = create_main_window()
    root.mainloop()
