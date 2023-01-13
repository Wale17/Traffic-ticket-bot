"""Template robot with Python."""
from handlers import process
from service import captcha_solver
from time import sleep


url = "https://consultas.transitobogota.gov.co:8010/publico/index3.php"
plate_number = "RBL907",
doc_number = "333333",
doc_type = "CC",
person_type = "Persona natural",
email = "pruebitas@trolazo.com",
mobile = "3174331649",
origin = "Juzto.co",
first_name = "Martha Janeth",
last_name = "Jimenez Zambrano",
recurrent_query = False,
update =  True


def minimal_task():
    process.open_webpage(url)
    process.make_search(doc_type, plate_number, doc_number)
    sleep(10)
    print("Done.")


if __name__ == "__main__":
    minimal_task()
    # captcha_solution = captcha_solver.twocaptcha_solver("captcha.png")
