from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time


driver = webdriver.Firefox(executable_path="C:\\Users\\ZoneTech\\Desktop\\Instagram\\geckodriver.exe")
driver.maximize_window()
driver.get('https://instagram.com')
driver.implicitly_wait(5)
driver.find_element_by_name("username").send_keys("You'r username here")
driver.find_element_by_name("password").send_keys("You'r password here")
driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div").click()
time.sleep(5)

driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
time.sleep(3)
driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(2) > a > svg').click()
time.sleep(3)
driver.find_element_by_css_selector('#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.oNO81 > div.Igw0E.IwRSH.eGOV_._4EzTm.i0EQd > div > div > div > div > div:nth-child(2) > a > div').click()
time.sleep(3)

for i in range(7):
    driver.find_element_by_css_selector('#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea').click()
    text = "you'r text"
    for e in text:
        pyautogui.typewrite(e)
        time.sleep(.3)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

time.sleep(3)
driver.close()
print("Done Boss")
