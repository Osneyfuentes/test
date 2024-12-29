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
import cv2
import numpy as np
import time
import keyboard
# Crear o leer el archivo de configuración
config_file = "window_config.ini"
config = configparser.ConfigParser()
import ctypes
import time


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
window_name = "Falconciuf - Ocra - 3.0.32.21 - Release"

# Cargar la posición y tamaño guardados
load_window_position_and_size(window_name)

# Guardar la posición y tamaño al terminar (llámalo según sea necesario en tu flujo)



def buscar_imagen(ruta_imagen):
    ubicacion = pyautogui.locateOnScreen(ruta_imagen, confidence=0.75)
    if ubicacion:
        pyautogui.moveTo(ubicacion)
        hacer_click()
        time.sleep(3)  # Puedes ajustar este tiempo de espera según sea necesario
def victoria():
    victoria = pyautogui.locateOnScreen('victori.png', confidence=0.85)
    if victoria:
        keyboard.press('2')
        keyboard.press('2')
        keyboard.press('esc')
        print('victoria')   
        time.sleep(4)
def buscar():
    victoria()
    menu()
    cap = pyautogui.locateOnScreen('cap.png', confidence=0.85)
    if cap:
            print('no puedes recolectar nada')
    else:
        ortigas = [
            {'img': 'objetos/ortiga_mapa2.png', 'region': (1163, 319, 50, 50)},
            {'img': 'objetos/ortiga_map03.png', 'region': (287, 452, 50, 50)},
            {'img': 'objetos/ortiga_map003.png', 'region': (1124, 202, 50, 50)},
            {'img': 'objetos/ortiga_map04.png', 'region': (765, 355, 50, 50)},
            {'img': 'objetos/ortiga_map004.png', 'region': (1084, 303, 50, 50)},
            {'img': 'objetos/ortiga_map05.png', 'region': (788, 538, 50, 50)},
            {'img': 'objetos/ortiga_map005.png', 'region': (925, 438, 50, 50)},
            {'img': 'objetos/ortiga_map06.png', 'region': (97, 319, 50, 50)},
            {'img': 'objetos/ortiga_map07.png', 'region': (222, 376, 50, 50)},
            {'img': 'objetos/ortiga_map007.png', 'region': (711, 664, 50, 50)},
            {'img': 'objetos/ortiga_map007.png', 'region': (1172, 727, 50, 50)},
            {'img': 'objetos/ortiga_map11.png', 'region': (878, 455, 50, 50)},
            {'img': 'objetos/ortiga_map12.png', 'region': (84, 588, 50, 50)},
            {'img': 'objetos/ortiga_map_12.png', 'region': (1138, 657, 50, 50)},
            {'img': 'objetos/ortiga.png', 'region': (121, 226, 50, 50)},
            {'img': 'objetos/ortigamap13.png', 'region': (745, 418, 50, 50)},
            {'img': 'objetos/ortiga11.png', 'region': (351, 141, 50, 50)},
            {'img': 'objetos/ortiga13.png', 'region': (1122, 175, 50, 50)},
            {'img': 'objetos/ortiga16.png', 'region': (1002, 103, 50, 50)},
            {'img': 'objetos/ortiga21.png', 'region': (550, 421, 50, 50)},
            {'img': 'objetos/ortiga50.png', 'region': (85, 593, 50, 50)},
            {'img': 'objetos/ortiga55.png', 'region': (1089, 234, 50, 50)},
            {'img': 'objetos/ortiga56.png', 'region': (1142, 655, 50, 50)},
            {'img': 'objetos/ortiga60.png', 'region': (534, 493, 50, 50)},
            {'img': 'objetos/ortiga61.png', 'region': (222, 588, 50, 50)},
            {'img': 'objetos/ortiga62.png', 'region': (1138, 446, 50, 50)},
            {'img': 'objetos/ortiga65.png', 'region': (939, 112, 50, 50)},
            {'img': 'objetos/ortiga70.png', 'region': (1092, 595, 50, 50)},
            {'img': 'objetos/ortiga71.png', 'region': (341, 441, 50, 50)},
            {'img': 'objetos/ortiga74.png', 'region': (915, 684, 50, 50)},
            {'img': 'objetos/oneone.png', 'region': (758, 645, 50, 50)},
            {'img': 'objetos/twotwo.png', 'region': (915, 691, 50, 50)},
            {'img': 'objetos/ortiss.png', 'region': (747, 427, 50, 50)},
            {'img': 'objetos/orrto.png', 'region': (386, 505, 50, 50)},
            {'img': 'objetos/otorrito.png', 'region': (246, 477, 50, 50)},
            {'img': 'objetos/terrete.png', 'region': (96, 238, 50, 50)},
            {'img': 'objetos/oksoksks.png', 'region': (1094, 592, 50, 50)},
            {'img': 'objetos/ksksksks.png', 'region': (343, 440, 50, 50)},
            {'img': 'objetos/fsfsfs.png', 'region': (631, 334, 50, 50)},
            {'img': 'objetos/kskskskss.png', 'region': (892, 669, 50, 50)},
            {'img': 'objetos/okokoskdoskos.png', 'region': (750, 601, 50, 50)},
            {'img': 'objetos/jsjfjisdja.png', 'region': (269, 381, 50, 50)},
            {'img': 'objetos/t1.png', 'region': (760, 646, 50, 50)},
            {'img': 'objetos/t2.png', 'region': (914, 683, 50, 50)},
            {'img': 'objetos/t3.png', 'region': (755, 425, 50, 50)},
            {'img': 'objetos/t4.png', 'region': (383, 500, 50, 50)},
            {'img': 'objetos/t5.png', 'region': (246, 476, 50, 50)},
            {'img': 'objetos/t6.png', 'region': (95, 232, 50, 50)},
            {'img': 'objetos/t99.png', 'region': (386, 585, 50, 50)},
            {'img': 'objetos/agarra.png', 'region': (716, 659, 50, 50)},
            {'img': 'objetos/tt1.png'},
            {'img': 'objetos/pin.png', 'region': (946, 109, 50, 50)}
        ]


        for ortiga in ortigas:
            pos = pyautogui.locateOnScreen(ortiga['img'], confidence=0.85, region=ortiga.get('region'))
            if pos:
                pyautogui.moveTo(pos)
                hacer_click()
                print(f"Se hizo clic en el objeto: {ortiga['img']}")
                time.sleep(4)  # Tiempo de espera uniforme para todos los objetos





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


