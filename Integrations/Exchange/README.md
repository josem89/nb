![Exchange](./Resources/Exchange.svg)

# Exchange

Integration provides support for Microsoft Exchange 2010 - 2019 and Microsoft Office365 mail servers. Integration uses Exchange Web Services (EWS) for communication. Integration includes a series of actions to send out emails and work with received emails, along with a connector to monitor specific mailboxes and ingest emails from that mailboxes as alerts to Siemplify for further analysis.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Mail Server Address|None|True|String||
|Mail address|None|True|String||
|Domain|None|False|String||
|Use Domain For Authentication|None|False|Boolean|False|
|Use Autodiscover Service|None|False|Boolean|False|
|Username|None|False|String||
|Password|None|False|Password|None|
|Client ID|None|False|String||
|Client Secret|None|False|Password|None|
|Tenant (Directory) ID|None|False|String||
|Redirect URL|None|False|String|http://localhost|
|Refresh Token|None|False|Password|None|
|Verify SSL|None|False|Boolean|False|



## Actions
#### Get Authorization
For integration configuration with Oauth authentication, run the action and browse to the received URL to get a link with access code. That link needs to be provided to the Generate Token action next to get the refresh token.
Timeout - 600 Seconds



#### Remove Senders from Exchange-Siemplify Inbox Rules
Action will get as a parameter a list of Senders, or will work on User entities (if parameters are not provided), and will be able to remove the provided Senders from the existing rules. WARNING: Action will modify your current users inbox rules, using EWS. NOTICE - to perform operation, please configure EDiscovery Group and Author permissions. For full details, please visit: https://integrations.siemplify.co/doc/exchang. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Senders|Specify the Senders you would like to remove from the rule, in a comma separated list. If no parameter will be provided, action will work with entities.|False|String||
|Rule to remove Senders from|Specify the rule to remove the Senders from. If the rule doesn't exist - action will do nothing.|True|List|Siemplify - Senders List - Move To Junk|
|Remove Senders from all available Rules|Specify whether action should look for the provided Senders in all of Siemplify inbox rules.|False|Boolean|false|
|Should remove senders' domains from the corresponding Domains List rule as well?|Specify whether the action should automatically take the domains of the provided email addresses and remove them as well from the corresponding domain rules (same rule action for domains)|False|Boolean|false|
|Perform action in all mailboxes|If checked, action will be performed in all mailboxes accessible with current impersonalization settings|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|50|



#### Search Mails
Search for specific emails in configured mailbox using multiple provided search criteria. Action return information on found in mailbox emails in JSON format. NOTICE - to search for an email in all mailboxes, please configure impersonation permissions. https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange. Note: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Mailbox folder to search email in. Parameter should also accept comma separated list of folders to check the user response in multiple folders.|False|String|Inbox|
|Message IDs|Specify a comma-separated list of message ids that need to be searched. Note: this filter has priority over the other ones.|False|String||
|Subject Filter|Filter condition, specify what subject to search for emails|False|String||
|Sender Filter|Filter condition, specify who should be the sender of needed emails|False|String||
|Recipient Filter|Filter condition, specify who should be the recipient of needed emails|False|String||
|Time Frame (minutes)|Filter condition, specify in what time frame in minutes should action look for emails|False|String||
|Only Unread|Filter condition, specify if search should look only for unread emails|False|Boolean|false|
|Max Emails To Return|Return max X emails as an action result|False|String|100|
|Search in all mailboxes|If checked, search in all mailboxes accessible with current impersonalization settings|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Search in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|25|
|Mailboxes|Specify a comma-separated list of mailboxes that need to be searched. This parameter has priority over "Search in all mailboxes".|False|String||
|Start Time|Specify the start time for the email search. Format: ISO 8601. This parameter has a priority over "Time Frame (minutes)".|False|String||
|End Time|Specify the end time for the email search. Format: ISO 8601. If nothing is provided and "Start Time" is valid then this parameter will use current time.|False|String||
|Body Regex Filter|Specify a regex pattern that needs to be searched in body part of the email.|False|String||



##### JSON Results
```json
[{"body": "Mail Body", "subject": "Mail Subject", "author": "john_doe@example.com"}, {"body": "", "subject": "Mail Subject", "author": "john_doe@example.com"}]
```



#### Ping
Test connectivity to Microsoft Exchange instance with parameters provided at the integration configuration page on Marketplace tab.
Timeout - 600 Seconds



#### Send Email And Wait
Send email and wait action, Send to field is comma separated. Note: Sender's display name can be configured in the client under the account settings
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Subject|The subject of the email|True|String||
|Send to|Recipient email address. Multiple addresses can be separated by commas|True|String||
|CC|CC email address. Multiple addresses can be separated by commas|False|String||
|BCC|bcc email address. Multiple addresses can be separated by commas|False|String||
|Mail content|Email body|True|Email Content||
|Fetch Response Attachments|Allows attachment of files from response mail.|False|Boolean||
|Folder to Check for Reply|Parameter can be used to specify mailbox email folder (mailbox that was used to send the email with question) to search for the user reply in this folder. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive.|False|String|Inbox|



##### JSON Results
```json
[{"EntityResult": {"attachments": [], "sensitivity": "Normal", "effective_rights": " test", "has_attachments": "false", "last_modified_name": "mail", "is_submitted": "false"}, "Entity": "mail@mail.com"}]
```



#### Delete Exchange-Siemplify Inbox Rules
Action will get as a parameter a rule name and will delete it from all the specified mailboxes. WARNING: Action will modify your current users inbox rules, using EWS. NOTICE - to perform operation, please configure EDiscovery Group and Author permissions. For full details, please visit: https://integrations.siemplify.co/doc/exchang. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule Name To Delete|Specify the Rule name you would like to completely delete from the relevant mailboxes|True|List||
|Perform action in all mailboxes|If checked, action will be performed in all mailboxes accessible with current impersonalization settings|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|50|



#### Extract EML Data
Extract data from email's EML attachments.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Folder to fetch from. Default is Inbox|False|String|Inbox|
|Message ID|e.g. <1701cf01ba314032b2f1df43262a7723@gmail.com>|True|String||
|Regex Map JSON|e.g. {ips: \b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\b}|False|String|{}|



##### JSON Results
```json
[{"count":3,"files":{"mxtoolbox_test_case.case":"090a131a0726dea8f5b0c2205ffc9527"},"from":"Exam Example<exam@test.com>","text":"hello eml test","regex":{},"regex_from_text_part":{},"to":"Test Test <test@test.com>","html":"<html><div></div></html>","date":"Wed, 12 Sep 2018 12:36:17 +0300","subject":"eml test"}]
```



#### Send Mail
Send Email from specific mailbox to an arbitrary list of recipients. Action can be used to inform users about specific alerts created in the Siemplify or inform about the results of processing of specific alerts.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Subject|The mail subject part|True|String||
|Send to|Arbitrary comma separated list of email addresses for the email recipients. For example: user1@company.co, user2@company.co|True|String||
|CC|Arbitrary comma separated list of email addresses to be put in the CC field of email. Format is the same as for the "Send to" field|False|String||
|BCC|Arbitrary comma separated list of email addresses to be put in the BCC field of email. Format is the same as for the "Send to" field|False|String||
|Attachments Paths|Comma separated list of attachments file paths stored on the server for addition to the email. For example: C:\<Siemplify work dir>\file1.pdf, C:\<Siemplify work dir>\image2.jpg|False|String||
|Mail content|The email body part|True|Email Content||
|Reply-To Recipients|Specify a comma-separated list of recipients that will be used in the "Reply-To" header. Note: The Reply-To header is added when the originator of the message wants any replies to the message to go to that particular email address rather than the one in the "From:" address.|False|String||
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to either encrypt or sign the email. Note: for signing you need to also provide "Base64 Encoded Signature". For encryption, only this parameter needs to have a value.|False|Password||
|Base64 Encoded Signature|Specify a base64 encoded signature that will be used to sign the email. Note: "Base64 Encoded Certificate" needs to be provided as well for signature to work and contain the signing certificate.|False|Password||



##### JSON Results
```json
{"mime_content": "'From: Administrator <Administrator@siemplifylab.local>\\r\\nTo: Administrator <Administrator@siemplifylab.local>\\r\\nSubject: Test subject\\r\\nThread-Topic: Test subject\\r\\nThread-Index: AQHWmsTgBEcHjewfyEKH4YkB+Lo0RQ==\\r\\nDate: Mon, 5 Oct 2020 06:09:02 +0300\\r\\nMessage-ID: <160186734388.8568.315529398955149940@siemplify>\\r\\nAccept-Language: en-US\\r\\nContent-Language: en-US\\r\\nX-MS-Has-Attach:\\r\\nX-MS-Exchange-Organization-SCL: -1\\r\\nX-MS-TNEF-Correlator:\\r\\nX-MS-Exchange-Organization-RecordReviewCfmType: 0\\r\\nContent-Type: multipart/alternative;\\r\\n\\tboundary=\"_000_1601867343888568315529398955149940siemplify_\"\\r\\nMIME-Version: 1.0\\r\\n\\r\\n--_000_1601867343888568315529398955149940siemplify_\\r\\nContent-Type: text/plain; charset=\"us-ascii\"\\r\\n\\r\\nTest mail content\\r\\n\\r\\n--_000_1601867343888568315529398955149940siemplify_\\r\\nContent-Type: text/html; charset=\"us-ascii\"\\r\\n\\r\\n<html>\\r\\n<head>\\r\\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=us-ascii\">\\r\\n</head>\\r\\n<body>\\r\\n<p>Test mail content </p>\\r\\n</body>\\r\\n</html>\\r\\n\\r\\n--_000_1601867343888568315529398955149940siemplify_--\\r\\n'", "_id": "ItemId(id='AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX/0/LnCkytWTOh2sCWzQAAAgEJAAAAMnX/0/LnCkytWTOh2sCWzQAAARDFFwAAAA==', changekey='CQAAABYAAAAydf/T8ucKTK1ZM6HawJbNAAAAEZla')", "parent_folder_id": "ParentFolderId(id='AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAuAAADneAeRbLkN0i93LTVa54xxwEAMnX/0/LnCkytWTOh2sCWzQAAAgEJAAAA', changekey='AQAAAA==')", "item_class": "IPM.Note", "subject": "Test subject", "sensitivity": "Normal", "text_body": "Test mail content\r\n", "body": "<html>\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n</head>\r\n<body>\r\n<p>Test mail content </p>\r\n</body>\r\n</html>\r\n", "attachments": [], "datetime_received": "2020-10-05 03:09:02+00:00", "size": 2568, "categories": null, "importance": "Normal", "in_reply_to": null, "is_submitted": true, "is_draft": true, "is_from_me": false, "is_resend": false, "is_unmodified": false, "headers": null, "datetime_sent": "2020-10-05 03:09:02+00:00", "datetime_created": "2020-10-05 03:09:02+00:00", "reminder_due_by": null, "reminder_is_set": false, "reminder_minutes_before_start": 0, "display_cc": null, "display_to": "Administrator", "has_attachments": false, "culture": "en-US", "effective_rights": "EffectiveRights(create_associated=False, create_contents=False, create_hierarchy=False, delete=True, modify=True, read=True, view_private_items=True)", "last_modified_name": "Administrator", "last_modified_time": "2020-10-05 03:09:02+00:00", "is_associated": false, "web_client_read_form_query_string": "?ItemID=AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX%2F0%2FLnCkytWTOh2sCWzQAAAgEJAAAAMnX%2F0%2FLnCkytWTOh2sCWzQAAARDFFwAAAA%3D%3D&exvsurl=1&viewmodel=ReadMessageItem", "web_client_edit_form_query_string": null, "conversation_id": "ConversationId(id='AAQkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAQAARHB43sH8hCh+GJAfi6NEU=')", "unique_body": "<html><body><div>\r\n<div>\r\n<div style=\"margin-top:14pt;margin-bottom:14pt;\">Test mail content </div>\r\n</div>\r\n</div>\r\n</body></html>", "sender": "Mailbox(name='Administrator', email_address='Administrator@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')", "to_recipients": ["Mailbox(name='Administrator', email_address='Administrator@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')"], "cc_recipients": null, "bcc_recipients": null, "is_read_receipt_requested": false, "is_delivery_receipt_requested": false, "conversation_index": "\\x01\\x01\\xd6\\x9a\\xc4\\xe0\\x04G\\x07\\x8d\\xec\\x1f\\xc8B\\x87\\xe1\\x89\\x01\\xf8\\xba4E'", "conversation_topic": "Test subject", "author": "Mailbox(name='Administrator', email_address='Administrator@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')", "message_id": "<160186734388.8568.315529398955149940@siemplify>", "is_read": true, "is_response_requested": false, "references": null, "reply_to": null, "received_by": null, "received_representing": null, "email_date": 1601867342}
```



#### Move Mail To Folder
Move one or multiple emails from source email folder to another folder in mailbox. NOTICE - to search and move emails in all mailboxes, please configure impersonation permissions. https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange. Note: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Source Folder Name|Source folder to move emails from|True|String||
|Destination Folder Name|Destination folder to move emails to|True|String||
|Message IDs|Filter condition, specify emails with which email ids to find. Should accept comma separated multiple message ids. If message id is provided, subject filter is ignored|False|String||
|Subject Filter|Filter condition, specify what subject to search for emails|False|String||
|Only Unread|Filter condition, specify if search should look only for unread emails|False|Boolean|false|
|Move in all mailboxes|If checked, search and move emails in all mailboxes accessible with current impersonalization settings|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Move in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|25|
|Time Frame (minutes)|Filter condition, specify in what time frame in minutes should action look for emails|False|String||
|Limit the Amount of Information Returned in the JSON Result|If enabled, the amount of information returned by the action will be limited only to the key email fields.|False|Boolean|true|
|Disable the Action JSON Result|If enabled, action will not return JSON result.|False|Boolean|false|



