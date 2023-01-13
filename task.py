"""Template robot with Python."""
from handlers import process
from service import captcha_solver
from time import sleep


url = "https://consultas.transitobogota.gov.co:8010/publico/index3.php"
plate_number = "Bch58d",
doc_number = "79302230",
doc_type = "CE",
person_type = "Persona natural",
email = "ariesgerman6405@gmail.com",
mobile = "3174331649",
origin = "Juzto.co",
first_name = "German Antonio",
last_name = "Diaz leon",
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
