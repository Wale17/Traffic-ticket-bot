from RPA.Browser.Selenium import Selenium
from utilities import handler_process_utils
from service import captcha_solver
import re
from time import sleep
# from RPA.Robocorp.WorkItems import WorkItems


browser = Selenium()
# workitem = WorkItems()

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
        for i in range(2):
            try:
                browser.screenshot("//img[@alt='Security Code']", "captcha.png")
                captcha_solution = captcha_solver.twocaptcha_solver("captcha.png")
                browser.input_text("//input[@id='captcha_user_text']", captcha_solution)
                browser.click_button("//input[@value='Buscar']")
                sleep(5)
                if browser.is_element_visible("//font[@color='red']"):
                    continue
                elif browser.is_element_visible("//body[1]/form[1]/center[4]/table[1]/tbody[1]/tr[1]/td[1]/table[1]"):
                    break
                elif browser.is_element_visible("//b[contains(text(),'NO se encontraron registros de comparendos para es')]"):
                    browser.clear_element_text("//input[@id='placa_veh']")
                    if doc_type == "CC":
                        browser.select_from_list_by_value("*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[2]/td/select']", "1")
                    elif doc_type == "NIT":
                        browser.select_from_list_by_value("//select[@name='tipo_documento']", "2")
                    elif doc_type == "CE":
                        browser.select_from_list_by_value("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[2]/td/select", "3")
                    elif doc_type == "TI":
                        browser.select_from_list_by_value("//select[@name='tipo_documento']", "4")
                    elif doc_type == "PA":
                        browser.select_from_list_by_value("//select[@name='tipo_documento']", "5")
                    else:
                        handler_process_utils.handle_error("invalid doc type")
                    browser.input_text("//input[@id='numero_identificacion']", doc_number)
                    for i in range(2):
                        try:
                            browser.screenshot("//img[@alt='Security Code']", "captcha.png")
                            captcha_solution = captcha_solver.twocaptcha_solver("captcha.png")
                            browser.input_text("//input[@id='captcha_user_text']", captcha_solution)
                            browser.click_button("//input[@value='Buscar']")
                            sleep(5)
                            if browser.is_element_visible("//font[@color='red']"):
                                continue
                            elif browser.is_element_visible("//tbody/tr[2]/td[1]/table[1]"):
                                break
                            elif browser.does_page_contain_element("//b[contains(text(),'NO se encontraron registros de comparendos para es')]"):
                                handler_process_utils.raise_error("No result found for both plate number and doc number")
                        except Exception as e:
                            raise(e)
                    else:
                        handler_process_utils.raise_error("couldn't solve captcha")       
            except Exception as e:
                raise(e)                
        else:
            handler_process_utils.raise_error("couldn't find comparendos for both plate number and doc number")
            
    return 1
    
def scrapr_from_the_initial_table(row_number, comparendo_list):
    if row_number >= 4 and len(comparendo_list) != 0:
        try:
            comparendo_dict = {}
            regex1 = '(?<=\[)[^][]*(?=])'
            regex2 = '(\-(.*))'
            for i in comparendo_list:
                if browser.does_page_contain_element("//body[1]/form[1]/center[4]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[{0}]".format(row_number+2)):
                    comparendo_dict[i] = browser.get_text("//body[1]/form[1]/center[4]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[{1}]/td[{0}]".format(comparendo_list.index(i)+1, row_number))
                else:
                    return ""
            browser.click_element("//*[@id='form1']/center[4]/table/tbody/tr/td/table/tbody/tr[{0}]/td[14]/a".format(row_number))
            comparendo_dict["comparendo_id_number"] = browser.get_text("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[5]/td[1]/span")
            comparendo_dict["comparendo_id_type"] = browser.get_text("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[5]/td[2]/span")
            Contravención = browser.get_text("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[8]/td/span")
            comparendo_dict["comparendo_infraction_detail"] = re.findall(regex1, Contravención)[0]
            comparendo_dict["comparendo_titular_name"] = re.findall(regex2, Contravención)[0][0]
            comparendo_dict["comparendo_notification_date"] = browser.get_text("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[7]/td[2]/span")   
            if browser.is_element_visible("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[14]/td/span"):
                if browser.get_text("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[12]/td/span") == "VER IMAGEN":
                    comparendo_dict["comparen_link"] = browser.get_element_attribute("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[12]/td/span/a", "href")
                if browser.get_text("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[13]/td/span") == "VER NOTIFICACIÓN":
                    comparendo_dict["comparendo_notification_link"] = browser.get_element_attribute("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[13]/td/span/a", "href")
            else:
                if browser.get_text("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[11]/td/span") == "VER IMAGEN":
                    comparendo_dict["comparen_link"] = browser.get_element_attribute("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[11]/td/span/a", "href")
                if browser.get_text("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[12]/td/span") == "VER NOTIFICACIÓN":
                    comparendo_dict["comparendo_notification_link"] = browser.get_element_attribute("//*[@id='form1']/table[1]/tbody/tr/td/table/tbody/tr[12]/td/span/a", "href")
            browser.go_back()
            sleep(3)
            browser.select_frame("mainFrame")
            del comparendo_dict["dummy"]
            return comparendo_dict
        except Exception as e:
            handler_process_utils.raise_error(e)
    else:
        handler_process_utils.raise_error("Please check your parameters, row_nos must not be less than 4 and comparendo list must not be empty")

