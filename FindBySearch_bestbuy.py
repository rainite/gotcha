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
    filterSet = {}
    searchKey = "rtx 3080"

    def start(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.bestbuy.com/")
        time.sleep(3)
        self.closePopUpWindow()

        # log in
        # self.logIn()

        # loop search
        findOne = False
        while not findOne:
            time.sleep(2)
            self.browser.find_element(By.CLASS_NAME, "search-input").send_keys(self.searchKey)
            self.browser.find_element(By.CLASS_NAME, "header-search-button").click()
            # loop item
            time.sleep(1)
            findOne = self.isItemAvailable()

            # find one
            if findOne:
                time.sleep(1)
                self.tryCheckOut()
                playSound()


    def logIn(self):
        # log in
        loginButtons = self.browser.find_elements(By.CLASS_NAME, "flyBtn")
        time.sleep(0.5)
        for b in loginButtons:
            if str(b.text).upper() == "account".upper():
                b.click()
                break
        time.sleep(1)
        self.browser.find_element(By.CLASS_NAME, "lam-signIn__button").click()
        input("type in email & password in web")
        self.browser.find_element(By.CLASS_NAME, "cia-form__controls__submit").click()
        time.sleep(2)

    def isItemAvailable(self):
        itemClassList = self.browser.find_elements(By.CLASS_NAME, "sku-item")
        for itemClass in itemClassList:
            try:
                itemClass.find_element(By.CLASS_NAME, "add-to-cart-button").click()
                return True
            except:
                return False
        return False

    def closePopUpWindow(self):
        try:
            self.browser.find_element(By.CLASS_NAME, "c-close-icon").click()
        except:
            return

    def tryCheckOut(self):
        self.browser.find_element(By.CLASS_NAME, "go-to-cart-button").click()
        time.sleep(1)
        self.browser.find_element(By.CLASS_NAME, "checkout-buttons__checkout").click()


# entry point
Main().start()
