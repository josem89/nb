
# MicrosoftAzureSentinel

Microsoft Azure Sentinel is a scalable, cloud-native, security information event management (SIEM) and security orchestration automated response (SOAR) solution. Azure Sentinel delivers intelligent security analytics and threat intelligence across the enterprise, providing a single solution for alert detection, threat visibility, proactive hunting, and threat response.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Azure Subscription ID|None|True|String||
|Azure Active Directory ID|None|True|String||
|Api Root|None|True|String|https://management.azure.com|
|OAUTH2 Login Endpoint Url|None|True|String|https://login.microsoftonline.com|
|Azure Resource Group|None|True|String||
|Azure Sentinel Workspace Name|None|True|String||
|Client ID|None|True|String||
|Client Secret|None|True|Password|None|
|Verify SSL|None|False|Boolean|False|



## Actions
#### Update Incident Details
Update Incident Details
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Case Number|Specify Azure Sentinel incident number to update.|True|String||
|Title|Specify new title for the Azure Sentinel incident.|False|String||
|Status|Specify new status for the Azure Sentinel incident.|False|List|Not Updated|
|Severity|Specify new severity for the Azure Sentinel incident.|False|List|Not Updated|
|Description|Specify new description for the Azure Sentinel incident.|False|String||
|Assigned To|Specify the user to assign the incident to.|False|String||
|Closed Reason|If status of the incident is set to Closed, provide a Closed Reason for the incident.|False|List|Not Updated|
|Closing Comment|Optional closing comment to provide for the closed Azure Sentinel Incident.|False|String||
|Number of retries|Specify the number of retry attempts the action should make if the incident update was unsuccessful.|False|String||
|Retry Every|Specify what time period action should wait between incident update retries.|False|String||



##### JSON Results
```json
{"id": "/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/2e0ce5a0-7563-43a1-86a4-xxxxx", "name": "2e0ce5a0-7563-43a1-86a4-xxxxx", "etag": "\"fb006b40-0000-0c00-0000-xxxxx\"", "type": "Microsoft.SecurityInsights/Incidents", "properties": {"title": "Test Name", "description": "", "severity": "Informational", "status": "Closed", "classification": "Undetermined", "classificationComment": "Hello Test", "owner": {"objectId": null, "email": null, "assignedTo": null, "userPrincipalName": null}, "labels": [], "firstActivityTimeUtc": "2021-04-09T05:47:55.4959374Z", "lastActivityTimeUtc": "2021-04-14T05:47:55.4959374Z", "lastModifiedTimeUtc": "2021-04-14T06:53:30.2380985Z", "createdTimeUtc": "2021-04-14T05:53:00.8171911Z", "incidentNumber": "106xxx", "additionalData": {"alertsCount": 1, "bookmarksCount": 0, "commentsCount": 0, "alertProductNames": ["Azure Sentinel"], "tactics": ["InitialAccess", "Execution"]}, "relatedAnalyticRuleIds": ["/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/alertRules/545ee671-a997-4a5a-8763-xxxxx"], "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/2e0ce5a0-7563-43a1-86a4-xxxxx", "providerName": "Azure Sentinel", "providerIncidentId": "106xxx"}}
```



#### Update Custom Hunting Rule
Update Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hunting Rule ID|Hunting Rule ID|True|String|None|
|Display Name|Display name of the new custom hunting rule|False|String|None|
|Query|Query of the new custom hunting rule|False|String|None|
|Description|Description of the new custom hunting rule|False|String|None|
|Tactics|Tactics of the new custom hunting rule. Comma-separated values.|False|String|None|



##### JSON Results
```json
{"Properties": {"Category": "Log Management O", "Tactics": ["NewCustomTactic", "NewNotCustomTactic"], "Tags": [{"Name": "description", "Value": "New Description"}, {"Name": "tactics", "Value": "NewCustomTactic"}, {"Name": "tactics", "Value": "NewNotCustomTactic"}], "Version": 2, "Display_Name": "New Display Name", "Query": "let timeframe = 7d;AWSCloudTrail| where TimeGenerated >= ago(timeframe)| where  EventName in~ (\"AttachGroupPolicy\", \"AttachRolePolicy\", \"AttachUserPolicy\", \"CreatePolicy\",\"DeleteGroupPolicy\", \"DeletePolicy\", \"DeleteRolePolicy\", \"DeleteUserPolicy\", \"DetachGroupPolicy\",\"PutUserPolicy\", \"PutGroupPolicy\", \"CreatePolicyVersion\", \"DeletePolicyVersion\", \"DetachRolePolicy\", \"CreatePolicy\")| project TimeGenerated, EventName, EventTypeName, UserIdentityAccountId, UserIdentityPrincipalid, UserAgent, UserIdentityUserName, SessionMfaAuthenticated, SourceIpAddress, AWSRegion, EventSource, AdditionalEventData, ResponseElements| extend timestamp = TimeGenerated, IPCustomEntity = SourceIpAddress, AccountCustomEntity = UserIdentityAccountId"}, "ETag": "W/\"datetime'2020-01-23T21%3A14%3A33.2335395Z'\"", "ID": "subscriptions/a052d33b-b7c4-4dc7-9e17-5c89ea594669/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/savedSearches/a5a24268-XXXX-XXXX-XXXX-4ab6c9b7ad5b", "Name": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}
```



