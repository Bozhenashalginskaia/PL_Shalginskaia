import tkinter as tk
from tkinter import ttk, messagebox, filedialog


root = tk.Tk()
root.title("Шалгинская Божена Игоревна")

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Работа с текстом')

tab_control.pack(expand=1, fill='both')

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = combo.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2

        label_result.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа!")

label1 = ttk.Label(tab1, text="Число 1:")
label1.pack(padx=10, pady=5)
entry1 = ttk.Entry(tab1)
entry1.pack(padx=10, pady=5)

label2 = ttk.Label(tab1, text="Число 2:")
label2.pack(padx=10, pady=5)
entry2 = ttk.Entry(tab1)
entry2.pack(padx=10, pady=5)

combo = ttk.Combobox(tab1, values=["+", "-", "*", "/"])
combo.pack(padx=10, pady=5)

button_calculate = ttk.Button(tab1, text="Вычислить", command=calculate)
button_calculate.pack(padx=10, pady=5)

label_result = ttk.Label(tab1, text="Результат:")
label_result.pack(padx=10, pady=5)

def show_choice():
    choice = ""
    if var1.get():
        choice += "Первый "
    if var2.get():
        choice += "Второй "
    if var3.get():
        choice += "Третий "
    if choice:
        messagebox.showinfo("Выбор", f"Вы выбрали: {choice}")
    else:
        messagebox.showinfo("Выбор", "Вы ничего не выбрали")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

checkbox1 = ttk.Checkbutton(tab2, text="Первый", variable=var1)
checkbox1.pack(padx=10, pady=5)

checkbox2 = ttk.Checkbutton(tab2, text="Второй", variable=var2)
checkbox2.pack(padx=10, pady=5)

checkbox3 = ttk.Checkbutton(tab2, text="Третий", variable=var3)
checkbox3.pack(padx=10, pady=5)

button_show = ttk.Button(tab2, text="Показать выбор", command=show_choice)
button_show.pack(padx=10, pady=5)

def load_text():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, text)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить текст", command=load_text)

text_box = tk.Text(tab3)
text_box.pack(expand=1, fill='both')

# Запуск главного цикла
root.mainloop()
