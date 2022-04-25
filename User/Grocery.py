import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestData():
    Base_Url = "https://www.flipkart.com/"
    Chrome_Executable_Path = "C:\\Users\\mgirish\\Downloads\\chromedriver.exe"
    Username = "7205502460"
    Password = "Giri@9040"


class Test_Data:
    pass


def grocery():
    # Click Login
    s = Service("C:\\Users\\mgirish\\Downloads\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    flipkart_home = "https://www.flipkart.com/"
    driver.get(flipkart_home)
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.find_element(by=By.XPATH, value="//input[@class='_2IX_2- VJZDxU']").send_keys("7205502460")
    driver.find_element(by=By.XPATH, value="//input[@class='_2IX_2- _3mctLh VJZDxU']").send_keys("Giri@9040")
    driver.find_element(by=By.XPATH, value="//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
    #Action
    driver.find_element(By.CSS_SELECTOR, "\_2xm1JU").click()
    time.sleep(4)
    a = driver.find_elements(by=By.XPATH, value='//div[@class="xtXmba"]')
    for i in a:
        if i.text == 'Grocery':
            i.click()
    # ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "pincode")))
    time.sleep(6)
    driver.find_element(by=By.XPATH, value='//input[@class="_3704LK"]').send_keys(Test_Data.search_item)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//button[@class="L0Z3Pu"]').click()
    time.sleep(2)
    brand_select = driver.find_element(by=By.XPATH,
                                       value='//*[@id="container"]/div/div[3]/div[2]/div[1]/div/div/section[2]/div[2]/div/div[4]/div/label')
    brand_select.click()
    brand = brand_select.text.split(' ')
    print(brand)
    brand_data = driver.find_elements(by=By.CLASS_NAME, value='_2gX9pM')
    brand_list = []
    for i in brand_data:
        brand_list.append(i.text)
    assert brand[0] in brand_list[0], 'Filtered data is not showing'


if __name__ == "__main__":
    grocery()

