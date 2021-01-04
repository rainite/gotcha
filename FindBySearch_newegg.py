import time
from py_imessage import imessage

from selenium import webdriver
from selenium.webdriver.common.by import By

# All wait times are needed to avoid being marked as bot

class Main:
    browser = None
    filterSet = {"Yeston"}
    phone = input("Input your iPhone number: ")

    def start(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.newegg.com/p/pl?d=rtx+3080&N=100007709&isdeptsrh=1&PageSize=96")
        time.sleep(5)
        self.closePopUpWindow()

        findOne = False
        # loop search
        while True:
            if findOne:
                time.sleep(60)
                findOne = False
            time.sleep(1)
            self.browser.get("https://www.newegg.com/p/pl?d=rtx+3080&N=100007709&isdeptsrh=1&PageSize=96")

            # loop item
            time.sleep(1)
            itemList = self.browser.find_elements_by_class_name("item-cell")
            for item in itemList:
                filterout = False
                for s in self.filterSet:
                    if s.upper() in str(item.text).upper():
                        filterout = True
                        break
                if filterout:
                    continue
                try:
                    button = item.find_element_by_class_name("item-button-area")
                    buttonText = button.find_element_by_xpath(".//button")
                    if buttonText.text != "AUTO NOTIFY" and buttonText.text != "VIEW DETAILS":
                        print("find one: " + item.text)
                        href = item.find_element(By.CLASS_NAME, "item-title").get_attribute('href')
                        findOne = True
                        imessage.send(self.phone, href)
                        time.sleep(2)
                except:
                    continue

    def closePopUpWindow(self):
        try:
            self.browser.find_element_by_class_name("close").click()
        except:
            return

# entry point
Main().start()
