import time
from playsound import playsound

from selenium import webdriver
from selenium.webdriver.common.by import By


def playSound():
    while True:
        time.sleep(0.2)
        playsound("alart.wav")


class Main:
    browser = None

    def __init__(self):
        self.browser = webdriver.Chrome()

    def start(self):
        self.browser.get("https://www.newegg.com/#")
        time.sleep(5)
        try:
            self.browser.find_element_by_class_name("close").click()
        except:
            print("No pop-in window, skip")

        # log in
        if self.browser.find_element_by_class_name("nav-complex-inner"):
            link = self.browser.find_element_by_class_name("nav-complex-inner").get_attribute('href')
            self.browser.get(link)
            self.browser.find_element(By.ID, "labeled-input-signEmail").send_keys("kevinchenlife@gmail.com")
            self.clickSignIn("ONE-TIME")

            time.sleep(2)
            secKey = input("Enter email Security Code:")
            divList = self.browser.find_elements_by_class_name("form-v-code")
            divList[0].find_element_by_xpath(".//input").send_keys(secKey)
            self.clickSignIn("sign in")
            time.sleep(1)

        # search
        # first time search
        searchBox = self.browser.find_element_by_class_name("header2020-search-box")
        searchBox.find_element_by_xpath(".//input").send_keys("3080 rtx")
        # loop search
        findOne = False
        while not findOne:
            time.sleep(2)
            searchButton = self.browser.find_element_by_class_name("header2020-search-button")
            searchButton.find_element_by_xpath(".//button").click()
            filterItems = self.browser.find_elements_by_class_name("filter-box-list")
            for item in filterItems:
                if "graphics card".upper() in str(item.text).upper():
                    item.click()
                    break
            itemList = self.browser.find_elements_by_class_name("item-cell")

            # loop item
            time.sleep(1)
            for item in itemList:
                try:
                    button = item.find_element_by_class_name("item-button-area")
                    buttonText = button.find_element_by_xpath(".//button")
                    if buttonText.text != "AUTO NOTIFY":
                        print("find one: " + item.text)
                        buttonText.click()
                        findOne = True
                        break
                except:
                    continue

            # find one
            if findOne:
                summary = self.browser.find_element_by_class_name("item-actions")
                cartButtons = summary.find_elements_by_xpath(".//button")
                time.sleep(1)
                for button in cartButtons:
                    if "Checkout".upper() in str(button.text).upper():
                        button.click()
                        break
                playSound()

    def clickSignIn(self, text):
        signInList = self.browser.find_elements_by_class_name("form-cell")
        for element in signInList:
            if text.upper() in str(element.text).upper():
                element.click()
                break