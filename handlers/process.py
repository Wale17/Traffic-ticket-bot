from RPA.Browser.Selenium import Selenium
from utilities import handler_process_utils
from time import sleep


browser = Selenium()

def open_webpage(url):
    if url == "":
        handler_process_utils.raise_error("Harcoded url is empty")
    else:
        for trial in range(1):
            try:
                browser.open_available_browser(url)
                print(browser.is_element_visible("//input[@id='numero_identificacion']"))
                sleep(5)
                print(browser.is_element_visible("//input[@id='numero_identificacion']"))
                sleep(5)
                print(browser.is_element_visible("//input[@id='numero_identificacion']"))
                sleep(5)
                print(browser.is_element_visible("//input[@id='numero_identificacion']"))
                sleep(5)
                print(browser.is_element_visible("//input[@id='numero_identificacion']"))
                if browser.is_element_visible("//input[@id='numero_identificacion']"):
                    print(browser.is_element_visible("//input[@id='numero_identificacion']"))
                    break
            except Exception as e:
                handler_process_utils.handle_error(e)
        # else:
        #     handler_process_utils.raise_error("Please check website url")//input[@id='numero_identificacion']