##### JSON Results
```json
[{"mime_content": "Received: from EX001.siemplifylab.local (0.0.0.0) by\r\n EX001.siemplifylab.local (0.0.0.0) with Microsoft SMTP Server\r\n (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id 0.0.0.0\r\n via Mailbox Transport; Thu, 8 Oct 2020 08:39:35 -0700\r\nReceived: from EX001.siemplifylab.local (0.0.0.0) by\r\n EX001.siemplifylab.local (0.0.0.0) with Microsoft SMTP Server\r\n (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id\r\n 0.0.0.0; Thu, 8 Oct 2020 08:39:34 -0700\r\nReceived: from EX001.siemplifylab.local ([0000::0000:0000:0000:0000]) by\r\n EX001.siemplifylab.local ([0000::0000:0000:0000:0000%5]) with mapi id\r\n 00.00.0000.000; Thu, 8 Oct 2020 08:39:34 -0700\r\nFrom: some_other_mail_3 <some_other_mail_3@siemplifylab.local>\r\nTo: some_other_mail_3 <some_other_mail_3@siemplifylab.local>\r\nSubject: Re: *h1test\r\nThread-Topic: *h1test\r\nThread-Index: AQHWnYjyAIejNr20W0S3qVKQbznvY6mN11k+\r\nDate: Thu, 8 Oct 2020 15:39:34 +0000\r\nMessage-ID: <some_mail@siemplifylab.local>\r\nReferences: <some_other_mail@siemplifylab.local>\r\nIn-Reply-To: <some_other_mail@siemplifylab.local>\r\nAccept-Language: en-US\r\nContent-Language: en-US\r\nX-MS-Exchange-Organization-AuthAs: Internal\r\nX-MS-Exchange-Organization-AuthMechanism: 04\r\nX-MS-Exchange-Organization-AuthSource: EX001.siemplifylab.local\r\nX-MS-Has-Attach:\r\nX-MS-Exchange-Organization-Network-Message-Id:\r\n\tad1fcc4b-55e0-4cc1-a39f-08d86ba05ba1\r\nX-MS-Exchange-Organization-SCL: -1\r\nX-MS-TNEF-Correlator:\r\nX-MS-Exchange-Organization-RecordReviewCfmType: 0\r\nContent-Type: multipart/alternative;\r\n\tboundary=\"_000_some_mailsiemplifylablocal_\"\r\nMIME-Version: 1.0\r\n\r\n--_000_some_mailsiemplifylablocal_\r\nContent-Type: text/plain; charset=\"iso-8859-1\"\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\n*h1 reply\r\n\r\n________________________________\r\nFrom: some_other_mail_3\r\nSent: Thursday, October 8, 2020 5:37:36 PM\r\nTo: some_other_mail_3; Test User1\r\nSubject: *h1test\r\n\r\n\r\n*h1test\r\n\r\n--_000_some_mailsiemplifylablocal_\r\nContent-Type: text/html; charset=\"iso-8859-1\"\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\n<html>\r\n<head>\r\n<meta http-equiv=3D\"Content-Type\" content=3D\"text/html; charset=3Diso-8859-=\r\n1\">\r\n<style type=3D\"text/css\" style=3D\"display:none;\"><!-- P {margin-top:0;margi=\r\nn-bottom:0;} --></style>\r\n</head>\r\n<body dir=3D\"ltr\">\r\n<style type=3D\"text/css\" style=3D\"display:none;\"><!-- P {margin-top:0;margi=\r\nn-bottom:0;} --></style>\r\n<div id=3D\"divtagdefaultwrapper\" style=3D\"font-size:12pt;color:#000000;font=\r\n-family:Calibri,Helvetica,sans-serif;\" dir=3D\"ltr\">\r\n<p>*h1 reply</p>\r\n</div>\r\n<hr style=3D\"display:inline-block;width:98%\" tabindex=3D\"-1\">\r\n<div id=3D\"divRplyFwdMsg\" dir=3D\"ltr\"><font face=3D\"Calibri, sans-serif\" st=\r\nyle=3D\"font-size:11pt\" color=3D\"#000000\"><b>From:</b> some_other_mail_3<br>\r\n<b>Sent:</b> Thursday, October 8, 2020 5:37:36 PM<br>\r\n<b>To:</b> some_other_mail_3; Test User1<br>\r\n<b>Subject:</b> *h1test</font>\r\n<div>&nbsp;</div>\r\n</div>\r\n<div>\r\n<div id=3D\"divtagdefaultwrapper\" style=3D\"font-size:12pt;color:#000000;font=\r\n-family:Calibri,Helvetica,sans-serif;\" dir=3D\"ltr\">\r\n<p><span>*h1test</span><br>\r\n</p>\r\n</div>\r\n</div>\r\n</body>\r\n</html>\r\n\r\n--_000_some_mailsiemplifylablocal_--\r\n", "_id": "ItemId(id='AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX/0/LnCkytWTOh2sCWzQAAAgEMAAAAMnX/0/LnCkytWTOh2sCWzQAAARCmyQAAAA==', changekey='CQAAABYAAAAydf/T8ucKTK1ZM6HawJbNAAAAEhnK')", "parent_folder_id": "ParentFolderId(id='AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAuAAADneAeRbLkN0i93LTVa54xxwEAMnX/0/LnCkytWTOh2sCWzQAAAgEMAAAA', changekey='AQAAAA==')", "item_class": "IPM.Note", "subject": "Re: *h1test", "sensitivity": "Normal", "text_body": "*h1 reply\r\n\r\n________________________________\r\nFrom: some_other_mail_3\r\nSent: Thursday, October 8, 2020 5:37:36 PM\r\nTo: some_other_mail_3; Test User1\r\nSubject: *h1test\r\n\r\n\r\n*h1test\r\n", "body": "*h1 reply\r\n\r\n________________________________\r\nFrom: some_other_mail_3\r\nSent: Thursday, October 8, 2020 5:37:36 PM\r\nTo: some_other_mail_3; Test User1\r\nSubject: *h1test\r\n\r\n\r\n*h1test", "attachments": [], "datetime_received": "2020-10-08 15:39:35+00:00", "size": "9163", "categories": "None", "importance": "Normal", "in_reply_to": "<some_other_mail@siemplifylab.local>", "is_submitted": "False", "is_draft": "False", "is_from_me": "True", "is_resend": "False", "is_unmodified": "True", "headers": ["MessageHeader(name='Received', value='from EX001.siemplifylab.local (0.0.0.0) by EX001.siemplifylab.local (0.0.0.0) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id 0.0.0.0 via Mailbox Transport; Thu, 8 Oct 2020 08:39:35 -0700')", "MessageHeader(name='Received', value='from EX001.siemplifylab.local (0.0.0.0) by EX001.siemplifylab.local (0.0.0.0) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id 0.0.0.0; Thu, 8 Oct 2020 08:39:34 -0700')", "MessageHeader(name='Received', value='from EX001.siemplifylab.local ([0000::0000:0000:0000:0000]) by EX001.siemplifylab.local ([0000::0000:0000:0000:0000%5]) with mapi id 00.00.0000.000; Thu, 8 Oct 2020 08:39:34 -0700')", "MessageHeader(name='Content-Type', value='application/ms-tnef')", "MessageHeader(name='Content-Transfer-Encoding', value='binary')", "MessageHeader(name='Subject', value='Re: *h1test')", "MessageHeader(name='Thread-Topic', value='*h1test')", "MessageHeader(name='Thread-Index', value='AQHWnYjyAIejNr20W0S3qVKQbznvY6mN11k+')", "MessageHeader(name='Date', value='Thu, 8 Oct 2020 08:39:34 -0700')", "MessageHeader(name='Message-ID', value='<some_mail@siemplifylab.local>')", "MessageHeader(name='References', value='<some_other_mail@siemplifylab.local>')", "MessageHeader(name='In-Reply-To', value='<some_other_mail@siemplifylab.local>')", "MessageHeader(name='Accept-Language', value='en-US')", "MessageHeader(name='Content-Language', value='en-US')", "MessageHeader(name='X-MS-Exchange-Organization-SCL', value='-1')", "MessageHeader(name='X-MS-TNEF-Correlator', value='<some_mail@siemplifylab.local>')", "MessageHeader(name='MIME-Version', value='1.0')", "MessageHeader(name='X-MS-Exchange-Organization-MessageDirectionality', value='Originating')", "MessageHeader(name='X-MS-Exchange-Organization-AuthSource', value='EX001.siemplifylab.local')", "MessageHeader(name='X-MS-Exchange-Organization-AuthAs', value='Internal')", "MessageHeader(name='X-MS-Exchange-Organization-AuthMechanism', value='04')", "MessageHeader(name='X-Originating-IP', value='[0.0.0.0]')", "MessageHeader(name='X-MS-Exchange-Organization-Network-Message-Id', value='ad1fcc4b-55e0-4cc1-a39f-08d86ba05ba1')", "MessageHeader(name='Return-Path', value='some_other_mail_3@siemplifylab.local')", "MessageHeader(name='X-MS-Exchange-Organization-AVStamp-Enterprise', value='1.0')", "MessageHeader(name='X-MS-Exchange-Transport-EndToEndLatency', value='00:00:00.2609087')", "MessageHeader(name='X-MS-Exchange-Processed-By-BccFoldering', value='15.01.1847.001')"], "datetime_sent": "2020-10-08 15:39:34+00:00", "datetime_created": "2020-10-08 15:39:35+00:00", "reminder_due_by": "None", "reminder_is_set": "False", "reminder_minutes_before_start": "0", "display_cc": "None", "display_to": "some_other_mail_3", "has_attachments": "False", "culture": "en-US", "effective_rights": "EffectiveRights(create_associated=False, create_contents=False, create_hierarchy=False, delete=True, modify=True, read=True, view_private_items=True)", "last_modified_name": "some_other_mail_3", "last_modified_time": "2020-10-08 15:39:35+00:00", "is_associated": "False", "web_client_read_form_query_string": "?ItemID=AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX%2F0%2FLnCkytWTOh2sCWzQAAAgEMAAAAMnX%2F0%2FLnCkytWTOh2sCWzQAAARCmyQAAAA%3D%3D&exvsurl=1&viewmodel=ReadMessageItem", "web_client_edit_form_query_string": "None", "conversation_id": "ConversationId(id='AAQkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAQAACHoza9tFtEt6lSkG8572M=')", "unique_body": "<html><body><div>\r\n<div dir=\"ltr\">\r\n<div id=\"divtagdefaultwrapper\"><font face=\"Calibri,Helvetica,sans-serif\" size=\"3\" color=\"black\"><span style=\"font-size:12pt;\" id=\"divtagdefaultwrapper\">\r\n<div style=\"margin-top:0;margin-bottom:0;\">*h1 reply</div>\r\n</span></font></div>\r\n</div>\r\n</div>\r\n</body></html>", "sender": "Mailbox(name='some_other_mail_3', email_address='some_other_mail_3@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')", "to_recipients": ["Mailbox(name='some_other_mail_3', email_address='some_other_mail_3@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')"], "cc_recipients": "None", "bcc_recipients": "None", "is_read_receipt_requested": "False", "is_delivery_receipt_requested": "False", "conversation_topic": "*h1test", "author": "some_other_mail_3@siemplifylab.local", "message_id": "<some_mail@siemplifylab.local>", "is_read": "False", "is_response_requested": "False", "references": "<some_other_mail@siemplifylab.local>", "reply_to": "None", "received_by": "Mailbox(name='some_other_mail_3', email_address='some_other_mail_3@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')", "received_representing": "Mailbox(name='some_other_mail_3', email_address='some_other_mail_3@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')", "plaintext_body": "*h1 reply\r\n\r\n________________________________\r\nFrom: some_other_mail_3\r\nSent: Thursday, October 8, 2020 5:37:36 PM\r\nTo: some_other_mail_3; Test User1\r\nSubject: *h1test\r\n\r\n\r\n*h1test", "html_body": "<html>\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n<style type=\"text/css\" style=\"display:none;\"><!-- P {margin-top:0;margin-bottom:0;} --></style>\r\n</head>\r\n<body dir=\"ltr\">\r\n<style type=\"text/css\" style=\"display:none;\"><!-- P {margin-top:0;margin-bottom:0;} --></style>\r\n<div id=\"divtagdefaultwrapper\" style=\"font-size:12pt;color:#000000;font-family:Calibri,Helvetica,sans-serif;\" dir=\"ltr\">\r\n<p>*h1 reply</p>\r\n</div>\r\n<hr style=\"display:inline-block;width:98%\" tabindex=\"-1\">\r\n<div id=\"divRplyFwdMsg\" dir=\"ltr\"><font face=\"Calibri, sans-serif\" style=\"font-size:11pt\" color=\"#000000\"><b>From:</b> some_other_mail_3<br>\r\n<b>Sent:</b> Thursday, October 8, 2020 5:37:36 PM<br>\r\n<b>To:</b> some_other_mail_3; Test User1<br>\r\n<b>Subject:</b> *h1test</font>\r\n<div>&nbsp;</div>\r\n</div>\r\n<div>\r\n<div id=\"divtagdefaultwrapper\" style=\"font-size:12pt;color:#000000;font-family:Calibri,Helvetica,sans-serif;\" dir=\"ltr\">\r\n<p><span>*h1test</span><br>\r\n</p>\r\n</div>\r\n</div>\r\n</body>\r\n</html>\r\n", "attachments_list": {}}]
```



#### Remove Domains from Exchange-Siemplify Inbox Rules
Action will get as a parameter a list of Domains, and will be able to remove the provided domains from the existing rules. WARNING: Action will modify your current users inbox rules, using EWS. NOTICE - to perform operation, please configure EDiscovery Group and Author permissions. For full details, please visit: https://integrations.siemplify.co/doc/exchang. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Domains|Specify the Domains you would like to remove from the rule, in a comma separated list.|False|String||
|Rule to remove Domains from|Specify the rule to remove the Domains from. If the rule doesn’t exist - action will do nothing.|True|List|Siemplify - Domains List - Move To Junk|
|Remove Domains from all available Rules|Specify whether action should look for the provided domains in all of Siemplify inbox rules.|False|Boolean|false|
|Perform action in all mailboxes|If checked, action will be performed in all mailboxes accessible with current impersonalization settings.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|50|



#### Get Mail EML File
Fetch message EML file.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Folder to fetch from. Default is Inbox|False|String|Inbox|
|Message ID||True|String||
|Base64 Encode||False|Boolean|true|



#### Get Account Out Of Facility Settings
Get account out of facility (OOF) settings for the provided Siemplify User entity. Note 1: If the target User entity is a username, not a mail address, please run Enrich Entities from Active Directory integration first to try to use the information about User's mail stored in Active Directory. Note 2: For integration to return the information, it should have delegation or impersonation permissions to the target account mailbox. Link to impersonation permission configuration: https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange
Timeout - 600 Seconds



##### JSON Results
```json
[{"Entity": "john_doe@example.com", "EntityResult": {"state": "Disabled", "external_audience": "All", "start": "2020-10-15 13:00:00+00:00", "end": "2020-10-16 13:00:00+00:00", "internal_reply": null, "external_reply": null}}, {"Entity": "lilydoe@example.com", "EntityResult": {"state": "Disabled", "external_audience": "All", "start": "2020-10-15 13:00:00+00:00", "end": "2020-10-16 13:00:00+00:00", "internal_reply": null, "external_reply": null}}]
```



#### Add Domains to Exchange-Siemplify Inbox Rules
Action will get as a parameter a list of Domains, and will be able to create or update a rule, filtering the domains from your mailboxes. Actions can be modified in the parameters using rule parameter. WARNING: Action will modify your current users inbox rules, using EWS. NOTICE - to perform operation, please configure EDiscovery Group and Author permissions. For full details, please visit: https://integrations.siemplify.co/doc/exchang. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Domains|Specify the Domains you would like to add to the rule, in a comma separated list.|False|String||
|Rule to add Domains to|Specify the rule to add the Domains to. If the rule doesn't exist - action will create it where it's missing.|True|List|Siemplify - Domains List - Move To Junk|
|Perform action in all mailboxes|If checked, action will be performed in all mailboxes accessible with current impersonalization settings|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|50|



#### Generate Token
For integration configuration with Oauth authentication, get a refresh token using the authorization URL received in the Get Authorization action.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Authorization URL|Use the authorization URL received in the Get Authorization URL action to request a refresh token.|True|String||