# Función para verificar si la imagen de batalla está activa
def is_battle_active(battle_image_path, screenshot_path='screenshot.png'):
    battle_image = cv2.imread(battle_image_path, 0)
    screenshot = cv2.imread(screenshot_path, 0)

    if battle_image is None or screenshot is None:
        return False

    result = cv2.matchTemplate(screenshot, battle_image, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(result >= threshold)

    return len(loc[0]) > 0

def take_screenshot(screenshot_path='screenshot.png'):
    import pyautogui
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)

# Función principal de batalla
def battle(battle_image_path):
    while True:
        take_screenshot()  # Tomamos una captura de pantalla
        listo = pyautogui.locateOnScreen('listo.png', confidence=0.75)
        if listo:
            keyboard.press('F1')
            time.sleep(1)
            keyboard.press('F1')
            time.sleep(1)
            keyboard.press('F1')
            time.sleep(1)

        
        if is_battle_active(battle_image_path):
            keyboard.press_and_release('2')
            for _ in range(4):
                keyboard.press_and_release('click')
                time.sleep(0.1)  # Pequeña pausa entre clics
                if range(4):
                    keyboard.press_and_release('F1')
            pyautogui.moveTo(714, 59)
            hacer_click()
        else:
            break
        time.sleep(1)  # Espera antes de la siguiente verificación

