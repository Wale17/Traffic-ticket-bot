"""Template robot with Python."""
from handlers import process


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
    print("Done.")


if __name__ == "__main__":
    minimal_task()
