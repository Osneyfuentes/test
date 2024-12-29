import pyautogui
import keyboard
import tkinter as tk
from tkinter import simpledialog
import pyscreeze
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
import traceback
import ctypes
import time
import os
import threading
pyautogui.pause = 0
from tkinter import filedialog
import win32gui
import win32con
import configparser
import os

# Crear o leer el archivo de configuración
config_file = "window_config.ini"
config = configparser.ConfigParser()

def save_window_position_and_size(window_name):
    hwnd = win32gui.FindWindow(None, window_name)
    if hwnd:
        rect = win32gui.GetWindowRect(hwnd)
        x, y, right, bottom = rect
        width = right - x
        height = bottom - y

        # Guardar en el archivo de configuración
        config['WINDOW'] = {
            'x': x,
            'y': y,
            'width': width,
            'height': height
        }

        with open(config_file, 'w') as configfile:
            config.write(configfile)
        print(f"Posición y tamaño guardados para la ventana '{window_name}'")
    else:
        print(f"No se encontró la ventana con el nombre '{window_name}'")

def load_window_position_and_size(window_name):
    if os.path.exists(config_file):
        config.read(config_file)
        if 'WINDOW' in config:
            hwnd = win32gui.FindWindow(None, window_name)
            if hwnd:
                # Establecer posición y tamaño de la ventana desde el archivo de configuración
                x = config.getint('WINDOW', 'x', fallback=100)
                y = config.getint('WINDOW', 'y', fallback=100)
                width = config.getint('WINDOW', 'width', fallback=800)
                height = config.getint('WINDOW', 'height', fallback=600)
                win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, width, height, win32con.SWP_SHOWWINDOW)
                print(f"Posición y tamaño cargados para la ventana '{window_name}'")
            else:
                print(f"No se encontró la ventana con el nombre '{window_name}'")

# Nombre de la ventana a modificar
window_name = "Jorgeily - Ocra - 3.0.28.18 - Release"

# Cargar la posición y tamaño guardados
load_window_position_and_size(window_name)

# Guardar la posición y tamaño al terminar (llámalo según sea necesario en tu flujo)



def buscar_imagen(ruta_imagen):
    ubicacion = pyautogui.locateOnScreen(ruta_imagen, confidence=0.75)
    if ubicacion:
        pyautogui.moveTo(ubicacion)
        hacer_click()
        time.sleep(3)  # Puedes ajustar este tiempo de espera según sea necesario

