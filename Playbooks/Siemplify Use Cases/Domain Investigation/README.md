# Domain Investigation
Enriches URLs, Emails, Domains, and IP addresses with WHOIS information.  Will create domain entities and link to URLs and Emails.  Will set any domain that is less than 180 days old as suspicious.  Checks to see if domains are look a like domains. 




**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False


##### Input Parameters
|Name|Default Value|
|----|-------------|
|Min Domain Age|180|


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Enrichment_Whois|Query WHOIS servers for domain registration information.  Supports IP Addresses, URLs, Email, Domains.  Supports creation of DOMAIN entities linked to target entity and a domain age threshold to set the entity to suspicious. |Enrichment|Whois|
|Tools_Add Alert Scoring Information_5|A URL shortener was found.Severity: Medium|Tools|Add Alert Scoring Information|
|Search for URL Shortener|Do any of the domains match a url shortener?|Tools|Search Text|
|Search for free file sharing links|Are there any free file sharing links?|Tools|Search Text|
|Tools_Add Alert Scoring Information_13|No free file share links were found.|Tools|Add Alert Scoring Information|
|Tools_Look-A-Like Domains|This action will compare domain entities against the list of domains defined for the environment.  If the domains are similar the entity will be marked as suspicious and enriched with the matching domain.|Tools|Look-A-Like Domains|
|Tools_Add Alert Scoring Information_10|Microsoft threat intel describes a phishing campaign that uses DGA domains, free email services, and compromised email accounts to send massive numbers of phishing emails.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_14|The domain is younger than the threshold.Severity: High|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_12|No URL Shortener|Tools|Add Alert Scoring Information|
|Case Comment_No Whois Entities||Siemplify|Case Comment|
|Tools_Add Alert Scoring Information_9|Microsoft threat intel describes a phishing campaign that uses DGA domains, free email services, and compromised email accounts to send massive numbers of phishing emails. Severity: MediumTag: suspicious-link|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_11|This action will add an entry to the alert scoring database.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_3|Look a like domain found. Severity: High|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_FreeFileShare|A free file share link was found. Severity: Medium|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_15|The youngest domain is older than the threshold.|Tools|Add Alert Scoring Information|
