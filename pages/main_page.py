import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
topper_text = 'Топперы Аскона 160х200'
topper_url = ''
class Main_page(Base):
    url = 'https://mnogosna.ru'

    # Locators

    search_window = "//input[@type='search']"
    search_window2 = "//input[@id='search-input']"
    home_button = "//a[@href='/']"
    # topper_link = "(//div[@class='slinks__link'])[1]"
    topper_link = "(//a[@class='slinks__item js-popular-search-request'])[1]"
    ascona_fitness_link = "//img[@alt='Матрас Аскона Фитнес Формула 160x200']"



    # Getters

    def get_search_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_window)))
    def get_search_window2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_window2)))
    def get_home_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.home_button)))

    def get_topper_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.topper_link)))
    def get_ascona_fitness_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ascona_fitness_link)))

    # Actions
    ### Search keywords and assert results ###
    def search_send_data(self):
        self.get_home_button().click()
        self.get_search_window().click()
        time.sleep(1)
        self.get_search_window2().send_keys('матрас аскона 160х200')
        print("Отправляем в поле поиска фразу")
        time.sleep(2)
        print("Проверяем первый результат поиска (ссылка)")
        src = self.get_topper_link().get_attribute('href')
        # self.assert_word(src, topper_text)
        print(src)
        print("Проверяем первый результат поиска (текст)")
        self.assert_word(self.get_topper_link(), topper_text)

        print(self.get_topper_link().text)
        time.sleep(2)
        src = self.get_ascona_fitness_link().get_attribute('src')
        print(src)