#### Wait for Vote Mail Results
Use this action to fetch the responses of a vote mail sent by the "Send Vote Mail" action, in order to wait for the responses and get them inside Siemplify.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Vote Mail message_id|Message_id of the vote email, which current action would be waiting for. If message has been sent using Send Vote Mail action, please select SendVoteMail.JSONResult.message_id field as a placeholder.|True|String||
|Mail Recipients|Comma-separated list of recipient emails, response from which current action would be waiting for. Please select SendVoteMail.JSONResult.to_recipients field as a placeholder.|True|String||
|Folder to Check for Reply|Parameter can be used to specify mailbox email folder (mailbox that was used to send the email with question) to search for the user reply in this folder. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive.|True|String|Inbox|
|Folder to check for Sent Mail|Parameter can be used to specify mailbox email folder (mailbox that was used to send the email with question) to search for the sent mail in this folder. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive.|True|String|Sent Items|
|How long to wait for recipient reply (minutes)|How long in minutes to wait for the user's reply before marking it timed out.|True|String|1440|
|Wait for All Recipients to Reply?|Parameter can be used to define if there are multiple recipients - should the Action wait for responses from all of recipients until timeout, or Action should wait for first reply to proceed.|False|Boolean|true|



##### JSON Results
```json
{"Responses":[{"recipient":"test1@example.com","vote":"Approve"},{"recipient":"test2@example.com","vote":"Reject"}]}
```



#### Send Thread Reply
Send a message as a reply to the email thread.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Message ID|Specify the ID of the message to which you want to send a reply.|True|String||
|Folder Name|Specify a comma-separated list of mailbox folders in which action should search for email.|True|String|Inbox|
|Content|Specify the content of the reply.|True|Email Content||
|Attachments Paths|Specify a comma separated list of attachments file paths stored on the server for addition to the email.|False|String||
|Reply All|If enabled, action will send a reply to all recipients related to the original email. Note: this parameter has priority over “Reply To“ parameter.|False|Boolean|true|
|Reply To|Specify a comma-separated list of emails to which you want to send this reply. If nothing is provided and “Reply All“ is disabled, action will only send a reply to the sender of the email. If “Reply All“ is enabled, action will ignore this parameter.|False|String||



##### JSON Results
```json
{"mime_content": "'From: Administrator <Administrator@siemplifylab.local>\\r\\nTo: Administrator <Administrator@siemplifylab.local>\\r\\nSubject: Test subject\\r\\nThread-Topic: Test subject\\r\\nThread-Index: AQHWmsTgBEcHjewfyEKH4YkB+Lo0RQ==\\r\\nDate: Mon, 5 Oct 2020 06:09:02 +0300\\r\\nMessage-ID: <160186734388.8568.315529398955149940@siemplify>\\r\\nAccept-Language: en-US\\r\\nContent-Language: en-US\\r\\nX-MS-Has-Attach:\\r\\nX-MS-Exchange-Organization-SCL: -1\\r\\nX-MS-TNEF-Correlator:\\r\\nX-MS-Exchange-Organization-RecordReviewCfmType: 0\\r\\nContent-Type: multipart/alternative;\\r\\n\\tboundary=\"_000_1601867343888568315529398955149940siemplify_\"\\r\\nMIME-Version: 1.0\\r\\n\\r\\n--_000_1601867343888568315529398955149940siemplify_\\r\\nContent-Type: text/plain; charset=\"us-ascii\"\\r\\n\\r\\nTest mail content\\r\\n\\r\\n--_000_1601867343888568315529398955149940siemplify_\\r\\nContent-Type: text/html; charset=\"us-ascii\"\\r\\n\\r\\n<html>\\r\\n<head>\\r\\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=us-ascii\">\\r\\n</head>\\r\\n<body>\\r\\n<p>Test mail content </p>\\r\\n</body>\\r\\n</html>\\r\\n\\r\\n--_000_1601867343888568315529398955149940siemplify_--\\r\\n'", "_id": "ItemId(id='AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX/0/LnCkytWTOh2sCWzQAAAgEJAAAAMnX/0/LnCkytWTOh2sCWzQAAARDFFwAAAA==', changekey='CQAAABYAAAAydf/T8ucKTK1ZM6HawJbNAAAAEZla')", "parent_folder_id": "ParentFolderId(id='AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAuAAADneAeRbLkN0i93LTVa54xxwEAMnX/0/LnCkytWTOh2sCWzQAAAgEJAAAA', changekey='AQAAAA==')", "item_class": "IPM.Note", "subject": "Test subject", "sensitivity": "Normal", "text_body": "Test mail content\r\n", "body": "<html>\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n</head>\r\n<body>\r\n<p>Test mail content </p>\r\n</body>\r\n</html>\r\n", "attachments": [], "datetime_received": "2020-10-05 03:09:02+00:00", "size": 2568, "categories": null, "importance": "Normal", "in_reply_to": null, "is_submitted": true, "is_draft": true, "is_from_me": false, "is_resend": false, "is_unmodified": false, "headers": null, "datetime_sent": "2020-10-05 03:09:02+00:00", "datetime_created": "2020-10-05 03:09:02+00:00", "reminder_due_by": null, "reminder_is_set": false, "reminder_minutes_before_start": 0, "display_cc": null, "display_to": "Administrator", "has_attachments": false, "culture": "en-US", "effective_rights": "EffectiveRights(create_associated=False, create_contents=False, create_hierarchy=False, delete=True, modify=True, read=True, view_private_items=True)", "last_modified_name": "Administrator", "last_modified_time": "2020-10-05 03:09:02+00:00", "is_associated": false, "web_client_read_form_query_string": "?ItemID=AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX%2F0%2FLnCkytWTOh2sCWzQAAAgEJAAAAMnX%2F0%2FLnCkytWTOh2sCWzQAAARDFFwAAAA%3D%3D&exvsurl=1&viewmodel=ReadMessageItem", "web_client_edit_form_query_string": null, "conversation_id": "ConversationId(id='AAQkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAQAARHB43sH8hCh+GJAfi6NEU=')", "unique_body": "<html><body><div>\r\n<div>\r\n<div style=\"margin-top:14pt;margin-bottom:14pt;\">Test mail content </div>\r\n</div>\r\n</div>\r\n</body></html>", "sender": "Mailbox(name='Administrator', email_address='Administrator@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')", "to_recipients": ["Mailbox(name='Administrator', email_address='Administrator@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')"], "cc_recipients": null, "bcc_recipients": null, "is_read_receipt_requested": false, "is_delivery_receipt_requested": false, "conversation_index": "\\x01\\x01\\xd6\\x9a\\xc4\\xe0\\x04G\\x07\\x8d\\xec\\x1f\\xc8B\\x87\\xe1\\x89\\x01\\xf8\\xba4E'", "conversation_topic": "Test subject", "author": "Mailbox(name='Administrator', email_address='Administrator@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')", "message_id": "<160186734388.8568.315529398955149940@siemplify>", "is_read": true, "is_response_requested": false, "references": null, "reply_to": null, "received_by": null, "received_representing": null, "email_date": 1601867342}
```



#### Delete Mail
Delete one or multiple email from the mailbox that matches search criterias. Delete can be done for the first email that matched the search criteria, or it can be done for all matching emails. NOTICE - to delete emails in all mailboxes, please configure impersonation permissions. https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange. Note: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Mailbox folder to search email in. Parameter should also accept comma separated list of folders to check the user response in multiple folders|False|String|Inbox|
|Message IDs|Filter condition, specify emails with which email ids to find. Should accept comma separated list of message ids to search for. If message id is provided, subject, sender and recipient filters are ignored.|False|String||
|Mailboxes|Specify a comma-separated list of mailboxes that need to be searched. This parameter has priority over “Delete in all mailboxes“.|False|String||
|Subject Filter|Filter condition, specify subject to search for emails|False|String||
|Sender Filter|Filter condition, specify who should be the sender of needed emails|False|String||
|Recipient Filter|Filter condition, specify who should be the recipient of needed emails|False|String||
|Delete All Matching Emails|Filter condition, specify if action should delete all matched by criteria emails from the mailbox or delete only first match.|False|Boolean|false|
|Delete from all mailboxes|If checked, delete emails in all mailboxes accessible with current impersonalization settings|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Delete from all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|25|
|Time Frame (minutes)|Filter condition, specify in what time frame in minutes should action look for emails|False|String||



##### JSON Results
```json
[{"mime_content": "Received: from EX001.example.local (xxx.30.xxx.29) by\r\n EX001.example.local (xxx.30.xxx.29) with Microsoft SMTP Server\r\n (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id xx.1.18xx.3\r\n via Mailbox Transport; Mon, 19 Oct 2020 02:42:23 -0700\r\nReceived: from EX001.example.local (xxx.30.xxx.29) by\r\n EX001.example.local (xxx.30.xxx.29) with Microsoft SMTP Server\r\n (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id\r\n xx.1.18xx.3; Mon, 19 Oct 2020 02:42:23 -0700\r\nReceived: from EX001.example.local ([fe80::xxxx:e3c3:xxxx:fc6f]) by\r\n EX001.example.local ([fe80::xxxx:e3c3:xxxx:fc6f%4]) with mapi id\r\n xx.01.18xx.003; Mon, 19 Oct 2020 02:42:23 -0700\r\nFrom: test <test@example.local>\r\nTo: test <test@example.local>\r\nSubject: #h4\r\nThread-Topic: #h4\r\nThread-Index: AQHWpfwlwSZWtJSb+EOtDk2WJ3xXaA==\r\nDate: Mon, 19 Oct 2020 09:42:23 +0000\r\nMessage-ID: <ec0fb6a4fa1a4bxxxxxxxxxxxxxxx269@example.local>\r\nAccept-Language: en-US\r\nContent-Language: en-US\r\nX-MS-Exchange-Organization-AuthAs: Internal\r\nX-MS-Exchange-Organization-AuthMechanism: 04\r\nX-MS-Exchange-Organization-AuthSource: EX001.example.local\r\nX-MS-Has-Attach:\r\nX-MS-Exchange-Organization-Network-Message-Id:\r\n\t20xxxxxxx-0fdf-40f6-d038-xxxxxx1347fb\r\nX-MS-Exchange-Organization-SCL: -1\r\nX-MS-TNEF-Correlator:\r\nX-MS-Exchange-Organization-RecordReviewCfmType: 0\r\nContent-Type: multipart/alternative;\r\n\tboundary=\"_000_ec0fb6a4fa1a4bxxxxxxxxxxxxxxx269siemplifylablocal_\"\r\nMIME-Version: 1.0\r\n\r\n--_000_ec0fb6a4fa1a4bxxxxxxxxxxxxxxx269siemplifylablocal_\r\nContent-Type: text/plain; charset=\"iso-8859-1\"\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\n#h4\r\n\r\n--_000_ec0fb6a4fa1a4bxxxxxxxxxxxxxxx269siemplifylablocal_\r\nContent-Type: text/html; charset=\"iso-8859-1\"\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\n<html>\r\n<head>\r\n<meta http-equiv=3D\"Content-Type\" content=3D\"text/html; charset=3Diso-8859-=\r\n1\">\r\n<style type=3D\"text/css\" style=3D\"display:none;\"><!-- P {margin-top:0;margi=\r\nn-bottom:0;} --></style>\r\n</head>\r\n<body dir=3D\"ltr\">\r\n<div id=3D\"divtagdefaultwrapper\" style=3D\"font-size:12pt;color:#000000;font=\r\n-family:Calibri,Helvetica,sans-serif;\" dir=3D\"ltr\">\r\n<p><span>#h4</span><br>\r\n</p>\r\n</div>\r\n</body>\r\n</html>\r\n\r\n--_000_ec0fb6a4fa1a4bxxxxxxxxxxxxxxx269siemplifylablocal_--\r\n", "_id": "ItemId(id='AAMkxxxxxxxxxxY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAAAAACd4B5FsuQ3SL3ctNVrxxxxxxxxxx/T8ucKTK1ZxxxxxxxxxxAAAEMAAAydf/T8ucKTK1ZM6HawJxxxxxxxxxxAAA=', changekey='CQAAABYAAAAydf/T8ucKTK1ZMxxxxxxxxxxxxxxx')", "parent_folder_id": "ParentFolderId(id='AQMkxxxxxxxxxxY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAuAAADneAeRbLkN0i93LTVaxxxxxxxxxx/0/LnCkytWTOh2sCWzQxxxxxxxxxx', changekey='AQAAAA==')", "item_class": "IPM.Note", "subject": "#h4", "sensitivity": "Normal", "text_body": "#h4\r\n", "body": "#h4", "attachments": [], "datetime_received": "2020-10-19 09:42:23+00:00", "size": "7310", "categories": "None", "importance": "Normal", "in_reply_to": "None", "is_submitted": "False", "is_draft": "False", "is_from_me": "True", "is_resend": "False", "is_unmodified": "True", "headers": ["MessageHeader(name='Received', value='from EX001.example.local (xxx.30.xxx.29) by EX001.example.local (xxx.30.xxx.29) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id xx.1.18xx.3 via Mailbox Transport; Mon, 19 Oct 2020 02:42:23 -0700')", "MessageHeader(name='Received', value='from EX001.example.local (xxx.30.xxx.29) by EX001.example.local (xxx.30.xxx.29) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id xx.1.18xx.3; Mon, 19 Oct 2020 02:42:23 -0700')", "MessageHeader(name='Received', value='from EX001.example.local ([fe80::xxxx:e3c3:xxxx:fc6f]) by EX001.example.local ([fe80::xxxx:e3c3:xxxx:fc6f%4]) with mapi id xx.01.18xx.003; Mon, 19 Oct 2020 02:42:23 -0700')", "MessageHeader(name='Content-Type', value='application/ms-tnef')", "MessageHeader(name='Content-Transfer-Encoding', value='binary')", "MessageHeader(name='Subject', value='#h4')", "MessageHeader(name='Thread-Topic', value='#h4')", "MessageHeader(name='Thread-Index', value='AQHWpfwlwSZWtJSb+EOtxxxxxxxxxx==')", "MessageHeader(name='Date', value='Mon, 19 Oct 2020 02:42:23 -0700')", "MessageHeader(name='Message-ID', value='<ec0fb6a4fa1a4bxxxxxxxxxxxxxxx269@example.local>')", "MessageHeader(name='Accept-Language', value='en-US')", "MessageHeader(name='Content-Language', value='en-US')", "MessageHeader(name='X-MS-Exchange-Organization-SCL', value='-1')", "MessageHeader(name='X-MS-TNEF-Correlator', value='<ec0fb6a4fa1a4bxxxxxxxxxxxxxxx269@example.local>')", "MessageHeader(name='MIME-Version', value='1.0')", "MessageHeader(name='X-MS-Exchange-Organization-MessageDirectionality', value='Originating')", "MessageHeader(name='X-MS-Exchange-Organization-AuthSource', value='EX001.example.local')", "MessageHeader(name='X-MS-Exchange-Organization-AuthAs', value='Internal')", "MessageHeader(name='X-MS-Exchange-Organization-AuthMechanism', value='04')", "MessageHeader(name='X-Originating-IP', value='[xx.0.150.xx]')", "MessageHeader(name='X-MS-Exchange-Organization-Network-Message-Id', value='208xxxxx-0fdf-40f6-xxxx-08d8741xxxxx')", "MessageHeader(name='Return-Path', value='test@example.local')", "MessageHeader(name='X-MS-Exchange-Organization-AVStamp-Enterprise', value='1.0')", "MessageHeader(name='X-MS-Exchange-Transport-EndToEndLatency', value='00:00:00.3261488')", "MessageHeader(name='X-MS-Exchange-Processed-By-BccFoldering', value='xx.01.18xx.001')"], "datetime_sent": "2020-10-19 09:42:23+00:00", "datetime_created": "2020-10-19 09:42:23+00:00", "reminder_due_by": "None", "reminder_is_set": "False", "reminder_minutes_before_start": "0", "display_cc": "None", "display_to": "test", "has_attachments": "False", "culture": "en-US", "effective_rights": "EffectiveRights(create_associated=False, create_contents=False, create_hierarchy=False, delete=True, modify=True, read=True, view_private_items=True)", "last_modified_name": "test", "last_modified_time": "2020-10-19 09:42:23+00:00", "is_associated": "False", "web_client_read_form_query_string": "?ItemID=AAMkxxxxxxxxxxY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAAAAACd4B5FsuQ3SL3ctNVrxxxxxxxxxx%2FT8ucKTK1ZxxxxxxxxxxAAAEMAAAydf%2FT8ucKTK1ZM6HawJxxxxxxxxxxAAA%3D&exvsurl=1&viewmodel=ReadMessageItem", "web_client_edit_form_query_string": "None", "conversation_id": "ConversationId(id='AAQkxxxxxxxxxxY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAxxxxxxxxxx/hDrQ5Nlid8V2g=')", "unique_body": "<html><body><div>\r\n<div dir=\"ltr\">\r\n<div id=\"divtagdefaultwrapper\"><font face=\"Calibri,Helvetica,sans-serif\" size=\"3\" color=\"black\"><span style=\"font-size:12pt;\" id=\"divtagdefaultwrapper\">\r\n<div style=\"margin-top:0;margin-bottom:0;\">#h4<br>\r\n\r\n</div>\r\n</span></font></div>\r\n</div>\r\n</div>\r\n</body></html>", "sender": "Mailbox(name='test', email_address='test@example.local', routing_type='SMTP', mailbox_type='Mailbox')", "to_recipients": ["Mailbox(name='test', email_address='test@example.local', routing_type='SMTP', mailbox_type='Mailbox')"], "cc_recipients": "None", "bcc_recipients": "None", "is_read_receipt_requested": "False", "is_delivery_receipt_requested": "False", "conversation_topic": "#h4", "author": "test@example.local", "message_id": "<ec0fb6a4fa1a4bxxxxxxxxxxxxxxx269@example.local>", "is_read": "True", "is_response_requested": "False", "references": "None", "reply_to": "None", "received_by": "Mailbox(name='test', email_address='test@example.local', routing_type='SMTP', mailbox_type='Mailbox')", "received_representing": "Mailbox(name='test', email_address='test@example.local', routing_type='SMTP', mailbox_type='Mailbox')", "plaintext_body": "#h4", "html_body": "<html>\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n<style type=\"text/css\" style=\"display:none;\"><!-- P {margin-top:0;margin-bottom:0;} --></style>\r\n</head>\r\n<body dir=\"ltr\">\r\n<div id=\"divtagdefaultwrapper\" style=\"font-size:12pt;color:#000000;font-family:Calibri,Helvetica,sans-serif;\" dir=\"ltr\">\r\n<p><span>#h4</span><br>\r\n</p>\r\n</div>\r\n</body>\r\n</html>\r\n", "attachments_list": {}}]
```



