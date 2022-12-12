# Submit Files For analysis
An embedded workflow that can receive inputs and return an output.



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** True


##### Input Parameters
|Name|Default Value|
|----|-------------|
|File Paths|None|


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|FalconSandbox_Submit File_1|Submit files for analysis|FalconSandbox|Submit File|
|AnyRun_AnalyzeFile_1|Create Any.Run file analysis task. Note: Action is not working with Siemplify entities, full path to file to analyze should be provided as action input parameter.|AnyRun|AnalyzeFile|
|FalconSandbox_Wait For Job and Fetch Report_1|Wait for a scan job to complete and fetch the scan report.|FalconSandbox|Wait For Job and Fetch Report|
