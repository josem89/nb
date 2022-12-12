# Certificate Check
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
|Tools_Add Alert Scoring Information_3|This action will add an entry to the alert scoring database.  Alert score is based off the ratio: 5 Low = 1 Medium.  3 Medium = 1 High.  2 High = 1 Critical.  Optional tag added to case.|Tools|Add Alert Scoring Information|
|Tools_Add Alert Scoring Information_1|This action will add an entry to the alert scoring database.  Alert score is based off the ratio: 5 Low = 1 Medium.  3 Medium = 1 High.  2 High = 1 Critical.  Optional tag added to case.|Tools|Add Alert Scoring Information|
|Case Comment_No entities for Certs|No URLs to grab certs from|Siemplify|Case Comment|
|Tools_Add Alert Scoring Information_2|This action will add an entry to the alert scoring database.  Alert score is based off the ratio: 5 Low = 1 Medium.  3 Medium = 1 High.  2 High = 1 Critical.  Optional tag added to case.|Tools|Add Alert Scoring Information|
|Tools_Copy of Get Certificate Details_1|Get all certs and examine|Tools|Copy of Get Certificate Details|