#### Download Attachments
Download email attachments from email to specific file path on Siemplify server. NOTICE - to search for an email in all mailboxes, please configure impersonation permissions. https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange. Note: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed. Additionally, please note that if the downloaded attachments have "/" or "\" characters in the names, those will be replaced with the '_' character.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Mailbox folder to search email in. Parameter should also accept comma separated list of folders to check the user response in multiple folders|True|String|Inbox|
|Download Path|File path on the server where to download the email attachments|True|String||
|Message IDs|Filter condition, specify emails with which email ids to find. Should accept comma separated multiple message ids. If message id is provided, subject filter is ignored|False|String||
|Subject Filter|Filter condition to search emails by specific subject|False|String||
|Sender Filter|Filter condition to search emails by specific sender|False|String||
|Only Unread|If checked, download attachments only from unread emails|False|Boolean|false|
|Download Attachments from EML|If checked, download attachments also from attached EML files|False|Boolean|false|
|Download Attachments to unique path?|If checked, download attachments to unique path  under file path provided in “Download Path” parameter to avoid previously downloaded attachments overwrite.|False|Boolean|false|
|Search in all mailboxes|If checked, search in all mailboxes accessible with current impersonalization settings|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Search in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|25|
|Mailboxes|Specify a comma-separated list of mailboxes that need to be searched. This parameter has priority over "Search in all mailboxes".|False|String||



##### JSON Results
```json
[{"attachment_name":"name1.png","downloaded_path":"file_path/name1.png"},{"attachment_name":"name2.png","downloaded_path":"file_path/name2.png"}]
```



#### Add Senders to Exchange-Siemplify Inbox Rule
Action will get as a parameter a list of Email Addresses, or will work on User entities with Email regexes (if parameters are not provided), and will be able to create a new rule, filtering the senders from your mailboxes. Actions can be modified in the parameters using the rule parameter. WARNING: Action will modify your current users inbox rules, using EWS. NOTICE - to perform operation, please configure EDiscovery Group and Author permissions. For full details, please visit: https://integrations.siemplify.co/doc/exchang. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Senders|Specify the Senders you would like to add to the rule, in a comma separated list. If no parameter will be provided, action will work with User entities.|False|String||
|Rule to add senders to|Specify the rule to add the sender to. If the rule doesn't exist - action will create it where it's missing.|True|List|Siemplify - Senders List - Move To Junk|
|Should add senders' domain to the corresponding Domains List rule as well?|Specify whether the action should automatically take the domains of the provided email addresses and add them as well to the corresponding domain rules (same rule action for domains)|False|Boolean|false|
|Perform action in all mailboxes|If checked, action will be performed in all mailboxes accessible with current impersonalization settings|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|50|



#### Send Vote Mail
Send emails with easy answering options, to allow stakeholders to be combined in the automated processes without accessing the Siemplify UI.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Subject|The mail subject part|True|String||
|Send To|Arbitrary comma separated list of email addresses for the email recipients. For example: user1@company.co, user2@company.co|True|String||
|CC|Arbitrary comma separated list of email addresses to be put in the CC field of email. Format is the same as for the "Send to" field|False|String||
|BCC|Arbitrary comma separated list of email addresses to be put in the BCC field of email. Format is the same as for the "Send to" field|False|String||
|Attachments Paths|Comma separated list of attachments file paths stored on the server for addition to the email. For example: C:\<Siemplify work dir>\file1.pdf, C:\<Siemplify work dir>\image2.jpg|False|String||
|Question or Decision Description|The question you would like to ask, or describe the decision you would like the recipient to be able to respond to|True|Email Content||
|Structure of voting options|Choose the structure of the vote to be sent to the recipients|True|List|Yes/No|



##### JSON Results
```json
{"mime_content": "'From: Administrator <Administrator@siemplifylab.local>\\r\\nTo: Administrator <Administrator@siemplifylab.local>\\r\\nSubject: Test subject\\r\\nThread-Topic: Test subject\\r\\nThread-Index: AQHWmsTgBEcHjewfyEKH4YkB+Lo0RQ==\\r\\nDate: Mon, 5 Oct 2020 06:09:02 +0300\\r\\nMessage-ID: <160186734388.8568.315529398955149940@siemplify>\\r\\nAccept-Language: en-US\\r\\nContent-Language: en-US\\r\\nX-MS-Has-Attach:\\r\\nX-MS-Exchange-Organization-SCL: -1\\r\\nX-MS-TNEF-Correlator:\\r\\nX-MS-Exchange-Organization-RecordReviewCfmType: 0\\r\\nContent-Type: multipart/alternative;\\r\\n\\tboundary=\"_000_1601867343888568315529398955149940siemplify_\"\\r\\nMIME-Version: 1.0\\r\\n\\r\\n--_000_1601867343888568315529398955149940siemplify_\\r\\nContent-Type: text/plain; charset=\"us-ascii\"\\r\\n\\r\\nTest mail content\\r\\n\\r\\n--_000_1601867343888568315529398955149940siemplify_\\r\\nContent-Type: text/html; charset=\"us-ascii\"\\r\\n\\r\\n<html>\\r\\n<head>\\r\\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=us-ascii\">\\r\\n</head>\\r\\n<body>\\r\\n<p>Test mail content </p>\\r\\n</body>\\r\\n</html>\\r\\n\\r\\n--_000_1601867343888568315529398955149940siemplify_--\\r\\n'", "_id": "ItemId(id='AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX/0/LnCkytWTOh2sCWzQAAAgEJAAAAMnX/0/LnCkytWTOh2sCWzQAAARDFFwAAAA==', changekey='CQAAABYAAAAydf/T8ucKTK1ZM6HawJbNAAAAEZla')", "parent_folder_id": "ParentFolderId(id='AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAuAAADneAeRbLkN0i93LTVa54xxwEAMnX/0/LnCkytWTOh2sCWzQAAAgEJAAAA', changekey='AQAAAA==')", "item_class": "IPM.Note", "subject": "Test subject", "sensitivity": "Normal", "text_body": "Test mail content\r\n", "body": "<html>\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n</head>\r\n<body>\r\n<p>Test mail content </p>\r\n</body>\r\n</html>\r\n", "attachments": [], "datetime_received": "2020-10-05 03:09:02+00:00", "size": 2568, "categories": null, "importance": "Normal", "in_reply_to": null, "is_submitted": true, "is_draft": true, "is_from_me": false, "is_resend": false, "is_unmodified": false, "headers": null, "datetime_sent": "2020-10-05 03:09:02+00:00", "datetime_created": "2020-10-05 03:09:02+00:00", "reminder_due_by": null, "reminder_is_set": false, "reminder_minutes_before_start": 0, "display_cc": null, "display_to": "Administrator", "has_attachments": false, "culture": "en-US", "effective_rights": "EffectiveRights(create_associated=False, create_contents=False, create_hierarchy=False, delete=True, modify=True, read=True, view_private_items=True)", "last_modified_name": "Administrator", "last_modified_time": "2020-10-05 03:09:02+00:00", "is_associated": false, "web_client_read_form_query_string": "?ItemID=AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX%2F0%2FLnCkytWTOh2sCWzQAAAgEJAAAAMnX%2F0%2FLnCkytWTOh2sCWzQAAARDFFwAAAA%3D%3D&exvsurl=1&viewmodel=ReadMessageItem", "web_client_edit_form_query_string": null, "conversation_id": "ConversationId(id='AAQkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAQAARHB43sH8hCh+GJAfi6NEU=')", "unique_body": "<html><body><div>\r\n<div>\r\n<div style=\"margin-top:14pt;margin-bottom:14pt;\">Test mail content </div>\r\n</div>\r\n</div>\r\n</body></html>", "sender": "Mailbox(name='Administrator', email_address='Administrator@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')", "to_recipients": ["Mailbox(name='Administrator', email_address='Administrator@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')"], "cc_recipients": null, "bcc_recipients": null, "is_read_receipt_requested": false, "is_delivery_receipt_requested": false, "conversation_index": "\\x01\\x01\\xd6\\x9a\\xc4\\xe0\\x04G\\x07\\x8d\\xec\\x1f\\xc8B\\x87\\xe1\\x89\\x01\\xf8\\xba4E'", "conversation_topic": "Test subject", "author": "Mailbox(name='Administrator', email_address='Administrator@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')", "message_id": "<160186734388.8568.315529398955149940@siemplify>", "is_read": true, "is_response_requested": false, "references": null, "reply_to": null, "received_by": null, "received_representing": null, "email_date": 1601867342}
```



#### List Exchange-Siemplify Inbox Rules
Action will get as a parameter a rule name, from the Exchange-Siemplify Inbox rules, and will list it. If no mailboxes to list for will be provided, the rules for the logged in user will be listed. NOTICE - to perform operation, please configure EDiscovery Group and Author permissions. For full details, please visit: https://integrations.siemplify.co/doc/exchang. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule Name To List|Specify the Rule name you would like to list from the relevant mailboxes|True|List||
|Mailboxes list to perform on|Filter condition, If you have a specific list of mailboxes you would like to conduct the operation on, for better timing, please provide them here. Should accept a comma separated list of mail addresses to list the rules from. If a mailboxes list is provided, "Perform Action in all Mailboxes" parameter will be ignored.|False|String||
|Perform action in all mailboxes|If checked, action will be performed in all mailboxes accessible with current impersonalization settings|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|50|



##### JSON Results
```json
[{"id":"xxxxxMTj5uI=","name":"Siemplify - Domains List - Move To Junk","priority":1,"is_enabled":true,"conditions":{"domains":["GMAIL.COM","SIEMPLIFY.CO"],"addresses":[]},"actions":["Move To Folder"]},{"id":"xxxxxMTj5uY=","name":"Siemplify - Senders List - Delete","priority":3,"is_enabled":true,"conditions":{"domains":[],"addresses":["example@gmail.com"]},"actions":["Delete"]}]
```



#### Send Mail HTML
Send an email with HTML template content, Send to field is comma separated. Note: Sender's display name can be configured in the client under the account settings
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Subject|The subject of the email|True|String||
|Send to|Recipient email address. Multiple addresses can be separated by commas|True|String||
|CC|CC email address. Multiple addresses can be separated by commas|False|String||
|BCC|BCC email address. Multiple addresses can be separated by commas|False|String||
|Attachments Paths|Full path to attachments to be uploaded. Comma sepreated. e.g. C:\Desktop\x.txt,C:\Desktop\sample.txt|False|String||
|Mail content|Mail body|True|Email Content||



