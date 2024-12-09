import tkinter as tk
from tkinter import messagebox
import sqlite3

# Crear base de datos y tabla de ejemplo
conn = sqlite3.connect('Final.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'ub123')")
conn.commit()
conn.close()

# Función de login (segura)
def login_parametrized():
    username = username_entry.get()
    password = password_entry.get()

    # Conexión a la base de datos
    conn = sqlite3.connect('Final.db')
    cursor = conn.cursor()

    # Consulta parametrizada (segura)
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"Ejecutando consulta: {query} con parámetros {username} y {password}")  # Debug

    try:
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        if user:
            messagebox.showinfo("Login", "¡Login exitoso!")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
    except sqlite3.OperationalError as e:
        messagebox.showerror("Error", f"Error en la consulta: {e}")
    finally:
        conn.close()

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Login Seguro")

tk.Label(root, text="Usuario:").grid(row=0, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

tk.Label(root, text="Contraseña:").grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

tk.Button(root, text="Login", command=login_parametrized).grid(row=2, column=0, columnspan=2)

root.mainloop()
