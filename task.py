"""Template robot with Python."""
from handlers import process
from service import final_json
from time import sleep
import json

comparendo_list = ["comparendo_type", "comparendo_status", "id_comparendo", "dummy", "placa", "comparendo_date", "comparendo_saldo", "comparen_intereses", "comparendo_total", "comparendo_medium"]
url = "https://consultas.transitobogota.gov.co:8010/publico/index3.php"
plate_number = "BRY010",
doc_number = "819063",
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
    number_of_pages = process.make_search(doc_type, plate_number, doc_number)
    total_comparendo = {}
    for j in range(number_of_pages):
        for i in range(10):
            try:
                comparendo_dict = process.scrapr_from_the_initial_table(4+i, comparendo_list)
                if comparendo_dict == "":
                    break
                else:
                    total_comparendo["comparendo{0}".format(i+1)] = comparendo_dict
            except Exception as e:
                raise(e)
    final_comparendo = final_json.create_response_object(total_comparendo)
    schema_comparendos = json.dumps(final_comparendo, indent=4)
    print(schema_comparendos)
    print("Done.")


if __name__ == "__main__":
    minimal_task()
    # captcha_solution = captcha_solver.twocaptcha_solver("captcha.png")
