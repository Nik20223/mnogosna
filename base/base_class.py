import os
import time
from datetime import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

    ### Assert text-on-element in page ###
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Assertation True")


    ### Making screenshots to folder /pages/screenshots ###
    def screenshot(self):
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        path = os.getcwd()
        self.driver.save_screenshot(os.path.abspath(os.path.join(path, os.pardir)) + '/screenshots/' + name_screenshot)
        time.sleep(1)
        print("Make screenshot to folder Screenshots")