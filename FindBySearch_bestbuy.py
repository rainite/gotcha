import time
from playsound import playsound

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


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
        self.logIn()

        # loop search
        findOne = False
        time.sleep(1)
        self.browser.find_element(By.CLASS_NAME, "search-input").send_keys(self.searchKey)
        while not findOne:
            time.sleep(2)
            self.browser.find_element(By.CLASS_NAME, "header-search-button").click()
            # loop item
            time.sleep(1)
            findOne = self.isItemAvailable()

            # find one
            if findOne:
                time.sleep(2)
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
        input("Please log in to home page")
        time.sleep(2)

    def isItemAvailable(self):
        itemClassList = self.browser.find_elements(By.CLASS_NAME, "sku-item")
        for itemClass in itemClassList:
            try:
                addCart = itemClass.find_element(By.CLASS_NAME, "add-to-cart-button")
                if "out".upper() not in str(addCart.text).upper() and ("coming".upper() not in str(addCart.text).upper()):
                    ActionChains(self.browser).move_to_element(addCart).perform()
                    time.sleep(1)
                    addCart.click()
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
        try:
            self.browser.find_element(By.CLASS_NAME, "go-to-cart-button").click()
            time.sleep(2)
            self.browser.find_element(By.CLASS_NAME, "checkout-buttons__checkout").click()
        except:
            return


# entry point
Main().start()
