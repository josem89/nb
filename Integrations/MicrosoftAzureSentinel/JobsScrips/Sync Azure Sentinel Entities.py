from SiemplifyJob import SiemplifyJob
from ExtendedMicrosoftAzureSentinelManager import ExtendedMicrosoftAzureSentinelManager
import datetime, json, requests, re
from SiemplifyUtils import extract_script_param, utc_now, convert_datetime_to_unix_time, convert_unixtime_to_datetime, unix_now
from TIPCommon import dict_to_flat

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
INTEGRATION_NAME = "MicrosoftAzureSentinel"
SCRIPT_NAME = "Sync Azure Sentinel Entities"
ENTITY_KINDS = ["Account", "File", "FileHash", "Host", "Ip", "Url"]


def create_entities(data,envrionment, siemplify):
    siemplify.LOGGER.info(f'Creating entities in case {data["case_id"]} - alert {data["identifier"]}')
    
    for entity in data["entities"]:
        try:
            siemplify.add_entity_to_case(data["case_id"], data["identifier"], entity["identifier"], entity["type"], False, False, False, False, entity["properties"], envrionment)
            
        except Exception as e:
            siemplify.LOGGER.error(f"Failed to create entity {entity['identifier']}")
            siemplify.LOGGER.exception(e)
    
    return True

def process_entities(entities, siemplify):
   
   target_entities = []
   
   for entity in entities:
       
       if entity.kind in ENTITY_KINDS:
            siemplify.LOGGER.info(f'Processing Entity {entity.name} of kind {entity.kind}')
            entity_data = {}
            if entity.kind == "Account":
               entity_data["identifier"] = entity.properties.account_name
               entity_data["type"] = "USERUNIQNAME"
               entity_data["properties"] = dict_to_flat(entity.properties.raw_data)
               target_entities.append(entity_data)
            elif entity.kind == "Filename":
               entity_data["identifier"] = entity.properties.file_name
               entity_data["type"] = "FILENAME"
               entity_data["properties"] = dict_to_flat(entity.properties.raw_data)
               target_entities.append(entity_data)
            elif entity.kind == "FileHash":
               entity_data["identifier"] = entity.properties.hash_value
               entity_data["type"] = "FILEHASH"
               entity_data["properties"] = dict_to_flat(entity.properties.raw_data)
               target_entities.append(entity_data)
            elif entity.kind == "Host":
               entity_data["identifier"] = entity.properties.host_name
               entity_data["type"] = "HOSTNAME"
               entity_data["properties"] = dict_to_flat(entity.properties.raw_data)
               target_entities.append(entity_data)
            elif entity.kind == "Ip":
               entity_data["identifier"] = entity.properties.address
               entity_data["type"] = "ADDRESS"
               entity_data["properties"] = dict_to_flat(entity.properties.raw_data)
               target_entities.append(entity_data)
            elif entity.kind == "Url":
               entity_data["identifier"] = entity.properties.url
               entity_data["type"] = "DestinationURL"
               entity_data["properties"] = dict_to_flat(entity.properties.raw_data)
               target_entities.append(entity_data)
        
       else:
           siemplify.LOGGER.info(f'Entity {entity.name} of {entity.kind} kind  not supported. Skipping')
    
   return target_entities     

        
def calculate_as_time(time):
    regex = re.compile(r"(\.\d{0,6})(\d)*(Z)")
    time = regex.sub('\\1\\3',time)
    _datetime = datetime.datetime.strptime(time, TIME_FORMAT)
    _datetime = _datetime.replace(tzinfo=datetime.timezone.utc)
    return _datetime
    

def validate_timestamp(last_run_timestamp, offset_in_hours):
    """
    Validate timestamp in range
    :param last_run_timestamp: {datetime} last run timestamp
    :param offset_in_hours: {datetime} last run timestamp
    :return: {datetime} if first run, return current time minus offset time, else return timestamp from file
    """
    
    current_time = utc_now()
    # Check if first run
    if current_time - last_run_timestamp > datetime.timedelta(hours=offset_in_hours):
        valid_timestamp = current_time - datetime.timedelta(hours=offset_in_hours)
        return valid_timestamp
        
    else:
        return last_run_timestamp


def get_instance_identifier(siemplify,environment,instance_name):
    url = f"{siemplify.API_ROOT}/external/v1/integrations/GetOptionalIntegrationInstances"
    payload = {"environments": [environment],"integrationIdentifier": INTEGRATION_NAME}
    headers = {"Content-Type": "application/json", "AppKey":siemplify.api_key, "accept":"application/json"}
    r = requests.post(url,headers=headers, json=payload, verify=False)
    available_instances = r.json()
    
    if instance_name:
        for instance in available_instances:
            if instance["instanceName"] == instance_name:
                return instance["identifier"]
    else:
        return available_instances[0]["identifier"]
    