# Ejemplo de uso
def oficio():
    oficio = pyautogui.locateOnScreen('oficio.png', confidence=0.75)
    if oficio:
            pyautogui.moveTo(366, 897)
            time.sleep(1)
            hacer_click()


import winsound

def check_map(image, region=None, confidence=0.95):
    try:
        map_location = pyautogui.locateOnScreen(image, confidence=confidence, region=region)
        if map_location:
            return True
    except Exception as e:
        print(f"Error en {image}: {e}")
    return False

def map_1():
    
    if check_map('objetos/map_1.png', region=(222, 281, 50, 50)):
        south()
        time.sleep(6)
        map_1()

def map_02():
    if check_map('objetos/map_02.png', region=(264, 500, 50, 50)):
        buscar()
        south()
        time.sleep(4)
        map_02()

def map_03():
    if check_map('objetos/map_03.png', region=(171, 715, 50, 50)):
        buscar()
        time.sleep(2)
        south()
        time.sleep(4)
        map_03()

def map_04():
    if check_map('objetos/map_04.png', region=(143, 413, 50, 50)):
        buscar()
        east()
        time.sleep(4)
        map_04()

def map_05():
    if check_map('objetos/map_05.png', region=(798, 91, 50, 50)):
        buscar()
        time.sleep(4)
        east()
        map_05()

def map_06():
    if check_map('objetos/map_06.png'):
        buscar()
        east()
        time.sleep(7)
        map_06()

def map_09():
    if check_map('objetos/map_09.png', region=(859, 814, 50, 50)):
        buscar()
        east()
        time.sleep(4)
        map_09()

def map_10():
    if check_map('objetos/map_10.png'):
        buscar()
        north()
        time.sleep(4)
        map_10()

def map_11():
    if check_map('objetos/map_11.png', region=(731, 241, 50, 50)):
        buscar()
        north()
        time.sleep(4)
        map_11()

def map_12():
    if check_map('objetos/map_12.png', region=(480, 227, 50, 50)):
        buscar()
        north()
        time.sleep(7)
        map_12()

def map_13():
    if check_map('objetos/map_13.png', region=(210, 135, 50, 50)):
        buscar()
        salida()
        north()
        print('map13')
        time.sleep(4)
        map_13()

def map_14():

    if check_map('objetos/map_14.png', region=(927, 225, 50, 50)):
        buscar()
        east()
        time.sleep(4)
        map_14()

def map_15():
    if check_map('objetos/map_15.png', region=(717, 461, 50, 50)):
        buscar()
        north()
        time.sleep(4)
        print('mapa15')
        map_15()
        

def map_16():
    if check_map('objetos/map_16.png', region=(402, 317, 50, 50)):
        buscar()
        west()
        time.sleep(4)
        map_16()

def map_17():
    if check_map('objetos/map_17.png', region=(822, 272, 50, 50)):
        buscar()
        west()
        time.sleep(4)
        map_17()

def map_18():
    if check_map('objetos/map_18.png', region=(566, 200, 50, 50)):
        buscar()
        west()
        time.sleep(4)
        map_18()

def map_19():
    if check_map('objetos/map_19.png', region=(665, 38, 50, 50)):
        buscar()
        west()
        time.sleep(4)
        map_19()

def map_20():
    if check_map('objetos/map_20.png', region=(343, 391, 50, 50)):
        west()
        time.sleep(4)
        map_20()

def map_21():
    if check_map('objetos/map_21.png', region=(397, 395, 50, 50)):
        buscar()
        south()
        time.sleep(4)
        map_21()

def map_22():
    if check_map('objetos/map_22.png', region=(109, 121, 50, 50)):
        buscar()
        south()
        time.sleep(4)
        map_22()

def menu():
    menu = pyautogui.locateOnScreen('menu.png', confidence=0.75)
    if menu:
        keyboard.press('esc')  
        print('menu')   
        time.sleep(4)


def salida():
    cap = pyautogui.locateOnScreen('cap.png', confidence=0.85)
    if cap:
            print('saliendo')
            east()
            time.sleep(8)
            east()
            time.sleep(8)