#### List Incidents
List Microsoft Azure Sentinel Incidents based on the provided search criteria.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Time Frame|Time frame in hours for which to fetch Incidents|False|String|3|
|Status|Statuses of the incidents to look for. Comma-separated string|False|String|New, Active, Closed|
|Severity|Severities of the incidents to look for. Comma-separated string.|False|String|Informational, Low, Medium, High|
|How Many Incidents to Fetch|How many incidents to fetch|False|String|200|



##### JSON Results
```json
[{"id":"/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/Incidents/XXXXXXXXXXXXXXXXXXXXXXXXXXXX","name":"XXXXXXXXXXXXXXXXXXXXXXXXXXXX","etag":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXX","type":"Microsoft.SecurityInsights/Incidents","properties":{"title":"X","description":"Activity policyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","severity":"Low","status":"New","owner":{"objectId":null,"email":null,"assignedTo":null,"userPrincipalName":null},"labels":[],"firstActivityTimeUtc":"2021-04-13T07:42:54.366Z","lastActivityTimeUtc":"2021-04-13T07:42:54.366Z","lastModifiedTimeUtc":"2021-04-13T07:43:02.870674Z","createdTimeUtc":"2021-04-13T07:43:02.870674Z","incidentNumber":10684490,"additionalData":{"alertsCount":1,"bookmarksCount":0,"commentsCount":0,"alertProductNames":["Microsoft Cloud App Security"],"tactics":[]},"relatedAnalyticRuleIds":["/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX"],"incidentUrl":"https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/Incidents/XXXXXXXXXXXXXXXXXXXXXXXXXXXX","providerName":"Azure Sentinel","providerIncidentId":"XXXXXXX"}},{"id":"/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/Incidents/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","name":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","etag":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","type":"Microsoft.SecurityInsights/Incidents","properties":{"title":"X","description":"Activity policyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","severity":"Low","status":"New","owner":{"objectId":null,"email":null,"assignedTo":null,"userPrincipalName":null},"labels":[],"firstActivityTimeUtc":"2021-04-13T07:33:03.572Z","lastActivityTimeUtc":"2021-04-13T07:33:03.572Z","lastModifiedTimeUtc":"2021-04-13T07:33:33.0348454Z","createdTimeUtc":"2021-04-13T07:33:33.0348454Z","incidentNumber":10444889,"additionalData":{"alertsCount":1,"bookmarksCount":0,"commentsCount":0,"alertProductNames":["Microsoft Cloud App Security"],"tactics":[]},"relatedAnalyticRuleIds":["/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXX","/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/alertRules/XXXXXXXXXXXXXXXXXXXXXX"],"incidentUrl":"https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXXXXXXXXXXX/providers/Microsoft.SecurityInsights/Incidents/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","providerName":"Azure Sentinel","providerIncidentId":"XXXXX"}}]
```



#### Ping
Test connectivity to Microsoft Azure Sentinel
Timeout - 600 Seconds



#### Run Custom Hunting Rule Query
Run Custom Hunting Rule Query
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hunting Rule ID|Hunting Rule ID|True|String||
|Timeout|Timeout value for the Azure Sentinel hunting rule API call|False|String||



##### JSON Results
```json
[{"Avg7Day": 327, "EventID": 455625, "Account": "host.local\\some.user", "StartTimeUtc": "2020-01-08T13:57:26.75Z", "LogonTypeName": "3 - Network", "timestamp": "2020-01-08T13:57:26.75Z", "CountLast7day": 2292, "EndTimeUtc": "2020-01-08T17:38:05.337Z", "CountToday": 1554, "SubStatus": "0xc0000071", "Computer": "XXXXXXXXXXX.XXX", "AccountType": "User", "HostCustomEntity": "XXXXXXXXXXX.XXX", "WorkstationName": "XXXXXX", "IpAddress": "127.0.0.1", "AccountCustomEntity": "host.local\\some.user"}]
```



