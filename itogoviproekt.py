import tkinter as tk
from tkinter import messagebox
import sqlite3

# Создание базы данных и таблицы сотрудников
conn = sqlite3.connect('employees.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY AUTOINCREMENT, full_name TEXT, phone_number TEXT, email TEXT, salary REAL)")

# Функция для добавления нового сотрудника
def add_employee():
    full_name = full_name_entry.get()
    phone_number = phone_number_entry.get()
    email = email_entry.get()
    salary = salary_entry.get()

    c.execute("INSERT INTO employees (full_name, phone_number, email, salary) VALUES (?, ?, ?, ?)", (full_name, phone_number, email, salary))
    conn.commit()
    messagebox.showinfo("Успех", "Сотрудник успешно добавлен")

# Функция для изменения данных сотрудника
def update_employee():
    employee_id = int(id_entry.get())
    full_name = full_name_entry.get()
    phone_number = phone_number_entry.get()
    email = email_entry.get()
    salary = salary_entry.get()

    c.execute("UPDATE employees SET full_name=?, phone_number=?, email=?, salary=? WHERE id=?", (full_name, phone_number, email, salary, employee_id))
    conn.commit()
    messagebox.showinfo("Успех", "Данные сотрудника успешно обновлены")

# Функция для удаления сотрудника
def delete_employee():
    employee_id = int(id_entry.get())
    c.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    conn.commit()
    messagebox.showinfo("Успех", "Сотрудник успешно удален")

# Функция для поиска сотрудника по ФИО
def search_employee():
    full_name = full_name_entry.get()
    c.execute("SELECT * FROM employees WHERE full_name=?", (full_name,))
    rows = c.fetchall()

    results_text.delete('1.0', tk.END)

    if rows:
        for row in rows:
            results_text.insert(tk.END, f"ФИО: {row[1]}\nНомер телефона: {row[2]}\nАдрес электронной почты: {row[3]}\nЗаработная плата: {row[4]}\n\n")
    else:
        results_text.insert(tk.END, "Сотрудник не найден")

# Создание графического интерфейса с использованием Tkinter
root = tk.Tk()
root.title("Список сотрудников компании")
root.resizable(False, False)

# Размещение элементов интерфейса
full_name_label = tk.Label(root, text="ФИО:")
full_name_label.grid(row=0, column=0, padx=10, pady=5)
full_name_entry = tk.Entry(root)
full_name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_number_label = tk.Label(root, text="Номер телефона:")
phone_number_label.grid(row=1, column=0, padx=10, pady=5)
phone_number_entry = tk.Entry(root)
phone_number_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Адрес электронной почты:")
email_label.grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

salary_label = tk.Label(root, text="Заработная плата:")
salary_label.grid(row=3, column=0, padx=10, pady=5)
salary_entry = tk.Entry(root)
salary_entry.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Добавить сотрудника", command=add_employee)
add_button.grid(row=0, column=2, padx=10, pady=5)

id_label = tk.Label(root, text="ID сотрудника (для изменения/удаления):")
id_label.grid(row=4, column=0, padx=10, pady=5)
id_entry = tk.Entry(root)
id_entry.grid(row=4, column=1, padx=10, pady=5)

update_button = tk.Button(root, text="Изменить данные", command=update_employee)
update_button.grid(row=4, column=2, padx=10, pady=5)

delete_button = tk.Button(root, text="Удалить сотрудника", command=delete_employee)
delete_button.grid(row=5, column=2, padx=10, pady=5)

search_button = tk.Button(root, text="Поиск по ФИО", command=search_employee)
search_button.grid(row=6, column=2, padx=10, pady=5)

results_text = tk.Text(root, height=10, width=50)
results_text.grid(row=7, columnspan=3, padx=10, pady=5)

root.mainloop()