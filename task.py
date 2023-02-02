"""Template robot with Python."""
from handlers import process
from service import final_json
import json
from RPA.Robocorp.WorkItems import WorkItems

workitem = WorkItems()
workitem.get_input_work_item()
comparendo_list = ["comparendo_type", "comparendo_status", "id_comparendo", "dummy", "placa", "comparendo_date", "comparendo_saldo", "comparen_intereses", "comparendo_total", "comparendo_medium"]
url = "https://consultas.transitobogota.gov.co:8010/publico/index3.php"
plate_number = workitem.get_work_item_variable("placa") #"BRY010gy"
doc_number = workitem.get_work_item_variable("doc_number")#"1060634"
doc_type = workitem.get_work_item_variable("doc_type")#"CE"

# plate_number = "BWL600"
# doc_number = "819063"
# doc_type = "CE"



def trafic_ticket():
    try:
        process.open_webpage(url)
        number_of_pages = process.make_search(doc_type, plate_number, doc_number)
        total_comparendo = {}
        final_comparendo = {}
        for j in range(number_of_pages):
            for i in range(50):
                try:
                    comparendo_dict = process.scrapr_from_the_initial_table(4+i, comparendo_list)
                    if comparendo_dict == "":
                        break
                    else:
                        total_comparendo["comparendo{0}".format(i+1)] = comparendo_dict
                except Exception as e:
                    raise(e)
        final_comparendo["data"] = total_comparendo
        json_object = json.dumps(final_comparendo, indent=4)
 
        with open("./output/schema.json", "w") as outfile:
            outfile.write(json_object)
        workitem.create_output_work_item(variables=final_comparendo, save=True)
    except Exception as e:
        workitem.release_input_work_item("FAILED", "BUSINESS", message=e)
    print("Done.")


if __name__ == "__main__":
    trafic_ticket()
    # captcha_solution = captcha_solver.twocaptcha_solver("captcha.png")
