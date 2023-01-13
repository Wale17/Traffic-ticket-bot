# # +
import requests
import sys
import os
from twocaptcha import TwoCaptcha
from service import variable_producer
from RPA.Robocorp.Vault import Vault

vault = Vault()
twocaptcha_api_key = vault.get_secret("apikey")
decaptcha_secrets = vault.get_secret("decaptcha")
"""Function to solve captcha"""
def solve_captcha(filename):
    URL = "http://poster.de-captcher.com/"
    multipart_form_data = {
        'pict':     open(filename, 'rb'),
        'function': ('', 'picture2'),
        'username': ('', decaptcha_secrets["username"]),
        'password': ('', decaptcha_secrets["password"])
    }


    iteracion = 0
    resultCode = 1
    captchaText = ''

    response = requests.post(URL, files=multipart_form_data)
    iteracion += 1

    print(response.content)

    respuesta = str(response.content, 'utf-8').split('|')

    for r in respuesta:
        print(r)

    try:
        print("An exception occurred")
        resultCode = respuesta[0]
        majorID = respuesta[1]
        minorID = respuesta[2]
        captchaText = respuesta[5]
        print(resultCode != 0 and len(captchaText) < 8)
        print(str(iteracion) + " - " + captchaText)
        return captchaText
    except:
        return "failed"

# """Function to so"""
# def bad_image(filename):
#     URL = "http://poster.de-captcher.com/"
#     multipart_form_data = {
#         'pict':     open(filename, 'rb'),
#         'function': ('', 'picture_bad2'),
#         'username': ('', 'itjuzto'),
#         'password': ('', 'Juzto@2021')
#     }

#     response = requests.post(URL, files=multipart_form_data)

#     print(response.content)

# -

def twocaptcha_solver(screenshot):

    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    api_key = os.getenv('APIKEY_2CAPTCHA', twocaptcha_api_key["key"])

    solver = TwoCaptcha(api_key)

    try:
        result = solver.normal(screenshot, regsense=1)

    except Exception as e:
        sys.exit(e)

    else:
        solved_captcha = variable_producer.produce_captcha(result)
        return solved_captcha