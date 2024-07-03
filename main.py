from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys  # to give us access to enter key, escape key, etc
import os
import dotenv

dotenv.load_dotenv()
PATH = "C:\Program Files (x86)\chromedriver-win64\chromedriver.exe"

cService = webdriver.ChromeService(executable_path=PATH)   # instantiate
options = webdriver.ChromeOptions()  # instantiate      
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service = cService, options=options)
global wait 
wait = WebDriverWait(driver, 10)

PASSWORD = os.environ['PASSWORD']

# use https://{username}:{password}@example.com when encounter pop up auth
driver.get(f"https://eldo0001:{PASSWORD}@loginfs.ntu.edu.sg/adfs/ls/wia?wtrealm=https%3a%2f%2fvenus2.wis.ntu.edu.sg%2fADFSSSO2%2fUser%2fLogin.aspx%2f&wctx=WsFedOwinState%3dKet50TI9KqUUJvhN0-JudB2NkmGDVt_IFdaju2KFITWWumiHM0nvvFb96FJjYHJBhPMXxnF8anuwHmnsVrSbI9kjBuM0emzDTkqZ5OqGb4KFcuEtNv6BNB_Oi33ovJJFDq8VK5-xJA0JfOJSjPl453jhkHtmV7DtfLHenAO-KUka4RHB8-NBSS5QopB-KJNPmwk2595OB3qXzsA7VQOGJuYZYh-uFYQEA2XdBD9EGsKdzPy5McmiGMS9d0he1HQA&wa=wsignin1.0&client-request-id=34a6fa7d-141c-4cbf-5b07-0080014400e0")

# userNameSearch = driver.find_element(By.ID, 'userNameInput')
# userNameSearch.send_keys('eldo0001@student.main.ntu.edu.sg')

# userPassword = driver.find_element(By.ID, 'passwordInput')
# # userPassword.send_keys(PASSWORD)

# submitButton = driver.find_element(By.ID, 'submitButton').click()

driver.implicitly_wait(5)
applyButton = driver.find_element(By.ID,'sd3')
applyButton.click()

badmintonButton = driver.find_element(By.CSS_SELECTOR,'[value = "1BB26"]')
badmintonButton.click()

driver.implicitly_wait(5)
#value format = 1BB2BB{courtNo}{date}{sessionNo}
session = driver.find_element(By.CSS_SELECTOR,'[value = "1BB2BB0209-Jul-20242"]')
session.click()

confirmButton = driver.find_element(By.CSS_SELECTOR,'[value = "Confirm"]')
confirmButton.click()

# driver.quit()



