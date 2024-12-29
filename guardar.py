import pyautogui
import keyboard
import time
import tkinter as tk
from tkinter import simpledialog, Label
from PIL import ImageTk, Image
import os

# Variables para almacenar la captura de pantalla y la ventana de congelación
screenshot = None
root = None

def crear_carpeta_si_no_existe(carpeta):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

def congelar_imagen():
    global screenshot, root
    # Congelar la pantalla capturando toda la pantalla
    screenshot = pyautogui.screenshot()
    
    # Crear una ventana de tkinter que muestre la captura de pantalla
    if root is not None:
        root.destroy()
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.overrideredirect(True)  # Eliminar bordes de la ventana
    screenshot_img = ImageTk.PhotoImage(screenshot)
    Label(root, image=screenshot_img).pack()
    
    # Mantener la ventana abierta
    root.update()

def capturar_area_alrededor_del_mouse():
    global screenshot, root
    if screenshot is None:
        print("Primero debes congelar la imagen presionando la tecla '5'.")
        return
    
    # Obtener la posición actual del mouse
    x, y = pyautogui.position()
    ancho = 50
    alto = 50
    izquierda = x - ancho // 2
    superior = y - alto // 2
    
    # Recortar la imagen capturada a la región alrededor del mouse
    captura = screenshot.crop((izquierda, superior, izquierda + ancho, superior + alto))
    
    # Cerrar la ventana de congelación
    if root is not None:
        root.destroy()
        root = None
    
    # Crear una ventana de tkinter para solicitar el archivo y el nombre
    root_nombre = tk.Tk()
    root_nombre.withdraw()  # Esconder la ventana principal
    
    # Solicitar en qué script se guardará la información
    archivo_opcion = simpledialog.askstring("Archivo de Script", "¿En qué script deseas guardar la información? (mapa/objeto):")
    
    if archivo_opcion not in ["mapa", "objeto"]:
        print("Opción inválida. Por favor, elige 'mapa' o 'objeto'.")
        root_nombre.destroy()
        return
    
    # Solicitar el nombre del archivo al usuario
    nombre_archivo = simpledialog.askstring("Nombre de Archivo", "Introduce el nombre del archivo para guardar la captura:")
    
    if nombre_archivo:
        # Crear la carpeta si no existe
        crear_carpeta_si_no_existe('objetos')
        
        # Guardar la captura con el nombre de archivo proporcionado en la carpeta objetos
        captura.save(f"objetos/{nombre_archivo}.png")
        print(f"Captura guardada como objetos/{nombre_archivo}.png")
        
        # Crear el código para comprobar la visibilidad de la imagen en pantalla
        script_variable = f"    {nombre_archivo} = pyautogui.locateOnScreen('objetos/{nombre_archivo}.png', confidence=0.85, region=({izquierda}, {superior}, {ancho}, {alto}))\n"
        script_variable += f"    if {nombre_archivo}:\n"
        script_variable += f"       pyautogui.moveTo({nombre_archivo})\n"
        script_variable += f"       hacer_click()\n"
        script_variable += f"       time.sleep(8)\n\n"
        
        # Guardar el código en el archivo correspondiente
        nombre_script = f"posiciones_{archivo_opcion}.py"
        with open(nombre_script, "a") as archivo:
            archivo.write(script_variable)
        print(f"Variable {nombre_archivo} creada y guardada en el archivo {nombre_script}")
    
    # Cerrar la ventana de tkinter
    root_nombre.destroy()
    screenshot = None  # Restablecer la captura de pantalla

def guardar_posicion_del_mouse():
    x, y = pyautogui.position()

    # Crear una ventana de tkinter
    root = tk.Tk()
    root.withdraw()  # Esconder la ventana principal

    # Solicitar el nombre de la variable al usuario
    nombre_variable = simpledialog.askstring("Nombre de Variable", "Introduce el nombre de la variable para guardar la posición:")

    # Guardar la posición en un script
    if nombre_variable:
        script_con_posicion = f"{nombre_variable} = ({x}, {y})\n"
        with open("posiciones_mouse.py", "a") as archivo:
            archivo.write(script_con_posicion)
        print(f"Posición guardada en la variable {nombre_variable} en el archivo posiciones_mouse.py")

    # Cerrar la ventana de tkinter
    root.destroy()

keyboard.add_hotkey('5', congelar_imagen)
keyboard.add_hotkey('6', capturar_area_alrededor_del_mouse)
keyboard.add_hotkey('7', guardar_posicion_del_mouse)

print("Presiona '5' para congelar la imagen.")
print("Presiona '6' para capturar el área alrededor del mouse.")
print("Presiona '7' para guardar la posición actual del mouse.")
keyboard.wait('esc')
