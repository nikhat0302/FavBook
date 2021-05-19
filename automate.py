import pyautogui
import time
import os

time.sleep(2)
os.startfile(r"C:\ProgramData\Nikhat Parween\WhatsApp\WhatsApp.exe")
print(pyautogui.locateOnScreen("gallery/whatsapp.png",grayscale=True,confidence=.5))
print(pyautogui.displayMousePosition())
text_list=["Hello", " how are you?", "I am nikhat"]
pyautogui.click(470,322)
pyautogui.click(1138,887)
for i in range(4):
    pyautogui.write(text_list[i],interval=.2)
    pyautogui.click(1555,887)
