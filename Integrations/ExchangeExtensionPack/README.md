
# ExchangeExtensionPack

Exchange Extension Pack integration works on Exchange Management Shell. The Exchange Management Shell is built on Windows PowerShell technology and provides a powerful command-line interface that enables the automation of Exchange administration tasks.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Exchange On-Prem Server Address|None|False|String|x.x.x.x|
|Exchange Office365 Compliance Uri|None|False|String|https://ps.compliance.protection.outlook.com/powershell-liveid/|
|Exchange Office365 Online Powershell Uri|None|False|String|https://outlook.office365.com/powershell-liveid/|
|Domain|None|False|String|domain.com|
|User name|None|False|String|user|
|Password|None|False|Password|None|
|Is Exchange On-Prem?|None|False|Boolean|False|
|Is Office365 (Exchange Online)?|None|False|Boolean|False|



## Actions
#### Add Senders to Exchange-Siemplify Mail Flow Rule
Action will get as a parameter a list of Email Addresses, or will work on User entities with Email regexes (if parameters are not provided), and will be able to create a new rule,filtering the senders from your Exchange Server. Actions can be modified in the parameters using the rule parameter. Note - to use this action, please make sure you have Organization Management permissions, as stated here: https://docs.microsoft.com/en-us/exchange/permissions-exo/feature-permissions
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Email Addresses|Specify the email addresses you would like to add to the rule, in a comma separated list. If no parameter will be provided, action will work with User entities.|False|String||
|Rule to add senders to|Specify the rule to add the sender to. If the rule doesn't exist - action will create it where it's missing.|True|List|Siemplify - Senders List - Permanently Delete|
|Should add senders' domain to the corresponding Domains List rule as well?|Specify whether the action should automatically take the domains of the provided email addresses and add them as well to the corresponding domain rules (same rule action for domains)|False|Boolean|false|



##### JSON Results
```json
{"success":["test1@example.com","test2@example.com"],"already_available":["test3@example.com"],"invalid":["invalid"]}
```



#### Fetch Compliance Search Results
Fetch results for the completed Compliance Search. Note: Action is not working on Siemplify entities. Note2: Maximum of 200 elements will be displayed, but actual search can have more findings that are shown.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Compliance Search Name|Name for the Compliance Search. Note that name shouldn't contain special characters.|True|String||
|Max Emails To Return|Specify how many emails action can return.|False|String||
|Remove Compliance Search Once Action Completes?|Specify whether action should remove from Exchange server the search action and any related fetch or purge tasks once the action completes.|False|Boolean|true|
|Create Case Wall Output Table?|Specify if action should create case wall output table. If Max Emails To Return is set to a bigger number, its recommended to uncheck this to increase action performance.|False|Boolean|true|



##### JSON Results
```json
[{"Location":"test@example.com","Sender":"James Bond","Subject":"search test","Type":"Email","Size":"61772","Received Time":"3/12/2021 9:43:59 AM","Data Link":"data/All/FLDR5402c62d-7730-4c93-8f34-6bxxxxxxxxxx/BATCH0000/MSG192bc965-18c9-4c06-8834-2cxxxxxxxxxx.eml","Name":"test"},{"Location":"test@example.com","Sender":"James Bond","Subject":"search test 2","Type":"Email","Size":"60881","Received Time":"3/12/2021 9:43:59 AM","Data Link":"data/All/FLDR5402c62d-7730-4c93-8f34-6bxxxxxxxxxx/BATCH0000/MSG9eefda9c-b1b5-46f0-8a54-bdxxxxxxxxxx.eml","Name":"test"}]
```



#### Ping
Test connectivity to the Exchange or O365 server with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Remove Domains from Exchange-Siemplify Mail Flow Rules
Action will get as a parameter a list of Domains, and will be able to remove the provided domains from the existing rules. Note - to use this action, please make sure you have Organization Management permissions, as stated here: https://docs.microsoft.com/en-us/exchange/permissions-exo/feature-permissions
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Domains|Specify the Domains you would like to remove from the rule, in a comma separated list.|False|String||
|Rule to remove Domains from|Specify the rule to remove the Domains from. If the rule doesn't exist - action will do nothing.|True|List|Siemplify - Domains List - Permanently Delete|