#### Wait for mail from user
Wait for user's response based on an email sent via Send Email action. Note: please adjust the async timeout for action (polling timeout) and global action timeout in Siemplify server configuration as needed. Action input parameter "How long to wait for recipient reply (minutes)" cant be bigger than Siemplify server global timeout value.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Mail message_id|Message_id of the email, which current action would be waiting for. If message has been sent using Send Email action, please select SendEmail.JSONResult.message_id field as a placeholder.|True|String||
|Mail Date|Send timestamp of the email, which current action would be waiting for. If message has been sent using Send Email action, please select SendEmail.JSONResult.email_date field as a placeholder.|True|String||
|Mail Recipients|Comma-separated list of recipient emails, response from which current action would be waiting for. If message has been sent using Send Email action, please select Select SendEmail.JSONResult.recipients field as a placeholder.|True|String||
|How long to wait for recipient reply (minutes)|How long in minutes to wait for the user's reply before marking it timed out.|True|String|1440|
|Wait for All Recipients to Reply?|Parameter can be used to define if there are multiple recipients - should the Action wait for responses from all of recipients until timeout, or Action should wait for first reply to proceed.|False|Boolean|true|
|Wait Stage Exclude pattern|Regular expression to exclude specific replies from the wait stage. Works with body part of email. Example is, to exclude automatic Out-Of-Office emails to be considered as recipient reply, and instead wait for actual user reply.|False|String||
|Folder to Check for Reply|Parameter can be used to specify mailbox email folder (mailbox that was used to send the email with question) to search for the user reply in this folder. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive.|False|String|Inbox|
|Fetch Response Attachments|If selected, if recipient replies with attachment - fetch recipient response and add it as attachment for the action result|False|Boolean|false|



##### JSON Results
```json
{"Responses": [{"recipient": "some_other_mail_3@siemplifylab.local", "content": {"mime_content": "Received: from EX001.siemplifylab.local (0.0.0.0) by\r\n EX001.siemplifylab.local (0.0.0.0) with Microsoft SMTP Server\r\n (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id 0.0.0.0\r\n via Mailbox Transport; Thu, 8 Oct 2020 08:39:35 -0700\r\nReceived: from EX001.siemplifylab.local (0.0.0.0) by\r\n EX001.siemplifylab.local (0.0.0.0) with Microsoft SMTP Server\r\n (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id\r\n 0.0.0.0; Thu, 8 Oct 2020 08:39:34 -0700\r\nReceived: from EX001.siemplifylab.local ([0000::0000:0000:0000:0000]) by\r\n EX001.siemplifylab.local ([0000::0000:0000:0000:0000%5]) with mapi id\r\n 00.00.0000.000; Thu, 8 Oct 2020 08:39:34 -0700\r\nFrom: some_other_mail_3 <some_other_mail_3@siemplifylab.local>\r\nTo: some_other_mail_3 <some_other_mail_3@siemplifylab.local>\r\nSubject: Re: *h1test\r\nThread-Topic: *h1test\r\nThread-Index: AQHWnYjyAIejNr20W0S3qVKQbznvY6mN11k+\r\nDate: Thu, 8 Oct 2020 15:39:34 +0000\r\nMessage-ID: <some_mail@siemplifylab.local>\r\nReferences: <some_other_mail@siemplifylab.local>\r\nIn-Reply-To: <some_other_mail@siemplifylab.local>\r\nAccept-Language: en-US\r\nContent-Language: en-US\r\nX-MS-Exchange-Organization-AuthAs: Internal\r\nX-MS-Exchange-Organization-AuthMechanism: 04\r\nX-MS-Exchange-Organization-AuthSource: EX001.siemplifylab.local\r\nX-MS-Has-Attach:\r\nX-MS-Exchange-Organization-Network-Message-Id:\r\n\tad1fcc4b-55e0-4cc1-a39f-08d86ba05ba1\r\nX-MS-Exchange-Organization-SCL: -1\r\nX-MS-TNEF-Correlator:\r\nX-MS-Exchange-Organization-RecordReviewCfmType: 0\r\nContent-Type: multipart/alternative;\r\n\tboundary=\"_000_some_mailsiemplifylablocal_\"\r\nMIME-Version: 1.0\r\n\r\n--_000_some_mailsiemplifylablocal_\r\nContent-Type: text/plain; charset=\"iso-8859-1\"\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\n*h1 reply\r\n\r\n________________________________\r\nFrom: some_other_mail_3\r\nSent: Thursday, October 8, 2020 5:37:36 PM\r\nTo: some_other_mail_3; Test User1\r\nSubject: *h1test\r\n\r\n\r\n*h1test\r\n\r\n--_000_some_mailsiemplifylablocal_\r\nContent-Type: text/html; charset=\"iso-8859-1\"\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\n<html>\r\n<head>\r\n<meta http-equiv=3D\"Content-Type\" content=3D\"text/html; charset=3Diso-8859-=\r\n1\">\r\n<style type=3D\"text/css\" style=3D\"display:none;\"><!-- P {margin-top:0;margi=\r\nn-bottom:0;} --></style>\r\n</head>\r\n<body dir=3D\"ltr\">\r\n<style type=3D\"text/css\" style=3D\"display:none;\"><!-- P {margin-top:0;margi=\r\nn-bottom:0;} --></style>\r\n<div id=3D\"divtagdefaultwrapper\" style=3D\"font-size:12pt;color:#000000;font=\r\n-family:Calibri,Helvetica,sans-serif;\" dir=3D\"ltr\">\r\n<p>*h1 reply</p>\r\n</div>\r\n<hr style=3D\"display:inline-block;width:98%\" tabindex=3D\"-1\">\r\n<div id=3D\"divRplyFwdMsg\" dir=3D\"ltr\"><font face=3D\"Calibri, sans-serif\" st=\r\nyle=3D\"font-size:11pt\" color=3D\"#000000\"><b>From:</b> some_other_mail_3<br>\r\n<b>Sent:</b> Thursday, October 8, 2020 5:37:36 PM<br>\r\n<b>To:</b> some_other_mail_3; Test User1<br>\r\n<b>Subject:</b> *h1test</font>\r\n<div>&nbsp;</div>\r\n</div>\r\n<div>\r\n<div id=3D\"divtagdefaultwrapper\" style=3D\"font-size:12pt;color:#000000;font=\r\n-family:Calibri,Helvetica,sans-serif;\" dir=3D\"ltr\">\r\n<p><span>*h1test</span><br>\r\n</p>\r\n</div>\r\n</div>\r\n</body>\r\n</html>\r\n\r\n--_000_some_mailsiemplifylablocal_--\r\n", "_id": "ItemId(id='AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX/0/LnCkytWTOh2sCWzQAAAgEMAAAAMnX/0/LnCkytWTOh2sCWzQAAARCmyQAAAA==', changekey='CQAAABYAAAAydf/T8ucKTK1ZM6HawJbNAAAAEhnK')", "parent_folder_id": "ParentFolderId(id='AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAuAAADneAeRbLkN0i93LTVa54xxwEAMnX/0/LnCkytWTOh2sCWzQAAAgEMAAAA', changekey='AQAAAA==')", "item_class": "IPM.Note", "subject": "Re: *h1test", "sensitivity": "Normal", "text_body": "*h1 reply\r\n\r\n________________________________\r\nFrom: some_other_mail_3\r\nSent: Thursday, October 8, 2020 5:37:36 PM\r\nTo: some_other_mail_3; Test User1\r\nSubject: *h1test\r\n\r\n\r\n*h1test\r\n", "body": "*h1 reply\r\n\r\n________________________________\r\nFrom: some_other_mail_3\r\nSent: Thursday, October 8, 2020 5:37:36 PM\r\nTo: some_other_mail_3; Test User1\r\nSubject: *h1test\r\n\r\n\r\n*h1test", "attachments": [], "datetime_received": "2020-10-08 15:39:35+00:00", "size": "9163", "categories": "None", "importance": "Normal", "in_reply_to": "<some_other_mail@siemplifylab.local>", "is_submitted": "False", "is_draft": "False", "is_from_me": "True", "is_resend": "False", "is_unmodified": "True", "headers": ["MessageHeader(name='Received', value='from EX001.siemplifylab.local (0.0.0.0) by EX001.siemplifylab.local (0.0.0.0) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id 0.0.0.0 via Mailbox Transport; Thu, 8 Oct 2020 08:39:35 -0700')", "MessageHeader(name='Received', value='from EX001.siemplifylab.local (0.0.0.0) by EX001.siemplifylab.local (0.0.0.0) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id 0.0.0.0; Thu, 8 Oct 2020 08:39:34 -0700')", "MessageHeader(name='Received', value='from EX001.siemplifylab.local ([0000::0000:0000:0000:0000]) by EX001.siemplifylab.local ([0000::0000:0000:0000:0000%5]) with mapi id 00.00.0000.000; Thu, 8 Oct 2020 08:39:34 -0700')", "MessageHeader(name='Content-Type', value='application/ms-tnef')", "MessageHeader(name='Content-Transfer-Encoding', value='binary')", "MessageHeader(name='Subject', value='Re: *h1test')", "MessageHeader(name='Thread-Topic', value='*h1test')", "MessageHeader(name='Thread-Index', value='AQHWnYjyAIejNr20W0S3qVKQbznvY6mN11k+')", "MessageHeader(name='Date', value='Thu, 8 Oct 2020 08:39:34 -0700')", "MessageHeader(name='Message-ID', value='<some_mail@siemplifylab.local>')", "MessageHeader(name='References', value='<some_other_mail@siemplifylab.local>')", "MessageHeader(name='In-Reply-To', value='<some_other_mail@siemplifylab.local>')", "MessageHeader(name='Accept-Language', value='en-US')", "MessageHeader(name='Content-Language', value='en-US')", "MessageHeader(name='X-MS-Exchange-Organization-SCL', value='-1')", "MessageHeader(name='X-MS-TNEF-Correlator', value='<some_mail@siemplifylab.local>')", "MessageHeader(name='MIME-Version', value='1.0')", "MessageHeader(name='X-MS-Exchange-Organization-MessageDirectionality', value='Originating')", "MessageHeader(name='X-MS-Exchange-Organization-AuthSource', value='EX001.siemplifylab.local')", "MessageHeader(name='X-MS-Exchange-Organization-AuthAs', value='Internal')", "MessageHeader(name='X-MS-Exchange-Organization-AuthMechanism', value='04')", "MessageHeader(name='X-Originating-IP', value='[0.0.0.0]')", "MessageHeader(name='X-MS-Exchange-Organization-Network-Message-Id', value='ad1fcc4b-55e0-4cc1-a39f-08d86ba05ba1')", "MessageHeader(name='Return-Path', value='some_other_mail_3@siemplifylab.local')", "MessageHeader(name='X-MS-Exchange-Organization-AVStamp-Enterprise', value='1.0')", "MessageHeader(name='X-MS-Exchange-Transport-EndToEndLatency', value='00:00:00.2609087')", "MessageHeader(name='X-MS-Exchange-Processed-By-BccFoldering', value='15.01.1847.001')"], "datetime_sent": "2020-10-08 15:39:34+00:00", "datetime_created": "2020-10-08 15:39:35+00:00", "reminder_due_by": "None", "reminder_is_set": "False", "reminder_minutes_before_start": "0", "display_cc": "None", "display_to": "some_other_mail_3", "has_attachments": "False", "culture": "en-US", "effective_rights": "EffectiveRights(create_associated=False, create_contents=False, create_hierarchy=False, delete=True, modify=True, read=True, view_private_items=True)", "last_modified_name": "some_other_mail_3", "last_modified_time": "2020-10-08 15:39:35+00:00", "is_associated": "False", "web_client_read_form_query_string": "?ItemID=AQMkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX%2F0%2FLnCkytWTOh2sCWzQAAAgEMAAAAMnX%2F0%2FLnCkytWTOh2sCWzQAAARCmyQAAAA%3D%3D&exvsurl=1&viewmodel=ReadMessageItem", "web_client_edit_form_query_string": "None", "conversation_id": "ConversationId(id='AAQkADIzZjA2MWY0LTcwMTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAQAACHoza9tFtEt6lSkG8572M=')", "unique_body": "<html><body><div>\r\n<div dir=\"ltr\">\r\n<div id=\"divtagdefaultwrapper\"><font face=\"Calibri,Helvetica,sans-serif\" size=\"3\" color=\"black\"><span style=\"font-size:12pt;\" id=\"divtagdefaultwrapper\">\r\n<div style=\"margin-top:0;margin-bottom:0;\">*h1 reply</div>\r\n</span></font></div>\r\n</div>\r\n</div>\r\n</body></html>", "sender": "Mailbox(name='some_other_mail_3', email_address='some_other_mail_3@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')", "to_recipients": ["Mailbox(name='some_other_mail_3', email_address='some_other_mail_3@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')"], "cc_recipients": "None", "bcc_recipients": "None", "is_read_receipt_requested": "False", "is_delivery_receipt_requested": "False", "conversation_topic": "*h1test", "author": "some_other_mail_3@siemplifylab.local", "message_id": "<some_mail@siemplifylab.local>", "is_read": "False", "is_response_requested": "False", "references": "<some_other_mail@siemplifylab.local>", "reply_to": "None", "received_by": "Mailbox(name='some_other_mail_3', email_address='some_other_mail_3@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')", "received_representing": "Mailbox(name='some_other_mail_3', email_address='some_other_mail_3@siemplifylab.local', routing_type='SMTP', mailbox_type='Mailbox')", "plaintext_body": "*h1 reply\r\n\r\n________________________________\r\nFrom: some_other_mail_3\r\nSent: Thursday, October 8, 2020 5:37:36 PM\r\nTo: some_other_mail_3; Test User1\r\nSubject: *h1test\r\n\r\n\r\n*h1test", "html_body": "<html>\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n<style type=\"text/css\" style=\"display:none;\"><!-- P {margin-top:0;margin-bottom:0;} --></style>\r\n</head>\r\n<body dir=\"ltr\">\r\n<style type=\"text/css\" style=\"display:none;\"><!-- P {margin-top:0;margin-bottom:0;} --></style>\r\n<div id=\"divtagdefaultwrapper\" style=\"font-size:12pt;color:#000000;font-family:Calibri,Helvetica,sans-serif;\" dir=\"ltr\">\r\n<p>*h1 reply</p>\r\n</div>\r\n<hr style=\"display:inline-block;width:98%\" tabindex=\"-1\">\r\n<div id=\"divRplyFwdMsg\" dir=\"ltr\"><font face=\"Calibri, sans-serif\" style=\"font-size:11pt\" color=\"#000000\"><b>From:</b> some_other_mail_3<br>\r\n<b>Sent:</b> Thursday, October 8, 2020 5:37:36 PM<br>\r\n<b>To:</b> some_other_mail_3; Test User1<br>\r\n<b>Subject:</b> *h1test</font>\r\n<div>&nbsp;</div>\r\n</div>\r\n<div>\r\n<div id=\"divtagdefaultwrapper\" style=\"font-size:12pt;color:#000000;font-family:Calibri,Helvetica,sans-serif;\" dir=\"ltr\">\r\n<p><span>*h1test</span><br>\r\n</p>\r\n</div>\r\n</div>\r\n</body>\r\n</html>\r\n", "attachments_list": {}}}, {"recipient": "some_other_mail_4@siemplifylab.local", "content": null}]}
```



#### Save Mail Attachments To The Case
Save email attachments from email stored in monitored mailbox to the Case Wall.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Mailbox folder to search email in. Parameter should also accept comma separated list of folders to check the user response in multiple folders|True|String|Inbox|
|Message ID|Message id to find an email to download attachments from.|True|String||
|Attachment To Save|If parameter is not specified - save all email attachments to the case wall. If parameter specified - save only matching attachment to the case wall.|False|String||



