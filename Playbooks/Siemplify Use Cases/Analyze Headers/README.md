# Analyze Headers
Block will analyze headers. 



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False


##### Input Parameters
|Name|Default Value|
|----|-------------|
|headers|None|


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Tools_Add Alert Scoring Information_38|The email was sent from a custom domain, but the reply-to is a freemail domain.Severity: Medium|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_43|Undisclosed Recipients in to, cc, or bcc.|Tools|Add Alert Scoring Information|
|EmailUtilities_Analyze Headers|Analyze Headers accepts a JSON object containing a list of Email headers.  The action will validate the SPF, DMARC, ARC, and DKIM records in the email.  It will also check to see if any of the relay servers are blacklisted by querying multiple RBLs.|EmailUtilities|Analyze Headers|
|Tools_Add Alert Scoring Information_31|This action will add an entry to the alert scoring database.  Alert score is based off the ratio: 5 Low = 1 Medium.  3 Medium = 1 High.  2 High = 1 Critical.  Optional tag added to case.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_30|The recipients are not all BCCed in the email.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_33|The email does not have a Reply-To header.|Tools|Add Alert Scoring Information|
|Render Template_Relay Info|This action will render a Jinja2 template using a JSON input.  |TemplateEngine|Render Template|
|Render Template_HeaderValidationCheck|This action will render a Jinja2 template using a JSON input.  |TemplateEngine|Render Template|
|Tools_Add Alert Scoring Information_45|The To header is the same as the From and Return-Path headers.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_32|The initial email server is not on any blacklist.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_41|SPF and DKIM invalid.Severity: Medium|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_40|SPF or DKIM is false. Severity: Low|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_27|DMARC is valid.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_49|The From and Reply-To headers are aligned.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_36|This action will add an entry to the alert scoring database.  Alert score is based off the ratio: 5 Low = 1 Medium.  3 Medium = 1 High.  2 High = 1 Critical.  Optional tag added to case.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_44|The To header is the same as the From, but Return-Path is different.Severity: Low|Tools|Add Alert Scoring Information|
|FromDomain In FreeEmail List|Check to see if the from domain is in the FreeEmail custom list.|Lists|Is String In Custom List|
|Tools_Add Alert Scoring Information_29|The email does not have a Return-Path header.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_35|The subject contains a suspicious string.  Severity: Medium|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_39|The email was sent from a free email service.Severity: Low|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_26|The email was not sent from a free email service|Tools|Add Alert Scoring Information|
|Case Comment_No Headers|No Headers found|Siemplify|Case Comment|
|Tools_Add Alert Scoring Information_37|This action will add an entry to the alert scoring database.  Alert score is based off the ratio: 5 Low = 1 Medium.  3 Medium = 1 High.  2 High = 1 Critical.  Optional tag added to case.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_28|There are no undisclosed recipients in to, cc, or bcc.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_42|SPF and DKIM pass|Tools|Add Alert Scoring Information|
|Buffer_Header JSON|Buffer the Header Json|Tools|Buffer|
|Search for Suspicious Subjects|Search the subject of the email for possible suspicious strings.|Tools|Search Text|
|Tools_Add Alert Scoring Information_34|The initial email server is on at least one blacklist.Severity: Low|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_48|The email has mismatched from and reply-to headers. Severity: Low|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_50|All the recipients are BCCed.Severity: LowTag: AllRecipientsBCCed|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_25|The subject does not contain any suspicious information.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_47|The email does not have mismatched From and Return-Path Headers|Tools|Add Alert Scoring Information|
|HeaderScoresJSON|The action receives a json and returns it as a json result|Tools|Buffer|
|Tools_Extract URL Domain_1|Extract the domain from the reply-to header.|Tools|Extract URL Domain|
|Tools_Add Alert Scoring Information_46|The email has mismatched From and Return-Path HeadersSeverity: Low|Tools|Add Alert Scoring Information|
