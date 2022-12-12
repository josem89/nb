# Body Analysis
This block will scan the body string for spelling errors and ...




**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False


##### Input Parameters
|Name|Default Value|
|----|-------------|
|parsed_message|None|


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Tools_Add Alert Scoring Information_5|This action will add an entry to the alert scoring database.  Alert score is based off the ratio: 5 Low = 1 Medium.  3 Medium = 1 High.  2 High = 1 Critical.  Optional tag added to case.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_PoorSpelling|The email has poor spelling.  Severity: Medium|Tools|Add Alert Scoring Information|
|Search_Message Body Keyword Search|Search the plaintext message body for keywords indicating urgency or for an action to be taken|Tools|Search Text|
|Tools_Add Alert Scoring Information_6|The email has good spelling.|Tools|Add Alert Scoring Information|
|Buffer_Parse Message|Buffer the parsed message input|Tools|Buffer|
|SerializeTXTBody |Serialize the Plaintext message body|Functions|String Functions|
|SanitizeHTML_HTML Message Body|Given a fragment of HTML, SantizeHTML will parse it according to the HTML5 parsing algorithm and sanitize any disallowed tags or attributes. This algorithm also takes care of things like unclosed and (some) misnested tags.|Functions|SanitizeHTML|
|Render Template_Plaintext Message Body|Render the plaintext message|TemplateEngine|Render Template|
|Tools_Add Alert Scoring Information_7|No zero-width spaces were found within the body of the email.|Tools|Add Alert Scoring Information|
|SerializeHTMLBody|Serialize the HTML message body|Functions|String Functions|
|Tools_Add Alert Scoring Information_8|Zero-width spaces were found within the body of the email.Severity: Medium|Tools|Add Alert Scoring Information|
|SanitizeHTML_Text Message Body|Sanitize the plaintext message body in case it contains any HTML formatting|Functions|SanitizeHTML|
|Search for Zero Width Spaces|Search for zero-width spaces (ZWSPs) in the middle of URLs within the RAW HTML of the emails.https://www.securityweek.com/phishers-use-zero-width-spaces-bypass-office-365-protections|Tools|Search Text|
|Tools_Add Alert Scoring Information_4|This action will add an entry to the alert scoring database.  Alert score is based off the ratio: 5 Low = 1 Medium.  3 Medium = 1 High.  2 High = 1 Critical.  Optional tag added to case.|Tools|Add Alert Scoring Information|
|Spell Check_Message Body|Spell Check the message body|Tools|Spell Check String|
|Buffer_Serialized Results|Buffer all the serialized results|Tools|Buffer|
