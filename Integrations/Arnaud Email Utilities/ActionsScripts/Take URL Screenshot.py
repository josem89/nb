from SiemplifyUtils import output_handler
from SiemplifyAction import SiemplifyAction
from SiemplifyDataModel import EntityTypes
#from TIPCommon import construct_csv, dict_to_flat, extract_configuration_param, extract_action_param
import json
import requests
import base64

INTEGRATION_NAME = u"Arnaud"
SCRIPT_NAME = u"URL Screenshot"

def get_entity_original_identifier(entity):
    return entity.additional_properties.get('OriginalIdentifier', entity.identifier)

@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = SCRIPT_NAME
    
    output_message = "Error occurred"
    result_value = "Failure"
    
    json_output = {'results': []}
    
    suitable_entities = [entity for entity in siemplify.target_entities if entity.entity_type == EntityTypes.URL]

    api_endpoint = siemplify.parameters.get("Endpoint")
    token = siemplify.parameters.get("Bearer Token")
    
    if token:
        headers = {"Authorization": "Bearer {}".format(token)}
    else:
        headers = {}
    
    for entity in suitable_entities:
        siemplify.LOGGER.info("Started processing URL: {}".format(get_entity_original_identifier(entity)))
        try:
            payload = {"url": get_entity_original_identifier(entity)}
            response = requests.post(api_endpoint, data=payload, headers=headers)

            if response.status_code == 200:
                    b64_binary = base64.b64encode(response.content)
                    html_value = '<img src="data:image/png;base64,{}"/>'.format(b64_binary.decode())
                    json_output["results"].append({'url':get_entity_original_identifier(entity), 'screenshot': html_value})
                    output_message = "URL screenshot taken"
                    result_value = "Success"
                    siemplify.LOGGER.info("Successfully enriched {}".format(get_entity_original_identifier(entity)))
            elif response.status_code == 401:
                output_message = "Bearer token is invalid"
                siemplify.LOGGER.error("Response code {}. Reason: {}".format(response.status_code, response.text))
            else:
                siemplify.LOGGER.error("Response code {}. Reason: {}".format(response.status_code, response.text))
                json_output["results"].append({'url':get_entity_original_identifier(entity), 'error': response.text})
                

        except HTTPError as e:
            status_code = e.response.status_code
            siemplify.LOGGER.error(e.response.text)
        
        
    siemplify.result.add_result_json(json_output)
    siemplify.end(output_message, result_value)

if __name__ == "__main__":
    main()
