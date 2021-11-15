from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome('C:/Users/ziado/chromedriver_win32/chromedriver.exe')
driver.get('https://www.google.it/')

driver.find_elements_by_id("L2AGLb").send_keys(Keys.ENTER)