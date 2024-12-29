import pyautogui
import keyboard
import time
import tkinter as tk
from tkinter import simpledialog
import pyscreeze
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

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

while True:
    ggsgs = pyautogui.locateOnScreen('ggsgs.png', confidence=0.85)
    if ggsgs:
        pyautogui.moveTo(ggsgs)
        hacer_click()
        safa = pyautogui.locateOnScreen('safa.png', confidence=0.85)
    if safa:
        pyautogui.moveTo(safa)
        hacer_click()
        hahahah = pyautogui.locateOnScreen('hahahah.png', confidence=0.85)
    if hahahah:
        pyautogui.moveTo(hahahah)
        hacer_click()
        time.sleep(2)