##### JSON Results
```json
{"mime_content":"Received: from EX001.example.local (xxx.30.202.xx) by\r\n EX001.example.local (xxx.30.202.xx) with Microsoft SMTP Server\r\n (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id xx.1.18xx.3\r\n via Mailbox Transport; Wed, 14 Oct 2020 07:19:20 -0700\r\nReceived: from EX001.example.local (xxx.30.202.xx) by\r\n EX001.example.local (xxx.30.202.xx) with Microsoft SMTP Server\r\n (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id\r\n xx.1.18xx.3; Wed, 14 Oct 2020 07:19:19 -0700\r\nReceived: from EX001.example.local ([fe80::xxxx:e3c3:10d7:xxxx]) by\r\n EX001.example.local ([fe80::xxxx:e3c3:xxxx:fc6f%5]) with mapi id\r\n xx.01.18xx.003; Wed, 14 Oct 2020 07:19:19 -0700\r\nFrom: Administrator <example@example.local>\r\nTo: Administrator <example@example.local>\r\nSubject: ~h22\r\nThread-Topic: ~h22\r\nThread-Index: AQHWojT/3eUm+4NfG0m+vpdrS2A55w==\r\nDate: Wed, 14 Oct 2020 14:19:19 +0000\r\nMessage-ID: <5c48cxxxxxxxxxxxxxxx5e44883a8026@example.local>\r\nAccept-Language: en-US\r\nContent-Language: en-US\r\nX-MS-Exchange-Organization-AuthAs: Internal\r\nX-MS-Exchange-Organization-AuthMechanism: 04\r\nX-MS-Exchange-Organization-AuthSource: EX001.example.local\r\nX-MS-Has-Attach: yes\r\nX-MS-Exchange-Organization-Network-Message-Id:\r\n\tfb2eaeb4-xxxx-447c-0d97-xxxx704c2418\r\nX-MS-Exchange-Organization-SCL: -1\r\nX-MS-TNEF-Correlator:\r\nX-MS-Exchange-Organization-RecordReviewCfmType: 0\r\nContent-Type: multipart/mixed;\r\n\tboundary=\"_004_5c48c79f346a4c0db4475e44883a8026siemplifylablocal_\"\r\nMIME-Version: 1.0\r\n\r\n--_004_5c48c79f346a4c0db4475e44883a8026siemplifylablocal_\r\nContent-Type: multipart/alternative;\r\n\tboundary=\"_000_5c48c79f346a4c0db4475e44883a8026siemplifylablocal_\"\r\n\r\n--_000_5c48c79f346a4c0db4475e44883a8026siemplifylablocal_\r\nContent-Type: text/plain; charset=\"iso-8859-1\"\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\n~h22\r\n\r\n--_000_5c48c79f346a4c0db4475e44883a8026siemplifylablocal_\r\nContent-Type: text/html; charset=\"iso-8859-1\"\r\nContent-Transfer-Encoding: quoted-printable\r\n\r\n<html>\r\n<head>\r\n<meta http-equiv=3D\"Content-Type\" content=3D\"text/html; charset=3Diso-8859-=\r\n1\">\r\n<style type=3D\"text/css\" style=3D\"display:none;\"><!-- P {margin-top:0;margi=\r\nn-bottom:0;} --></style>\r\n</head>\r\n<body dir=3D\"ltr\">\r\n<div id=3D\"divtagdefaultwrapper\" style=3D\"font-size:12pt;color:#000000;font=\r\n-family:Calibri,Helvetica,sans-serif;\" dir=3D\"ltr\">\r\n<p><span>~h22</span><br>\r\n</p>\r\n</div>\r\n</body>\r\n</html>\r\n\r\n--_000_5c48c79f346a4c0db4475e44883a8026siemplifylablocal_--\r\n\r\n--_004_5c48c79f346a4c0db4475e44883a8026siemplifylablocal_\r\nContent-Type: image/jpeg; name=\"photo.jpg\"\r\nContent-Description: photo.jpg\r\nContent-Disposition: attachment; filename=\"photo.jpg\"; size=26756;\r\n\tcreation-date=\"Wed, 14 Oct 2020 14:19:18 GMT\";\r\n\tmodification-date=\"Wed, 14 Oct 2020 14:19:18 GMT\"\r\nContent-Transfer-Encoding: base64\r\n\r\niVBORw0KGgoAAAANSUhExxxxxxxxxx","_id":"ItemId(id='AQMkADxxxxxxxxxxxxxxxTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX/0/LnCkytWTOh2sCWzQAAAgEMAAAAMnX/0/LnCkytWTOh2sCWzQAAARCnugAAAA==', changekey='CQAAABYAAAAydf/T8ucKTK1ZM6HawJbNAAAAEn14')","parent_folder_id":"ParentFolderId(id='AQMkADxxxxxxxxxxxxxxxTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAuAAADneAeRbLkN0i93LTVa54xxwEAMnX/0/LnCkytWTOh2sCWzQAAAgEMAAAA', changekey='AQAAAA==')","item_class":"IPM.Note","subject":"~h22","sensitivity":"Normal","text_body":"~h22\r\n","body":"~h22","attachments":["FileAttachment(attachment_id=AttachmentId(id='AQMkADxxxxxxxxxxxxxxxTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX/0/LnCkytWTOh2sCWzQAAAgEMAAAAMnX/0/LnCkytWTOh2sCWzQAAARCnugAAAAESABAAqRTobv7YLEOIk6p3FVuMQw==', root_id=None, root_changekey=None), name='photo.jpg', content_type='image/jpeg', size=26756, last_modified_time=EWSDateTime(2020, 10, 14, 14, 19, 18, tzinfo=<UTC>), is_inline=False, is_contact_photo=False)"],"datetime_received":"2020-10-14 14:19:20+00:00","size":"34144","categories":"None","importance":"Normal","in_reply_to":"None","is_submitted":"False","is_draft":"False","is_from_me":"True","is_resend":"False","is_unmodified":"True","headers":["MessageHeader(name='Received', value='from EX001.example.local (xxx.30.202.xx) by EX001.example.local (xxx.30.202.xx) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id xx.1.18xx.3 via Mailbox Transport; Wed, 14 Oct 2020 07:19:20 -0700')","MessageHeader(name='Received', value='from EX001.example.local (xxx.30.202.xx) by EX001.example.local (xxx.30.202.xx) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) id xx.1.18xx.3; Wed, 14 Oct 2020 07:19:19 -0700')","MessageHeader(name='Received', value='from EX001.example.local ([fe80::xxxx:e3c3:10d7:xxxx]) by EX001.example.local ([fe80::xxxx:e3c3:xxxx:fc6f%5]) with mapi id xx.01.1847.xxx; Wed, 14 Oct 2020 07:19:19 -0700')","MessageHeader(name='Content-Type', value='application/ms-tnef')","MessageHeader(name='Content-Transfer-Encoding', value='binary')","MessageHeader(name='Subject', value='~h22')","MessageHeader(name='Thread-Topic', value='~h22')","MessageHeader(name='Thread-Index', value='AQHWojT/3eUm+4NfG0m+vpdrS2A55w==')","MessageHeader(name='Date', value='Wed, 14 Oct 2020 07:19:19 -0700')","MessageHeader(name='Message-ID', value='<5c48cxxxxxxxxxxxxxxx5e44883a8026@example.local>')","MessageHeader(name='Accept-Language', value='en-US')","MessageHeader(name='Content-Language', value='en-US')","MessageHeader(name='X-MS-Has-Attach', value='yes')","MessageHeader(name='X-MS-Exchange-Organization-SCL', value='-1')","MessageHeader(name='X-MS-TNEF-Correlator', value='<5c48cxxxxxxxxxxxxxxx5e44883a8026@example.local>')","MessageHeader(name='MIME-Version', value='1.0')","MessageHeader(name='X-MS-Exchange-Organization-MessageDirectionality', value='Originating')","MessageHeader(name='X-MS-Exchange-Organization-AuthSource', value='EX001.example.local')","MessageHeader(name='X-MS-Exchange-Organization-AuthAs', value='Internal')","MessageHeader(name='X-MS-Exchange-Organization-AuthMechanism', value='04')","MessageHeader(name='X-Originating-IP', value='[xx.0.xxx.45]')","MessageHeader(name='X-MS-Exchange-Organization-Network-Message-Id', value='fb2eaeb4-xxxx-447c-0d97-08d8704cxxxx')","MessageHeader(name='Return-Path', value='example@example.local')","MessageHeader(name='X-MS-Exchange-Organization-AVStamp-Enterprise', value='1.0')","MessageHeader(name='X-MS-Exchange-Transport-EndToEndLatency', value='00:00:00.3029870')","MessageHeader(name='X-MS-Exchange-Processed-By-BccFoldering', value='xx.01.18xx.001')"],"datetime_sent":"2020-10-14 14:19:19+00:00","datetime_created":"2020-10-14 14:19:20+00:00","reminder_due_by":"None","reminder_is_set":"False","reminder_minutes_before_start":"0","display_cc":"None","display_to":"Administrator","has_attachments":"True","culture":"en-US","effective_rights":"EffectiveRights(create_associated=False, create_contents=False, create_hierarchy=False, delete=True, modify=True, read=True, view_private_items=True)","last_modified_name":"Administrator","last_modified_time":"2020-10-14 14:19:20+00:00","is_associated":"False","web_client_read_form_query_string":"?ItemID=AQMkADxxxxxxxxxxxxxxxTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgBGAAADneAeRbLkN0i93LTVa54xxwcAMnX%2F0%2FLnCkytWTOh2sCWzQAAAgEMAAAAMnX%2F0%2FLnCkytWTOh2sCWzQAAARCnugAAAA%3D%3D&exvsurl=1&viewmodel=ReadMessageItem","web_client_edit_form_query_string":"None","conversation_id":"ConversationId(id='AAQkADIzZxxxxxxxxxxxxTMtNDcxMy1iZWY4LTdlMzk2OTVkNDFmMgAQAN3lJvuDXxtJvr6Xa0tgOec=')","unique_body":"<html><body><div>\r\n<div dir=\"ltr\">\r\n<div id=\"divtagdefaultwrapper\"><font face=\"Calibri,Helvetica,sans-serif\" size=\"3\" color=\"black\"><span style=\"font-size:12pt;\" id=\"divtagdefaultwrapper\">\r\n<div style=\"margin-top:0;margin-bottom:0;\">~h22<br>\r\n\r\n</div>\r\n</span></font></div>\r\n</div>\r\n</div>\r\n</body></html>","sender":"Mailbox(name='Administrator', email_address='example@example.local', routing_type='SMTP', mailbox_type='Mailbox')","to_recipients":["Mailbox(name='Administrator', email_address='example@example.local', routing_type='SMTP', mailbox_type='Mailbox')"],"cc_recipients":"None","bcc_recipients":"None","is_read_receipt_requested":"False","is_delivery_receipt_requested":"False","conversation_topic":"~h22","author":"example@example.local","message_id":"<5c48cxxxxxxxxxxxxxxx5e44883a8026@example.local>","is_read":"True","is_response_requested":"False","references":"None","reply_to":"None","received_by":"Mailbox(name='Administrator', email_address='example@example.local', routing_type='SMTP', mailbox_type='Mailbox')","received_representing":"Mailbox(name='Administrator', email_address='example@example.local', routing_type='SMTP', mailbox_type='Mailbox')","plaintext_body":"~h22","html_body":"<html>\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n<style type=\"text/css\" style=\"display:none;\"><!-- P {margin-top:0;margin-bottom:0;} --></style>\r\n</head>\r\n<body dir=\"ltr\">\r\n<div id=\"divtagdefaultwrapper\" style=\"font-size:12pt;color:#000000;font-family:Calibri,Helvetica,sans-serif;\" dir=\"ltr\">\r\n<p><span>~h22</span><br>\r\n</p>\r\n</div>\r\n</body>\r\n</html>\r\n","attachments_list":{"photo.jpg":"iVBORw0KGgoAAAANSUhEUgxxxxxxxxxx"}}
```



#### Unblock Sender by Message ID
Action will get as a parameter a list of message IDs, and will be able to unmark it as junk. Unmarking an item as junk using this action will remove the item sender's mail address from the "Blocked Senders List". To move it back to the inbox, please tick the appropriate checkbox in the action parameters. NOTICE - to unmark emails in all mailboxes, please configure impersonation permissions: https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed. NOTE: Action is supported only from Exchange Server version 2013 and newer, if a lower version is used, action will fail with the appropriate message.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Move items back to Inbox?|Should the action move the specified messages back to the inbox folder|False|Boolean|true|
|Message IDs|Filter condition, specify emails with which email ids to find. Should accept comma separated list of message ids to unmark as junk. If message id is provided, subject, sender and recipient filters are ignored.|False|String||
|Mailboxes list to perform on|Filter condition, If you have a specific list of mailboxes you would like to conduct the operation on, for better timing, please provide them here. Should accept a comma separated list of mail addresses to unmark the messages as junk in. If a mailboxes list is provided, "Perform Action in all Mailboxes" parameter will be ignored.|False|String||
|Folder Name|Mailbox folder to search email in. Parameter should also accept comma separated list of folders to move the item from|False|String|Junk Email|
|Subject Filter|Filter condition, specify subject to search for emails|False|String||
|Sender Filter|Filter condition, specify who should be the sender of needed emails|False|String||
|Recipient Filter|Filter condition, specify who should be the recipient of needed emails|False|String||
|Unmark All Matching Emails|Filter condition, specify if action should Unmark all matched by criteria emails from the mailbox or Unmark only first match.|False|Boolean|false|
|Perform action in all mailboxes|If checked, move to junk and block sender emails in all mailboxes accessible with current impersonalization settings|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action  in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|25|
|Time Frame (minutes)|Filter condition, specify in what time frame in minutes should action look for emails.|False|String||



