![ThreatConnect](./Resources/ThreatConnect.svg)

# ThreatConnect

Identify Manage and Block Threats Faster with Intelligence. Make informed decisions with ThreatConnect's in-platform analytics and automation.

Python Version - 1
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Access Id|None|True|String|None|
|ApiSecretKey|None|True|Password|None|
|Api Default Org|None|True|String||
|Api Root|None|True|String|https://sandbox.threatconnect.com/api|


#### Dependencies
| |
|-|
|cross/idna-2.6-py2.py3-none-any.whl|
|cross/threatconnect-2.4.20.tar.gz|
|cross/six-1.11.0-py2.py3-none-any.whl|
|cross/urllib3-1.22-py2.py3-none-any.whl|
|cross/requests-2.18.4-py2.py3-none-any.whl|
|cross/python_dateutil-2.6.1-py2.py3-none-any.whl|
|cross/enum34-1.1.6-py2-none-any.whl|
|cross/certifi-2018.1.18-py2.py3-none-any.whl|
|cross/chardet-3.0.4-py2.py3-none-any.whl|
|cross/pytz-2018.3-py2.py3-none-any.whl|


## Actions
#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Enrich Entities
Enrich IP addresses, hosts, URLs and hashes with information from ThreatConnect
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Owner Name|Owner name to fetch the data from.|False|String||



##### JSON Results
```json
[{"EntityResult": {"securityLabels": {"securityLabel": [], "resultCount": 0}, "owners": {"owner": [{"type": "Organization", "id": 440, "name": "S"}]}, "victims": {"resultCount": 0, "victim": []}, "tags": ["C2", "Malware"], "general": {"url": {"rating": 5.0, "confidence": 100, "dateAdded": "2018-01-09T20: 12: 11Z", "description": "URLAssociatedwithCryptoLockerC2Servers", "threatAssessConfidence": 93.33, "lastModified": "2018-01-09T20: 13: 24Z", "threatAssessRating": 4.33, "webLink": "https: //sandbox.threatconnect.com/auth/indicators/details/url.xhtml?orgid=43743075&owner=S", "text": "http: //markossolomon.com/f1q7qx.php", "owner": {"type": "Organization", "id": 440, "name": "S"}, "id": 43743075}}, "observations": {"resultCount": 0, "observation": []}, "groups": null, "indicators": {"indicator": [], "resultCount": 0}, "attributes": {"Description": ["URLAssociatedwithCryptoLockerC2Servers"]}, "observationCount": {"observationCount": {"count": 0}}, "victimAssets": {"victimAsset": [], "resultCount": 0}}, "Entity": "HTTP: //MARKOSSOLOMON.COM/F1Q7QX.PHP"}]
```









