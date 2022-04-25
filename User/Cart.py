import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def cart():
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
    #
    title=driver.title
    time.sleep(2)
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.XPATH, "//*[@alt='Fashion']")).perform()
    time.sleep(1)
    a.move_to_element(driver.find_element(By.LINK_TEXT, "Women Ethnic")).perform()
    driver.find_element(By.LINK_TEXT, "Women Sarees").click()
    driver.find_element(By.XPATH,
                        '//*[@id="container"]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/a/div[1]').click()
    time.sleep(4)
    fashion_list = driver.find_elements(by=By.XPATH, value='//div[@class="_2hVSre _1DmLJ5 -o7Q4n"]')
    time.sleep(3)
    j = 1
    for i in fashion_list:
        if j <= 2:
            i.click()
            # driver.find_element(by=By.XPATH, value='//div[@class="_2hVSre _1DmLJ5 -o7Q4n"]').click()
            j = j + 1
    # Verifying wishlist
    a = ActionChains(driver)
    a.move_to_element(driver.find_element(By.CSS_SELECTOR, ".go_DOp:nth-child(3) .exehdJ")).perform()
    time.sleep(6)
    driver.find_element(By.CSS_SELECTOR, '.\_2NOVgj:nth-child(5) > .\_2kxeIr').click()
    time.sleep(6)
    wish_list_count = driver.find_element(By.CSS_SELECTOR, '.\_3FVYY1 > span').text
    print(wish_list_count)
    wish_listed = ''
    for i in wish_list_count:
        if i.isdigit():
            wish_listed = wish_listed + str(i)
        assert wish_listed ==2, 'More than 2 items are added'





if __name__ == "__main__":
     cart()
