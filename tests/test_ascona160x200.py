from selenium import webdriver
from pages.main_page import Main_page
import pytest

driver = webdriver.Chrome()

base_url = 'https://mnogosna.ru/'
driver.get(base_url)
driver.maximize_window()

@pytest.fixture()
def set_up():
    print("mnogosna.ru")

def test_ascona(set_up):
    mp = Main_page(driver)
    mp.search_send_data()
