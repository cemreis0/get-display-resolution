import pyautogui

screenWidth, screenHeight = pyautogui.size()

print(screenWidth, screenHeight)

pyautogui.alert(text=f'Screen Width: {screenWidth}, Screen Height: {screenHeight}', title='Display Resolution')