def exit():
    exit = pyautogui.locateOnScreen('exit.png', confidence=0.75)
    if exit:
            print('saliendo a astrub')
            time.sleep(2)
            pyautogui.moveTo(834, 615)
            hacer_click()
            time.sleep(2)
            pyautogui.moveTo(417, 678)
            hacer_click()
            time.sleep(1)
            pyautogui.moveTo(417, 678)
            hacer_click()
            time.sleep(15)
def astrub():
    astrub = pyautogui.locateOnScreen('exit.png', confidence=0.75)
    if astrub:
            print('camino al bancoa')
            pyautogui.moveTo(402, 882)
            hacer_click()
            time.sleep(1)
    astrub1 = pyautogui.locateOnScreen('astrub1.png', confidence=0.75)
    if astrub1:
            print('astrub1')
            pyautogui.moveTo(27, 489)
            hacer_click()
            time.sleep(5)
    astrub2 = pyautogui.locateOnScreen('astrub2.png', confidence=0.75)
    if astrub2:
            print('astrub2')
            pyautogui.moveTo(27, 489)
            hacer_click()
            time.sleep(5)
    astrub3 = pyautogui.locateOnScreen('astrub3.png', confidence=0.75)
    if astrub3:
            print('astru3')
            pyautogui.moveTo(581, 889)
            hacer_click()
            time.sleep(5)
    astrub4 = pyautogui.locateOnScreen('astrub4.png', confidence=0.75)
    if astrub4:
            print('astrub4')
            pyautogui.moveTo(828, 357)
            hacer_click()
            time.sleep(5)
    banco()
def banco():
    banco = pyautogui.locateOnScreen('banco.png', confidence=0.75)
    if banco:
            print('banco')
            pyautogui.moveTo(789, 395)
            hacer_click()
            time.sleep(2)
            banco1 = pyautogui.locateOnScreen('banco1.png', confidence=0.75)
            if banco1:
                print(banco1)
                pyautogui.moveTo(banco1)
                hacer_click()
                time.sleep(2)
            ortiga = pyautogui.locateOnScreen('ortiga.png', confidence=0.75, region=(597, 230, 291, 543))
            if ortiga:
                pyautogui.moveTo(ortiga)
                guardar() 
                
            fresno = pyautogui.locateOnScreen('fresno.png', confidence=0.75, region=(597, 230, 291, 543))
            if fresno:
                
                pyautogui.moveTo(fresno)
                guardar() 
            agua = pyautogui.locateOnScreen('agua.png', confidence=0.75, region=(597, 230, 291, 543))
            if agua:
                
                pyautogui.moveTo(agua)
                guardar() 
            agu = pyautogui.locateOnScreen('ag.png', confidence=0.75, region=(597, 230, 291, 543))
            if agu:
                
                pyautogui.moveTo(agu)
                guardar() 
            valor0()
def valor0():
    valor0 = pyautogui.locateOnScreen('valor0.png', confidence=0.85)
    if valor0:
        pyautogui.moveTo(875, 253)
        print('valor0 saliendo del banco')
        keyboard.press('esc')
        print('valor0')   
        hacer_click()
        time.sleep(5)
        pyautogui.moveTo(397, 657)
        hacer_click()
        time.sleep(10)
        pyautogui.moveTo(627, 888)
        hacer_click()
        time.sleep(5)


