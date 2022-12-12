
# Arnaud Email Utilities



Python Version - 2


#### Dependencies
| |
|-|
|cffi-1.15.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pyssdeep-1.0.0-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|pycparser-2.21-py2.py3-none-any.whl|
|dnstwist-20220815-py3-none-any.whl|


## Actions
#### HTML-to-PNG

Timeout - 60 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Endpoint|The API endpoint being targeted|True|String|https://us-central1-static-resources-361419.cloudfunctions.net/html-to-png|
|Bearer Token|Bearer Token|False|String|None|
|Text|Text to render as a PNG|True|String|<html><body>Hello there!</body></html>|



##### JSON Results
```json
{}
```



#### Get Ssdeep Hash

Timeout - 30 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|String to Hash|The content to be hashed|True|String|<insert here>|



##### JSON Results
```json
{}
```



#### Get DNStwist

Timeout - 60 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|parameter|parameter|True|String|parameter|



##### JSON Results
```json
{}
```



#### Get Pydeep Hash

Timeout - 30 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|String to Hash|The content to be hashed|True|String|<insert here>|



##### JSON Results
```json
{}
```



#### Take URL Screenshot

Timeout - 120 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Endpoint|The API endpoint being targeted|True|String|https://us-central1-static-resources-361419.cloudfunctions.net/url-to-png|
|Bearer Token|Bearer Token|False|String|None|



##### JSON Results
```json
{}
```









