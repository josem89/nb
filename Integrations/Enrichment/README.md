
# Enrichment

A set of entity enrichment actions to assist in the managing of entity attributes.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Key|Siemplify API Key - Required to Enrich Entities from Explorer|False|Password|None|



## Actions
#### Ping
Check connectivity
Timeout - 300 Seconds



##### JSON Results
```json
{}
```



#### Enrich Source and Destinations
This action will add the source and destination links to IPs and hostnames in the alert.
Timeout - 300 Seconds



##### JSON Results
```json
{}
```



#### Enrich Entity From JSON
The action extracts fields from a json file and adds them to the entity fields
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Enrichment JSON| JSON from which you would like to enrich an entity. (List of JSONs)|True|String|[   {     "EntityResult": {       "permalink": "https://www.virustotal.com/file/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f/analysis/1549381312/",       "sha1": "3395856ce81f2b7382dee72602f798b642f14140",       "resource": "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F",       "response_code": 1,       "scan_date": "2019-02-05 15:41:52",       "scan_id": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f-1549381312",       "verbose_msg": "Scan finished, information embedded",       "total": 60,       "positives": 54,       "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",       "md5": "44d88612fea8a8f36de82e1278abb02f",       "scans": {         "Bkav": {           "detected": true,           "version": "1.1.1.1",           "result": "DOS.EiracA.Trojan",           "update": "20190201"         },         "MicroWorld-eScan": {           "detected": true,           "version": "14.0.297.0",           "result": "EICAR-Test-File",           "update": "20190205"         }       }     },     "Entity": "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F"   } ]|
|Identifier KeyPath|KeyPath to the Entity Identifier in the JSON|True|String|key1.key2|
|Separator|The "Separator" for the keypath. For example, if its XXX then the example would be:key1XXXkey2|True|String|.|
|PrefixForEnrichment|What prefix to use for enrichment|False|String|None|
|Enrichment JSONPath|JSONPath expressions always refers to a JSON structure in the same way as XPath expressions are used in combination with an XML document.|False|String|None|



##### JSON Results
```json
{}
```



#### Mark Entity as Suspicious
This action will mark the entities in the scope as suspicious.
Timeout - 300 Seconds



##### JSON Results
```json
{  
  "user label": "SiemplifyTest",  
  "user email": "siemplifytest@siemplify.co"  
}
```



#### Enrich FileName Entity with Path
This action will parse out path, file name, and extension from an entity and enrich it with file_path, file_name, and file_extension.
Timeout - 300 Seconds



##### JSON Results
```json
[{"Entity":"/var/log/messages","EntityResult":{"file_name":"messages","file_path":"/var/log","file_extension":""}},{"Entity":"file.exe","EntityResult":{"file_name":"file.exe","file_path":"","file_extension":".exe"}},{"Entity":"c:\\windows\\cmd.com","EntityResult":{"file_name":"cmd.com","file_path":"c:\\windows","file_extension":".com"}},{"Entity":"C:\\windows\\test\\test.exe","EntityResult":{"file_name":"test.exe","file_path":"C:\\windows\\test","file_extension":".exe"}}]
```



#### Enrich Entity from Explorer Attributes
Enriches entities with historic enrichment data using the entity explorer.  Requires API key to be configured for the integration.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Field Name|The field(s) from the Entity Explorer that will be used to enrich the entity. When null all fields will be enriched. Supports comma delimited string.|False|String||
|Use Field Name as Whitelist|When true, entities will be enriched with fields from 'Field Name' param.  When False, the list will be used as a blacklist and all other fields added|False|Boolean|true|



##### JSON Results
```json
[{"Entity": "F.ATTACKER4@GMAIL.COM", "EntityResult": {}}, {"Entity": "VICKIE.B@SIEMPLIFY.CO", "EntityResult": {}}, {"Entity": "HTTP://MARKOSSOLOMON.COM/F1Q7QX.PHP", "EntityResult": {"VT3_id": "057e8630c8880da8778b4f99e048933efb7cee9abdcf57fad89a7e7a2c7eae04", "VT3_title": "Registrant WHOIS contact information verification | Namecheap.com", "VT3_last_http_response_code": "200", "VT3_last_http_response_content_length": "183116", "VT3_threat_names": "C2/Generic-A", "VT3_harmless_count": "74", "VT3_malicious_count": "5", "VT3_undetected_count": "8", "VT3_reputation": "-7", "VT3_malicious_vote_count": "1", "VT3_report_link": "https://www.virustotal.com/gui/url/aHR0cDovL21hcmtvc3NvbG9tb24uY29tL0YxcTdRWC5waHA/detection", "VT3_widget_link": "https://www.virustotal.com/ui/widget/html/MDU3ZTg2MzBjODg4MGRhODc3OGI0Zjk5ZTA0ODkzM2VmYjdjZWU5YWJkY2Y1N2ZhZDg5YTdlN2EyYzdlYWUwNHx8dXJsfHx7ImJkMSI6ICIjNGQ2Mzg1IiwgImJnMSI6ICIjMzEzZDVhIiwgImJnMiI6ICIjMjIyYzQyIiwgImZnMSI6ICIjZmZmZmZmIiwgInR5cGUiOiAiZGVmYX...", "VT3_Forcepoint ThreatSeeker": "bot networks", "VT3_Sophos": "command and control", "VT3_Comodo Valkyrie Verdict": "unknown", "VT3_Webroot": "Dead Sites"}}, {"Entity": "YOUR NEW SALARY NOTIFICATION", "EntityResult": {}}]  
  

```



#### Whois
Query WHOIS servers for domain registration information.  Supports IP Addresses, URLs, Email, Domains.  Supports creation of DOMAIN entities linked to target entity and a domain age threshold to set the entity to suspicious. 
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Entities|Create and link domain entities to URL and Email / User names.|False|Boolean|true|
|Domain Age Threshold|Domains who's age is less than the than the supplied days will be marked suspicious.  |False|String||



##### JSON Results
```json
[  
	{  
		"Entity": "outlook.com",  
		"EntityResult": {  
			"id": [  
				"2019401_DOMAIN_COM-VRSN"  
			],  
			"status": [  
				"clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited",  
				"clientTransferProhibited https://icann.org/epp#clientTransferProhibited",  
				"clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited",  
				"serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited",  
				"serverTransferProhibited https://icann.org/epp#serverTransferProhibited",  
				"serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited"  
			],  
			"creation_date": [  
				"1994-08-18T04:00:00"  
			],  
			"expiration_date": [  
				"2022-08-17T04:00:00"  
			],  
			"updated_date": [  
				"2021-07-16T09:32:12"  
			],  
			"registrar": [  
				"MarkMonitor Inc."  
			],  
			"whois_server": [  
				"whois.markmonitor.com"  
			],  
			"nameservers": [  
				"NS1-38.AZURE-DNS.COM",  
				"NS2-38.AZURE-DNS.NET",  
				"NS3-38.AZURE-DNS.ORG",  
				"NS4-38.AZURE-DNS.INFO",  
				"NSE12.O365FILTERING.COM",  
				"NSE13.O365FILTERING.COM",  
				"NSE21.O365FILTERING.COM",  
				"NSE24.O365FILTERING.COM"  
			],  
			"emails": [  
				"abusecomplaints@markmonitor.com"  
			],  
			"contacts": {  
				"registrant": null,  
				"tech": null,  
				"admin": null,  
				"billing": null  
			},  
			"age_in_days": 9987  
		}  
	},  
	{  
		"Entity": "104.198.157.10",  
		"EntityResult": {  
			"nir": null,  
			"asn_registry": "arin",  
			"asn": "15169",  
			"asn_cidr": "104.198.128.0/19",  
			"asn_country_code": "US",  
			"asn_date": "2014-08-27",  
			"asn_description": "GOOGLE, US",  
			"query": "104.198.157.10",  
			"network": {  
				"handle": "NET-104-196-0-0-1",  
				"status": [  
					"active"  
				],  
				"remarks": [  
					{  
						"title": "Registration Comments",  
						"description": "** The IP addresses under this netblock are in use by Google Cloud customers ** \r\n\r\nDirect all copyright and legal complaints to \r\nhttps://support.google.com/legal/go/report\r\n\r\nDirect all spam and abuse complaints to \r\nhttps://support.google.com/code/go/gce_abuse_report\r\n\r\nFor fastest response, use the relevant forms above.\r\n\r\nComplaints can also be sent to the GC Abuse desk \r\n(google-cloud-compliance@google.com) \r\nbut may have longer turnaround times.\r\n\r\nComplaints sent to any other POC will be ignored.",  
						"links": null  
					}  
				],  
				"notices": [  
					{  
						"title": "Terms of Service",  
						"description": "By using the ARIN RDAP/Whois service, you are agreeing to the RDAP/Whois Terms of Use",  
						"links": [  
							"https://www.arin.net/resources/registry/whois/tou/"  
						]  
					},  
					{  
						"title": "Whois Inaccuracy Reporting",  
						"description": "If you see inaccuracies in the results, please visit: ",  
						"links": [  
							"https://www.arin.net/resources/registry/whois/inaccuracy_reporting/"  
						]  
					},  
					{  
						"title": "Copyright Notice",  
						"description": "Copyright 1997-2021, American Registry for Internet Numbers, Ltd.",  
						"links": null  
					}  
				],  
				"links": [  
					"https://rdap.arin.net/registry/ip/104.196.0.0",  
					"https://whois.arin.net/rest/net/NET-104-196-0-0-1"  
				],  
				"events": [  
					{  
						"action": "last changed",  
						"timestamp": "2015-09-21T20:50:14-04:00",  
						"actor": null  
					},  
					{  
						"action": "registration",  
						"timestamp": "2014-08-27T13:55:35-04:00",  
						"actor": null  
					}  
				],  
				"raw": null,  
				"start_address": "104.196.0.0",  
				"end_address": "104.199.255.255",  
				"cidr": "104.196.0.0/14",  
				"ip_version": "v4",  
				"type": "DIRECT ALLOCATION",  
				"name": "GOOGLE-CLOUD",  
				"country": null,  
				"parent_handle": "NET-104-0-0-0-0"  
			},  
			"entities": [  
				"GOOGL-2"  
			],  
			"objects": {  
				"GOOGL-2": {  
					"handle": "GOOGL-2",  
					"status": null,  
					"remarks": [  
						{  
							"title": "Registration Comments",  
							"description": "*** The IP addresses under this Org-ID are in use by Google Cloud customers *** \r\n\r\nDirect all copyright and legal complaints to \r\nhttps://support.google.com/legal/go/report\r\n\r\nDirect all spam and abuse complaints to \r\nhttps://support.google.com/code/go/gce_abuse_report\r\n\r\nFor fastest response, use the relevant forms above.\r\n\r\nComplaints can also be sent to the GC Abuse desk \r\n(google-cloud-compliance@google.com) \r\nbut may have longer turnaround times.\r\n\r\nComplaints sent to any other POC will be ignored.",  
							"links": null  
						}  
					],  
					"notices": null,  
					"links": [  
						"https://rdap.arin.net/registry/entity/GOOGL-2",  
						"https://whois.arin.net/rest/org/GOOGL-2"  
					],  
					"events": [  
						{  
							"action": "last changed",  
							"timestamp": "2019-11-01T05:34:25-04:00",  
							"actor": null  
						},  
						{  
							"action": "registration",  
							"timestamp": "2006-09-29T16:40:11-04:00",  
							"actor": null  
						}  
					],  
					"raw": null,  
					"roles": [  
						"registrant"  
					],  
					"contact": {  
						"name": "Google LLC",  
						"kind": "org",  
						"address": [  
							{  
								"type": null,  
								"value": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States"  
							}  
						],  
						"phone": null,  
						"email": null,  
						"role": null,  
						"title": null  
					},  
					"events_actor": null,  
					"entities": [  
						"GCABU-ARIN",  
						"ZG39-ARIN"  
					]  
				},  
				"GCABU-ARIN": {  
					"handle": "GCABU-ARIN",  
					"status": [  
						"validated"  
					],  
					"remarks": null,  
					"notices": [  
						{  
							"title": "Terms of Service",  
							"description": "By using the ARIN RDAP/Whois service, you are agreeing to the RDAP/Whois Terms of Use",  
							"links": [  
								"https://www.arin.net/resources/registry/whois/tou/"  
							]  
						},  
						{  
							"title": "Whois Inaccuracy Reporting",  
							"description": "If you see inaccuracies in the results, please visit: ",  
							"links": [  
								"https://www.arin.net/resources/registry/whois/inaccuracy_reporting/"  
							]  
						},  
						{  
							"title": "Copyright Notice",  
							"description": "Copyright 1997-2021, American Registry for Internet Numbers, Ltd.",  
							"links": null  
						}  
					],  
					"links": [  
						"https://rdap.arin.net/registry/entity/GCABU-ARIN",  
						"https://whois.arin.net/rest/poc/GCABU-ARIN"  
					],  
					"events": [  
						{  
							"action": "last changed",  
							"timestamp": "2021-04-09T11:46:04-04:00",  
							"actor": null  
						},  
						{  
							"action": "registration",  
							"timestamp": "2011-03-30T00:36:28-04:00",  
							"actor": null  
						}  
					],  
					"raw": null,  
					"roles": [  
						"abuse",  
						"noc"  
					],  
					"contact": {  
						"name": "GC Abuse",  
						"kind": "group",  
						"address": [  
							{  
								"type": null,  
								"value": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States"  
							}  
						],  
						"phone": [  
							{  
								"type": [  
									"work",  
									"voice"  
								],  
								"value": "+1-650-253-0000"  
							}  
						],  
						"email": [  
							{  
								"type": null,  
								"value": "google-cloud-compliance@google.com"  
							}  
						],  
						"role": null,  
						"title": null  
					},  
					"events_actor": null,  
					"entities": null  
				},  
				"ZG39-ARIN": {  
					"handle": "ZG39-ARIN",  
					"status": [  
						"validated"  
					],  
					"remarks": null,  
					"notices": [  
						{  
							"title": "Terms of Service",  
							"description": "By using the ARIN RDAP/Whois service, you are agreeing to the RDAP/Whois Terms of Use",  
							"links": [  
								"https://www.arin.net/resources/registry/whois/tou/"  
							]  
						},  
						{  
							"title": "Whois Inaccuracy Reporting",  
							"description": "If you see inaccuracies in the results, please visit: ",  
							"links": [  
								"https://www.arin.net/resources/registry/whois/inaccuracy_reporting/"  
							]  
						},  
						{  
							"title": "Copyright Notice",  
							"description": "Copyright 1997-2021, American Registry for Internet Numbers, Ltd.",  
							"links": null  
						}  
					],  
					"links": [  
						"https://rdap.arin.net/registry/entity/ZG39-ARIN",  
						"https://whois.arin.net/rest/poc/ZG39-ARIN"  
					],  
					"events": [  
						{  
							"action": "last changed",  
							"timestamp": "2021-11-10T10:26:54-05:00",  
							"actor": null  
						},  
						{  
							"action": "registration",  
							"timestamp": "2000-11-30T13:54:08-05:00",  
							"actor": null  
						}  
					],  
					"raw": null,  
					"roles": [  
						"administrative",  
						"technical"  
					],  
					"contact": {  
						"name": "Google LLC",  
						"kind": "group",  
						"address": [  
							{  
								"type": null,  
								"value": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States"  
							}  
						],  
						"phone": [  
							{  
								"type": [  
									"work",  
									"voice"  
								],  
								"value": "+1-650-253-0000"  
							}  
						],  
						"email": [  
							{  
								"type": null,  
								"value": "arin-contact@google.com"  
							}  
						],  
						"role": null,  
						"title": null  
					},  
					"events_actor": null,  
					"entities": null  
				}  
			},  
			"raw": null  
		}  
	}  
]
```



#### Enrich Entity With Field
The action adds enrichment fields to the entity based on a list of key values 
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fields to enrich|Takes a list of key/value pairs and enriches the entity with that data. Can be used to add multiple static values easily.|True|String|[   {     "entity_field_name": "Title",     "entity_field_value": "SalseManager"   },   {     "entity_field_name": "City",     "entity_field_value": "NewYork"   } ]|



##### JSON Results
```json
{}
```



#### Enrich Entities from List with Field
This action enriches entities supplied by a list with a field and a value.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|List of Entities|A list of entities of the same type, delimited by a field.|True|String||
|Entity Type|The type of entity.|True|String| |
|Entity Delimiter|The value of the field that is delimiting the list of entities.|True|String|,|
|Enrichment Field|The name of the field that will be added to the entity.|True|String| |
|Enrichment Value|The value of the field that will be enriched to the entity.|True|String| |



##### JSON Results
```json
{}
```



#### Enrich Entity From Event Field
The action extracts fields from the event and adds them to the Entity fields
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fields to enrich|The name of the fields in the event that will be used to enrich the entity.  Supports comma separated list.|True|String|field_name_1,field_name_2|



##### JSON Results
```json
{  
  "user label": "SiemplifyTest",  
  "user email": "siemplifytest@siemplify.co"  
}
```






## Jobs



## Connectors


