
def create_response_object(comparendo_properties):

    final_comparendo = {}
    final_comparendo["type"] = "object"
    final_comparendo['properties']= {}
    final_comparendo["properties"]["data"] = {}
    final_comparendo["properties"]["data"]["type"] = "object"
    final_comparendo["properties"]["data"]["properties"] = {}
    final_comparendo["properties"]["data"]["properties"]["comparendos"] = {}
    final_comparendo["properties"]["data"]["properties"]["comparendos"]["type"] = ["object", "array"]
    final_comparendo["properties"]["data"]["properties"]["comparendos"]["items"]= {}
    final_comparendo["properties"]["data"]["properties"]["comparendos"]["items"]["type"] = "object"
    final_comparendo["properties"]["data"]["properties"]["comparendos"]["items"]["properties"] = comparendo_properties
    final_comparendo["properties"]["data"]["properties"]["comparendos"]["items"]["required"] = ["comparendo_type",
                                "comparendo_status",
                                "id_comparendo",
                                "placa",
                                "comparendo_date",
                                "comparendo_saldo",
                                "comparen_intereses",
                                "comparendo_total",
                                "comparendo_medium",
                                "comparendo_id_number",
                                "comparendo_id_type",
                                "comparendo_infraction_detail",
                                "comparendo_titular_name",
                                "comparendo_notification_date",
                                "comparen_link",
                                "comparendo_notification_link"
                                ]
    final_comparendo["properties"]["data"]["required"] = ["comparendos"]
    final_comparendo["required"] = ["data"]

    return final_comparendo
