# Process Attachments
An embedded workflow that can receive inputs and return an output.



**Enabled:** True

**Version:** 1

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False


##### Input Parameters
|Name|Default Value|
|----|-------------|


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|FileUtilities_Save Base64 to File_1|The action saves a base64 string to a file.  It supports comma separated lists for Filename and Base64 Input.  The optional File Extension parameter is used to add an extension to the output filename.|FileUtilities|Save Base64 to File|
|FileUtilities_Get Attachment_1|The actions gets an attachment from the case wall (the result is presented as a Base64)|FileUtilities|Get Attachment|
|TemplateEngine_Render Template_1|This action will render a Jinja2 template using a JSON input.  |TemplateEngine|Render Template|
