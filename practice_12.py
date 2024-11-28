import requests 
import json
from pprint import pprint
import tkinter as tk
from tkinter import ttk, messagebox

def fetch():
    username = entry.get()
    url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        output = response.json()

        with open("data_file.json", "w") as write_file:
            json.dump(output, write_file)

        filtered_data = {
            "company": output.get("company"), 
            "created_at": output.get("created_at"), 
            "email": output.get("email"), 
            "id": output.get("id"), 
            "name": output.get("name"), 
            "url": output.get("url")
        }

        with open("data_end.json", "w") as write_file: 
            json.dump(filtered_data, write_file, indent=4)

        # pprint(filtered_data)
        messagebox.showinfo("Успех", "Данные сохранены в файл data_end.json")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Ошибка при запросе: {e}")

window = tk.Tk()
window.title("Нахождение репозитория")
window.geometry("666x666")

frame = ttk.Frame(window, padding="10")
frame.pack(expand=True)

label = ttk.Label(frame, 
                  text="Введите имя репозитория:"
                  )
label.pack(pady=10)

entry = ttk.Entry(frame, width=40)
entry.pack(pady=10)

button = ttk.Button(frame, text="Найти", command=fetch)
button.pack(pady=10)

window.mainloop()
