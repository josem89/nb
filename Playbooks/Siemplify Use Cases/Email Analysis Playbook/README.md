# Email Analysis Playbook




**Enabled:** True

**Version:** 0

**Type:** Playbook

**Priority:** 1

**Playbook Simulator:** True


### Playbook Trigger
**Trigger Type:** Product Name

**Conditions Operator:** And

##### Conditions
|Key|Operator|Value|
|---|--------|-----|
||Equals|Graph Mail|


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Siemplify_Change Alert Priority_1|Automatically change the alert priority to the given input|Siemplify|Change Alert Priority|
|Buffer_HeaderJSONResults|JSON Results from Analyze Headers|Tools|Buffer|
|Siemplify_Change Case Stage_1|Change case stage to handling|Siemplify|Change Case Stage|
|VirusTotalV3_Enrich URL_1|Enrich URL using information from VirusTotal.|VirusTotalV3|Enrich URL|
|Create List of Words from Email Body|Create a list of words from the email bodies.  This list will be passed to the Extract Zip file as possible passwords to test.|Functions|String Functions|
|UnshortenMe_Unshorten URL_1|Resolve short URLs to long URLs|UnshortenMe|Unshorten URL|
|EmailUtilities_Parse Case Wall Email Attachment|This action will parse an EML or MSG file that has been attached to the case wall.|EmailUtilities|Parse Case Wall Email|
|Change Case Name_Email Subject|Change the case name to 'Phishing - EMAILSUBJECT'|Tools|Change Case Name|
|Siemplify_Case Comment_1|Add a comment to the case the current alert has been grouped to|Siemplify|Case Comment|
|VirusTotalV3_Enrich IP_1|Enrich IP using information from VirusTotal.|VirusTotalV3|Enrich IP|
|VirusTotalV3_Get Domain Details_1|Get detailed information about the domain using information from VirusTotal. Supported entities: URL (entity extracts domain part), Hostname.|VirusTotalV3|Get Domain Details|
|Siemplify_Close Alert_1|Closes the current alert|Siemplify|Close Alert|
|VirusTotalV3_Enrich Hash_1|Enrich Hash using information from VirusTotal. Only MD5, SHA-1 and SHA-256 are supported.|VirusTotalV3|Enrich Hash|
|Render Template_Message Summary|This action will render a Jinja2 template using a JSON input.  |TemplateEngine|Render Template|
|Add General Insight_Shortened Links|Display the result to the Analyst. Optionally add another action to create entities from the results.|Siemplify|Add General Insight|
|FileUtilities_Add Attachment_1|The action adds an attachment to the case wall (similar to attach evidence)|FileUtilities|Add Attachment|
|Create Subject Entity|Creates an entity and adds to requested alert. Note - Please make sure to read our documentation regarding the differences in the delimiter’s behavior, between different Siemplify’s platform versions 5.6.0 inclusive and 5.6.2 exclusive, here: https://integrations.siemplify.co/doc/siemplify#create-entity|Siemplify|Create Entity|
|ThreatConnect_Enrich Entities_1|Enrich IP addresses, hosts, URLs and hashes with information from ThreatConnect|ThreatConnect|Enrich Entities|
|Case Comment_EML Level|Level 0 is the parent EML attached to the case wall.Level 1 is the embedded EML that was sent as an attachment.|Siemplify|Case Comment|
### Involved Blocks
|Name|Description|
|----|-----------|
|Attachments|An embedded workflow that can receive inputs and return an output.|
|IMPORT 6 - Analyze Headers|Block will analyze headers. |
|Domain Investigation|Enriches URLs, Emails, Domains, and IP addresses with WHOIS information.  Will create domain entities and link to URLs and Emails.  Will set any domain that is less than 180 days old as suspicious.  Checks to see if domains are look a like domains. |
|Certificate Check|An embedded workflow that can receive inputs and return an output.|
|IMPORT 6 - Body Analysis|This block will scan the body string for spelling errors and ...|
|Sanitization|An embedded workflow that can receive inputs and return an output.|