#### List Custom Hunting Rules
List Custom Hunting Rules available in Sentinel
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hunting Rule Names to Return|Names for the hunting rules action should return. Comma-separated string|False|String||
|Fetch Specific Hunting Rule Tactics|What hunting rule tactics action should return. Comma-separated string|False|String||
|Max rules to return|How many scheduled alert rules the action should return, for example, 50.|False|String||



##### JSON Results
```json
[{"Properties": {"Category": "General Exploration", "Tactics": ["Execution"], "Tags": [{"Name": "description", "Value": "456"}, {"Name": "tactics", "Value": "DefenseEvasion"}], "Version": 2, "Display_Name": "All Computers with their most recent data", "Query": "search not(ObjectName == \"Advisor Metrics\" or ObjectName == \"ManagedSpace\") | summarize AggregatedValue = max(TimeGenerated) by Computer | limit 500000 | sort by Computer asc\r\n// Oql: NOT(ObjectName=\"Advisor Metrics\" OR ObjectName=ManagedSpace) | measure max(TimeGenerated) by Computer | top 500000 | Sort Computer // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PTT: True; SortI: True; SortF: True} // Version: 0.1.122"}, "ETag": null, "ID": "subscriptions/a052d33b-b7c4-4dc7-9e17-5c89ea594669/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXX/savedSearches/LogManagement(XXXXXX)_General|AlphabeticallySortedComputers", "Name": "LogManagement(XXXXXX)_General|AlphabeticallySortedComputers"}, {"Properties": {"Category": "General Exploration", "Tactics": [], "Tags": null, "Version": 2, "Display_Name": "Stale Computers (data older than 24 hours)", "Query": "search not(ObjectName == \"Advisor Metrics\" or ObjectName == \"ManagedSpace\") | summarize lastdata = max(TimeGenerated) by Computer | limit 500000 | where lastdata < ago(24h)\r\n// Oql: NOT(ObjectName=\"Advisor Metrics\" OR ObjectName=ManagedSpace) | measure max(TimeGenerated) as lastdata by Computer | top 500000 | where lastdata < NOW-24HOURS // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PTT: True; SortI: True; SortF: True} // Version: 0.1.122"}, "ETag": null, "ID": "subscriptions/a052d33b-b7c4-4dc7-9e17-5c89ea594669/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/XXXXXX/savedSearches/LogManagement(XXXXXX)_General|StaleComputers", "Name": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}]
```



#### Get Incident Statistic
Get Azure Sentinel Incident Statistics
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Time Frame|Time frame in hours for which to fetch Incidents|False|String||



##### JSON Results
```json
{"ID":"/subscriptions/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/XXXXXXXXXX/providers/Microsoft.XXXXXX","Name":"Cases","Kind":"CasesAggregation","Type":"Microsoft.SecurityInsights/Aggregations","Properties":{"Aggregation_By_Severity":{"Total_Critical_Severity":0,"Total_High_Severity":2,"Total_Medium_Severity":0,"Total_Low_Severity":0,"Total_Informational_Severity":0},"Aggregation_By_Status":{"Total_New_Status":2,"Total_In_Progress_Status":0,"Total_Resolved_Status":0,"Total_Dismissed_Status":0,"Total_True_Positive_Status":0,"Total_False_Positive_Status":0}}}
```



#### List Alert Rules
Get Azure Sentinel Scheduled Rules list
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Rule Severity|Severities of the alert rules to look for. Comma-separated string|False|String||
|Fetch Specific Alert Rule Types|What alert rule types action should return. Comma-separated string|False|String||
|Fetch Specific Alert Rule Tactics|What alert rule tactics action should return. Comma-separated string|False|String||
|Fetch only Enabled Alert Rules|If action should return only enabled alert rules|False|Boolean|false|
|Max rules to return|How many scheduled alert rules the action should return, for example, 50.|False|String||



##### JSON Results
```json
[{"ID": "/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/alertRules/d7e959da-20fb-4257-8744-xxxx", "ETag": "\"ef00b54e-0000-0c00-0000-5fa8eddd0000\"", "Name": "d7e959da-20fb-4257-8744-xxxx", "Kind": "Scheduled", "Type": "Microsoft.SecurityInsights/alertRules", "Properties": {"Alert_Rule_Template_Name": null, "Description": "", "Display_Name": "Multiple failed login attempts from the same IP", "Enabled": false, "Last_Modified_UTC": "2020-11-09T07:21:01.7747459Z", "Query": "SecurityEvent\r\n| where Activity startswith \"4625\"\r\n| summarize count() by IpAddress, Computer\r\n| where count_ >3\r\n| extend HostCustomEntity = Computer\r\n| extend IPCustomEntity = IpAddress", "Query_Frequency": "0 days 1 hour 0 minutes 0 seconds", "Query_Period": "5 days 0 hours 0 minutes 0 seconds", "Severity": "High", "Suppression_Duration": "0 days 5 hours 0 minutes 0 seconds", "Suppression_Enabled": false, "Tactics": ["InitialAccess", "Execution", "Persistence", "PrivilegeEscalation", "DefenseEvasion", "CredentialAccess", "Discovery", "LateralMovement", "Collection", "Exfiltration", "CommandAndControl", "Impact"], "Trigger": null}}]
```



