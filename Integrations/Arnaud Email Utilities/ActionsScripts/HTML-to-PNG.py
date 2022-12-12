from SiemplifyUtils import output_handler
from SiemplifyAction import SiemplifyAction
#from TIPCommon import construct_csv, dict_to_flat, extract_configuration_param, extract_action_param
import json
import requests
import base64

INTEGRATION_NAME = u"Arnaud"
SCRIPT_NAME = u"HTML-to-PNG"

@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = SCRIPT_NAME
    
    output_message = "Error occurred"
    result_value = "Failure"
    
    #json_output = {}
    
    api_endpoint = siemplify.parameters.get("Endpoint")
    token = siemplify.parameters.get("Bearer Token")
    message_text = siemplify.parameters.get("Text")
    
    message_bytes = message_text.encode()
    b64_text = base64.b64encode(message_bytes)
    b64_decoded = b64_text.decode()
    
    if token:
        headers = {"Authorization": "Bearer {}".format(token)}
    else:
        headers = {}
    
    siemplify.LOGGER.info("Started processing text")
    try:
        payload = {"message": b64_decoded }
        siemplify.LOGGER.info("Payload: {}".format(payload))

        response = requests.post(api_endpoint, data=payload, headers=headers)

        if response.status_code == 200:
                siemplify.LOGGER.info("Received screenshot")
                b64_binary = base64.b64encode(response.content)
                html_value = '<img src="data:image/png;base64,{}"/>'.format(b64_binary.decode())
                #json_output["results"].append({'url':get_entity_original_identifier(entity), 'screenshot': html_value})
                output_message = "Screenshot taken"
                result_value = html_value
                    
        elif response.status_code == 401:
            output_message = "Bearer token is invalid"
            siemplify.LOGGER.error("Response code {}. Reason: {}".format(response.status_code, response.text))
        else:
            siemplify.LOGGER.error("Response code {}. Reason: {}".format(response.status_code, response.text))
    except Exception as e:
        print(e)

    siemplify.end(output_message, result_value)

if __name__ == "__main__":
    main()