def regresando():
    regresando = pyautogui.locateOnScreen('regresando.png', confidence=0.75)
    if regresando:
        pyautogui.moveTo(1251, 402)
        hacer_click()
        time.sleep(5)
    regresando1 = pyautogui.locateOnScreen('regresando1.png', confidence=0.75)
    if regresando1:
        pyautogui.moveTo(1251, 402)
        hacer_click()
        time.sleep(5)
    regresando2 = pyautogui.locateOnScreen('regresando2.png', confidence=0.75)
    if regresando2:
        pyautogui.moveTo(530, 30)
        hacer_click()
        time.sleep(5)
    regresando3 = pyautogui.locateOnScreen('regresando3.png', confidence=0.75)
    if regresando3:
        pyautogui.moveTo(530, 30)
        hacer_click()
        time.sleep(10)
    regresando4 = pyautogui.locateOnScreen('regresando4.png', confidence=0.75)
    if regresando4:
        pyautogui.moveTo(688, 293)
        hacer_click()
        time.sleep(20)
        pyautogui.moveTo(603, 267)
        hacer_click()
        time.sleep(20)
        pyautogui.moveTo(40, 468)
        hacer_click()
        time.sleep(20)
    regresando5 = pyautogui.locateOnScreen('regresando5.png', confidence=0.75)
    if regresando5:
        pyautogui.moveTo(290, 905)
        hacer_click()
        time.sleep(5)
        pyautogui.moveTo(53, 438)
        hacer_click()
        time.sleep(5)


def guardar():
    # Ejemplo de uso
    arrastrar_click(285, 673)

def aceptar():
    aceptar = pyautogui.locateOnScreen('aceptar.png', confidence=0.75)
    if aceptar:
        time.sleep(1)
        pyautogui.moveTo(aceptar)
        time.sleep(1)
        hacer_click()


def arrastrar_click(fin_x, fin_y):

    pyautogui.mouseDown()
    time.sleep(0.05)

    # Arrastrar a la posición final
    pyautogui.moveTo(fin_x, fin_y, duration=0.2)

    # Soltar el clic
    pyautogui.mouseUp()
    time.sleep(2)
    aceptar()
    time.sleep(2)
def map_bugs():
    zaap = pyautogui.locateOnScreen('bug/zaap.png', confidence=0.75)
    if zaap:
        west()
        time.sleep(4)


def encontrar_batalla(imagen_batalla):
    oficio()
    while True:  # Bucle infinito
        listo = pyautogui.locateOnScreen('listo.png', confidence=0.85)
        if listo:
            keyboard.press('F1')
            time.sleep(1)
            keyboard.press('F1')
            time.sleep(1)
            keyboard.press('F1')
            time.sleep(1)
        battle = pyautogui.locateOnScreen(imagen_batalla, confidence=0.85)
        if battle:
            time.sleep(1)  # Esperar 1 segundo
            for _ in range(3):  # Repetir la acción 3 veces
                keyboard.send('2')  # Simular el envío del botón 2
                pyautogui.moveTo(battle)  # Mover el cursor a la imagen 'battle'
                hacer_click()  # Hacer clic sobre la imagen 'battle'
                time.sleep(1)
            keyboard.press('F1')
            time.sleep(1)
            keyboard.press('F1')
        else:
            break  # Salir del bucle si la imagen 'battle' no está en pantalla



def batalla():
        encontrar_batalla('battle.png')
        encontrar_batalla('battle/mgrande.png')
        encontrar_batalla('battle/mpe.png')
        imagen = pyautogui.locateOnScreen('battle/retos.png', confidence=0.75)

        if imagen is not None:
            # Si la imagen está en la pantalla, presiona F1 tres veces
            for _ in range(3):
                keyboard.press('f1')
                time.sleep(0.5)  # Espera medio segundo entre cada pulsación

            # Revisa nuevamente después de un corto período de tiempo
            time.sleep(2)
    
    
while True:
    map_bugs()
    batalla()
    map_1()
    map_02()
    map_03()
    map_04()
    map_bugs()
    batalla()
    map_05()
    map_06()
    map_09()
    map_bugs()
    batalla()
    map_10()
    map_11()
    map_12()
    map_13()
    map_bugs()
    batalla()
    map_14()
    map_15()
    map_16()
    map_17()
    map_bugs()
    batalla()
    map_18()
    map_19()
    map_20()
    map_21()
    map_bugs()
    batalla()
    map_22()
    
    cap = pyautogui.locateOnScreen('cap.png', confidence=0.75)
    if cap:
            exit()
            astrub()
            banco()
            regresando()