##### JSON Results
```json
[{"mime_content":"content example","_id":"ItemId(id='xxxxxxxxxxJjNjJkLTc3MzAtNGM5My04ZjM0LTZiYzVjMDI4ZTZlNQBGAAAAAADLc0XF/C8kRJTduC5WOJE/BwDby9ZjVdTJTJRS8jxrcA+oAAAAAAEMAADby9ZjVdTJTJRS8jxrcA+oAxxxxxxxxxx=', changekey='xxxxxxxxxxDby9ZjVdTJTJRS8jxrcA+oAAEy4kvx')","parent_folder_id":"ParentFolderId(id='xxxxxxxxxxJjNjJkLTc3ADMwLTRjOTMtOGYzNC02YmM1YzAyOGU2ZTUALgAAA8tzRcX8LyRElN24LlY4kT8BANvL1mNV1MlMlFLyPGtwD6gAxxxxxxxxxx==', changekey='xxxAAA==')","item_class":"IPM.Note","subject":"test","sensitivity":"Normal","text_body":"test\r\n","body":"test","attachments":[],"datetime_received":"2021-01-19 14:31:39+00:00","size":"47965","categories":"None","importance":"Normal","in_reply_to":"None","is_submitted":"False","is_draft":"False","is_from_me":"False","is_resend":"False","is_unmodified":"True","headers":["MessageHeader(name='Received', value='from xxxxx05MB7074.eurprd05.prod.outlook.com (xxxx:10a6:20b:1a6::xx) by xxxxx05MB5957.eurprd05.prod.outlook.com with HTTPS; Tue, 19 Jan 2021 14:31:38 +0000')","MessageHeader(name='Received', value='from xxxxx81CA0021.DEUP281.PROD.OUTLOOK.COM (xxxx:10a6:b10:14::x) by xxxxx05MB7074.eurprd05.prod.outlook.com (xxxx:10a6:20b:1a6::xx) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id xx.20.3763.x; Tue, 19 Jan 2021 14:31:37 +0000')"],"datetime_sent":"2021-01-19 14:31:24+00:00","datetime_created":"2021-01-19 14:31:39+00:00","reminder_due_by":"None","reminder_is_set":"False","reminder_minutes_before_start":"0","display_cc":"None","display_to":"ג'יימס בונד","has_attachments":"False","culture":"en-US","effective_rights":"EffectiveRights(create_associated=False, create_contents=False, create_hierarchy=False, delete=True, modify=True, read=True, view_private_items=True)","last_modified_name":"Test User","last_modified_time":"2021-01-19 14:33:08+00:00","is_associated":"False","web_client_read_form_query_string":"https://outlook.office365.com/owa/?ItemID=xxxxxxxxxxJjNjJkLTc3MzAtNGM5My04ZjM0LTZiYzVjMDI4ZTZlNQBGAAAAAADLc0XF%2FC8kRJTduC5WOJE%2FBwDby9ZjVdTJTJRS8jxrcA%2BoAAAAAAEMAADby9ZjVdTJTJRS8jxrcA%2BoAAEzKVFJAAA%3D&exvsurl=1&viewmodel=ReadMessageItem","web_client_edit_form_query_string":"None","conversation_id":"ConversationId(id='xxxxxxxxxxJjNjJkLTc3MzAtNGM5My04ZjM0LTZiYzVjMDI4ZTZlNQAQAHyj1LciNtFHpS4ZbBghSeM=')","unique_body":"<html><body><div>\r\n<div>\r\n<div dir=\"ltr\">test</div>\r\n</div>\r\n</div>\r\n</body></html>","sender":"Mailbox(name='Test User', email_address='test.user@siemplify.co', routing_type='SMTP', mailbox_type='OneOff')","to_recipients":["Mailbox(name=\"ג'יימס בונד\", email_address='test@test.onmicrosoft.com', routing_type='SMTP', mailbox_type='Mailbox')"],"cc_recipients":"None","bcc_recipients":"None","is_read_receipt_requested":"False","is_delivery_receipt_requested":"False","conversation_topic":"test","author":"test.user@siemplify.co","message_id":"<xxxxxxxxxxGt5T8SAeM7mnbuOPXXCe6r0mhiqNh6VNA2aVJRyKQ@mail.gmail.com>","is_read":"True","is_response_requested":"False","references":"None","reply_to":"None","received_by":"Mailbox(name=\"ג'יימס בונד\", email_address='test@test.onmicrosoft.com', routing_type='SMTP', mailbox_type='Mailbox')","received_representing":"Mailbox(name=\"ג'יימס בונד\", email_address='test@test.onmicrosoft.com', routing_type='SMTP', mailbox_type='Mailbox')","account":"test@test.onmicrosoft.com","plaintext_body":"test","html_body":"<html><head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"></head><body><div dir=\"ltr\">test</div></body></html>","attachments_list":{}},{"mime_content":"content example","_id":"ItemId(id='xxxxxxxxxxJjNjJkLTc3MzAtNGM5My04ZjM0LTZiYzVjMDI4ZTZlNQBGAAAAAADLc0XF/C8kRJTduC5WOJE/BwDby9ZjVdTJTJRS8jxrcA+oAAAAAAEMAADby9ZjVdTJTJRS8jxrcA+oAAEzKVFHAAA=', changekey='xxxxxxxxxxDby9ZjVdTJTJRS8jxrcA+oAAEy4kvE')","parent_folder_id":"ParentFolderId(id='xxxxxxxxxxJjNjJkLTc3ADMwLTRjOTMtOGYzNC02YmM1YzAyOGU2ZTUALgAAA8tzRcX8LyRElN24LlY4kT8BANvL1mNV1MlMlFLyPGtwD6gAxxxxxxxxxx==', changekey='xxxAAA==')","item_class":"IPM.Note","subject":"test","sensitivity":"Normal","text_body":"test \r\n","body":"test","attachments":[],"datetime_received":"2021-01-19 14:31:30+00:00","size":"47390","categories":"None","importance":"Normal","in_reply_to":"None","is_submitted":"False","is_draft":"False","is_from_me":"False","is_resend":"False","is_unmodified":"True","headers":["MessageHeader(name='Received', value='from xxxxx0502MB3111.eurprd05.prod.outlook.com (xxxx:10a6:4:96::xx) by xxxxx05MB5957.eurprd05.prod.outlook.com with HTTPS; Tue, 19 Jan 2021 14:31:29 +0000')","MessageHeader(name='Received', value='from xxxxx0402CA0005.eurprd04.prod.outlook.com (xxxx:10a6:4:91::xx) by xxxxx0502MB3111.eurprd05.prod.outlook.com (xxxx:10a6:4:96::xx) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id xx.20.3763.xx; Tue, 19 Jan 2021 14:31:27 +0000')"],"datetime_sent":"2021-01-19 14:31:15+00:00","datetime_created":"2021-01-19 14:31:29+00:00","reminder_due_by":"None","reminder_is_set":"False","reminder_minutes_before_start":"0","display_cc":"None","display_to":"ג'יימס בונד","has_attachments":"False","culture":"en-US","effective_rights":"EffectiveRights(create_associated=False, create_contents=False, create_hierarchy=False, delete=True, modify=True, read=True, view_private_items=True)","last_modified_name":"Test User","last_modified_time":"2021-01-19 14:31:30+00:00","is_associated":"False","web_client_read_form_query_string":"https://outlook.office365.com/owa/?ItemID=xxxxxxxxxxJjNjJkLTc3MzAtNGM5My04ZjM0LTZiYzVjMDI4ZTZlNQBGAAAAAADLc0XF%2FC8kRJTduC5WOJE%2FBwDby9ZjVdTJTJRS8jxrcA%2BoAAAAAAEMAADby9ZjVdTJTJRS8jxrcA%2BoAAEzKVFHAAA%3D&exvsurl=1&viewmodel=ReadMessageItem","web_client_edit_form_query_string":"None","conversation_id":"ConversationId(id='xxxxxxxxxxJjNjJkLTc3MzAtNGM5My04ZjM0LTZiYzVjMDI4ZTZlNQAQAC1GApVgHVlBtJWYxzGtVqU=')","unique_body":"<html><body><div>\r\n<div>\r\n<div dir=\"ltr\">test</div>\r\n</div>\r\n</div>\r\n</body></html>","sender":"Mailbox(name='Test User', email_address='test.user@siemplify.co', routing_type='SMTP', mailbox_type='OneOff')","to_recipients":["Mailbox(name=\"ג'יימס בונד\", email_address='test@test.onmicrosoft.com', routing_type='SMTP', mailbox_type='Mailbox')"],"cc_recipients":"None","bcc_recipients":"None","is_read_receipt_requested":"False","is_delivery_receipt_requested":"False","conversation_topic":"test","author":"test.user@siemplify.co","message_id":"<xxxxxxxxxxEce+P27nsq-V3Jc69iCW9tTrfy6zQpuqug0kBwh=g@mail.gmail.com>","is_read":"True","is_response_requested":"False","references":"None","reply_to":"None","received_by":"Mailbox(name=\"ג'יימס בונד\", email_address='test@test.onmicrosoft.com', routing_type='SMTP', mailbox_type='Mailbox')","received_representing":"Mailbox(name=\"ג'יימס בונד\", email_address='test@test.onmicrosoft.com', routing_type='SMTP', mailbox_type='Mailbox')","account":"test@test.onmicrosoft.com","plaintext_body":"test","html_body":"<html><head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"></head><body><div dir=\"ltr\">test</div></body></html>","attachments_list":{}}]
```



#### Block Sender by Message ID
Action will get as a parameter a list of message IDs, and will be able to mark it as junk. Marking an item as junk using this action will add the item sender's mail address to the "Blocked Senders List", and will also move it to the "Junk" folder. NOTICE - to mark emails in all mailboxes, please configure impersonation permissions: https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed. NOTE: Action is supported only from Exchange Server version 2013 and newer, if a lower version is used, action will fail with the appropriate message.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Move item to Junk folder?|Should the action move the specified messages to the junk folder|False|Boolean|true|
|Message IDs|Filter condition, specify emails with which message ids to find. Should accept comma separated list of message ids to mark as junk. If message id is provided, subject, sender and recipient filters are ignored.|False|String||
|Mailboxes list to perform on|Filter condition, If you have a specific list of mailboxes you would like to conduct the operation on, for better timing, please provide them here. Should accept a comma separated list of mail addresses, to mark the messages as junk in. If a mailboxes list is provided, "Perform Action in all Mailboxes" parameter will be ignored.|False|String||
|Folder Name|Mailbox folder to search email in. Parameter should also accept comma separated list of folders to move the item from|False|String|Inbox|
|Subject Filter|Filter condition, specify subject to search for emails|False|String||
|Sender Filter|Filter condition, specify who should be the sender of needed emails|False|String||
|Recipient Filter|Filter condition, specify who should be the recipient of needed emails|False|String||
|Mark All Matching Emails|Filter condition, specify if action should Mark all matched by criteria emails from the mailbox or Mark only first match.|False|Boolean|false|
|Perform action in all mailboxes|If checked, move to junk and block sender emails in all mailboxes accessible with current impersonalization settings|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|25|
|Time Frame (minutes)|Filter condition, specify in what time frame in minutes should action look for emails.|False|String||



##### JSON Results
```json
[{"mime_content":"content example","_id":"ItemId(id='xxxxxxxxxxJjNjJkLTc3MzAtNGM5My04ZjM0LTZiYzVjMDI4ZTZlNQBGAAAAAADLc0XF/C8kRJTduC5WOJE/BwDby9ZjVdTJTJRS8jxrcA+oAAAAAAEMAADby9ZjVdTJTJRS8jxrcA+oAxxxxxxxxxx=', changekey='xxxxxxxxxxDby9ZjVdTJTJRS8jxrcA+oAAEy4kvx')","parent_folder_id":"ParentFolderId(id='xxxxxxxxxxJjNjJkLTc3ADMwLTRjOTMtOGYzNC02YmM1YzAyOGU2ZTUALgAAA8tzRcX8LyRElN24LlY4kT8BANvL1mNV1MlMlFLyPGtwD6gAxxxxxxxxxx==', changekey='xxxAAA==')","item_class":"IPM.Note","subject":"test","sensitivity":"Normal","text_body":"test\r\n","body":"test","attachments":[],"datetime_received":"2021-01-19 14:31:39+00:00","size":"47965","categories":"None","importance":"Normal","in_reply_to":"None","is_submitted":"False","is_draft":"False","is_from_me":"False","is_resend":"False","is_unmodified":"True","headers":["MessageHeader(name='Received', value='from xxxxx05MB7074.eurprd05.prod.outlook.com (xxxx:10a6:20b:1a6::xx) by xxxxx05MB5957.eurprd05.prod.outlook.com with HTTPS; Tue, 19 Jan 2021 14:31:38 +0000')","MessageHeader(name='Received', value='from xxxxx81CA0021.DEUP281.PROD.OUTLOOK.COM (xxxx:10a6:b10:14::x) by xxxxx05MB7074.eurprd05.prod.outlook.com (xxxx:10a6:20b:1a6::xx) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id xx.20.3763.x; Tue, 19 Jan 2021 14:31:37 +0000')"],"datetime_sent":"2021-01-19 14:31:24+00:00","datetime_created":"2021-01-19 14:31:39+00:00","reminder_due_by":"None","reminder_is_set":"False","reminder_minutes_before_start":"0","display_cc":"None","display_to":"ג'יימס בונד","has_attachments":"False","culture":"en-US","effective_rights":"EffectiveRights(create_associated=False, create_contents=False, create_hierarchy=False, delete=True, modify=True, read=True, view_private_items=True)","last_modified_name":"Test User","last_modified_time":"2021-01-19 14:33:08+00:00","is_associated":"False","web_client_read_form_query_string":"https://outlook.office365.com/owa/?ItemID=xxxxxxxxxxJjNjJkLTc3MzAtNGM5My04ZjM0LTZiYzVjMDI4ZTZlNQBGAAAAAADLc0XF%2FC8kRJTduC5WOJE%2FBwDby9ZjVdTJTJRS8jxrcA%2BoAAAAAAEMAADby9ZjVdTJTJRS8jxrcA%2BoAAEzKVFJAAA%3D&exvsurl=1&viewmodel=ReadMessageItem","web_client_edit_form_query_string":"None","conversation_id":"ConversationId(id='xxxxxxxxxxJjNjJkLTc3MzAtNGM5My04ZjM0LTZiYzVjMDI4ZTZlNQAQAHyj1LciNtFHpS4ZbBghSeM=')","unique_body":"<html><body><div>\r\n<div>\r\n<div dir=\"ltr\">test</div>\r\n</div>\r\n</div>\r\n</body></html>","sender":"Mailbox(name='Test User', email_address='test.user@siemplify.co', routing_type='SMTP', mailbox_type='OneOff')","to_recipients":["Mailbox(name=\"ג'יימס בונד\", email_address='test@test.onmicrosoft.com', routing_type='SMTP', mailbox_type='Mailbox')"],"cc_recipients":"None","bcc_recipients":"None","is_read_receipt_requested":"False","is_delivery_receipt_requested":"False","conversation_topic":"test","author":"test.user@siemplify.co","message_id":"<xxxxxxxxxxGt5T8SAeM7mnbuOPXXCe6r0mhiqNh6VNA2aVJRyKQ@mail.gmail.com>","is_read":"True","is_response_requested":"False","references":"None","reply_to":"None","received_by":"Mailbox(name=\"ג'יימס בונד\", email_address='test@test.onmicrosoft.com', routing_type='SMTP', mailbox_type='Mailbox')","received_representing":"Mailbox(name=\"ג'יימס בונד\", email_address='test@test.onmicrosoft.com', routing_type='SMTP', mailbox_type='Mailbox')","account":"test@test.onmicrosoft.com","plaintext_body":"test","html_body":"<html><head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"></head><body><div dir=\"ltr\">test</div></body></html>","attachments_list":{}},{"mime_content":"content example","_id":"ItemId(id='xxxxxxxxxxJjNjJkLTc3MzAtNGM5My04ZjM0LTZiYzVjMDI4ZTZlNQBGAAAAAADLc0XF/C8kRJTduC5WOJE/BwDby9ZjVdTJTJRS8jxrcA+oAAAAAAEMAADby9ZjVdTJTJRS8jxrcA+oAAEzKVFHAAA=', changekey='xxxxxxxxxxDby9ZjVdTJTJRS8jxrcA+oAAEy4kvE')","parent_folder_id":"ParentFolderId(id='xxxxxxxxxxJjNjJkLTc3ADMwLTRjOTMtOGYzNC02YmM1YzAyOGU2ZTUALgAAA8tzRcX8LyRElN24LlY4kT8BANvL1mNV1MlMlFLyPGtwD6gAxxxxxxxxxx==', changekey='xxxAAA==')","item_class":"IPM.Note","subject":"test","sensitivity":"Normal","text_body":"test \r\n","body":"test","attachments":[],"datetime_received":"2021-01-19 14:31:30+00:00","size":"47390","categories":"None","importance":"Normal","in_reply_to":"None","is_submitted":"False","is_draft":"False","is_from_me":"False","is_resend":"False","is_unmodified":"True","headers":["MessageHeader(name='Received', value='from xxxxx0502MB3111.eurprd05.prod.outlook.com (xxxx:10a6:4:96::xx) by xxxxx05MB5957.eurprd05.prod.outlook.com with HTTPS; Tue, 19 Jan 2021 14:31:29 +0000')","MessageHeader(name='Received', value='from xxxxx0402CA0005.eurprd04.prod.outlook.com (xxxx:10a6:4:91::xx) by xxxxx0502MB3111.eurprd05.prod.outlook.com (xxxx:10a6:4:96::xx) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id xx.20.3763.xx; Tue, 19 Jan 2021 14:31:27 +0000')"],"datetime_sent":"2021-01-19 14:31:15+00:00","datetime_created":"2021-01-19 14:31:29+00:00","reminder_due_by":"None","reminder_is_set":"False","reminder_minutes_before_start":"0","display_cc":"None","display_to":"ג'יימס בונד","has_attachments":"False","culture":"en-US","effective_rights":"EffectiveRights(create_associated=False, create_contents=False, create_hierarchy=False, delete=True, modify=True, read=True, view_private_items=True)","last_modified_name":"Test User","last_modified_time":"2021-01-19 14:31:30+00:00","is_associated":"False","web_client_read_form_query_string":"https://outlook.office365.com/owa/?ItemID=xxxxxxxxxxJjNjJkLTc3MzAtNGM5My04ZjM0LTZiYzVjMDI4ZTZlNQBGAAAAAADLc0XF%2FC8kRJTduC5WOJE%2FBwDby9ZjVdTJTJRS8jxrcA%2BoAAAAAAEMAADby9ZjVdTJTJRS8jxrcA%2BoAAEzKVFHAAA%3D&exvsurl=1&viewmodel=ReadMessageItem","web_client_edit_form_query_string":"None","conversation_id":"ConversationId(id='xxxxxxxxxxJjNjJkLTc3MzAtNGM5My04ZjM0LTZiYzVjMDI4ZTZlNQAQAC1GApVgHVlBtJWYxzGtVqU=')","unique_body":"<html><body><div>\r\n<div>\r\n<div dir=\"ltr\">test</div>\r\n</div>\r\n</div>\r\n</body></html>","sender":"Mailbox(name='Test User', email_address='test.user@siemplify.co', routing_type='SMTP', mailbox_type='OneOff')","to_recipients":["Mailbox(name=\"ג'יימס בונד\", email_address='test@test.onmicrosoft.com', routing_type='SMTP', mailbox_type='Mailbox')"],"cc_recipients":"None","bcc_recipients":"None","is_read_receipt_requested":"False","is_delivery_receipt_requested":"False","conversation_topic":"test","author":"test.user@siemplify.co","message_id":"<xxxxxxxxxxEce+P27nsq-V3Jc69iCW9tTrfy6zQpuqug0kBwh=g@mail.gmail.com>","is_read":"True","is_response_requested":"False","references":"None","reply_to":"None","received_by":"Mailbox(name=\"ג'יימס בונד\", email_address='test@test.onmicrosoft.com', routing_type='SMTP', mailbox_type='Mailbox')","received_representing":"Mailbox(name=\"ג'יימס בונד\", email_address='test@test.onmicrosoft.com', routing_type='SMTP', mailbox_type='Mailbox')","account":"test@test.onmicrosoft.com","plaintext_body":"test","html_body":"<html><head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"></head><body><div dir=\"ltr\">test</div></body></html>","attachments_list":{}}]
```






