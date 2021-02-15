from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox(executable_path="C:\\Users\\ZoneTech\\Desktop\\Instagram\\geckodriver.exe")
driver.maximize_window()
driver.get('https://instagram.com')
driver.implicitly_wait(5)
driver.find_element_by_name("username").send_keys("You'r username here")
driver.find_element_by_name("password").send_keys("You'r password here")
driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div").click()
time.sleep(5)

driver.get('https://www.instagram.com/fso0c1ety.exe/')
time.sleep(5)

for i in range(180):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//button[text()="Following"]').click()
    driver.find_element(By.XPATH, '//button[text()="Unfollow"]').click()
    time.sleep(2)
    driver.refresh()

time.sleep(5)
driver.close()
print("Done Boss Good To Goo")