#### Delete Alert Rule
Delete Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Rule ID|Alert Rule ID|True|String||



#### Add Comment to Incident
Add a comment to Azure Sentinel Incident.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Number|Specify Incident number to add comment to.|True|String||
|Comment to Add|Specify comment to add to Incident|True|String||



##### JSON Results
```json
{"id":"/subscriptions/a052d33b-xxxx-4dc7-9e17-xxxxxxxxxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/00cfebdc-xxxx-463f-8355-xxxxxxxxxxxx/Comments/f0f31d1a-xxxx-4774-a21d-xxxxxxxxxxxx","name":"f0f31d1a-xxxx-4774-a21d-xxxxxxxxxxxx","etag":"\"7e000812-0000-0c00-0000-xxxxxxxxxxxx\"","type":"Microsoft.SecurityInsights/Incidents/Comments","properties":{"message":"Some message","createdTimeUtc":"2021-04-09T03:21:35.0894288Z","lastModifiedTimeUtc":"2021-04-09T03:21:35.0894288Z","author":{"objectId":"f6ce2f43-xxxx-4b30-9a4a-xxxxxxxxxxxx","email":null,"name":"Comment created from external application - log_analytics_rest_api_for_sentinel","userPrincipalName":null}}}
```



#### Update Alert Rule
Update Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Rule ID|Alert Rule ID|True|String||
|Enable Alert Rule|Enable or disable new alert rule|False|Boolean|true|
|Name|Display name of the new alert rule|False|String||
|Severity|Severity of the new alert rule|False|List|Informational|
|Query|Query of the new alert rule|False|String||
|Frequency|How frequently to run the query, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.|False|String||
|Period of Lookup Data|Time of the last lookup data, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.|False|String||
|Trigger Operator|Trigger operator for this alert rule.Possible values are: GreaterThan, LessThan, Equal, NotEqual|False|List|GreaterThan|
|Trigger Threshold|Trigger threshold for this alert rule|False|String||
|Enable Suppression|Whether you want to stop running query after alert is generated|False|Boolean|true|
|Suppression Duration|How long you want to stop running query after alert is generated, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.|False|String||
|Description|Description of the new alert rule|False|String||
|Tactics|Tactics of the new alert rule. Comma-separated values.|False|String||



##### JSON Results
```json
{"Kind": "Scheduled", "Name": "31d38dc9-16fc-4464-8586-xxxx", "ID": "/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/alertRules/31d38dc9-16fc-4464-8586-xxxx", "ETag": "\"390028e7-0000-0d00-0000-xxxx\"", "Type": "Microsoft.SecurityInsights/alertRules", "Properties": {"Tactics": ["Discovery", "InitialAccess"], "Severity": "High", "Suppression_Enabled": false, "Query_Period": "5 days 0 hours 0 minutes 0 seconds", "Enabled": true, "Query_Frequency": "0 days 1 hour 0 minutes 0 seconds", "Alert_Rule_Template_Name": null, "Display_Name": "some name", "Description": "test", "Last_Modified_UTC": "2020-01-23T21:00:17.0860777Z", "Suppression_Duration": "0 days 5 hours 0 minutes 0 seconds", "Trigger": null, "Query": "SecurityEvent\r\n| where Activity startswith \"4625\"\r\n| summarize count() by IpAddress, Computer\r\n| where count_ >3\r\n| extend HostCustomEntity = Computer\r\n| extend IPCustomEntity = IpAddress"}}
```



#### Create Alert Rule
Create Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Enable Alert Rule|Enable or disable new alert rule|False|Boolean|true|
|Name|Display name of the new alert rule|True|String||
|Severity|Severity of the new alert rule|True|List|Informational|
|Query|Query of the new alert rule|True|String||
|Frequency|How frequently to run the query, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.|True|String||
|Period of Lookup Data|Time of the last lookup data, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.|True|String||
|Trigger Operator|Trigger operator for this alert rule.Possible values are: GreaterThan, LessThan, Equal, NotEqual|True|List|GreaterThan|
|Trigger Threshold|Trigger threshold for this alert rule|True|String||
|Enable Suppression|Whether you want to stop running query after alert is generated|False|Boolean|true|
|Suppression Duration|How long you want to stop running query after alert is generated, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute. Minimum is 5 minutes, maximum is 14 days.|True|String||
|Description|Description of the new alert rule|False|String||
|Tactics|Tactics of the new alert rule. Comma-separated values.|False|String||



