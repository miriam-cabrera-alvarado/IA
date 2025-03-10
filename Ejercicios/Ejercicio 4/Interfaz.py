# Interfaz.py
import tkinter as tk
from Numero import Validador  # Importamos la clase Validador

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de Número")  # Título de la ventana
        self.root.geometry("300x200")  # Tamaño de la ventana
        self.app = Validador()  # Instanciamos la clase Validador
        self.setup_ui()

    def setup_ui(self):
        # Etiqueta de mensaje estático en la parte superior
        self.label = tk.Label(self.root, text="Ingrese un valor menor que 10")
        self.label.pack(pady=10)

        # Campo de entrada donde el usuario ingresa el número
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        # Botón para validar el número ingresado
        self.button = tk.Button(self.root, text="Validar", command=self.on_validar)
        self.button.pack(pady=10)

    def on_validar(self):
        try:
            # Intenta convertir lo que el usuario ingresa a entero
            numero = int(self.entry.get())
            if self.app.validar_numero(numero):
                # Si es válido, muestra un mensaje indicando que el número es válido
                self.label.config(text=f"Número válido ingresado: {numero}", fg="green")
                self.entry.delete(0, tk.END)  # Borra el campo de entrada para ingresar otro número
            else:
                # Si el número no es válido (mayor o igual a 10), limpia el campo para intentar de nuevo
                self.entry.delete(0, tk.END)  # Borra el campo de entrada
        except ValueError:
            # Si no es un número, limpia el campo para que el usuario intente nuevamente
            self.entry.delete(0, tk.END)  # Borra el campo de entrada
