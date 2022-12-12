# Manual Case Enrichment




**Enabled:** True

**Version:** 0

**Type:** Playbook

**Priority:** 2

**Playbook Simulator:** True


### Playbook Trigger
**Trigger Type:** Alert Type

**Conditions Operator:** And

##### Conditions
|Key|Operator|Value|
|---|--------|-----|
||Equals|Manual Case|


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Siemplify_Case Tag_2|Add given tag to the case the current alert is grouped to|Siemplify|Case Tag|
### Involved Blocks
|Name|Description|
|----|-----------|
|Submit Files For analysis|An embedded workflow that can receive inputs and return an output.|
|Entity Triage|An embedded workflow that can receive inputs and return an output.|
|Process Attachments|An embedded workflow that can receive inputs and return an output.|
