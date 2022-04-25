import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\mgirish\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

def log():
      try:
        flipkart_home="https://www.flipkart.com/"
        driver.get(flipkart_home)
        driver.implicitly_wait(3)
        driver.maximize_window()

        #get the user name
        username=driver.find_element(by=By.XPATH,value="//input[@class='_2IX_2- VJZDxU']")
        #Get the password Field
        password=driver.find_element(by=By.XPATH,value="//input[@class='_2IX_2- _3mctLh VJZDxU']")

        #Submit click
        login=driver.find_element(by=By.XPATH,value="//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")

        #send to login Credintial
        username.send_keys("7205502460")
        password.send_keys("Giri@9040")
        login.click()
        print("login Successfull")

      except:
       print("")


if __name__ == "__main__":
    log()
