import random
import time
from playsound import playsound

from selenium import webdriver
from selenium.webdriver.common.by import By


def playSound():
    while True:
        time.sleep(0.2)
        playsound("alart.wav")


# All wait times are needed to avoid being marked as bot

class Main:
    browser = None
    searchKey = "3080 combo"

    def start(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.newegg.com/#")
        time.sleep(5)
        self.closePopUpWindow()

        # log in
        input("please log in to main page")

        # search
        # first time search
        searchBox = self.browser.find_element_by_class_name("header2020-search-box")
        searchBox.find_element_by_xpath(".//input").send_keys(self.searchKey)
        # loop search
        findOne = False
        while not findOne:
            time.sleep(1)
            searchButton = self.browser.find_element_by_class_name("header2020-search-button")
            searchButton.find_element_by_xpath(".//button").click()

            # loop item
            time.sleep(2)
            itemList = self.browser.find_elements_by_class_name("item-cell")
            random.shuffle(itemList)
            for item in itemList:
                try:
                    button = item.find_element_by_class_name("item-button-area")
                    buttonText = button.find_element_by_xpath(".//button")
                    if buttonText.text != "AUTO NOTIFY" and buttonText.text != "VIEW DETAILS":
                        print("find one: " + item.text)
                        buttonText.click()
                        try:
                            self.browser.find_element(By.CLASS_NAME, "close").click()
                            buttonText.click()
                        except:
                            print("No pop-up window comes up")

                        findOne = True
                        break
                except:
                    continue

            # find one
            if findOne:
                time.sleep(1)
                self.tryCheckOut(0)
                playSound()

    def logIn(self):
        def clickSignIn(text):
            signInList = self.browser.find_elements_by_class_name("form-cell")
            for element in signInList:
                if text.upper() in str(element.text).upper():
                    element.click()
                    break
        # log in
        if self.browser.find_element_by_class_name("nav-complex-inner"):
            link = self.browser.find_element_by_class_name("nav-complex-inner").get_attribute('href')
            self.browser.get(link)
            accountName = input("Enter email: ")
            self.browser.find_element(By.ID, "labeled-input-signEmail").send_keys(accountName)
            clickSignIn("sign in")

            time.sleep(2)
            secKey = input("Enter email Security Code:")
            divList = self.browser.find_elements_by_class_name("form-v-code")
            divList[0].find_element_by_xpath(".//input").send_keys(secKey)
            clickSignIn("sign in")
            time.sleep(1)

    def isItemAvailable(self):
        itemClassNames = ["btn-primary", "atnPrimary"]
        try:
            for className in itemClassNames:
                buttons = self.browser.find_elements(By.CLASS_NAME, className)
                for button in buttons:
                    if "cart".upper() in str(button.text).upper():
                        self.closePopUpWindow()
                        # add to cart
                        button.click()
                        desc = self.browser.find_element(By.CLASS_NAME, "product-title")
                        print(desc.text)
                        return True
        except:
            return False
        return False

    def closePopUpWindow(self):
        try:
            self.browser.find_element_by_class_name("close").click()
        except:
            return

    def tryCheckOut(self, times):
        if times > 1:
            return
        buttonNames = ["btn-undefined", "btn-primary"]
        for button in buttonNames:
            try:
                buttons = self.browser.find_elements(By.CLASS_NAME, button)
                for b in buttons:
                    if "checkout".upper() in str(b.text).upper():
                        b.click()
                        time.sleep(1)
                        self.tryCheckOut(times + 1)
                        return
            except:
                return

# entry point
Main().start()