##### JSON Results
```json
{"success":["test1.com","test2.com"],"didn't_exist":["test3.com"],"invalid":["invalid"]}
```



#### Delete Exchange-Siemplify Mail Flow Rules
Action will get as a parameter a rule name and will delete it. Note - to use this action, please make sure you have Organization Management permissions, as stated here: https://docs.microsoft.com/en-us/exchange/permissions-exo/feature-permissions
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule Name To Delete|Specify the Rule name you would like to completely delete|True|List||



#### List Exchange-Siemplify Mail Flow Rules
Action will get as a parameter a rule name and will list it. Note - to use this action, please make sure you have Organization Management permissions, as stated here: https://docs.microsoft.com/en-us/exchange/permissions-exo/feature-permissions
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule Name To List|Specify the Rule name you would like to list|True|List||



##### JSON Results
```json
[{"Priority":0,"ManuallyModified":false,"Description":"If the message:\r\n\tIs received from 'test@example1.com' or 'test@example2.com'\r\nTake the following actions:\r\n\tDelete the message without notifying the recipient or sender\r\n","Conditions":["Microsoft.Exchange.MessagingPolicies.Rules.Tasks.FromPredicate"],"Actions":["Microsoft.Exchange.MessagingPolicies.Rules.Tasks.DeleteMessageAction"],"State":"Enabled","Mode":"Enforce","FromAddressContainsWords":null,"Identity":"Siemplify - Senders List - Permanently Delete","Name":"Siemplify - Senders List - Permanently Delete","DistinguishedName":"CN=Siemplify - Senders List - Permanently Delete,CN=TransportVersioned,CN=Rules,CN=Transport Settings,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=exlab,DC=local","IsValid":true,"From":["test@example1.com","test@example2.com"],"Guid":"xxxxx426-b665-41f9-82e0-0f1fd63xxxxx","ImmutableId":"xxxxx426-b665-41f9-82e0-0f1fd63xxxxx","WhenChanged":"/Date(1621952909000)/","ExchangeVersion":"0.1 (8.0.535.0)","OrganizationId":"","ObjectState":"Unchanged"},{"Priority":1,"ManuallyModified":false,"Description":"If the message:\r\n\tIncludes these words in the sender's address: 'example1.com' or 'example2.com'\r\nTake the following actions:\r\n\tDelete the message without notifying the recipient or sender\r\n","Conditions":["Microsoft.Exchange.MessagingPolicies.Rules.Tasks.FromAddressContainsPredicate"],"Actions":["Microsoft.Exchange.MessagingPolicies.Rules.Tasks.DeleteMessageAction"],"State":"Enabled","Mode":"Enforce","FromAddressContainsWords":["example1.com","example2.com"],"Identity":"Siemplify - Domains List - Permanently Delete","Name":"Siemplify - Domains List - Permanently Delete","DistinguishedName":"CN=Siemplify - Domains List - Permanently Delete,CN=TransportVersioned,CN=Rules,CN=Transport Settings,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=exlab,DC=local","IsValid":true,"From":null,"Guid":"xxxxx697-e143-41aa-8dee-b783a78xxxxx","ImmutableId":"xxxxx697-e143-41aa-8dee-b783a78xxxxx","WhenChanged":"/Date(1621952960000)/","ExchangeVersion":"0.1 (8.0.535.0)","OrganizationId":"","ObjectState":"Unchanged"}]
```



#### Purge Compliance Search Results
Purge emails found by the completed Compliance Search. Note: Action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Compliance Search Name|Name for the Compliance Search. Note that name shouldn't contain special characters.|True|String||
|Perform a HardDelete for deleted emails?|Specify whether HardDelete should be performed. This option is applies only to O365 and mark emails for permanent removal from the mailbox.|False|Boolean|false|
|Remove Compliance Search Once Action Completes?|Specify whether action should remove from Exchange server the search action and any related fetch or purge tasks once the action completes.|False|Boolean|true|



##### JSON Results
```json
{"Item count":"5","Purge Type":"SoftDelete"}
```



