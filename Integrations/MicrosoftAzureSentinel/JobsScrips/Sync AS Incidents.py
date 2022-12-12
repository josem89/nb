from SiemplifyJob import SiemplifyJob
from ExtendedMicrosoftAzureSentinelManager import ExtendedMicrosoftAzureSentinelManager
import datetime, json, requests, re
from SiemplifyUtils import extract_script_param, utc_now, convert_datetime_to_unix_time, convert_unixtime_to_datetime, unix_now

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
OPEN_CASE_STATUS = '1'
CLOSE_CASE_STATUS = '2'
INTEGRATION_NAME = "MicrosoftAzureSentinel"
SCRIPT_NAME = "Sync AS Incidents"
GET_USERS_URL = '{}/external/v1/settings/GetUserProfiles'
UPDATE_PRORITY = "external/v1/sdk/UpdateAlertPriority"
CLOSE_REASONS = ["True Positive - Suspicious activity","Bening Positive - Suspicious but expected", "False Positive - Incorrect alert logic","False Positive - Inaccurate data","Undetermined"]

def update_alert_priority(priority, alert, siemplify):
    if priority == "Informational":
        priority = "Informative"
    if priority != alert["severity"]:
        url = f"{siemplify.API_ROOT}/{UPDATE_PRORITY}"
        payload = {"caseId": alert["case_id"], "alertIdentifier": alert["identifier"],"priority": priority}
        response = siemplify.session.post(url, json=payload)
        siemplify.validate_siemplify_error(response)
        return True
    
    else:
        
        return None

def update_alert_description(description, alert, siemplify):
    
    if description != alert["description"] and description:
        case_id = alert["case_id"]
        request_dict = {u"case_id": case_id,
                        u"description": description}
        address = u"{}/{}".format(siemplify.API_ROOT, u"external/v1/cases/ChangeCaseDescription?format=snake")
        response = siemplify.session.post(address, json=request_dict)
        siemplify.validate_siemplify_error(response)
        return True 
    
    else:
        
        return None

def update_alert_owner(owner, alert, siemplify):
    
    if owner != alert["assigned_user"]:
        assign_to = validate_user(owner,siemplify)
        if assign_to:
            case_id = alert["case_id"]
            alert_id = alert["identifier"]
            json_payload = {"caseId": case_id, "alertIdentifier": alert_id, "userId": assign_to}
            result = siemplify.session.post('{}/external/v1/cases/AssignUserToCase'.format(siemplify.API_ROOT), json=json_payload)
            result.raise_for_status()
            return True
        else:
            return None
    
    else:
        
        return None

def close_alert(incident, alert, siemplify):
    
    if incident["classification"] == "True Positive":
        reason = "Malicious"
    elif incident["classification"] in ["Bening Positive", "False Positive"]:
        reason = "NotMalicious"
    else:
        reason = "Inconclusive"
    
    root_cause = f'{incident["classification"]} - {incident["classification_reason"]}'
    comment = incident["classification_comment"]
    case_id = alert["case_id"]
    alert_id = alert["identifier"]
    
    response = siemplify.close_alert(root_cause, comment, reason, case_id, alert_id)
    return True

def update_siemplify_case(incident,siemplify_alerts,siemplify):
    
    for alert in siemplify_alerts:
        if incident["ticketid"] == alert["ticketid"]:
            updated_alert = False
            priority = update_alert_priority(incident["severity"], alert, siemplify)
            if priority:
                updated_alert= True
            description = update_alert_description(incident["description"], alert, siemplify)
            if description:
                updated_alert= True
            if incident["assigned_user"]:
                owner = update_alert_owner(incident["assigned_user"], alert, siemplify)
            else:
                owner = None
            if owner:
                updated_alert= True
            if incident["comments_to_sync"]:
                for comment in incident["comments_to_sync"]:
                    siemplify.add_comment(comment, incident["case_id"], alert["identifier"])
                    updated_alert = True
            if incident["status"] == "Closed" and alert["status"] ==1:
                close_alert_success = close_alert(incident, alert, siemplify)
                if close_alert_success:
                    updated_alert = True
            if not updated_alert:
                siemplify.LOGGER.info(f'Nothing to update, skipping case {incident["case_id"]}')
            
            return updated_alert
    
          
                
                    
                

