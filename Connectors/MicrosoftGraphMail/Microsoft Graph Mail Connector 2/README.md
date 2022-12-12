# Microsoft Graph Mail Connector 2
Connector can be used to fetch emails from the Microsoft Graph Mail service. Connector dynamic list can be used to filter specific values from the email body and subject parts using regexes. By default, regex is used to filter out the urls from the email.


Integration: MicrosoftGraphMail

Integration Version: 2.0

Device Product Field: device_product

Event Name Field: event_name
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Email exclude pattern|Regular expression to exclude specific emails from being ingested by the connector. Works with both subject and body part of email. Example is, to exclude mass mailing emails like news from being ingested.|False||
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|300|
|Azure AD Endpoint|Azure AD endpoint to connect to. Can be different for different tenant types.|True|https://login.microsoftonline.com|
|Microsoft Graph Endpoint|Microsoft Graph endpoint to connect to.  Can be different for different tenant types.|True|https://graph.microsoft.com|
|Client ID|For Office 365 Oauth authentication, Client (Application) ID of Azure Active Directory App that will be used for the integration.|True|de2cd7d5-88b3-4f0e-8322-089683733bbc|
|Client Secret|For Office 365 Oauth authentication, secret can be provided for the auth flow.|True|***************|
|Environment Field Name|Describes the name of the field where the environment name is stored.
If environment field isn't found, environment is ""
|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.
Default is .* to catch all and return value unchanged.
Used to allow the user to manipulate the environment field via regex logic
If regex pattern is null or empty, or the environment value is null, the final environment result is ""
|False|.*|
|Max Emails Per Cycle|Fetch X emails per connector cycle|True|10|
|Tenant (Directory) ID|For Office 365 Oauth authentication, Azure Tenant (Directory) ID.|True|3f06a216-e798-47d3-9b06-31482aa5a648|
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter is case sensitive|True|SiemplifyTest|
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False||
|Proxy Server Address|The address of the proxy server to use.|False|None|
|Proxy Username|The proxy username to authenticate with.|False||
|Offset Time In Hours|Fetch emails from X hours backwards|True|48|
|Create a Separate Siemplify Alert per Attached Mail File|If enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|false|
|Unread Emails Only|If checked, cases will be pulled only from unread emails|False|false|
|Mark Emails as Read|If checked, after the emails have been pulled they will be marked as read.|False|false|
|Disable Overflow|If enabled, the connector will ignore the Siemplify overflow mechanism when creating alerts.|False|false|
|Original Received Mail Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the original email received in the monitored mailbox.|False||
|Attached Mail File Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False||
|Headers to add to events|Specify what values should be filtered from the "internetMessageHeaders" list and what will be added to the Siemplify event. By default, all headers are added, if only specific headers are needed - specify them as a comma separated list by their name, example: "DKIM-Signature", "Received", "From". If no internetHeaders should be added specify a keyword: None|False|None|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Siemplify Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled.|False||
|Proxy Password|The proxy password to authenticate with.|False||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Microsoft Graph Mail server is valid.|False|true|
|Mail Address|Mail address to use for connector.|True|paul.dragoi@nb.com|

