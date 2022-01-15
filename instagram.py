import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium import webdriver

navegador = webdriver.Firefox()

navegador.get("https://www.instagram.com")
time.sleep(7)
navegador.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').click()
pyautogui.typewrite('tes@test.com')  # insert login
time.sleep(1)
navegador.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').click()
pyautogui.typewrite('XXXXXXX')  # insert password
time.sleep(1)
navegador.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button').click()
time.sleep(7)
navegador.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div').click()
pyautogui.typewrite('leillaj')  # insert profile
time.sleep(3)
navegador.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div').click()
time.sleep(3)
navegador.find_element(By.XPATH, '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div').click()
time.sleep(5)
navegador.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]').click()
time.sleep(1)
navegador.find_element(By.XPATH, '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()
time.sleep(2)
pyautogui.typewrite('Hi')  # insert message
pyautogui.hotkey('enter')