def get_user_email(userid, siemplify):
    json_payload = {"searchTerm": "",
                    "filterRole": False,
                    "requestedPage": 0,
                    "pageSize": 1000,
                    "shouldHideDisabledUsers": True
                    }
                    
    response = siemplify.session.post(GET_USERS_URL.format(siemplify.API_ROOT), json=json_payload)
    response.raise_for_status()
    siemplify_users = response.json()['objectsList']
    if userid:
        for user in siemplify_users:
            if userid[0] == "@":
                return userid
            elif user["userName"] == userid:
                return user["email"]
        return None
    else:
        return None

def validate_user(usermail, siemplify):
    json_payload = {"searchTerm": "",
                    "filterRole": False,
                    "requestedPage": 0,
                    "pageSize": 1000,
                    "shouldHideDisabledUsers": True
                    }
    response = siemplify.session.post(GET_USERS_URL.format(siemplify.API_ROOT), json=json_payload)
    response.raise_for_status()
    siemplify_users = response.json()['objectsList']
    
    for user in siemplify_users:
        if usermail[0] == "@":
            return usermail
        elif user["email"] == usermail:
            return user["userName"]
        else:
            return None
    
        
def calculate_as_time(time):
    regex = re.compile(r"(\.\d{0,6})(\d)*(Z)")
    time = regex.sub('\\1\\3',time)
    _datetime = datetime.datetime.strptime(time, TIME_FORMAT)
    _datetime = _datetime.replace(tzinfo=datetime.timezone.utc)
    return _datetime
    

def update_sentinel_incident(alert, manager, siemplify):
    
    is_updated = False
    
    if alert["Sync Values"] != [alert["severity"],alert["description"],alert["assigned_user"]]:
        incident_number = alert["incident_id"]
        
        if alert["status"] == 2 and alert["incident_status"] != "Closed":
            status = "closed"
            if alert["root_cause"] in CLOSE_REASONS:
                close_reason = alert["root_cause"]
            else:
                close_reason = "Undetermined"
            alert["incident_status"] = "Closed"    
        else:
            close_reason = None
            if alert["incident_status"] == "New":
                status = "Active"
            else:
                status = None
        if alert["severity"] == "Informative":
            severity = "Informational"
        elif alert["severity"] == "Critical":
            severity = "High"
        
        else:
            severity = alert["severity"]
    
        description = alert["description"]
        assigned_to = alert["assigned_user"]

        incident = manager.update_incident(incident_number=incident_number, status=status, close_reason =close_reason,
                                                   severity=severity, description=description, assigned_to=assigned_to)
        sync_values_updated = update_sync_values(alert,status,siemplify)
        
        is_updated = True
    
    if alert["comments_to_sync"]:
        incident = manager.get_incident_by_incident_number(incident_number=alert["incident_id"])
        for comment in alert["comments_to_sync"]:
            incident_comment_data = manager.add_comment_to_incident(incident_name=incident.name, comment=comment)
        
        is_updated = True
    
    return True
    
def get_sync_values(alert,siemplify):
    severity = siemplify.get_context_property(2, alert["additional_properties"]["AlertGroupIdentifier"], "AzureSentinel Severity")
    description = siemplify.get_context_property(2, alert["additional_properties"]["AlertGroupIdentifier"], "AzureSentinel Description")
    owner = siemplify.get_context_property(2, alert["additional_properties"]["AlertGroupIdentifier"], "AzureSentinel Owner")
    status = siemplify.get_context_property(2, alert["additional_properties"]["AlertGroupIdentifier"], "AzureSentinel Status")
    return [severity, description, owner], status

def update_sync_values(alert,status, siemplify):
    try:
        
        siemplify.set_context_property(2,alert["group_identifier"],"AzureSentinel Severity",alert["severity"])
        if alert["description"]:
            siemplify.set_context_property(2,alert["group_identifier"],"AzureSentinel Description",alert["description"])
        if alert["assigned_user"]:
            siemplify.set_context_property(2,alert["group_identifier"],"AzureSentinel Owner",alert["assigned_user"])
        if alert["incident_status"]:
            siemplify.set_context_property(2,alert["group_identifier"],"AzureSentinel Status",alert["incident_status"])
    except Exception as e:
        siemplify.LOGGER.error("Failed to update sync values in siemplify")
        siemplify.LOGGER.exception(e)
    
    return True

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

