import pyautogui
import keyboard
import time
import tkinter as tk
from tkinter import simpledialog, Label, Button, Entry, messagebox
from PIL import ImageTk, Image
import os

# Variables para almacenar la captura de pantalla y la ventana de congelación
screenshot = None
root = None

# Crear la carpeta 'mapas' si no existe
if not os.path.exists('mapas'):
    os.makedirs('mapas')

def congelar_imagen():
    global screenshot, root
    screenshot = pyautogui.screenshot()
    if root is not None:
        root.destroy()
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    screenshot_img = ImageTk.PhotoImage(screenshot)
    Label(root, image=screenshot_img).pack()
    root.update()

def capturar_area_alrededor_del_mouse():
    global screenshot, root
    if screenshot is None:
        print("Primero debes congelar la imagen presionando la tecla '5'.")
        return

    x, y = pyautogui.position()
    ancho = 50
    alto = 50
    izquierda = x - ancho // 2
    superior = y - alto // 2
    captura = screenshot.crop((izquierda, superior, izquierda + ancho, superior + alto))
    
    if root is not None:
        root.destroy()
        root = None
    
    def guardar_captura():
        try:
            nombre_archivo = nombre_entry.get()
            accion1 = accion_var1.get()
            accion2 = accion_var2.get()
            tiempo_espera = int(tiempo_entry.get())

            if not nombre_archivo or not accion1 or not accion2 or not tiempo_espera:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            captura.save(f"mapas/{nombre_archivo}.png")
            print(f"Captura guardada como mapas/{nombre_archivo}.png")
            
            # Capturar la región de la imagen
            region = (izquierda, superior, izquierda + ancho, superior + alto)
            print(f"Región guardada: {region}")

            script_variable = (
                f"    {nombre_archivo} = pyautogui.locateOnScreen('mapas/{nombre_archivo}.png', confidence=0.85, region={region})\n"
                f"    if {nombre_archivo}:\n"
                f"        buscar()\n"
            )
            
            if accion1 != "buscar":
                script_variable += f"        {accion1}()\n"
            if accion2 != "buscar" or accion1 == "buscar":
                script_variable += f"        {accion2}()\n"
            
            script_variable += f"        time.sleep({tiempo_espera})\n\n"
            
            with open("posiciones_mouse.py", "a") as archivo:
                archivo.write(script_variable)
            print(f"Variable {nombre_archivo} creada y guardada en el archivo posiciones_mouse.py con las acciones {accion1}, {accion2} y tiempo de espera {tiempo_espera} segundos")
        
        except ValueError:
            messagebox.showerror("Error", "El tiempo de espera debe ser un número entero.")
        
        configuracion_root.destroy()
    
    configuracion_root = tk.Tk()
    configuracion_root.title("Configuración de Captura")

    nombre_label = Label(configuracion_root, text="Nombre de Archivo:")
    nombre_label.pack()
    nombre_entry = Entry(configuracion_root)
    nombre_entry.pack()
    
    accion_label1 = Label(configuracion_root, text="Primera Acción a realizar:")
    accion_label1.pack()

    accion_var1 = tk.StringVar(value="buscar")
    acciones = ["buscar", "north", "south", "east", "west"]
    for accion in acciones:
        button = tk.Radiobutton(configuracion_root, text=accion.capitalize(), variable=accion_var1, value=accion)
        button.pack()
    
    accion_label2 = Label(configuracion_root, text="Segunda Acción a realizar:")
    accion_label2.pack()

    accion_var2 = tk.StringVar(value="buscar")
    for accion in acciones:
        button = tk.Radiobutton(configuracion_root, text=accion.capitalize(), variable=accion_var2, value=accion)
        button.pack()
    
    tiempo_label = Label(configuracion_root, text="Tiempo de Espera (segundos):")
    tiempo_label.pack()
    tiempo_entry = Entry(configuracion_root)
    tiempo_entry.pack()

    guardar_button = Button(configuracion_root, text="Guardar Captura", command=guardar_captura)
    guardar_button.pack()

    configuracion_root.mainloop()
    screenshot = None

def guardar_posicion_del_mouse():
    x, y = pyautogui.position()
    root = tk.Tk()
    root.withdraw()
    nombre_variable = simpledialog.askstring("Nombre de Variable", "Introduce el nombre de la variable para guardar la posición:")
    
    if nombre_variable:
        script_con_posicion = f"{nombre_variable} = ({x}, {y})\n"
        with open("posiciones_mouse.py", "a") as archivo:
            archivo.write(script_con_posicion)
        print(f"Posición guardada en la variable {nombre_variable} en el archivo posiciones_mouse.py")
    
    root.destroy()

keyboard.add_hotkey('5', congelar_imagen)
keyboard.add_hotkey('6', capturar_area_alrededor_del_mouse)
keyboard.add_hotkey('7', guardar_posicion_del_mouse)

print("Presiona '5' para congelar la imagen.")
print("Presiona '6' para capturar el área alrededor del mouse.")
print("Presiona '7' para guardar la posición actual del mouse.")
keyboard.wait('esc')
