"""
# introdução a projetos dautomatizados em Python
# Projeto utilizando a biblioteca Pyautogui
# Minicurso de automação https://pages.hashtagtreinamentos.com/minicurso-python-automacao?blog=1n4033rer&video=3dep762tr
# https://pyautogui.readthedocs.io/en/latest/
# intalar o Pyautogui => pip install pyautogui

#* pode ser preciso instalar o pydirectInput
pip install pydirectinput

#instalar as dependecias
sudo dnf    install scrot
sudo dnf install python3-tk
sudo dnf install python3-dev

#instalar pyautogui no fedora
pip3 install --user python3-xlib
pip3 install --user pyautogui
"""

import keyboard
import pyautogui
import time

pyautogui.alert('Vai começar!')
pyautogui.PAUSE = 1
# Abrir o firefox
# time.sleep(5)
# pyautogui.KEYBOARD_KEYS


print(pyautogui.position())

# pyautogui.move(x=1838, y=15)
# pyautogui.hotkey('alt', 'tab')
pyautogui.click(x=1838, y=15)
pyautogui.click()

time.sleep(5)


# abrir uma nova aba ctrl + t

# acessar o site
# https://www.tce.ce.gov.br/cidadao/diario-oficial-eletronico

# fazer o download

pyautogui.alert('Terminou')
