import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar():
    try:
        m = float(entry_m.get()) #pendiente
        b = float(entry_b.get()) #termino independiente

        x = np.linspace(-10, 10, 100) #da 100 valores entre -10 y 10
        y = m * x + b

        ax.clear() #limpia la gráfica para q la use despues
        ax.plot(x, y, color='pink', linestyle='--', label=f"f(x) = {m}x + {b}")
        ax.legend() #
        ax.grid() #cuadrícula

        canvas.draw()
    except ValueError:
        lbl_resultado.config(text="Ingrese valores numéricos válidos.")


root = tk.Tk()
root.title("Función Lineal")

tk.Label(root, text="Pendiente (m):").pack()
entry_m = tk.Entry(root) #entry = input
entry_m.pack()

tk.Label(root, text="Término independiente (b):").pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Button(root, text="Graficar", command=graficar).pack()

lbl_resultado = tk.Label(root, text="")
lbl_resultado.pack()

# Área de gráfica
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