def buscar():
    pyautogui.sleep(0)
    ortiga_mapa2 = pyautogui.locateOnScreen('objetos/ortiga_mapa2.png', confidence=0.85, region=(1163, 319, 50, 50))
    if ortiga_mapa2:
       pyautogui.moveTo(ortiga_mapa2)
       hacer_click()
       time.sleep(10)

    ortiga_map03 = pyautogui.locateOnScreen('objetos/ortiga_map03.png', confidence=0.85, region=(287, 452, 50, 50))
    if ortiga_map03:
       pyautogui.moveTo(ortiga_map03)
       hacer_click()
       time.sleep(10)

    ortiga_map003 = pyautogui.locateOnScreen('objetos/ortiga_map003.png', confidence=0.85, region=(1124, 202, 50, 50))
    if ortiga_map003:
       pyautogui.moveTo(ortiga_map003)

    ortiga_map04 = pyautogui.locateOnScreen('objetos/ortiga_map04.png', confidence=0.85, region=(765, 355, 50, 50))
    if ortiga_map04:
       pyautogui.moveTo(ortiga_map04)
       hacer_click()
       time.sleep(10)

    ortiga_map004 = pyautogui.locateOnScreen('objetos/ortiga_map004.png', confidence=0.85, region=(1084, 303, 50, 50))
    if ortiga_map004:
       pyautogui.moveTo(ortiga_map004)
       hacer_click()
       time.sleep(10)

    ortiga_map05 = pyautogui.locateOnScreen('objetos/ortiga_map05.png', confidence=0.85, region=(788, 538, 50, 50))
    if ortiga_map05:
       pyautogui.moveTo(ortiga_map05)
       hacer_click()
       time.sleep(10)

    ortiga_map005 = pyautogui.locateOnScreen('objetos/ortiga_map005.png', confidence=0.85, region=(925, 438, 50, 50))
    if ortiga_map005:
       pyautogui.moveTo(ortiga_map005)
       hacer_click()
       time.sleep(10)

    ortiga_map06 = pyautogui.locateOnScreen('objetos/ortiga_map06.png', confidence=0.85, region=(97, 319, 50, 50))
    if ortiga_map06:
       pyautogui.moveTo(ortiga_map06)
       hacer_click()
       time.sleep(10)

    ortiga_map07 = pyautogui.locateOnScreen('objetos/ortiga_map07.png', confidence=0.85, region=(222, 376, 50, 50))
    if ortiga_map07:
       pyautogui.moveTo(ortiga_map07)
       hacer_click()
       time.sleep(10)

    ortiga_map007 = pyautogui.locateOnScreen('objetos/ortiga_map007.png', confidence=0.85, region=(711, 664, 50, 50))
    if ortiga_map007:
       pyautogui.moveTo(ortiga_map007)
       hacer_click()
       time.sleep(10)

    ortiga_map007 = pyautogui.locateOnScreen('objetos/ortiga_map007.png', confidence=0.85, region=(1172, 727, 50, 50))
    if ortiga_map007:
       pyautogui.moveTo(ortiga_map007)
       hacer_click()
       time.sleep(10)

    ortiga_map11 = pyautogui.locateOnScreen('objetos/ortiga_map11.png', confidence=0.85, region=(878, 455, 50, 50))
    if ortiga_map11:
       pyautogui.moveTo(ortiga_map11)
       hacer_click()
       time.sleep(10)

    ortiga_map12 = pyautogui.locateOnScreen('objetos/ortiga_map12.png', confidence=0.85, region=(84, 588, 50, 50))
    if ortiga_map12:
       pyautogui.moveTo(ortiga_map12)
       hacer_click()
       time.sleep(10)

    ortiga_map_12 = pyautogui.locateOnScreen('objetos/ortiga_map_12.png', confidence=0.85, region=(1138, 657, 50, 50))
    if ortiga_map_12:
       pyautogui.moveTo(ortiga_map_12)
       hacer_click()
       time.sleep(10)
    ortiga = pyautogui.locateOnScreen('objetos/ortiga.png', confidence=0.85, region=(121, 226, 50, 50))
    if ortiga:
       pyautogui.moveTo(ortiga)
       hacer_click()
       time.sleep(10)

    ortigamap13 = pyautogui.locateOnScreen('objetos/ortigamap13.png', confidence=0.85, region=(745, 418, 50, 50))
    if ortigamap13:
       pyautogui.moveTo(ortigamap13)
       hacer_click()
       time.sleep(10)
    lena = pyautogui.locateOnScreen('objetos/lena.png', confidence=0.85, region=(798, 684, 50, 50))
    if lena:
       pyautogui.moveTo(lena)
       hacer_click()
       time.sleep(2)

    ortiga11 = pyautogui.locateOnScreen('objetos/ortiga11.png', confidence=0.85, region=(351, 141, 50, 50))
    if ortiga11:
       pyautogui.moveTo(ortiga11)
       hacer_click()
       time.sleep(2)

    ortiga13 = pyautogui.locateOnScreen('objetos/ortiga13.png', confidence=0.85, region=(1122, 175, 50, 50))
    if ortiga13:
       pyautogui.moveTo(ortiga13)
       hacer_click()
       time.sleep(2)

    ortiga16 = pyautogui.locateOnScreen('objetos/ortiga16.png', confidence=0.85, region=(1002, 103, 50, 50))
    if ortiga16:
       pyautogui.moveTo(ortiga16)
       hacer_click()
       time.sleep(2)

    leña3 = pyautogui.locateOnScreen('objetos/lena3.png', confidence=0.85, region=(591, 333, 50, 50))
    if leña3:
       pyautogui.moveTo(leña3)
       hacer_click()
       time.sleep(2)

    leña4 = pyautogui.locateOnScreen('objetos/lena4.png', confidence=0.85, region=(299, 436, 50, 50))
    if leña4:
       pyautogui.moveTo(leña4)
       hacer_click()
       time.sleep(2)

    leña5 = pyautogui.locateOnScreen('objetos/lena5.png', confidence=0.85, region=(425, 151, 50, 50))
    if leña5:
       pyautogui.moveTo(leña5)
       hacer_click()
       time.sleep(2)

    ortiga21 = pyautogui.locateOnScreen('objetos/ortiga21.png', confidence=0.85, region=(550, 421, 50, 50))
    if ortiga21:
       pyautogui.moveTo(ortiga21)
       hacer_click()
       time.sleep(2)

    leña10 = pyautogui.locateOnScreen('objetos/lena10.png', confidence=0.85, region=(134, 434, 50, 50))
    if leña10:
       pyautogui.moveTo(leña10)
       hacer_click()
       time.sleep(2)

    leña10 = pyautogui.locateOnScreen('objetos/lena50.png', confidence=0.85, region=(428, 575, 50, 50))
    if leña10:
       pyautogui.moveTo(leña10)
       hacer_click()
       time.sleep(2)

    ortiga50 = pyautogui.locateOnScreen('objetos/ortiga50.png', confidence=0.85, region=(85, 593, 50, 50))
    if ortiga50:
       pyautogui.moveTo(ortiga50)
       hacer_click()
       time.sleep(2)

    ortiga55 = pyautogui.locateOnScreen('objetos/ortiga55.png', confidence=0.85, region=(1089, 234, 50, 50))
    if ortiga55:
       pyautogui.moveTo(ortiga55)
       hacer_click()
       time.sleep(2)

    ortiga56 = pyautogui.locateOnScreen('objetos/ortiga56.png', confidence=0.85, region=(1142, 655, 50, 50))
    if ortiga56:
       pyautogui.moveTo(ortiga56)
       hacer_click()
       time.sleep(6)

    ortiga60 = pyautogui.locateOnScreen('objetos/ortiga60.png', confidence=0.85, region=(534, 493, 50, 50))
    if ortiga60:
       pyautogui.moveTo(ortiga60)
       hacer_click()
       time.sleep(6)

    ortiga61 = pyautogui.locateOnScreen('objetos/ortiga61.png', confidence=0.85, region=(222, 588, 50, 50))
    if ortiga61:
       pyautogui.moveTo(ortiga61)
       hacer_click()
       time.sleep(6)

    ortiga62 = pyautogui.locateOnScreen('objetos/ortiga62.png', confidence=0.85, region=(1138, 446, 50, 50))
    if ortiga62:
       pyautogui.moveTo(ortiga62)
       hacer_click()
       time.sleep(6)

    ortiga65 = pyautogui.locateOnScreen('objetos/ortiga65.png', confidence=0.85, region=(939, 112, 50, 50))
    if ortiga65:
       pyautogui.moveTo(ortiga65)
       hacer_click()
       time.sleep(6)

    ortiga70 = pyautogui.locateOnScreen('objetos/ortiga70.png', confidence=0.85, region=(1092, 595, 50, 50))
    if ortiga70:
       pyautogui.moveTo(ortiga70)
       hacer_click()
       time.sleep(6)

    ortiga71 = pyautogui.locateOnScreen('objetos/ortiga71.png', confidence=0.85, region=(341, 441, 50, 50))
    if ortiga71:
       pyautogui.moveTo(ortiga71)
       hacer_click()
       time.sleep(6)

    ortiga74 = pyautogui.locateOnScreen('objetos/ortiga74.png', confidence=0.85, region=(915, 684, 50, 50))
    if ortiga74:
       pyautogui.moveTo(ortiga74)
       hacer_click()
       time.sleep(6)
    oneone = pyautogui.locateOnScreen('objetos/oneone.png', confidence=0.85, region=(758, 645, 50, 50))
    if oneone:
       pyautogui.moveTo(oneone)
       hacer_click()
       time.sleep(6)

    twotwo = pyautogui.locateOnScreen('objetos/twotwo.png', confidence=0.85, region=(915, 691, 50, 50))
    if twotwo:
       pyautogui.moveTo(twotwo)
       hacer_click()
       time.sleep(6)
    ortiss = pyautogui.locateOnScreen('objetos/ortiss.png', confidence=0.85, region=(747, 427, 50, 50))
    if ortiss:
       pyautogui.moveTo(ortiss)
       hacer_click()
       time.sleep(6)

    orrto = pyautogui.locateOnScreen('objetos/orrto.png', confidence=0.85, region=(386, 505, 50, 50))
    if orrto:
       pyautogui.moveTo(orrto)
       hacer_click()
       time.sleep(6)

    otorrito = pyautogui.locateOnScreen('objetos/otorrito.png', confidence=0.85, region=(246, 477, 50, 50))
    if otorrito:
       pyautogui.moveTo(otorrito)
       hacer_click()
       time.sleep(6)

    terrete = pyautogui.locateOnScreen('objetos/terrete.png', confidence=0.85, region=(96, 238, 50, 50))
    if terrete:
       pyautogui.moveTo(terrete)
       hacer_click()
       time.sleep(6)

    oksoksks = pyautogui.locateOnScreen('objetos/oksoksks.png', confidence=0.85, region=(1094, 592, 50, 50))
    if oksoksks:
       pyautogui.moveTo(oksoksks)
       hacer_click()
       time.sleep(6)

    ksksksks = pyautogui.locateOnScreen('objetos/ksksksks.png', confidence=0.85, region=(343, 440, 50, 50))
    if ksksksks:
       pyautogui.moveTo(ksksksks)
       hacer_click()
       time.sleep(6)
    fsfsfs = pyautogui.locateOnScreen('objetos/fsfsfs.png', confidence=0.85, region=(631, 334, 50, 50))
    if fsfsfs:
       pyautogui.moveTo(fsfsfs)
       hacer_click()
       time.sleep(6)
    kskskskss = pyautogui.locateOnScreen('objetos/kskskskss.png', confidence=0.85, region=(892, 669, 50, 50))
    if kskskskss:
       pyautogui.moveTo(kskskskss)
       hacer_click()
       time.sleep(6)
    okokoskdoskos = pyautogui.locateOnScreen('objetos/okokoskdoskos.png', confidence=0.85, region=(750, 601, 50, 50))
    if okokoskdoskos:
       pyautogui.moveTo(okokoskdoskos)
       hacer_click()
       time.sleep(6)

    jsjfjisdja = pyautogui.locateOnScreen('objetos/jsjfjisdja.png', confidence=0.85, region=(269, 381, 50, 50))
    if jsjfjisdja:
       pyautogui.moveTo(jsjfjisdja)
       hacer_click()
       time.sleep(6)
    t1 = pyautogui.locateOnScreen('objetos/t1.png', confidence=0.85, region=(760, 646, 50, 50))
    if t1:
        pyautogui.moveTo(t1)
        hacer_click()
        time.sleep(9)

    t2 = pyautogui.locateOnScreen('objetos/t2.png', confidence=0.85, region=(914, 683, 50, 50))
    if t2:
        pyautogui.moveTo(t2)
        hacer_click()
        time.sleep(9)
    t3 = pyautogui.locateOnScreen('objetos/t3.png', confidence=0.85, region=(755, 425, 50, 50))
    if t3:
       pyautogui.moveTo(t3)
       hacer_click()
       time.sleep(9)

    t4 = pyautogui.locateOnScreen('objetos/t4.png', confidence=0.85, region=(383, 500, 50, 50))
    if t4:
       pyautogui.moveTo(t4)
       hacer_click()
       time.sleep(9)

    t5 = pyautogui.locateOnScreen('objetos/t5.png', confidence=0.85, region=(246, 476, 50, 50))
    if t5:
       pyautogui.moveTo(t5)
       hacer_click()
       time.sleep(9)

    t6 = pyautogui.locateOnScreen('objetos/t6.png', confidence=0.85, region=(95, 232, 50, 50))
    if t6:
       pyautogui.moveTo(t6)
       hacer_click()
       time.sleep(9)
    t99 = pyautogui.locateOnScreen('objetos/t99.png', confidence=0.85, region=(386, 585, 50, 50))
    if t99:
       pyautogui.moveTo(t99)
       hacer_click()
       time.sleep(8)
    agarra = pyautogui.locateOnScreen('objetos/agarra.png', confidence=0.85, region=(716, 659, 50, 50))
    if agarra:
       pyautogui.moveTo(agarra)
       hacer_click()
       time.sleep(8)
    pin = pyautogui.locateOnScreen('objetos/pin.png', confidence=0.85, region=(946, 109, 50, 50))
    if pin:
       pyautogui.moveTo(pin)
       hacer_click()
       time.sleep(8)

    try:
        pun = pyautogui.locateOnScreen('objetos/exit.png', confidence=0.75)
        if pun:
            while pun:
                print('sin cap')
                emitir_beep()
                # Actualizar el valor de pun dentro del bucle
                pun = pyautogui.locateOnScreen('objetos/exit.png', confidence=0.75)
    except Exception as e:
        print(f"Error en pun: {e}")