def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME # In order to use the SiemplifyLogger, you must assign a name to the script.
    environment = siemplify.extract_job_param(param_name="Environment", print_value=True)
    instance_name = siemplify.extract_job_param(param_name="Instance Name", print_value=True, default_value=None)
    hours_back = siemplify.extract_job_param(param_name = "Hours Back", print_value=True, default_value=24, input_type = int)
    tags = siemplify.extract_job_param(param_name = "Sync Tags", print_value=True, input_type = str).split(",")
    is_favorite = siemplify.extract_job_param(param_name = "Only Favorite Comments", print_value=True, input_type = bool)

    
    try:
        siemplify.LOGGER.info(f"Checking available integrations for {INTEGRATION_NAME} in {environment}")
        integration_identifier = get_instance_identifier(siemplify,environment,instance_name)
        siemplify.LOGGER.info(f"Using integration Identifier {integration_identifier}")
        siemplify.LOGGER.info(f"Getting integration config details")
        integration_settings =  siemplify.get_configuration(INTEGRATION_NAME, environment = environment, integration_instance = integration_identifier)
        api_root = extract_script_param(siemplify=siemplify, input_dictionary=integration_settings, param_name='Api Root', print_value = True)
        login_url = extract_script_param(siemplify = siemplify, input_dictionary=integration_settings, print_value = True,
                                            param_name='OAUTH2 Login Endpoint Url')
        client_id = extract_script_param(siemplify = siemplify, input_dictionary=integration_settings, print_value = True, param_name='Client ID')
        client_secret = extract_script_param(siemplify = siemplify, input_dictionary=integration_settings, param_name='Client Secret')
        tenant_id = extract_script_param(siemplify = siemplify, input_dictionary=integration_settings, print_value = True,
                                            param_name='Azure Active Directory ID')
        workspace_id = extract_script_param(siemplify = siemplify, input_dictionary=integration_settings, print_value = True,
                                               param_name='Azure Sentinel Workspace Name')
        resource = extract_script_param(siemplify = siemplify, input_dictionary=integration_settings, print_value = True, param_name='Azure Resource Group')
        subscription_id = extract_script_param(siemplify = siemplify, input_dictionary=integration_settings, print_value = True,
                                                  param_name='Azure Subscription ID')
        verify_ssl = extract_script_param(siemplify = siemplify, input_dictionary=integration_settings, print_value = True, param_name='Verify SSL',
                                             input_type=bool, default_value=False)
        
        last_successful_execution_time = siemplify.fetch_timestamp(datetime_format=True, timezone = "UTC")
        last_successful_execution_time = validate_timestamp(last_successful_execution_time, hours_back)
        last_successful_execution_timestamp = convert_datetime_to_unix_time(last_successful_execution_time)
        siemplify.LOGGER.info(f"Fetching Azure Sentinel Incidents updated after {last_successful_execution_time}")
        
        manager = ExtendedMicrosoftAzureSentinelManager(
            api_root=api_root,
            client_id=client_id,
            client_secret=client_secret,
            tenant_id=tenant_id,
            workspace_id=workspace_id,
            resource=resource,
            subscription_id=subscription_id,
            login_url=login_url,
            verify_ssl=verify_ssl
        )
        
        incidents = manager.get_updated_incidents(updated_time = last_successful_execution_time, limit =200)
        incidents = [incident.to_json() for incident in incidents]
        
        siemplify_cases = siemplify.get_cases_by_filter(environments = [environment], tags = tags, statuses = [1])
        siemplify_alerts = []
        incidents_list = []
        
        if siemplify_cases:
            for case in siemplify_cases:
                case_data = siemplify._get_case_by_id(case)
                
                for alert in case_data["cyber_alerts"]:
                    if alert["additional_properties"]["SourceSystemName"] == "MicrosoftAzureSentinel":
                        alert_data = {}
                        alert_data["case_id"] = case_data["identifier"]
                        alert_data["identifier"] = alert["identifier"]
                        alert_data["incident_id"] = alert["additional_properties"]["incidentNumber"]
                        incidents_list.append(int(alert_data["incident_id"]))
                        siemplify_alerts.append(alert_data)
        
        filtered_incidents = []        
        for incident in incidents:
            if incident["properties"]["incidentNumber"] in incidents_list:
                filtered_incidents.append(incident)
        
        siemplify.LOGGER.info("Fetching Entities for relevant Azure Sentinel Incidents")
        entities_to_sync = []
        
        for incident in filtered_incidents:
            
            entities_data = {}
            entities = manager.get_incident_entities_sync(incident["name"])
            if entities:
                alert_data = {}
                siemplify.LOGGER.info(f'Processing Entities for incident {incident["properties"]["incidentNumber"]}')
                target_entities = process_entities(entities,siemplify)
                alert_data["entities"] = target_entities
                for alert in siemplify_alerts:
                    if incident["properties"]["incidentNumber"] == int(alert["incident_id"]):
                        alert_data["case_id"] = alert["case_id"]
                        alert_data["identifier"] = alert["identifier"]
                entities_to_sync.append(alert_data)        
            else:
                siemplify.LOGGER.info(f'No entities found for incident {incident["properties"]["incidentNumber"]}')
        
        siemplify.LOGGER.info(f'Creating entities in {len(entities_to_sync)} alerts in Siemplify')
        
        for data in entities_to_sync:
            result = create_entities(data, environment, siemplify)
            if not result:
                siemplify.LOGGER.info("Entities creation Failed")
        
        
        new_timestamp = utc_now()
        siemplify.LOGGER.info(f"Update Job last execution timestamp to {new_timestamp}")
        new_timestamp = datetime.datetime.timestamp(new_timestamp) *1000
            
            
        siemplify.save_timestamp(new_timestamp=int(new_timestamp))

            


    except Exception as e:
        siemplify.LOGGER.error("General error performing Job {}".format(SCRIPT_NAME))
        siemplify.LOGGER.exception(e)
        raise

    siemplify.end_script()


if __name__ == "__main__":
    main()