## Jobs

#### Oauth Token Expiry Notification Job
Oauth Token Expiry Notification Job is recommended to use if integration is working with Oauth refresh tokens. Refresh tokens are valid only for 90 days, after that User will need to create a new refresh token to use in the integration. This job will send reminder emails to the configured recipient list when the token will expire in 10, 5 and 1 day. Once a new token is set in this job, the notification timer will start over.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Mail Server Address|True|String|outlook.office365.com|
|Mail Address for sending notifications|True|String||
|Notifications Recipients List|True|String||
|Client ID|True|String||
|Client Secret|False|Password||
|Tenant (Directory) ID|True|String||
|Refresh Token|True|Password||



## Connectors
#### Exchange EML Connector


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The field name used to determine the device product|True|String|device_product|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|siemplify_event_mapping_field|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|30|
|Server IP||True|IP|x.x.x.x|
|Domain|Specify the domain value to use for authentication.|True|String|None|
|Username|Specify Username to authenticate with on mail server. Username can be provided without the domain part or in either UPN (user@fully_qualified_DNS_domain_name) or Down-Level Logon Name (domain\username) format.|True|String|None|
|Password||True|Password|None|
|Mail Address||True|Email||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|Boolean|false|
|Use Domain For Authentication|If enabled, value provided for domain parameter will be concatenated to authenticate on the mail server as username@domain. If “Username” is specified in the username@domain or domain\username formats, this parameter is ignored and values from “Domain” and “Username” parameters are not concatenated.|False|Boolean|True|
|Folder Name||True|String|Inbox|
|Environment Field Name||False|String|None|
|Environment Regex Pattern||False|String|None|
|Unread Emails Only||False|Boolean|false|
|Mark Emails as Read||False|Boolean|false|
|Max Days Backwards||False|Integer|1|
|Encode Data as UTF-8|Indicates whether to encode the email data with UTF-8 or not. Setting to True is recommended.|False|Boolean|true|
|Attach EML or MSG File to the Case Wall|If checked, the forwarded EML or MSG file will be attached to the Case Wall.|False|Boolean|None|
|Exclusion Body Regex|Exclude those emails, whose body matches this regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|String|None|
|Proxy Server Address|The address of the proxy server to use.|False|String|None|
|Proxy Username|The proxy username to authenticate with.|False|String|None|
|Proxy Password|The proxy password to authenticate with.|False|Password|None|
|Extract urls from HTML email part?|Specify whether connector should additionally try to extract urls from html part of email. This will allow connector to extract complex urls, but urls from plain text part of email will not be extracted with this method. Extracted urls will be available in urls_from_html_part event field.|False|Boolean|false|


#### Exchange Mail Connector
Exchange Mail Connector

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Proxy Server Address|The address of the proxy server to use.|False|String|None|
|Proxy Username|The proxy username to authenticate with.|False|String|None|
|Proxy Password|The proxy password to authenticate with.|False|Password|None|
|DeviceProductField|The field name used to determine the device product|True|String|device_product|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|siemplify_event_mapping_field|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|60|
|Server Ip|x.x.x.x|True|IP|None|
|Domain|Specify the domain value to use for authentication.|True|String|None|
|Username|Specify Username to authenticate with on mail server. Username can be provided without the domain part or in either UPN (user@fully_qualified_DNS_domain_name) or Down-Level Logon Name (domain\username) format.|False|String|None|
|Password||True|Password|None|
|Mail Address|Mail address to pull emails from. e.g. user@domain.com|True|String|None|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|Boolean|false|
|Use Domain For Authentication|If enabled, value provided for domain parameter will be concatenated to authenticate on the mail server as username@domain. If “Username” is specified in the username@domain or domain\username formats, this parameter is ignored and values from “Domain” and “Username” parameters are not concatenated.|False|Boolean|True|
|Unread Emails Only|If checked, pull only unread mails|False|Boolean|True|
|Mark Emails as Read|If checked, mark mails as read after pulling them|False|Boolean|False|
|Attach Original EML|If checked, attach the original message as eml file.|False|Boolean|false|
|Folder Name|The field name used to determine the folder name. e.g. Inbox|True|String|Inbox|
|Environment Field Name|If defined - connector will extract the environment from the specified event field. You can manipulate the field data using the Regex pattern field to extract specific string. In case the the extracted environment field and Siemplify environment name are not equal - you can map them in the map.json that is auto-generated on the first run, inside the <run-folder>.<run-folder> = C:\Siemplify_Server\Scripting\SiemplifyConnectorExecution<Connector_Folder>|False|Integer|None|
|Environment Regex Pattern|If defined - the connector will implement the specific RegEx pattern on the data from "envirnment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"|False|Integer|None|
|Max Days Backwards|Max number of days to fetch mails since. e.g. 3|True|String|5|
|Exclusion Subject Regex|Exclude those emails, whose subject matches this regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|String|None|
|Exclusion Body Regex|Exclude those emails, whose body matches this regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|String|None|


#### Exchange Mail Connector v2
Exchange Mail Connector v2

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|device_product|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|event_name|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|String||
|Headers to add to events|Specify what headers from emails should be added to the events. Parameter accepts multiple values as a comma separated string. Provided values can be exact match or set as a regex.|False|String||
|Email exclude pattern|Regular expression to exclude specific emails from being ingested by the connector. Works with both subject and body part of email. Example is, to exclude mass mailing emails like news from being ingested.|False|String||
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|60|
|Mail Server Address|Mail server IP address to connect to. If connecting to O365, server address should be set to outlook.office365.com|True|String||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|Boolean|false|
|Mail Address|Mail address to use in integration, to use for sending out emails and work with received emails for this email (mailbox)|True|String||
|Use Domain For Authentication|If enabled, value provided for domain parameter will be concatenated to authenticate on the mail server as username@domain. If “Username” is specified in the username@domain or domain\username formats, this parameter is ignored and values from “Domain” and “Username” parameters are not concatenated.|False|Boolean|false|
|Domain|Specify the domain value to use for authentication.|True|String||
|Username|Specify Username to authenticate with on mail server. Username can be provided without the domain part or in either UPN (user@fully_qualified_DNS_domain_name) or Down-Level Logon Name (domain\username) format.|True|String||
|Password|A password to authenticate with on mail server|True|Password||
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders.  Parameter is case sensitive|True|String|Inbox|
|Unread Emails Only|If checked, cases will be pulled only from unread emails|False|Boolean|false|
|Mark Emails as Read|If checked, after the emails have been pulled they will be marked as read|False|Boolean|false|
|Attach Original EML|If checked, the original email will be attached to the case info as an eml file|False|Boolean|false|
|Offset Time In Days|Fetch emails from X days backwards|True|Integer|5|
|Fetch Backwards Time Interval (minutes)|Time interval connector should use to fetch events from max hours backwards or connector last run timestamp. This parameter in minutes can be used to split max hours backwards on smaller segments and process them individually. Its recommended to adjust this value accordingly to the environment, for example 60 minutes or less.|False|Integer|0|
|Max Emails Per Cycle|Fetch x emails per connector cycle|True|Integer|10|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password||
|Extract urls from HTML email part?|Specify whether connector should additionally try to extract urls from html part of email. This will allow connector to extract complex urls, but urls from plain text part of email will not be extracted with this method. Extracted urls will be available in urls_from_html_part event field.|False|Boolean|false|
|Disable Overflow|If enabled, the connector will ignore the overflow mechanism.|False|Boolean|false|
|Original Received Mail Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|String||
|Attached Mail File Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|String||
|Create a Separate Siemplify Alert per Attached Mail File?|If enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|Boolean|false|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Siemplify Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled.|False|String||
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|String||
|Email Padding Period (minutes)|Specify an optional time period in minutes connector should fetch emails for prior to the latest timestamp.|False|Integer|0|


##### Whitelist
| |
|-|
|subject: (?<=Subject: ).*|
|to: (?m)(?<=^To: ).*|


#### Exchange Mail Connector v2 with Oauth Authentication
Connector can be used to monitor specific mailboxes on Office 365 mail servers that require Oauth authentication. Get Authorization and Generate Token actions can be used to obtain refresh token that should be set in the connector. Note: Make sure to configure the integration first for the Oauth authentication.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Framework parameter, must be set for every connector. Describes the name of the field where the product name is stored.|True|String|device_product|
|EventClassId|Framework parameter, must be set for every connector. Describes the name of the field where the event name is stored.|True|String|event_name|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|String||
|Headers to add to events|Specify what headers from emails should be added to the events. Parameter accepts multiple values as a comma separated string. Provided values can be exact match or set as a regex.|False|String||
|Email exclude pattern|Regular expression to exclude specific emails from being ingested by the connector. Works with both subject and body part of email. Example is, to exclude mass mailing emails like news from being ingested.|False|String||
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|60|
|Mail Server Address|Mail server IP address to connect to. If connecting to O365, server address should be set to outlook.office365.com|True|String|outlook.office365.com|
|Mail Address|Mail address to use for connector.|True|String||
|Client ID|For Office 365 Oauth authentication, Client (Application) ID of Azure Active Directory App that will be used for the integration.|True|String||
|Client Secret|For Office 365 Oauth authentication, secret can be provided for the auth flow.|False|Password||
|Tenant (Directory) ID|For Office 365 Oauth authentication, Azure Tenant (Directory) ID.|True|String||
|Refresh Token|For Office 365 Oauth authentication, refresh token that was obtained from running “Get Authorization” and “Generate Token” actions.|True|Password||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|Boolean|false|
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive|True|String|Inbox|
|Unread Emails Only|If checked, cases will be pulled only from unread emails|False|Boolean|false|
|Mark Emails as Read|If checked, after the emails have been pulled they will be marked as read|False|Boolean|false|
|Attach Original EML|If checked, the original email will be attached to the case info as an eml file|False|Boolean|false|
|Offset Time In Days|Fetch emails from X days backwards|True|Integer|5|
|Fetch Backwards Time Interval (minutes)|Time interval connector should use to fetch events from max hours backwards or connector last run timestamp. This parameter in minutes can be used to split max hours backwards on smaller segments and process them individually. Its recommended to adjust this value accordingly to the environment, for example 60 minutes or less.|False|Integer|0|
|Max Emails Per Cycle|Fetch x emails per connector cycle|True|Integer|10|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password||
|Extract urls from HTML email part?|Specify whether connector should additionally try to extract urls from html part of email. This will allow connector to extract complex urls, but urls from plain text part of email will not be extracted with this method. Extracted urls will be available in urls_from_html_part event field.|False|Boolean|false|
|Disable Overflow|If enabled, the connector will ignore the overflow mechanism.|False|Boolean|false|
|Original Received Mail Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|String||
|Attached Mail File Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|String||
|Create a Separate Siemplify Alert per Attached Mail File?|If enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|Boolean|false|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Siemplify Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled.|False|String||
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|String||
|Email Padding Period (minutes)|Specify an optional time period in minutes connector should fetch emails for prior to the latest timestamp.|False|Integer|0|


##### Whitelist
| |
|-|
|subject: (?<=Subject: ).*|
|to: (?m)(?<=^To: ).*|