def antibot():
    try:
        battle = pyautogui.locateOnScreen('objetos/battle.png', confidence=0.75)
        if battle:
            while battle:
                print('en battle')
                emitir_beep()
                # Actualizar el valor de battle dentro del bucle
                battle = pyautogui.locateOnScreen('objetos/battle.png', confidence=0.75)
    except Exception as e:
        print(f"Error en battle: {e}")

    try:
        battle = pyautogui.locateOnScreen('objetos/battle.png', confidence=0.75)
        if battle:
            while battle:
                print('en battle')
                emitir_beep()
                # Actualizar el valor de battle dentro del bucle
                battle = pyautogui.locateOnScreen('objetos/battle.png', confidence=0.75)
    except Exception as e:
        print(f"Error en battle: {e}")

    # Pausa para evitar sobrecarga del CPU
    time.sleep(1)


# Importar funciones de ctypes
SendInput = ctypes.windll.user32.SendInput

# Código para el clic del mouse
MOUSE_LEFTDOWN = 0x0002
MOUSE_LEFTUP = 0x0004

# Estructura de INPUT de Windows
class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

class Input(ctypes.Structure):
    class _Input(ctypes.Union):
        _fields_ = [("mi", MouseInput)]
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", _Input)]

def north():
    pyautogui.moveTo(615, 23)
    time.sleep(0.5)
    hacer_click()
