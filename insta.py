from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options 
  
usr=input('Enter Email Id:')  
pwd=input('Enter Password:')  
  
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://www.instagram.com/') 
print ("Opened instagram") 
sleep(1) 
  
username_box = driver.find_element_by_name('username')
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_name('password')
password_box.send_keys(pwd) 
print ("Password entered") 
login_box = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div") 
login_box.click() 
sleep(8)

driver.get('https://www.instagram.com/explore/people/suggested/')
print('opend account')
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)

Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")
Follow_Button.click()
sleep(3)
driver.refresh()
sleep(4)

print ("Good to go boss") 
input('Quit whenever you whant') 
driver.quit() 
print("Finished") 