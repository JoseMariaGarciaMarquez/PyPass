import tkinter as tk
import csv
import random
import string

from tkinter import Label, Entry, Button, messagebox
from PIL import Image, ImageTk 

def generar_contrasena(longitud, caracteres):
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def guardar_contrasena(nombre, contrasena, archivo_csv):
    try:
        with open(archivo_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Agregar encabezados si el archivo está vacío
            if file.tell() == 0:
                writer.writerow(['account', 'password'])
            writer.writerow([nombre, contrasena])
            messagebox.showinfo("Éxito", "Contraseña guardada exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar la contraseña: {str(e)}")

def generar_y_mostrar_contrasena():
    nombre = entry_nombre.get()
    longitud_contrasena_str = entry_longitud.get()

    try:
        longitud_contrasena = int(longitud_contrasena_str)
    except ValueError:
        messagebox.showerror("Error", "La longitud de la contraseña debe ser un número entero.")
        return

    if not nombre or longitud_contrasena <= 0:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un nombre y una longitud válida.")
        return

    caracteres = obtener_conjunto_caracteres()
    contrasena = generar_contrasena(longitud_contrasena, caracteres)

    resultado.config(text=f"Contraseña generada: {contrasena}")
    contrasena_generada.set(contrasena)  # Guarda la contraseña generada en una variable de control

def guardar_contrasena_manual():
    nombre = entry_nombre.get()
    contrasena = contrasena_generada.get()  # Obtiene la contraseña generada previamente

    if not nombre or not contrasena:
        messagebox.showwarning("Advertencia", "Por favor, genera una contraseña antes de intentar guardarla.")
        return

    archivo_csv = 'passwords.csv'
    guardar_contrasena(nombre, contrasena, archivo_csv)
    resultado_csv.config(text=f"Contraseña y nombre guardados en {archivo_csv}.")

def obtener_conjunto_caracteres():
    # Puedes personalizar esta función según las preferencias del usuario
    return string.ascii_letters + string.digits + string.punctuation

# Crear ventana
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

# Configurar el icono de la aplicación
icono_path = "images/pypassicon.png"
icon_image = Image.open(icono_path)
icon_image = icon_image.resize((150, 150), Image.BICUBIC)
icon_tk = ImageTk.PhotoImage(icon_image)
ventana.iconphoto(True, icon_tk)

# Elementos de la interfaz
label_nombre = Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=10)

entry_nombre = Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

label_longitud = Label(ventana, text="Longitud de Contraseña:")
label_longitud.grid(row=1, column=0, padx=10, pady=10)

entry_longitud = Entry(ventana)
entry_longitud.grid(row=1, column=1, padx=10, pady=10)

boton_generar = Button(ventana, text="Generar Contraseña", command=generar_y_mostrar_contrasena)
boton_generar.grid(row=2, column=0, columnspan=2, pady=10)

resultado = Label(ventana, text="")
resultado.grid(row=3, column=0, columnspan=2, pady=10)

contrasena_generada = tk.StringVar()  # Variable de control para almacenar la contraseña generada

boton_guardar = Button(ventana, text="Guardar Contraseña", command=guardar_contrasena_manual)
boton_guardar.grid(row=4, column=0, columnspan=2, pady=10)

resultado_csv = Label(ventana, text="")
resultado_csv.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar la interfaz
ventana.mainloop()