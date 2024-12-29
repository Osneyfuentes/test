import pyautogui
import os
import time

def esperar_imagen(nombre_imagen, tiempo_espera=0.5):
    """Espera hasta que una imagen específica aparezca en la pantalla."""
    while True:
        ubicacion = pyautogui.locateOnScreen(f'objetos/{nombre_imagen}.png', confidence=0.85)
        if ubicacion:
            print(f"Imagen {nombre_imagen} encontrada.")
            break
        time.sleep(tiempo_espera)

def buscar():
    # Recorrer todas las imágenes en la carpeta 'objetos'
    for archivo in os.listdir('objetos'):
        if archivo.endswith('.png'):
            ruta_imagen = os.path.join('objetos', archivo)
            ubicacion = pyautogui.locateOnScreen(ruta_imagen, confidence=0.85)
            if ubicacion:
                pyautogui.moveTo(ubicacion)
                hacer_click()
                time.sleep(1)  # Puedes ajustar este tiempo de espera según sea necesario

def hacer_click():
    pyautogui.click()

# Ejemplo de cómo podrías llamar a la función esperar_imagen
if __name__ == "__main__":
    buscar()
    esperar_imagen("nombre_imagen_del_mapa_2")  # Cambia "nombre_imagen_del_mapa_2" por el nombre real del archivo de imagen del mapa
    # Realiza acciones después de que la imagen del mapa 2 se detecte...
