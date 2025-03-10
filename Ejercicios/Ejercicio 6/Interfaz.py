# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 00:23:49 2025

@author: Alex
"""

# Interfaz.py
import tkinter as tk
from Validador import Validador  # Importamos la clase Validador

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Números")  # Título de la ventana
        self.root.geometry("300x250")  # Tamaño de la ventana
        self.app = Validador()  # Instanciamos la clase Validador
        self.setup_ui()

    def setup_ui(self):
        # Etiqueta de mensaje estático en la parte superior
        self.label = tk.Label(self.root, text="Ingrese cualquier número")
        self.label.pack(pady=10)

        # Campo de entrada donde el usuario ingresa el número
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        # Botón para validar el número ingresado
        self.button = tk.Button(self.root, text="Ingresar", command=self.on_validar)
        self.button.pack(pady=10)

        # Etiqueta para mostrar la cantidad de números ingresados
        self.contador_label = tk.Label(self.root, text="Números ingresados: 0", fg="blue")
        self.contador_label.pack(pady=10)

    def on_validar(self):
        try:
            # Intenta convertir lo que el usuario ingresa a un número (puede ser entero o decimal)
            numero = float(self.entry.get())  # Cambié a float para aceptar decimales
            total_numeros = self.app.registrar_numero(numero)  # Aumenta el contador

            # Mostramos el número ingresado y actualizamos el contador
            self.label.config(text=f"Número ingresado: {numero}", fg="green")
            self.contador_label.config(text=f"Números ingresados: {total_numeros}")  # Actualiza el contador en pantalla
            self.entry.delete(0, tk.END)  # Borra el campo de entrada para ingresar otro número
        except ValueError:
            # Si no es un número válido, limpia el campo y no aumenta el contador
            self.entry.delete(0, tk.END)  # Borra el campo de entrada