def west():
    pyautogui.moveTo(7, 464)
    time.sleep(0.5)
    hacer_click()

def esperar_imagen(nombre_imagen, tiempo_espera=0.1):
    """Espera hasta que una imagen específica aparezca en la pantalla."""
    while True:
        ubicacion = pyautogui.locateOnScreen(f'mapas/{nombre_imagen}.png', confidence=0.75)
        if ubicacion:
            print(f"Imagen {nombre_imagen} encontrada.")
            break
        time.sleep(tiempo_espera)
def south():
    pyautogui.moveTo(646, 896)
    time.sleep(0.5)
    hacer_click()

def east():
    pyautogui.moveTo(1264, 446)
    time.sleep(0.5)
    hacer_click()

def hacer_click():
    # Configurar el clic del mouse
    mi = MouseInput(0, 0, 0, MOUSE_LEFTDOWN, 0, None)
    input_ = Input(type=0, ii=Input._Input(mi=mi))
    SendInput(1, ctypes.byref(input_), ctypes.sizeof(input_))
    time.sleep(0.05)  # Pequeña pausa para simular clic real
    mi = MouseInput(0, 0, 0, MOUSE_LEFTUP, 0, None)
    input_ = Input(type=0, ii=Input._Input(mi=mi))
    SendInput(1, ctypes.byref(input_), ctypes.sizeof(input_))
    print("Click realizado en la posición actual del mouse")
