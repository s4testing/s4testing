import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.location import locators2 as lc


class contactpages:

    def contact(self):

        path = 'C:\\Selenium\\chromedriver.exe'  # this is defined as a path value
        driver = webdriver.Chrome(path)  # determining the driver in which browser should it work
        driver.get(lc.url)  # opening url of the site
        driver.maximize_window()  # maximizes the browser

        Contact = driver.find_element(By.XPATH, lc.contact)

        Contact.click()
        driver.implicitly_wait(5)
        Email = driver.find_element(By.ID, lc.emailId)

        Email.send_keys("Test1@email")

        driver.find_element(By.ID, lc.recepientName).send_keys("Test Name")

        driver.find_element(By.ID, lc.textMessage).send_keys("Message 1")

        driver.find_element(By.XPATH, lc.submitButton).click()

        # freezes code
        time.sleep(5)

        # quiting the browser
        driver.quit()