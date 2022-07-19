import pyautogui

screenWidth, screenHeight = pyautogui.size()

pyautogui.alert(text=f'Screen Width: {screenWidth}, Screen Height: {screenHeight}', title='Display Resolution')