
# Connectors

A set of custom connectors created for Siemplify Community to power up automation capabilities.

Python Version - 2



## Actions



## Jobs



## Connectors
#### Scheduled Connector
A custom connector created to trigger playbooks by a given alert product, name and type and enables to edit the parameters according to your specific use case. 

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert fields|The alert fields you would like to insert in a json format|True|String|{
  "field_name_1": "field_value_1",
  "field_name_2": "field_value_2"
}|
|Alert name|The Alert name associated with the alert that will be created|True|String|<alert_name>|
|Alert type|The Alert type associated with the alert that will be created|False|String|<alert_type>|
|DeviceProductField|The field name used to determine the device product|True|String|<none>|
|EventClassId|The field name used to determine the event name (sub-type)|True|String|<none>|
|Product name|The Product name associated with the alert that will be created|False|String|<product_name>|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|30|


#### Cron Scheduled Connector
A custom connector created to trigger playbooks by a given alert product, name and type and enables to edit the parameters according to your specific use case. 

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert fields|The alert fields you would like to insert in a json format|True|String|{
  "field_name_1": "field_value_1",
  "field_name_2": "field_value_2"
}|
|Alert name|The Alert name associated with the alert that will be created|True|String|<alert_name>|
|Alert type|The Alert type associated with the alert that will be created|False|String|<alert_type>|
|Cron Expression|If defined, will determine when the connector should create a case.|False|String|None|
|DeviceProductField|The field name used to determine the device product|True|String|<none>|
|EventClassId|The field name used to determine the event name (sub-type)|True|String|<none>|
|Product name|The Product name associated with the alert that will be created|False|String|<product_name>|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|30|