##### JSON Results
```json
{"Kind": "Scheduled", "Name": "31d38dc9-16fc-4464-8586-41bbfa220766", "ID": "/subscriptions/a052d33b-b7c4-4dc7-9e17-5c89ea594669/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/alertRules/31d38dc9-16fc-4464-8586-41bbfa220766", "ETag": "\"390028e7-0000-0d00-0000-5e2a09660000\"", "Type": "Microsoft.SecurityInsights/alertRules", "Properties": {"Tactics": ["Discovery", "InitialAccess"], "Severity": "High", "Suppression_Enabled": false, "Query_Period": "5 days 0 hours 0 minutes 0 seconds", "Enabled": true, "Query_Frequency": "0 days 1 hour 0 minutes 0 seconds", "Alert_Rule_Template_Name": null, "Display_Name": "some name", "Description": "dsadad", "Last_Modified_UTC": "2020-01-23T21:00:17.0860777Z", "Suppression_Duration": "0 days 5 hours 0 minutes 0 seconds", "Trigger": null, "Query": "SecurityEvent\r\n| where Activity startswith \"4625\"\r\n| summarize count() by IpAddress, Computer\r\n| where count_ >3\r\n| extend HostCustomEntity = Computer\r\n| extend IPCustomEntity = IpAddress"}}
```



#### Update Incident Labels
Update Incident Labels
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Case Number|Specify Azure Sentinel incident number to update with new labels.|True|String||
|Labels|Specify new labels that should be appended to the Incident. Parameter accepts multiple values as a comma-separated string.|True|String||



##### JSON Results
```json
{"id": "/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/2e0ce5a0-7563-43a1-86a4-xxxxx", "name": "2e0ce5a0-7563-43a1-86a4-xxxxx", "etag": "\"fb006b40-0000-0c00-0000-xxxxx\"", "type": "Microsoft.SecurityInsights/Incidents", "properties": {"title": "Test Name", "description": "", "severity": "Informational", "status": "Closed", "classification": "Undetermined", "classificationComment": "Hello Test", "owner": {"objectId": null, "email": null, "assignedTo": null, "userPrincipalName": null}, "labels": [], "firstActivityTimeUtc": "2021-04-09T05:47:55.4959374Z", "lastActivityTimeUtc": "2021-04-14T05:47:55.4959374Z", "lastModifiedTimeUtc": "2021-04-14T06:53:30.2380985Z", "createdTimeUtc": "2021-04-14T05:53:00.8171911Z", "incidentNumber": "106xxx", "additionalData": {"alertsCount": 1, "bookmarksCount": 0, "commentsCount": 0, "alertProductNames": ["Azure Sentinel"], "tactics": ["InitialAccess", "Execution"]}, "relatedAnalyticRuleIds": ["/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/alertRules/545ee671-a997-4a5a-8763-xxxxx"], "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxxx/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/providers/Microsoft.SecurityInsights/Incidents/2e0ce5a0-7563-43a1-86a4-xxxxx", "providerName": "Azure Sentinel", "providerIncidentId": "106xxx"}}
```



#### Get Alert Rule Details
Get Details of the Azure Sentinel Scheduled Alert Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Rule ID|Alert Rule ID|True|String||



##### JSON Results
```json
{"Kind": "MLBehaviorAnalytics", "Name": "872ddb07-0415-4e57-b519-xxxx", "ID": "/subscriptions/a052d33b-b7c4-4dc7-9e17-xxxx/resourceGroups/Sentinel-Check/providers/Microsoft.OperationalInsights/workspaces/sentinelWork01/providers/Microsoft.SecurityInsights/alertRules/872ddb07-0415-4e57-b519-xxxx", "ETag": "\"62003e11-0000-0d00-0000-xxxx\"", "Type": "Microsoft.SecurityInsights/alertRules", "Properties": {"Tactics": ["InitialAccess"], "Severity": "Medium", "Suppression_Enabled": null, "Query_Period": null, "Enabled": true, "Query_Frequency": null, "Alert_Rule_Template_Name": "fa118b98-de46-4e94-87f9-xxxx", "Display_Name": "(Preview) Anomalous SSH Login Detection", "Description": "This detection uses machine learning (ML) to identify anomalous Secure Shell (SSH) login activity, based on syslog data. Scenarios include:\n\n* Impossible travel \u2013 when two successful login events occur from two locations that are impossible to reach within the timeframe of the two login events.\n* Unexpected location \u2013 the location from where a successful login event occurred is suspicious. For example, the location has not been seen recently.\n\nAllow two weeks after this alert is enabled for Azure Sentinel to build a profile of normal activity for your environment.\n\nThis detection requires a specific configuration of the data source. [Learn more](https://aka.ms/SentinelAnomalousSSHLoginDetection)", "Last_Modified_UTC": "2020-01-04T04:23:03.5607962Z", "Suppression_Duration": null, "Trigger": null, "Query": null}}
```



