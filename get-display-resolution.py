import pywhatkit
import pyautogui

screenWidth, screenHeight = pyautogui.size()

print(screenWidth, screenHeight)

pyautogui.alert(text=f'Ekran Genişliği: {screenWidth}, Ekran Yüksekliği: {screenHeight}', title='Ekran Çözünürlüğü')