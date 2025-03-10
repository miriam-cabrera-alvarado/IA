# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 00:52:55 2025

@author: Alex
"""

from tkinter import Tk
from Interfaz import Interfaz
from tienda import Descuento

def procesar_datos(fecha, monto):
    descuento = Descuento(fecha, monto)
    monto_final = descuento.calcular_descuento()
    mensaje = f"Fecha: {descuento.fecha}, Monto final: ${monto_final:.2f}"
    app.mostrar_mensaje(mensaje)

if __name__ == "__main__":
    root = Tk()
    app = Interfaz(root, procesar_datos)
    root.mainloop()