#### Delete Custom Hunting Rule
Delete Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hunting Rule ID|Hunting Rule ID|True|String||



#### Create Custom Hunting Rule
Create Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Display Name|Display name of the new custom hunting rule|True|String||
|Query|Query of the new custom hunting rule|True|String||
|Description|Description of the new custom hunting rule|False|String||
|Tactics|Tactics of the new custom hunting rule. Comma-separated values.|False|String||



##### JSON Results
```json
{"Properties": {"Category": "Log Management O", "Tactics": ["CustomTactic", "NotCustomTactic"], "Tags": [{"Name": "description", "Value": "Some Desc"}, {"Name": "tactics", "Value": "CustomTactic"}, {"Name": "tactics", "Value": "NotCustomTactic"}], "Version": 2, "Display_Name": "Some Name", "Query": "let timeframe = 7d;AWSCloudTrail| where TimeGenerated >= ago(timeframe)| where  EventName in~ (\"AttachGroupPolicy\", \"AttachRolePolicy\", \"AttachUserPolicy\", \"CreatePolicy\",\"DeleteGroupPolicy\", \"DeletePolicy\", \"DeleteRolePolicy\", \"DeleteUserPolicy\", \"DetachGroupPolicy\",\"PutUserPolicy\", \"PutGroupPolicy\", \"CreatePolicyVersion\", \"DeletePolicyVersion\", \"DetachRolePolicy\", \"CreatePolicy\")| project TimeGenerated, EventName, EventTypeName, UserIdentityAccountId, UserIdentityPrincipalid, UserAgent, UserIdentityUserName, SessionMfaAuthenticated, SourceIpAddress, AWSRegion, EventSource, AdditionalEventData, ResponseElements| extend timestamp = TimeGenerated, IPCustomEntity = SourceIpAddress, AccountCustomEntity = UserIdentityAccountId"}, "ETag": "W/\"datetime'2020-01-23T21%3A13%3A18.968169Z'\"", "ID": "subscriptions/a052d33b-b5c4-4dc7-9e17-5c89ea594669/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/savedSearches/a5a24268-XXXX-XXXX-XXXX-4ab6c9b7ad5b", "Name": "a052d33b-b5c4-XXXX-XXXX-5c89ea594669"}
```



#### Get Custom Hunting Rule Details
Get Details of the Azure Sentinel Custom Hunting Rule
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hunting Rule ID|Hunting Rule ID|True|String||



##### JSON Results
```json
{"Properties": {"Category": "Hunting Queries", "Tactics": ["DefenseEvasion"], "Tags": [{"Name": "description", "Value": "123"}, {"Name": "tactics", "Value": "DefenseEvasion"}, {"Name": "createdBy", "Value": "yuriy.landovskyy@siemplifycyarx.onmicrosoft.com"}, {"Name": "createdTimeUtc", "Value": "12/02/2019 09:21:18"}], "Version": 2, "Display_Name": "Yura Query", "Query": "\r\nlet timeframe = 7d;\r\nAWSCloudTrail\r\n| where TimeGenerated >= ago(timeframe)\r\n| where  EventName in~ (\"AttachGroupPolicy\", \"AttachRolePolicy\", \"AttachUserPolicy\", \"CreatePolicy\",\r\n\"DeleteGroupPolicy\", \"DeletePolicy\", \"DeleteRolePolicy\", \"DeleteUserPolicy\", \"DetachGroupPolicy\",\r\n\"PutUserPolicy\", \"PutGroupPolicy\", \"CreatePolicyVersion\", \"DeletePolicyVersion\", \"DetachRolePolicy\", \"CreatePolicy\")\r\n| project TimeGenerated, EventName, EventTypeName, UserIdentityAccountId, UserIdentityPrincipalid, UserAgent, \r\nUserIdentityUserName, SessionMfaAuthenticated, SourceIpAddress, AWSRegion, EventSource, AdditionalEventData, ResponseElements\r\n| extend timestamp = TimeGenerated, IPCustomEntity = SourceIpAddress, AccountCustomEntity = UserIdentityAccountId\r\n"}, "ETag": "W/\"datetime'2019-12-08T09%3A34%3A10.176586Z'\"", "ID": "subscriptions/a052d33b-XXXX-XXXX-XXXX-5c89ea594669/resourceGroups/sentinel-check/providers/Microsoft.OperationalInsights/workspaces/sentinelwork01/savedSearches/XXXXXXXXXXXXXXXXXXXXXXXXXX", "Name": "XXXXXXXXXXXXXXXXXXXXXXXXXX"}
```



