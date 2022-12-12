# Attachments
An embedded workflow that can receive inputs and return an output.



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False


##### Input Parameters
|Name|Default Value|
|----|-------------|
|attachments_json|None|
|zip_passwords|None|


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Tools_Add Alert Scoring Information_4|File contains VBA Macros.Severity: High|Tools|Add Alert Scoring Information|
|Case Comment_No Attachments|No attachments for the Attachment Block|Siemplify|Case Comment|
|Tools_Add Alert Scoring Information_7|Add score of low due to unable to extract zip file.Severity: Low|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_5|The attachment is an encrypted ole2 file.Severity: Medium|Tools|Add Alert Scoring Information|
|FileUtilities_Extract Zip Files_1|This action will extract files from a ZIP archive.  It has the ability to extract password protected files by either a supplied password or bruteforce. Requires FILENAME entity to have attachment_id attribute to download file from Case Wall.|FileUtilities|Copy of Extract Zip Files|
|Tools_Add Alert Scoring Information_6|Add score of low for email containing zip files.|Tools|Add Alert Scoring Information|
|Buffer_AttachmentsJSON|The action receives a json and returns it as a json result|Tools|Buffer|
