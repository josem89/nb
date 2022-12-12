
# Insights

A set of insight actions created for Siemplify Community to power up playbook capabilities.  

Python Version - 2



## Actions
#### Create Entity Insight From Multiple JSONs
The action creates an entity insight from multiple json files. 
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fields4|The fields that will be extracted from the fourth  JSON string.|False|String|None|
|JSON4|The fourth JSON string to be parsed for the insight.|False|String|None|
|Title5|The title used for the fifth entity section.|False|String|None|
|Fields5|The fields that will be extracted from the fifth JSON string.|False|String|None|
|JSON5|The fifth JSON string to be parsed for the insight.|False|String|None|
|Placeholder Separator|A string that will be used to "break" lines.|False|String|,|
|Title1|The title used for the first entity section.|False|String|None|
|Fields1|The fields that will be extracted from the first JSON string.|False|String|None|
|JSON1|The first JSON string to be parsed for the insight.|False|String|None|
|Title2|The title used for the second entity section.|False|String|None|
|Fields2|The fields that will be extracted from the second JSON string.|False|String|None|
|JSON2|The second  JSON string to be parsed for the insight.|False|String|None|
|Title3|The title used for the third entity section.|False|String|None|
|Fields3|The fields that will be extracted from the third JSON string.|False|String|None|
|JSON3|The third JSON string to be parsed for the insight.|False|String|None|
|Title4|The title used for the fourth entity section.|False|String|None|



##### JSON Results
```json
{}
```



#### Ping
Check connectivity
Timeout - 300 Seconds



##### JSON Results
```json
{}
```



#### Create Entity Insight From Enrichment
The action creates an entity insight from an Enrichment action
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Message|Formatted string that incorporates entity enrichment. For example:Hi {AD_name}, please review.|True|String| |
|Triggered By|What integration should be associated with the insight|False|String|Siemplify|



##### JSON Results
```json
{}
```



#### Create Entity Insight From JSON
The action creates an entity insight from a json file
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|JSON|The JSON string that will be used to produce the Entity Insight.|True|String|{}|
|Identifier KeyPath|Key path for where to find the entity identifier to match the insight with the associated entity|True|String|Entity|
|Message|Formatted string that incorporates entity enrichment. For example:Hi {AD_name}, please review.|True|String||
|Triggered By|What integration should be associated with the insight|False|String|Siemplify|



##### JSON Results
```json
{}
```






## Jobs



## Connectors


