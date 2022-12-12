# Azure Sentinel




**Enabled:** True

**Version:** 0

**Type:** Playbook

**Priority:** 2

**Playbook Simulator:** True


### Playbook Trigger
**Trigger Type:** Custom Trigger

**Conditions Operator:** And

##### Conditions
|Key|Operator|Value|
|---|--------|-----|
|[Alert.SourceSystemName]|Equals|MicrosoftAzureSentinel|


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Siemplify_Case Tag_1|Add given tag to the case the current alert is grouped to|Siemplify|Case Tag|
### Involved Blocks
|Name|Description|
|----|-----------|
|Process Azure Sentinel|An embedded workflow that can receive inputs and return an output.|