def get_alert_comments(alert,siemplify,is_favorite, last_successful_execution_timestamp):
    comments = siemplify.get_case_comments(alert["case_identifier"])
    comments_to_sync = []
    synced_comments = []
    for comment in comments:
        if comment["creation_time_unix_time_in_ms"] > last_successful_execution_timestamp:
            if comment["comment"].startswith("AzureSentinel Comment:"):
                synced_comments.append(comment["comment"])
            else:
                if is_favorite:
                    if comment["is_favorite"]:
                        comments_to_sync.append(comment["comment"])
                else:
                    comments_to_sync.append(f'SOARComment: {comment["comment"]}')
    
    return comments_to_sync, synced_comments
    

def process_alert(alert,siemplify, is_favorite, last_successful_execution_timestamp):
    alert_data = {}
    alert_data["incident_id"] = alert["additional_properties"]["incidentNumber"]
    alert_data["severity"] = alert["additional_properties"]["Priority"]
    alert_data["ticketid"] = alert["additional_properties"]["TicketId"]
    alert_data["name"] = alert["name"]
    alert_data["identifier"] = alert["identifier"]
    alert_data["group_identifier"] = alert["additional_properties"]["AlertGroupIdentifier"]
    alert_data["Sync Values"], alert_data["incident_status"] = get_sync_values(alert,siemplify)
    alert_data["comments_to_sync"], alert_data["synced_comments"] = get_alert_comments(alert,siemplify, is_favorite, last_successful_execution_timestamp)
    
    return alert_data
    