#### Remove Senders from Exchange-Siemplify Mail Flow Rules
Action will get as a parameter a list of Senders, or will work on User entities (if parameters are not provided), and will be able to remove the provided Senders from the existing rules. Note - to use this action, please make sure you have Organization Management permissions, as stated here: https://docs.microsoft.com/en-us/exchange/permissions-exo/feature-permissions
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Email Addresses|Specify the email addresses you would like to remove from the rule, in a comma separated list. If no parameter will be provided, action will work with entities.|False|String||
|Rule to remove Senders from|Specify the rule to remove the Senders from. If the rule doesn't exist - action will do nothing.|True|List|Siemplify - Senders List - Permanently Delete|
|Should remove senders' domains from the corresponding Domains List rule as well?|Specify whether the action should automatically take the domains of the provided email addresses and remove them as well from the corresponding domain rules (same rule action for domains)|False|Boolean|false|



##### JSON Results
```json
{"success":["test1@example.com","test2@example.com"],"didn't_exist":["test3@example.com"],"invalid":["invalid"]}
```



#### Delete Compliance Search
Delete Compliance Search and any associated with it fetch results or purge emails tasks. Note: Action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Compliance Search Name|Name for the Compliance Search. Note that name shouldn't contain special characters.|True|String||



#### Run Compliance Search
Run Exchange Compliance Search based on the provided search conditions. If the fetch compliance search results checkbox is set, action returns the search results similarly to the fetch compliance search results action. Exchange Compliance Search provides a fast mechanism to search in multiple mailboxes that will be most useful for large Organizations with 1000+ mailboxes. Note: Action is not working on Siemplify entities.  Note2: If "Fetch Compliance Search Results?" checkbox is checked, maximum of 200 elements will be displayed, but actual search can have more findings that are shown.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Compliance Search Name|Name for the Compliance Search. Note that name shouldn't contain special characters.|True|String||
|Subject Filter|Filter condition, specify what subject to search for emails|False|String||
|Sender Filter|Filter condition, specify who should be the sender of needed emails|False|String||
|Recipient Filter|Filter condition, specify who should be the recipient of needed emails|False|String||
|Operator|Operator to use to construct query from conditions above.|False|List|AND|
|Time Frame (hours)|Time frame interval in hours to search for emails.|False|String||
|Location to Search Emails In|Location to search emails in, can be one of the following: Comma separate list of mailboxes. A distribution group or mail-enabled security group All - for all mailboxes in organization.|True|String||
|Fetch Compliance Search Results?|Specify whether the action should immediately fetch the compliance search results. Note that maximum of 200 elements will be displayed, but actual search can have more findings that are shown.|False|Boolean|false|
|Max Emails To Return|Specify how many emails action can return.|False|String||
|Create Case Wall Output Table?|Specify if action should create case wall output table. If Max Emails To Return is set to a bigger number, its recommended to uncheck this to increase action performance.|False|Boolean|false|
|Advanced Query|Instead of subject, sender or recipient filters, provide a query you want to run compliance search on. Consider https://docs.microsoft.com/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference and https://docs.microsoft.com/en-us/exchange/message-properties-indexed-by-exchange-search-exchange-2013-help?redirectedfrom=MSDN for reference on query syntax.|False|String||



##### JSON Results
```json
{"Name":"test","RunBy":"James Bond","JobEndTime":"2021-03-18T12:42:49.92","Status":"Completed"}
```



#### Add Domains to Exchange-Siemplify Mail Flow Rules
Action will get as a parameter a list of Domains, and will be able to create a new rule, filtering the domains from your Exchange Server. Actions to take can be modified in the parameters using rule parameters. Note - to use this action, please make sure you have Organization Management permissions, as stated here: https://docs.microsoft.com/en-us/exchange/permissions-exo/feature-permissions
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Domains|Specify the Domains you would like to add to the rule, in a comma separated list.|False|String||
|Rule to add Domains to|Specify the rule to add the Domains to. If the rule doesn't exist - action will create it where it's missing.|True|List|Siemplify - Domains List - Permanently Delete|



##### JSON Results
```json
{"success":["test1.com","test2.com"],"already_available":["test3.com"],"invalid":["invalid"]}
```






## Jobs



## Connectors


