import pyautogui
import keyboard
import tkinter as tk
from tkinter import simpledialog, Label, Button, Entry, messagebox
import os
import time
# Crear la carpeta 'mapas' si no existe
if not os.path.exists('mapas'):
    os.makedirs('mapas')

# Variables globales para almacenar la posición del mouse
mouse_x = None
mouse_y = None

def mostrar_ventana_de_configuracion():
    configuracion_root = tk.Tk()
    configuracion_root.title("Configuración de Captura")

    nombre_mapa_label = Label(configuracion_root, text="Nombre del Mapa:")
    nombre_mapa_label.pack()
    nombre_mapa_entry = Entry(configuracion_root)
    nombre_mapa_entry.pack()

    nombre_imagen_label = Label(configuracion_root, text="Nombre de la Imagen:")
    nombre_imagen_label.pack()
    nombre_imagen_entry = Entry(configuracion_root)
    nombre_imagen_entry.pack()
    
    esperar_imagen_label = Label(configuracion_root, text="Nombre de la Imagen para Esperar:")
    esperar_imagen_label.pack()
    esperar_imagen_entry = Entry(configuracion_root)
    esperar_imagen_entry.pack()

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
    tiempo_entry.insert(0, "10")  # Tiempo de espera por defecto de 10 segundos
    tiempo_entry.pack()

    pos_label = Label(configuracion_root, text="Posición del Mouse: ")
    pos_label.pack()

    def capturar_posicion_del_mouse():
        global mouse_x, mouse_y
        configuracion_root.withdraw()
        messagebox.showinfo("Capturar Posición", "Mueve el mouse a la posición deseada y presiona 'K' para capturarla.")
        keyboard.wait('k')
        mouse_x, mouse_y = pyautogui.position()
        configuracion_root.deiconify()
        pos_label.config(text=f"Posición del Mouse: {mouse_x}, {mouse_y}")

    capturar_button = Button(configuracion_root, text="Capturar Posición del Mouse", command=capturar_posicion_del_mouse)
    capturar_button.pack()

    def guardar_captura():
        try:
            nombre_mapa = nombre_mapa_entry.get()
            nombre_imagen = nombre_imagen_entry.get()
            esperar_imagen = esperar_imagen_entry.get()
            accion1 = accion_var1.get()
            accion2 = accion_var2.get()
            tiempo_espera = int(tiempo_entry.get())

            if not nombre_mapa or not nombre_imagen or not esperar_imagen or not accion1 or not accion2 or not tiempo_espera:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            script_variable = (
                f"    {nombre_mapa} = pyautogui.locateOnScreen('mapas/{nombre_imagen}.png', confidence=0.85)\n"
                f"    if {nombre_mapa}:\n"
                f"        buscar()\n"
            )
            
            if accion1 != "buscar":
                script_variable += f"        {accion1}()\n"
            if accion2 != "buscar" or accion1 == "buscar":
                script_variable += f"        {accion2}()\n"
            
            script_variable += f"        time.sleep({tiempo_espera})\n"
            script_variable += f"        esperar_siguiente_mapa('{nombre_mapa}', '{esperar_imagen}', {tiempo_espera})\n\n"
            
            with open("posiciones_mouse.py", "a") as archivo:
                archivo.write(script_variable)
            print(f"Variable {nombre_mapa} creada y guardada en el archivo posiciones_mouse.py con las acciones {accion1}, {accion2} y tiempo de espera {tiempo_espera} segundos")
        
        except ValueError:
            messagebox.showerror("Error", "El tiempo de espera debe ser un número entero.")
    
    guardar_button = Button(configuracion_root, text="Guardar Configuración", command=guardar_captura)
    guardar_button.pack()

    configuracion_root.mainloop()

def esperar_siguiente_mapa(nombre_mapa_actual, nombre_imagen_siguiente, tiempo_espera):
    while True:
        siguiente_mapa = pyautogui.locateOnScreen(f'mapas/{nombre_imagen_siguiente}.png', confidence=0.85)
        if siguiente_mapa:
            print(f"Mapa {nombre_imagen_siguiente} encontrado.")
            break
        else:
            print(f"Esperando que aparezca el mapa {nombre_imagen_siguiente}...")
            time.sleep(tiempo_espera)
            continuar_mapa = pyautogui.locateOnScreen(f'mapas/{nombre_imagen_siguiente}.png', confidence=0.85)
            if continuar_mapa:
                print(f"Mapa {nombre_imagen_siguiente} aún no encontrado, permaneciendo en el mapa {nombre_mapa_actual}.")
                # Aquí puedes agregar lógica adicional para manejar la situación mientras espera.

# Ejecutar la ventana de configuración al iniciar el script
mostrar_ventana_de_configuracion()
