# main.py
from Interfaz import Interfaz
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()  # Creamos la ventana principal de Tkinter
    app = Interfaz(root)  # Creamos una instancia de la clase Interfaz
    root.mainloop()  # Ejecutamos la interfaz gráfica