#### Run KQL Query
Run Azure Sentinel KQL Query based on the provided action input parameters.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|KQL Query|A KQL Query to execute in Azure Sentinel. For example, to get security alerts available in Sentinel, query will be "SecurityAlert". Use other action input parameters (time span, limit) to filter the query results. For the examples of KQL queries consider Sentinel "Logs" Web page|True|String||
|Time Span|Time span to look for, use the following format: PT + number + (M, H), where M - minutes, H - hours. Use P + number + D to specify a number of days. Can be combined as P1DT1H1M - 1 day, 1 hour and 1 minute.|False|String||
|Query Timeout|Timeout value for the Azure Sentinel hunting rule API call. Note that Siemplify action python process timeout should be adjusted accordingly for this parameter, to not timeout action sooner than specified value because of the python process timeout.|False|String||
|Record Limit|How many records should be fetched. Optional parameter, if set, adds a "| limit x" to the kql query where x is the value set for the record limit. Can be removed if "limit" is already set in kql query or not needed.|False|String||



##### JSON Results
```json
[{"Avg7Day": 327, "EventID": 4625, "Account": "host.local\\some.user", "StartTimeUtc": "2020-01-08T13:57:26.75Z", "LogonTypeName": "3 - Network", "timestamp": "2020-01-08T13:57:26.75Z", "CountLast7day": 2292, "EndTimeUtc": "2020-01-08T17:38:05.337Z", "CountToday": 1554, "SubStatus": "0xc0000071", "Computer": "us-dc-v01001.host.local", "AccountType": "User", "HostCustomEntity": "us-dc-v01001.host.local", "WorkstationName": "US-DC-V01001", "IpAddress": "127.0.0.1", "AccountCustomEntity": "host.local\\some.user"}]
```






## Jobs

#### Sync AS Incidents


|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment|True|String|Default Environment|
|Instance Name|False|String|None|
|Hours Back|True|Integer|24|
|Sync Tags|True|String|Azure Sentinel|
|Only Favorite Comments|False|Boolean|false|

#### Sync Azure Sentinel Entities
Will create new entities in Siemplify Alerts from AS incidents

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment|True|String|Default Environment|
|Instance Name|False|String|None|
|Hours Back|True|Integer|24|
|Sync Tags|True|String|Azure Sentinel|



## Connectors
#### Microsoft Azure Sentinel Incident Connector
Fetches Incidents from Azure Sentinel.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The field name used to determine the device product|True|String|ProductName|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|AlertName|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|180|
|Environment Field Name|Describes the name of the field where the environment name is stored.|False|String||
|Environment Regex Pattern|If defined - the connector will implement the specific RegEx pattern on the data from "environment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"|False|Integer|None|
|API Root|The API Root of Microsoft Azure Sentinel REST API root.|True|String|https://management.azure.com|
|OAUTH2 Login Endpoint Url|Specify the url, that connector should use for OAUTH2 Login.|True|String|https://login.microsoftonline.com|
|Client ID|Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.|True|String|None|
|Client Secret|Secret that was entered for Azure AD app registration|True|Password|None|
|Azure Active Directory ID|Azure Active Directory Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.|True|String|None|
|Azure Sentinel Workspace Name|Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.|True|String||
|Azure Subscription ID|Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. |True|String|None|
|Azure Resource Group|Name of Azure Resource Group where Azure Sentinel is located.|True|String||
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|Boolean|false|
|Max Incidents per Cycle|How many incidents should be processed during one connector run|False|Integer|10|
|Offset Time In Hours|Fetch alerts from X hours backwards. Default value: 24 hours.|False|Integer|24|
|Incident Statuses to Fetch|Specify the statuses of the incidents that should be fetched by the Siemplify server. Comma-separated string.|True|String|Draft, New, InProgress, Closed|
|Incident Severities to Fetch|Specify the severities of the incidents that should be fetched by the Siemplify server. Comma-separated string.|True|String|Informational, Low, Medium, High, Critical|
|Proxy Server Address|Proxy server to use for connection.|False|IP||
|Proxy Server Username|Proxy server username|False|String||
|Proxy Server Password|Proxy server password|False|Password||


