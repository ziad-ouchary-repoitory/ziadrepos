from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import getpass
import serial.tools.list_ports

user = input("Username Insta: ")
pwd = getpass.getpass("Password Insta: ")

ports = serial.tools.list_ports.comports()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

serialInstance = serial.Serial(portVar, 9600, timeout = 1)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach" , True)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\ziado\chromedriver_win32\chromedriver.exe')

driver.get('https://www.instagram.com/')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="aOOlW  bIiDR  "]'))).click()

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

username.send_keys(user)
time.sleep(1.5)
password.send_keys(pwd)
time.sleep(7)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="sqdOP  L3NKy   y3zKF     "]'))).click()
time.sleep(10)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="sqdOP yWX7d    y3zKF     "]'))).click()
time.sleep(10)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="aOOlW   HoLwm "]'))).click()
time.sleep(10)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="xWeGp"]'))).click()

while (True):
    time.sleep(10)
    bhoStatus = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[2]/div[2]/div/div/span/span')
    status = bhoStatus.text

    if (status == 'Attivo/a ora'):
        print('È Online!')
        serialInstance.write("on".encode())
        time.sleep(30)
        driver.refresh()
    else:
        isOnline = status.replace('Attivo/a', '')
        print('Ultimo accesso ', isOnline)
        serialInstance.write("off".encode())
        time.sleep(30)
        driver.refresh()
        
    
