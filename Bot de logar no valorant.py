
import pyautogui
import time

pyautogui.alert("O código vai começar! Não utilize nada do computador até o código finalizar!")
pyautogui.PAUSE = 1

pyautogui.press('winleft')
pyautogui.write('Valorant')
pyautogui.press('enter')
time.sleep(7)

pyautogui.moveTo(284,366)
pyautogui.click()
pyautogui.write('tevonrs')

pyautogui.moveTo(273,433)
pyautogui.click()
pyautogui.write('colocar senha aqui')

pyautogui.moveTo(394, 796)
pyautogui.click()
time.sleep(5)
pyautogui.moveTo(375, 908)
pyautogui.click()


pyautogui.alert("O código já foi finalizado, Estevão! Aproveite seu jogo.")