#### Microsoft Azure Sentinel Incident Connector v2
Fetches Incidents from Azure Sentinel.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Describes the name of the field where the product name is stored.|True|String|product_type|
|EventClassId|Describes the name of the field where the event name is stored.|False|String|event_type|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|Integer|480|
|Environment Field Name|Describes the name of the field where the environment name is stored. If environment field isn't found, environment is "".|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is "".|False|String|.*|
|Azure Subscription ID|Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. |True|String||
|Azure Active Directory ID|Azure Active Directory Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.|True|String||
|API Root|The API Root of Microsoft Azure Sentinel REST API root.|True|String|https://management.azure.com|
|OAUTH2 Login Endpoint Url|Specify the url, that connector should use for OAUTH2 Login.|True|String|https://login.microsoftonline.com|
|Azure Resource Group|Name of Azure Resource Group where Azure Sentinel is located.|True|String||
|Azure Sentinel Workspace Name|Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.|True|String||
|Client ID|Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.|True|String||
|Client Secret|Secret that was entered for Azure AD app registration|True|Password||
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|Boolean|false|
|Max New Incidents Per Cycle|How many incidents should be processed during one connector run|True|Integer|10|
|Max Backlog Incidents per cycle|How many incidents  connector should try to fetch from the backlog during one connector run.|True|Integer|10|
|Offset Time In Hours|Fetch alerts from X hours backwards. Default value: 24 hours.|True|Integer|24|
|Incident Statuses to Fetch|Specify the statuses of the incidents that should be fetched by the Siemplify server. Parameter can take multiple values as a comma separated string.|True|String|New, Closed|
|Incident Severities to Fetch|Specify the severities of the incidents that should be fetched by the Siemplify server. Parameter can take multiple values as a comma separated string.|True|String|Informational, Low, Medium, High|
|Use the same approach with event creation for all alert types?|By default connector uses a different approach with Scheduled Alert or NRT types of alerts - it tries to fetch events that caused the alert by running the query specified in alert details. Specify whether to change this behavior and use the same approach for the scheduled and NRT alerts as for other alert types.|False|Boolean|false|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Alerts Padding Period|Time frame in minutes to try to fetch alerts for incidents.|True|Integer|60|
|EventFieldFallback|Specify a comma separated list of alert attributes that should be used as a fallback for the "Event Field Name" parameter in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.|True|String|kind|
|ProductFieldFallback|Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "Product Field Name" parameter and "DeviceProduct" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.|True|String|ProductName,properties_providerName|
|VendorFieldFallback|Specify a comma separated list of incident attributes that should be used as a fallback for the "DeviceVendor" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.|True|String|vendorName|
|StartTimeFallback|Specify a comma separated list of incident or alert attributes that should be used as a fallback for the “Start Time” alert field in descending order. Additionally, new “Siemplify_Start_Time“ attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to Siemplify.|True|String|properties_firstActivityTimeGenerated,properties_startTimeUtc,properties_createdTimeUtc,properties_firstAlertTimeGenerated|
|EndTimeFallback|Specify a comma separated list of incident or alert attributes that should be used as a fallback for the “End Time” alert field in descending order. Additionally, new “Siemplify_End_Time“ attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to Siemplify.|True|String|properties_lastActivityTimeGenerated,properties_endTimeUtc,properties_createdTimeUtc,properties_lastAlertTimeGenerated|
|Enable Fallback Logic Debug?|Specify if connector should add to the created events a “debug“ fields that will contain the values it used for fallback.|False|Boolean|false|
|Scheduled Alerts Events Limit to Ingest|Specify the maximum number of events the connector should ingest per a single Azure Sentinel Scheduled or NRT Alert.|False|Integer|100|
|Create Siemplify Alerts for Sentinel incidents that do not have entities?|If enabled, connector will create Siemplify alerts from Microsoft Sentinel incidents that dont have entities. Otherwise, such incidents will be skipped for all Sentinel incidents types except Sentinel Scheduled and NRT alerts.|False|Boolean|false|
|Incident's Alerts Limit to Ingest|Specify the maximum number of  alerts the connector should ingest per a single Azure Sentinel incident.|False|Integer|10|
|Proxy Server Address|Proxy server to use for connection.|False|String||
|Proxy Username|Proxy server username|False|String||
|Proxy Password|Proxy server password|False|Password||
|Incidents Padding Period (minutes)|If specified, to get incidents returned not in chronological order, connector will fetch Sentinel incidents from this value backwards in time.|False|Integer||
|Alert Name Template|If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Siemplify Alert Name. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [title]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|String||
|Rule Generator Template|If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Siemplify Rule Generator. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [severity]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default rule generator value.|False|String||




