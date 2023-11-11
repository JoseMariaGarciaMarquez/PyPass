import tkinter as tk
from tkinter import Label, Entry, Button
import csv
import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def guardar_contrasena(nombre, contrasena, archivo_csv):
    with open(archivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Agregar encabezados si el archivo está vacío
        if file.tell() == 0:
            writer.writerow(['account', 'password'])
        writer.writerow([nombre, contrasena])

def generar_y_guardar_contrasena():
    nombre = entry_nombre.get()
    longitud_contrasena = int(entry_longitud.get())
    
    contrasena = generar_contrasena(longitud_contrasena)
    
    resultado.config(text=f"Contraseña generada: {contrasena}")
    
    archivo_csv = 'passwords.csv'
    guardar_contrasena(nombre, contrasena, archivo_csv)
    
    resultado_csv.config(text=f"Contraseña y nombre guardados en {archivo_csv}.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

# Elementos de la interfaz
label_nombre = Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=10)

entry_nombre = Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

label_longitud = Label(ventana, text="Longitud de Contraseña:")
label_longitud.grid(row=1, column=0, padx=10, pady=10)

entry_longitud = Entry(ventana)
entry_longitud.grid(row=1, column=1, padx=10, pady=10)

boton_generar = Button(ventana, text="Generar Contraseña", command=generar_y_guardar_contrasena)
boton_generar.grid(row=2, column=0, columnspan=2, pady=10)

resultado = Label(ventana, text="")
resultado.grid(row=3, column=0, columnspan=2, pady=10)

resultado_csv = Label(ventana, text="")
resultado_csv.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar la interfaz
ventana.mainloop()
