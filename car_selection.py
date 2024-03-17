import time
from tkinter import *
from tkinter import ttk, messagebox, filedialog

root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'500x450+{int(w / 2) - 250}+{int(h / 2) - 225}')

history = {}

production = ['Власне', 'Іноземне']
model = ['BMW', 'Mercedes', 'Wolkcvagen', 'Mazda', 'VAZ', 'Інша']
year = ['нова', 'до 5 років', '6-10 років', '11-15 років', 'більше 15 років']
volume = ['менше 1200', '1200-1500', '1501-2200', 'більше 2200']
motor = ['Дизель', 'Бензин']
colors = ['Blue', 'Red', 'Yellow', 'Orange', 'Purple', 'Green', 'Black', 'White', 'Brown', 'Gray']

lang1 = IntVar()
lang2 = IntVar()
lang3 = IntVar()
lang4 = IntVar()
lang5 = IntVar()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def close_program():
    message = messagebox.askyesno('😦', 'Невже ВИ хочете закрити МОЮ прогромальку?!')
    if message == True:
        new_window = Toplevel(root)
        lab = Label(new_window, text='Закриття програми')
        lab.pack()
        progress = ttk.Progressbar(new_window, orient="horizontal", length=300, mode="determinate", value=0,
                                   maximum=100)
        progress.pack()
        currentValue = 0
        for i in range(25):
            currentValue = currentValue + 5
            progress["value"] = currentValue
            time.sleep(0.1)
            progress.update()
        root.quit()


def save_info():
    file_paths = filedialog.asksaveasfilename(title="Зберегти в...", initialfile='car_options',
                                              filetypes=[("Текстові файли", "*.txt"), ("Усі файли", "*.*")])
    messagebox.showinfo('Ура!', 'Файл успішно збережено!')


def record_in_history(key, value):
    history[key] = value


def result():
    new_window = Toplevel(root)
    new_window.geometry("300x200")
    new_window.title("Результат")
    label = Label(new_window, text="Ваш автомобіль:")
    label.pack()
    t = Text(new_window, height=7, width=40)
    t.pack()
    for key, value in history.items():
        t.insert(1.0, f'{key} {value}\n')
    btn_save = Button(new_window, text='Зберегти', width=12, command=save_info)
    btn_save.place(x=90, y=155)
    btn_exit = Button(new_window, width=15, text='Вийти з програми', command=close_program)
    btn_exit.place(x=185, y=155)


def update_color():
    color = sbox.get()
    lab.config(bg=color)
    record_in_history('Колір авто:', color)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

lab = Label(root, text='Виберіть параметри для машини своєї мрії!', font=(None, 16), pady=15)
lab.pack()

frm_production = LabelFrame(root, text='Виробництво:')
frm_production.place(x=20, y=50)
for i in production:
    rb = Radiobutton(frm_production, value=i, text=i, variable=lang1, height=4, width=15,
                     command=lambda i=i: record_in_history('Виробництво:', i))
    rb.pack(anchor="w")

frm_model = LabelFrame(root, text='Марка автомобіля')
frm_model.place(x=170, y=50)
for i in model:
    rb = Radiobutton(frm_model, value=i, text=i, variable=lang2, height=0,
                     command=lambda i=i: record_in_history('Марка автомобіля:', i))
    rb.pack(anchor="w")

frm_age = LabelFrame(root, text='Скільки років')
frm_age.place(x=320, y=50)
for i in year:
    rb = Radiobutton(frm_age, value=i, text=i, variable=lang3,
                     command=lambda i=i: record_in_history('Вік машини:', i))
    rb.pack(anchor="w")

frm_volume = LabelFrame(root, text="Об'єм двигуна")
frm_volume.place(x=20, y=230)
for i in volume:
    rb = Radiobutton(frm_volume, value=i, text=i, variable=lang4,
                     command=lambda i=i: record_in_history("Об'єм двигуна:", i))
    rb.pack(anchor="w")

frm_motor = LabelFrame(root, text='Вид палива')
frm_motor.place(x=170, y=230)
for i in motor:
    rb = Radiobutton(frm_motor, value=i, text=i, variable=lang5, height=3, width=12,
                     command=lambda i=i: record_in_history('Вид палива:', i))
    rb.pack(anchor="w")

frm_color = LabelFrame(root, text='Колір')
frm_color.place(x=320, y=230)
sbox = Spinbox(frm_color, values=colors, wrap=True, command=update_color)
sbox.pack()
lab = Label(frm_color, width=15, height=5, bg='blue')
lab.pack(padx=2, pady=5)
sbox.bind()

btn_res = Button(root, text='Результат', command=result, width=10, height=2, font=18)
btn_res.place(x=200, y=385)

root.mainloop()
