    uno = pyautogui.locateOnScreen('uno.png', confidence=0.85, region=(219, 273, 50, 50))
    if uno:
       pyautogui.moveTo(uno)
       hacer_click()
       time.sleep(4)

    dos = pyautogui.locateOnScreen('dos.png', confidence=0.85, region=(263, 502, 50, 50))
    if dos:
       pyautogui.moveTo(dos)
       hacer_click()
       time.sleep(4)