def esperar_siguiente_mapa(nombre_mapa_actual, nombre_imagen_siguiente, tiempo_espera):
    intentos = 0
    max_intentos = 1
    while intentos < max_intentos:
        siguiente_mapa = pyautogui.locateOnScreen(f'objetos/{nombre_imagen_siguiente}.png', confidence=0.75)
        if siguiente_mapa:
            print(f"Mapa {nombre_imagen_siguiente} encontrado.")
            break
        else:
            print(f"Esperando que aparezca el mapa {nombre_imagen_siguiente}... Intento {intentos + 1}")
            time.sleep(tiempo_espera)
            intentos += 1

    if intentos == max_intentos:
        print(f"Mapa {nombre_imagen_siguiente} no encontrado después de {max_intentos} intentos, permaneciendo en el mapa {nombre_mapa_actual}.")
        # Aquí puedes agregar lógica adicional para manejar la situación cuando se alcanzan los intentos máximos.
import winsound

def emitir_beep():
    # Emitir un sonido de beep
    frequency = 1000  # Frecuencia en Hertz
    duration = 500    # Duración en milisegundos
    winsound.Beep(frequency, duration)
    print("Beep emitido")

while True:
    time.sleep(3)
    buscar()
    antibot()
    try:
        map_1 = pyautogui.locateOnScreen('objetos/map_1.png', confidence=0.85, region=(222, 281, 50, 50))
        if map_1:
            south()
            time.sleep(6)
    except Exception as e:
        print(f"Error en map_1: {e}")

    try:
        map_02 = pyautogui.locateOnScreen('objetos/map_02.png', confidence=0.85, region=(264, 500, 50, 50))
        if map_02:
            buscar()
            south()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_02: {e}")
    antibot()
    try:
        map_03 = pyautogui.locateOnScreen('objetos/map_03.png', confidence=0.85, region=(171, 715, 50, 50))
        if map_03:
            buscar()
            time.sleep(2)
            south()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_03: {e}")
    antibot()
    try:
        map_04 = pyautogui.locateOnScreen('objetos/map_04.png', confidence=0.85, region=(143, 413, 50, 50))
        if map_04:
            buscar()
            east()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_04: {e}")
    antibot()
    try:
        pun = pyautogui.locateOnScreen('objetos/exit.png', confidence=0.75)
        if pun:
            while True:
                print('sin cap')
                emitir_beep()
    except Exception as e:
        print(f"Error en pun: {e}")
    antibot()
    try:
        map_05 = pyautogui.locateOnScreen('objetos/map_05.png', confidence=0.85, region=(798, 91, 50, 50))
        if map_05:
            buscar()
            time.sleep(4)
            east()

    except Exception as e:
        print(f"Error en map_05: {e}")
    antibot()
    try:
        map_05 = pyautogui.locateOnScreen('objetos/map_06.png', confidence=0.85)
        if map_05:
            buscar()
            time.sleep(4)
            east()
            emitir_beep()
            

    except Exception as e:
        print(f"Error en map_05: {e}")
    
    antibot()
    try:
        map_09 = pyautogui.locateOnScreen('objetos/map_09.png', confidence=0.85, region=(859, 814, 50, 50))
        if map_09:
            buscar()
            east()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_09: {e}")
    antibot()
    try:
        map_10 = pyautogui.locateOnScreen('objetos/map_10.png', confidence=0.85)
        if map_10:
            buscar()
            north()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_10: {e}")
    antibot()
    try:
        map_11 = pyautogui.locateOnScreen('objetos/map_11.png', confidence=0.85, region=(731, 241, 50, 50))
        if map_11:
            buscar()
            north()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_11: {e}")
    antibot()
    try:
        map_12 = pyautogui.locateOnScreen('objetos/map_12.png', confidence=0.85, region=(480, 227, 50, 50))
        if map_12:
            buscar()
            north()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_12: {e}")
    antibot()
    try:
        map_13 = pyautogui.locateOnScreen('objetos/map_13.png', confidence=0.85, region=(210, 135, 50, 50))
        if map_13:
            buscar()
            north()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_13: {e}")
    antibot()
    try:
        map_14 = pyautogui.locateOnScreen('objetos/map_14.png', confidence=0.85, region=(927, 225, 50, 50))
        if map_14:
            buscar()
            east()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_14: {e}")
    antibot()
    try:
        map_15 = pyautogui.locateOnScreen('objetos/map_15.png', confidence=0.85, region=(717, 461, 50, 50))
        if map_15:
            buscar()
            north()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_15: {e}")
    antibot()
    try:
        map_16 = pyautogui.locateOnScreen('objetos/map_16.png', confidence=0.85, region=(402, 317, 50, 50))
        if map_16:
            buscar()
            west()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_16: {e}")
    antibot()
    try:
        map_17 = pyautogui.locateOnScreen('objetos/map_17.png', confidence=0.85, region=(822, 272, 50, 50))
        if map_17:
            buscar()
            west()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_17: {e}")
    antibot()
    try:
        map_18 = pyautogui.locateOnScreen('objetos/map_18.png', confidence=0.85, region=(566, 200, 50, 50))
        if map_18:
            buscar()
            west()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_18: {e}")
    antibot()
    try:
        map_19 = pyautogui.locateOnScreen('objetos/map_19.png', confidence=0.85, region=(665, 38, 50, 50))
        if map_19:
            buscar()
            west()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_19: {e}")

    try:
        map_20 = pyautogui.locateOnScreen('objetos/map_20.png', confidence=0.85, region=(343, 391, 50, 50))
        if map_20:
            west()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_20: {e}")
    antibot()
    try:
        map_21 = pyautogui.locateOnScreen('objetos/map_21.png', confidence=0.85, region=(397, 395, 50, 50))
        if map_21:
            buscar()
            south()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_21: {e}")
    antibot()
    try:
        map_22 = pyautogui.locateOnScreen('objetos/map_22.png', confidence=0.85, region=(109, 121, 50, 50))
        if map_22:
            buscar()
            south()
            time.sleep(4)
    except Exception as e:
        print(f"Error en map_22: {e}")
