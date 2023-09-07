import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
class Main_page(Base):
    url = 'https://mnogosna.ru'

    # Locators

    search_window = "//input[@type='search']"
    search_window2 = "//input[@id='search-input']"
    home_button = "//a[@href='/']"



    # Getters

    def get_search_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_window)))
    def get_search_window2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_window2)))
    def get_home_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.home_button)))

    def get_password(self):
        return self.driver.find_element(By.XPATH, self.password)

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_login_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_name)))

    # Actions
    ### Authorisation by sending username and password ###
    def search_send_data(self):
        self.get_home_button().click()
        self.get_search_window().click()
        time.sleep(5)
        self.get_search_window2().send_keys('матрас аскона 160х200')

        time.sleep(60)
