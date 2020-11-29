import time
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.common.by import By

URLs = [
    "https://www.newegg.com/asus-geforce-rtx-3080-rog-strix-rtx3080-o10g-gaming/p/N82E16814126457?Description=3080%20rtx&cm_re=3080_rtx-_-14-126-457-_-Product&quicklink=true",
    "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3897-kr/p/N82E16814487518?Description=3080%20rtx&cm_re=3080_rtx-_-14-487-518-_-Product&quicklink=true",
    "https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4190361",
    "https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4190357",
    "https://www.newegg.com/asus-geforce-rtx-3080-tuf-rtx3080-o10g-gaming/p/N82E16814126452?Description=3080%20rtx&cm_re=3080_rtx-_-14-126-452-_-Product",
    "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-gaming-x-trio-10g/p/N82E16814137597?Description=3080%20rtx&cm_re=3080_rtx-_-14-137-597-_-Product",
    "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3885-kr/p/N82E16814487520?Description=3080%20rtx&cm_re=3080_rtx-_-14-487-520-_-Product",
    "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080aorus-m-10gd/p/N82E16814932336?Description=3080%20rtx&cm_re=3080_rtx-_-14-932-336-_-Product",
    "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g-oc/p/N82E16814137598?Description=3080%20rtx&cm_re=3080_rtx-_-14-137-598-_-Product",
    "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-10gd/p/N82E16814932329?Description=3080%20rtx&cm_re=3080_rtx-_-14-932-329-_-Product",
    "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080eagle-oc-10gd/p/N82E16814932330?Description=3080%20rtx&cm_re=3080_rtx-_-14-932-330-_-Product",
    "https://www.newegg.com/asus-geforce-rtx-3080-tuf-rtx3080-10g-gaming/p/N82E16814126453?Description=3080%20rtx&cm_re=3080_rtx-_-14-126-453-_-Product",
    "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080vision-oc-10gd/p/N82E16814932337?Description=3080%20rtx&cm_re=3080_rtx-_-14-932-337-_-Product",
    "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080eagle-10gd/p/N82E16814932367?Description=3080%20rtx&cm_re=3080_rtx-_-14-932-367-_-Product",
    "https://www.newegg.com/asus-geforce-rtx-3080-tuf-rtx3080-10g-gaming/p/N82E16814126453?Description=3080%20rtx&cm_re=3080_rtx-_-14-126-453-_-Product",
    "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080vision-oc-10gd/p/N82E16814932337?Description=3080%20rtx&cm_re=3080_rtx-_-14-932-337-_-Product",
    "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080eagle-10gd/p/N82E16814932367?Description=3080%20rtx&cm_re=3080_rtx-_-14-932-367-_-Product",
    "https://www.newegg.com/msi-geforce-rtx-3080-rtx3080-suprim-x-10g/p/N82E16814137609?Description=3080%20rtx&cm_re=3080_rtx-_-14-137-609-_-Product",
    "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g/p/N82E16814137600?Description=3080%20rtx&cm_re=3080_rtx-_-14-137-600-_-Product",
    "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3883-kr/p/N82E16814487521?Description=3080%20rtx&cm_re=3080_rtx-_-14-487-521-_-Product",
    "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3881-kr/p/N82E16814487522?Description=3080%20rtx&cm_re=3080_rtx-_-14-487-522-_-Product",
    "https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4207523",
    "https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4207521",
    "https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4190359",
    "https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4190483",
    "https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4191565",
    "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3895-kr/p/N82E16814487519?Description=3080%20rtx&cm_re=3080_rtx-_-14-487-519-_-Product",
    "https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4190363&quicklink=true"
]
#need to test combo link and separate item link separately
testURLs = [
    "https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4190483",
    "https://www.newegg.com/asus-geforce-rtx-2070-dual-rtx2070-o8g/p/N82E16814126274?Description=2070&cm_re=2070-_-9SIAGKCBZH1643-_-Product",
    "https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4191565"

]


def playSound():
    while True:
        time.sleep(0.2)
        playsound("alart.wav")


class Main:
    browser = None

    def start(self, URLs):
        self.browser = webdriver.Chrome()
        for i in range(len(URLs)):
            self.browser.get(URLs[i])
            if i != len(URLs) - 1:
                self.browser.switch_to.new_window('tab')

        # we only need to log in one time
        # self.logIn()

        # loop refresh
        find = False
        while not find:
            for window in self.browser.window_handles:
                self.browser.switch_to.window(window)
                self.browser.refresh()

                find = self.isItemAvailable()

                # find & checkout
                if find:
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
main = Main()
main.start(["https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4205209"])
