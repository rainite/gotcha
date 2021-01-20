import time
from py_imessage import imessage

from selenium import webdriver
from selenium.webdriver.common.by import By

# All wait times are needed to avoid being marked as bot
""" 
Must use a MAC and an iPhone to receive the notification. Mac should login with a different account from your iPhone,
otherwise iPhone won't alert notifications for iMessage

Alter key word in filterSet manually to exclude item in notification
"""

class Main:
    browser = None
    filterSet = {"Yeston"}
    phone = input("Input your iPhone number: ")
    searchKey = input("Input search key word, eg: rtx 3080: \n")
    searchKey = searchKey.replace(" ", "+")
    searchURL = "https://www.newegg.com/p/pl?d=" + searchKey + "&N=100007709&isdeptsrh=1&PageSize=96"

    def start(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.searchURL)
        time.sleep(5)
        self.closePopUpWindow()

        findOne = False
        # loop search
        while True:
            if findOne:
                time.sleep(60)
                findOne = False
            time.sleep(1)
            self.browser.get(self.searchURL)

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
