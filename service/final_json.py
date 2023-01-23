
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
    final_comparendo["properties"]["data"]["properties"]["comparendos"]["items"]["required"] = ["codigoInfraccion", "descripcionInfraccion", "direccionComparendo",
                                            "estadoComparendo", "fechaComparendo", "infractorComparendo",
                                            "numeroComparendo", "placaVehiculo", "secretariaComparendo",
                                            "servicioVehiculo", "tipoVehiculo", "total"
                                            ]
    final_comparendo["properties"]["data"]["required"] = ["comparendos"]
    final_comparendo["required"] = ["data"]

    return final_comparendo
