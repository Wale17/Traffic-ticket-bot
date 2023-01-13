from RPA.Browser.Selenium import Selenium
from utilities import handler_process_utils
from service import captcha_solver
from time import sleep


browser = Selenium()

def open_webpage(url):
    if url == "":
        handler_process_utils.raise_error("Harcoded url is empty")
    else:
        for trial in range(2):
            try:
                browser.open_available_browser(url)
                browser.select_frame("mainFrame")
                if browser.is_element_visible("//input[@id='numero_identificacion']"):
                    break
            except Exception as e:
                handler_process_utils.handle_error(e)
        else:
            handler_process_utils.raise_error("Please check website url")

def make_search(doc_type, plate_number, doc_number):
    if plate_number != "" or plate_number != "null" or plate_number != None:
        browser.input_text("//input[@id='placa_veh']", plate_number)
        for i in range(1):
            try:
                browser.screenshot("//img[@alt='Security Code']", "captcha.png")
                captcha_solution = captcha_solver.twocaptcha_solver("captcha.png")
                browser.input_text("//input[@id='captcha_user_text']", captcha_solution)
                browser.click_button("//input[@value='Buscar']")
                sleep(5)
                if browser.is_element_visible("//font[@color='red']"):
                    continue
                elif browser.is_element_visible("//b[@xpath='1']"):
                    if doc_type == "CC":
                        browser.select_all_from_list("//select[@name='tipo_documento']", "1")
                    elif doc_type == "NIT":
                        browser.select_all_from_list("//select[@name='tipo_documento']", "2")
                    elif doc_type == "CE":
                        browser.select_all_from_list("//select[@name='tipo_documento']", "3")
                    elif doc_type == "TI":
                        browser.select_all_from_list("//select[@name='tipo_documento']", "4")
                    elif doc_type == "PA":
                        browser.select_all_from_list("//select[@name='tipo_documento']", "5")
                    browser.input_text("//input[@id='numero_identificacion']", doc_number)
                    for i in range(1):
                        try:
                            browser.screenshot("//img[@alt='Security Code']", "captcha.png")
                            captcha_solution = captcha_solver.twocaptcha_solver("captcha.png")
                            browser.input_text("//input[@id='captcha_user_text']", captcha_solution)
                            browser.click_button("//input[@value='Buscar']")
                            sleep(5)
                            if browser.is_element_visible("//font[@color='red']"):
                                continue
                        except Exception as e:
                            raise(e)
                    else:
                        handler_process_utils.raise_error("couldn't solve captcha")        
            except Exception as e:
                raise(e)
        else:
            handler_process_utils.raise_error("couldn't solve captcha")
    