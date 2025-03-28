import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

    # USER: admin
    # CONTRASEÑA: 1234

credenciales = pd.read_csv("credenciales.csv")

def mostrar_interfaz_consultas():
    global tabla, df

    ventana = tk.Tk()
    ventana.title("Consultas de Clientes")
    ventana.geometry("900x600")
    ventana.configure(bg="#FCE4EC")

    df = pd.read_csv("clientes.csv")

    # Frame superior para consultas
    frame_superior = tk.Frame(ventana, bg="#FCE4EC", padx=10, pady=10)
    frame_superior.pack(fill="x")
    
    
    #Consultas con nombre o país: pais == "Epesña", nombre == "Ana"
    tk.Label(frame_superior, text="Consulta (por ejemplo, saldo > 3000):", font=("Arial", 12), bg="#FCE4EC", fg="#424242").pack(side="left")

    consulta_entry = tk.Entry(frame_superior, width=40, font=("Arial", 12))
    consulta_entry.pack(side="left", padx=5)

    btn_ejecutar = tk.Button(frame_superior, text="Ejecutar", bg="#D1C4E9", fg="black", font=("Arial", 12),
                             command=lambda: ejecutar_consulta(consulta_entry.get()))
    btn_ejecutar.pack(side="left", padx=5)

    btn_limpiar = tk.Button(frame_superior, text="Limpiar", bg="#F48FB1", fg="black", font=("Arial", 12),
                            command=limpiar_tabla)
    btn_limpiar.pack(side="left", padx=5)

    # Frame para mostrar resultados
    frame_resultados = tk.Frame(ventana, bg="#FCE4EC")
    frame_resultados.pack(pady=10, expand=True, fill="both")

    columnas = list(df.columns)
    tabla = ttk.Treeview(frame_resultados, columns=columnas, show="headings")

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#CE93D8", foreground="#365633")
    estilo.configure("Treeview", font=("Arial", 11), rowheight=30)

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150, anchor="center")

    tabla.pack(expand=True, fill="both")

    ventana.mainloop()

def ejecutar_consulta(query):
    global df

    try:
        resultado_df = df.query(query)

        limpiar_tabla()

        if resultado_df.empty:
            messagebox.showinfo("Sin resultados", "No se encontraron coincidencias.")
        else:
            for _, row in resultado_df.iterrows():
                tabla.insert("", "end", values=list(row))

    except Exception as e:
        messagebox.showerror("Error", f"Consulta inválida: {str(e)}")

def limpiar_tabla():
    """Elimina todas las filas de la tabla."""
    for row in tabla.get_children():
        tabla.delete(row)

# Función para validar el login
def validar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    if ((credenciales["usuario"] == usuario) & (credenciales["contraseña"] == contraseña)).any():
        messagebox.showinfo("Acceso Permitido", f"Bienvenido, {usuario}")
        ventana_login.destroy()
        mostrar_interfaz_consultas()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Login
ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")
ventana_login.geometry("400x250")
ventana_login.configure(bg="#FCE4EC")

tk.Label(ventana_login, text="Usuario:", font=("Arial", 12), bg="#FCE4EC", fg="#424242").grid(row=0, column=0, pady=10, padx=10)
entry_usuario = tk.Entry(ventana_login, font=("Arial", 12))
entry_usuario.grid(row=0, column=1, pady=10, padx=10)

tk.Label(ventana_login, text="Contraseña:", font=("Arial", 12), bg="#FCE4EC", fg="#424242").grid(row=1, column=0, pady=10, padx=10)
entry_contraseña = tk.Entry(ventana_login, show="*", font=("Arial", 12))
entry_contraseña.grid(row=1, column=1, pady=10, padx=10)

btn_login = tk.Button(ventana_login, text="Ingresar", command=validar_login, bg="#D1C4E9", fg="black", font=("Arial", 12))
btn_login.grid(row=2, column=0, columnspan=2, pady=15)

ventana_login.mainloop()