def get_incident_comments(incidentid, manager, last_successful_execution_time, siemplify):
    comments = manager.get_incident_comments(incidentid)
    comments.reverse()
    comments_to_sync = []
    synced_comments = []

    for comment in comments:
        if comment["properties"]["message"].startswith("SOARComment:"):
            synced_comments.append(comment["properties"]["message"])
           
        else:
            if calculate_as_time(comment["properties"]["lastModifiedTimeUtc"]) > last_successful_execution_time:
                comments_to_sync.append(f'AzureSentinel Comment: {comment["properties"]["message"]}')
                
    return comments_to_sync, synced_comments            

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
        siemplify.LOGGER.info(f"Fetching cases modified after {last_successful_execution_time}")
        
        
        siemplify_cases = siemplify.get_cases_by_filter(environments = [environment], tags = tags, statuses = [OPEN_CASE_STATUS])
        siemplify_closed_ticket_ids = siemplify.get_alerts_ticket_ids_from_cases_closed_since_timestamp(last_successful_execution_timestamp, None)
        closed_cases_ids = []
        closed_alerts = []
        relevant_cases = []
        siemplify_alerts = []
        incident_list =[]
        target_alerts =[]
        target_alerts_ids = []
        
        if siemplify_closed_ticket_ids:
            for ticket_id in siemplify_closed_ticket_ids:
                try:
                    closed_cases_ids.extend(
                        [case_id for case_id in siemplify.get_cases_by_ticket_id(ticket_id)]
                    )
                except Exception as e:
                    siemplify.LOGGER.error('Failed to fetch case with ticket id {}. Reason {}'.format(ticket_id, e))
       
        filtered_closed_case_ids = []
        for case in closed_cases_ids:
            if siemplify.get_cases_by_filter(environments = [environment], tags = tags, statuses = [CLOSE_CASE_STATUS], case_ids_free_search =str(case)):
                filtered_closed_case_ids.append(case)
        
        siemplify_cases.extend(filtered_closed_case_ids)
        
        if siemplify_cases:
            for case in siemplify_cases:
                case_data = siemplify._get_case_by_id(case)
                
                for alert in case_data["cyber_alerts"]:
                    if alert["additional_properties"]["SourceSystemName"] == "MicrosoftAzureSentinel":
                        alert_data = process_alert(alert, siemplify, is_favorite, last_successful_execution_timestamp)
                        alert_data["status"] = case_data["status"]
                        alert_data["assigned_user"] = get_user_email(case_data["assigned_user"], siemplify)
                        alert_data["description"] = case_data["description"]
                        alert_data["modification_time"] = case_data["modification_time"]
                        alert_data["case_id"] = case_data["identifier"]
                        if  case in filtered_closed_case_ids :
                            closure_data = siemplify.get_case_closure_details([case])
                            alert_data["reason"] = closure_data[0]["reason"]
                            alert_data["root_cause"] = closure_data[0]["root_cause"]
                        siemplify_alerts.append(alert_data)
                        incident_list.append(int(alert_data["incident_id"]))
                        
                        
        
                        
        for alert in siemplify_alerts:
            if (alert["modification_time"] > last_successful_execution_timestamp):
                if alert["Sync Values"] != [alert["severity"],alert["description"],alert["assigned_user"]]:
                    target_alerts.append(alert)
                    target_alerts_ids.append(alert["incident_id"])
                elif alert["comments_to_sync"]:
                    target_alerts.append(alert)
                    target_alerts_ids.append(alert["incident_id"])
        
        
        siemplify.LOGGER.info(f"Found {len(target_alerts)} relevant alerts in Siemplify")
        
        siemplify.LOGGER.info(f"Getting AS incidents updated after {last_successful_execution_time}")
        
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
        
        siemplify.LOGGER.info(f"Updating Azure Sentinel Incidents")
        
        updated_incidents = []
        
        for alert in target_alerts:
                siemplify.LOGGER.info(f"Updating AS incident {alert['incident_id']} from case {alert['case_id']}")
                result = update_sentinel_incident(alert, manager, siemplify)
                updated_incidents.append(result)
        
        siemplify.LOGGER.info(f"Succesfully Updated {len(updated_incidents)} incidents in Azure Sentinel")
        
        for case in relevant_cases:
            for alert in case["cyber_alerts"]:
                if alert["additional_properties"]["SourceSystemName"] == "MicrosoftAzureSentinel":
                    incident_list.append(int(alert["additional_properties"]["incidentNumber"]))
        
        filtered_incidents = []
        for incident in incidents:
            if incident["properties"]["incidentNumber"] in incident_list:
                filtered_incidents.append(incident)
                
        
        siemplify.LOGGER.info(f"Found {len(filtered_incidents)} relevant incident(s) in AS")
        
        target_incidents = []
        target_incidents_ids =[]
        
        if filtered_incidents:
            for incident in filtered_incidents:
                for alert in siemplify_alerts:
                    if int(alert["incident_id"]) == incident["properties"]["incidentNumber"]:
                        incident_data ={}
                        incident_data["incident_id"] = str(incident["properties"]["incidentNumber"])
                        incident_data["case_id"] = alert["case_id"]
                        incident_data["ticketid"] = alert["ticketid"]
                        incident_data["modification_time"] = calculate_as_time(incident["properties"]["lastModifiedTimeUtc"])
                        incident_data["status"] = incident["properties"]["status"]
                        incident_data["assigned_user"] = incident["properties"]["owner"]["assignedTo"]
                        incident_data["severity"] = incident["properties"]["severity"]
                        if incident["properties"]["status"] == "Closed":
                            incident_data["classification"] = incident["properties"]["classification"]
                            incident_data["classification_reason"] = incident["properties"]["classificationReason"]
                            incident_data["classification_comment"] = incident["properties"]["classificationComment"]
                        incident_data["description"] = incident["properties"]["description"]
                        incident_data["comments_to_sync"], incident_data["synced_comments"] = get_incident_comments(incident["name"],manager, last_successful_execution_time, siemplify)
                        target_incidents.append(incident_data)
                        target_incidents_ids.append(incident_data["incident_id"])
        if target_incidents:
            siemplify.LOGGER.info(f"Attempting to Update {len(target_incidents)} relevant cases in Siemplify")
        updated_alerts = []
        for incident in target_incidents:
            if incident["incident_id"] in target_alerts_ids:
                for alert in target_alerts:
                    if convert_datetime_to_unix_time(incident["modification_time"]) > alert["modification_time"]:
                        siemplify.LOGGER.info(f'Attempting to update case {incident["case_id"]}')
                        updated_alert = update_siemplify_case(incident, siemplify_alerts, siemplify)
                        if updated_alert:
                            updated_alerts.append(updated_alert)
            else:
                siemplify.LOGGER.info(f'Attempting to update case {incident["case_id"]}')
                updated_alert = update_siemplify_case(incident, siemplify_alerts, siemplify)
                if updated_alert:
                    updated_alerts.append(updated_alert)
        if updated_alerts:
            siemplify.LOGGER.info(f"Succesfully updated {len(updated_alerts)} Alerts in siemplify")
        
        
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