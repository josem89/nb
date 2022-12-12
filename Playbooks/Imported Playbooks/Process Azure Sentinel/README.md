# Process Azure Sentinel
An embedded workflow that can receive inputs and return an output.



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False


##### Input Parameters
|Name|Default Value|
|----|-------------|


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Tools_Set Context Value_3|The action sets a key and value in a specific context (alert or case)|Tools|Set Context Value|
|Set AS Owner|The action sets a key and value in a specific context (alert or case)|Tools|Set Context Value|
|Siemplify_Update Case Description_1|Ability to set Case Description from playbooks.|Siemplify|Update Case Description|
|Set AS Description|The action sets a key and value in a specific context (alert or case)|Tools|Set Context Value|
|Set AS Status|The action sets a key and value in a specific context (alert or case)|Tools|Set Context Value|
|Set AS Severity|The action sets a key and value in a specific context (alert or case)|Tools|Set Context Value|
