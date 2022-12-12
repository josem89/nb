# Entity Triage
An embedded workflow that can receive inputs and return an output.



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** True


##### Input Parameters
|Name|Default Value|
|----|-------------|


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Tools_Add Alert Scoring Information_2|No suspicious hashes were found by Virus Total.  |Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_1|A suspicious hash was found by Virus Total. Severity: Critical|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_SuspiciousURL|A suspicious URL was found by Virus Total.  Severity: Critical|Tools|Add Alert Scoring Information|
|VirusTotalV3_Enrich Hash_1|Enrich Hash using information from VirusTotal. Only MD5, SHA-1 and SHA-256 are supported.|VirusTotalV3|Enrich Hash|
|Tools_Add Alert Scoring Information_6|No suspicious hashes were found by Virus Total.  |Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_SuspiciousIP|A suspicious IP was found by Virus Total.  Severity: Critical|Tools|Add Alert Scoring Information|
|VirusTotalV3_Enrich URL_1|Enrich URL using information from VirusTotal.|VirusTotalV3|Enrich URL|
|Siemplify_Remove Tag_1|Remove tags from a case.|Siemplify|Remove Tag|
|VirusTotalV3_Enrich IP_1|Enrich IP using information from VirusTotal.|VirusTotalV3|Enrich IP|
|VT_Widget|This action will render a Jinja2 template using a JSON input.  |TemplateEngine|Render Template|
|ThreatConnect_Enrich Entities_1|Enrich IP addresses, hosts, URLs and hashes with information from ThreatConnect|ThreatConnect|Enrich Entities|
|Tools_Add Alert Scoring Information_5|No suspicious URLs were found by VirusTotal.|Tools|Add Alert Scoring Information|
