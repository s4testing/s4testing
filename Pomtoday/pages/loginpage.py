import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from s4testing.Pomtoday.locators.location import locators2

class loginpages:

    def loginpage(self):
        lc = locators2()
        path = "C:/Users/phyne/Desktop/chromedriver_win32/chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.maximize_window()
        driver.get(lc.url)
        driver.find_element(By.ID, lc.loginId).click()

        driver.implicitly_wait(10)

        loginfield = driver.find_element(By.XPATH, lc.username)
        loginfield.send_keys('testmorning')
        driver.find_element(By.XPATH, lc.password).send_keys('test123')
        driver.find_element(By.XPATH, lc.button).click()
        time.sleep(5)
        driver.quit()



