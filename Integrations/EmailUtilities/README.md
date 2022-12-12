
# EmailUtilities

A set of utility actions to assist with working with emails.  Includes actions to parse EMLs and analyze email headers.

Python Version - 2



## Actions
#### Analyze Headers
Analyze Headers accepts a JSON object containing a list of Email headers.  The action will validate the SPF, DMARC, ARC, and DKIM records in the email.  It will also check to see if any of the relay servers are blacklisted by querying multiple RBLs and enrich them with geo-location and IP whois information.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Headers JSON|The JSON object that contains the email headers.|True|String|{}|



##### JSON Results
```json
{  
    "ARCVerify": {  
        "details": [],  
        "reason": "Message is not ARC signed",  
        "result": "none"  
    },  
    "DKIMVerify": false,  
    "DMARC": {  
        "location": "siemplify.co",  
        "record": "v=DMARC1; p=quarantine; rua=mailto:postmaster@siemplify.co,mailto:y7c5gybh11g81e1c@securemailanalytics.com; ruf=mailto:postmaster@siemplify.co,mailto:x34spt4wbipf9u91@securemailanalytics.com; fo=1;",  
        "tags": {  
            "adkim": {  
                "default": "r",  
                "description": "In relaxed mode, the Organizational Domains of both the DKIM-authenticated signing domain (taken from the value of the \"d=\" tag in the signature) and that of the RFC 5322 From domain must be equal if the identifiers are to be considered aligned.",  
                "explicit": false,  
                "name": "DKIM Alignment Mode",  
                "value": "r"  
            },  
            "aspf": {  
                "default": "r",  
                "description": "In relaxed mode, the SPF-authenticated domain and RFC5322 From domain must have the same Organizational Domain. In strict mode, only an exact DNS domain match is considered to produce Identifier Alignment.",  
                "explicit": false,  
                "name": "SPF alignment mode",  
                "value": "r"  
            },  
            "fo": {  
                "default": "0",  
                "description": "1: Generate a DMARC failure report if any underlying authentication mechanism produced something other than an aligned \"pass\" result.",  
                "explicit": true,  
                "name": "Failure Reporting Options",  
                "value": [  
                    "1"  
                ]  
            },  
            "p": {  
                "description": "Specifies the policy to be enacted by the Receiver at the request of the Domain Owner. The policy applies to the domain and to its subdomains, unless subdomain policy is explicitly described using the \"sp\" tag.",  
                "explicit": true,  
                "name": "Requested Mail Receiver Policy",  
                "value": "quarantine"  
            },  
            "pct": {  
                "default": 100,  
                "description": "Integer percentage of messages from the Domain Owner's mail stream to which the DMARC policy is to be applied. However, this MUST NOT be applied to the DMARC-generated reports, all of which must be sent and received unhindered. The purpose of the \"pct\" tag is to allow Domain Owners to enact a slow rollout of enforcement of the DMARC mechanism.",  
                "explicit": false,  
                "name": "Percentage",  
                "value": 100  
            },  
            "rf": {  
                "default": "afrf",  
                "description": "afrf:  \"Authentication Failure Reporting Using the Abuse Reporting Format\", RFC 6591, April 2012,<http://www.rfc-editor.org/info/rfc6591>",  
                "explicit": false,  
                "name": "Report Format",  
                "value": [  
                    "afrf"  
                ]  
            },  
            "ri": {  
                "default": 86400,  
                "description": "Indicates a request to Receivers to generate aggregate reports separated by no more than the requested number of seconds. DMARC implementations MUST be able to provide daily reports and SHOULD be able to provide hourly reports when requested. However, anything other than a daily report is understood to be accommodated on a best-effort basis.",  
                "explicit": false,  
                "name": "Report Interval",  
                "value": 86400  
            },  
            "rua": {  
                "description": " A comma-separated list of DMARC URIs to which aggregate feedback is to be sent.",  
                "explicit": true,  
                "name": "Aggregate Feedback Addresses",  
                "value": [  
                    {  
                        "address": "postmaster@siemplify.co",  
                        "scheme": "mailto",  
                        "size_limit": null  
                    },  
                    {  
                        "address": "y7c5gybh11g81e1c@securemailanalytics.com",  
                        "scheme": "mailto",  
                        "size_limit": null  
                    }  
                ]  
            },  
            "ruf": {  
                "description": " A comma-separated list of DMARC URIs to which forensic feedback is to be sent.",  
                "explicit": true,  
                "name": "Forensic Feedback Addresses",  
                "value": [  
                    {  
                        "address": "postmaster@siemplify.co",  
                        "scheme": "mailto",  
                        "size_limit": null  
                    },  
                    {  
                        "address": "x34spt4wbipf9u91@securemailanalytics.com",  
                        "scheme": "mailto",  
                        "size_limit": null  
                    }  
                ]  
            },  
            "sp": {  
                "description": "Indicates the policy to be enacted by the Receiver at the request of the Domain Owner. It applies only to subdomains of the domain queried, and not to the domain itself. Its syntax is identical to that of the \"p\" tag defined above. If absent, the policy specified by the \"p\" tag MUST be applied for subdomains.",  
                "explicit": false,  
                "name": "Subdomain Policy",  
                "value": "quarantine"  
            },  
            "v": {  
                "description": "Identifies the record retrieved as a DMARC record. It MUST have the value of \"DMARC1\". The value of this tag MUST match precisely; if it does not or it is absent, the entire retrieved record MUST be ignored. It MUST be the first tag in the list.",  
                "explicit": true,  
                "name": "Version",  
                "value": "DMARC1"  
            }  
        },  
        "valid": true,  
        "warnings": []  
    },  
    "DNSSec": false,  
    "Date": "Thu, 03 Feb 2022 14:28:59 -0500",  
    "DmarcDomain": "siemplify.co",  
    "From": "string",  
    "FromDomain": "siemplify.co",  
    "FromParentDomain": "siemplify.co",  
    "MFromDomain": "siemplify.co",  
    "MX": {  
        "hosts": [  
            {  
                "addresses": [  
                    "44.196.125.110",  
                    "44.198.0.192",  
                    "52.72.180.143"  
                ],  
                "hostname": "mailstream-east.mxrecord.io",  
                "preference": 10,  
                "starttls": false,  
                "tls": false  
            },  
            {  
                "addresses": [  
                    "34.216.5.229",  
                    "35.164.179.171",  
                    "54.191.239.242"  
                ],  
                "hostname": "mailstream-west.mxrecord.io",  
                "preference": 10,  
                "starttls": false,  
                "tls": false  
            }  
        ],  
        "warnings": [  
            "mailstream-east.mxrecord.io: Connection timed out",  
            "mailstream-west.mxrecord.io: Connection timed out"  
        ]  
    },  
    "MessageID": "string",  
    "RelayInfo": [  
        {  
            "blacklist_info": [],  
            "blacklisted": false,  
            "by": "mail-ej1-f44.google.com",  
            "by_ip_whois": {  
                "asn": "15169",  
                "asn_cidr": "209.85.128.0/17",  
                "asn_country_code": "US",  
                "asn_date": "2006-01-13",  
                "asn_description": "GOOGLE, US",  
                "asn_registry": "arin",  
                "entities": [  
                    "GOGL"  
                ],  
                "network": {  
                    "cidr": "209.85.128.0/17",  
                    "country": null,  
                    "end_address": "209.85.255.255",  
                    "events": [  
                        {  
                            "action": "last changed",  
                            "actor": null,  
                            "timestamp": "2012-02-24T09:44:34-05:00"  
                        },  
                        {  
                            "action": "registration",  
                            "actor": null,  
                            "timestamp": "2006-01-13T13:42:45-05:00"  
                        }  
                    ],  
                    "handle": "NET-209-85-128-0-1",  
                    "ip_version": "v4",  
                    "links": [  
                        "https://rdap.arin.net/registry/ip/209.85.128.0",  
                        "https://whois.arin.net/rest/net/NET-209-85-128-0-1"  
                    ],  
                    "name": "GOOGLE",  
                    "notices": [  
                        {  
                            "description": "By using the ARIN RDAP/Whois service, you are agreeing to the RDAP/Whois Terms of Use",  
                            "links": [  
                                "https://www.arin.net/resources/registry/whois/tou/"  
                            ],  
                            "title": "Terms of Service"  
                        },  
                        {  
                            "description": "If you see inaccuracies in the results, please visit: ",  
                            "links": [  
                                "https://www.arin.net/resources/registry/whois/inaccuracy_reporting/"  
                            ],  
                            "title": "Whois Inaccuracy Reporting"  
                        },  
                        {  
                            "description": "Copyright 1997-2022, American Registry for Internet Numbers, Ltd.",  
                            "links": null,  
                            "title": "Copyright Notice"  
                        }  
                    ],  
                    "parent_handle": "NET-209-0-0-0-0",  
                    "raw": null,  
                    "remarks": null,  
                    "start_address": "209.85.128.0",  
                    "status": [  
                        "active"  
                    ],  
                    "type": "DIRECT ALLOCATION"  
                },  
                "nir": null,  
                "objects": {  
                    "ABUSE5250-ARIN": {  
                        "contact": {  
                            "address": [  
                                {  
                                    "type": null,  
                                    "value": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States"  
                                }  
                            ],  
                            "email": [  
                                {  
                                    "type": null,  
                                    "value": "network-abuse@google.com"  
                                }  
                            ],  
                            "kind": "group",  
                            "name": "Abuse",  
                            "phone": [  
                                {  
                                    "type": [  
                                        "work",  
                                        "voice"  
                                    ],  
                                    "value": "+1-650-253-0000"  
                                }  
                            ],  
                            "role": null,  
                            "title": null  
                        },  
                        "entities": null,  
                        "events": [  
                            {  
                                "action": "last changed",  
                                "actor": null,  
                                "timestamp": "2018-10-24T11:23:55-04:00"  
                            },  
                            {  
                                "action": "registration",  
                                "actor": null,  
                                "timestamp": "2015-11-06T15:36:35-05:00"  
                            }  
                        ],  
                        "events_actor": null,  
                        "handle": "ABUSE5250-ARIN",  
                        "links": [  
                            "https://rdap.arin.net/registry/entity/ABUSE5250-ARIN",  
                            "https://whois.arin.net/rest/poc/ABUSE5250-ARIN"  
                        ],  
                        "notices": [  
                            {  
                                "description": "By using the ARIN RDAP/Whois service, you are agreeing to the RDAP/Whois Terms of Use",  
                                "links": [  
                                    "https://www.arin.net/resources/registry/whois/tou/"  
                                ],  
                                "title": "Terms of Service"  
                            },  
                            {  
                                "description": "If you see inaccuracies in the results, please visit: ",  
                                "links": [  
                                    "https://www.arin.net/resources/registry/whois/inaccuracy_reporting/"  
                                ],  
                                "title": "Whois Inaccuracy Reporting"  
                            },  
                            {  
                                "description": "Copyright 1997-2022, American Registry for Internet Numbers, Ltd.",  
                                "links": null,  
                                "title": "Copyright Notice"  
                            }  
                        ],  
                        "raw": null,  
                        "remarks": [  
                            {  
                                "description": "Please note that the recommended way to file abuse complaints are located in the following links.\n\nTo report abuse and illegal activity: https://www.google.com/contact/\n\nFor legal requests: http://support.google.com/legal \n\nRegards,\nThe Google Team",  
                                "links": null,  
                                "title": "Registration Comments"  
                            },  
                            {  
                                "description": "ARIN has attempted to validate the data for this POC, but has received no response from the POC since 2019-10-24",  
                                "links": null,  
                                "title": "Unvalidated POC"  
                            }  
                        ],  
                        "roles": [  
                            "abuse"  
                        ],  
                        "status": null  
                    },  
                    "GOGL": {  
                        "contact": {  
                            "address": [  
                                {  
                                    "type": null,  
                                    "value": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States"  
                                }  
                            ],  
                            "email": null,  
                            "kind": "org",  
                            "name": "Google LLC",  
                            "phone": null,  
                            "role": null,  
                            "title": null  
                        },  
                        "entities": [  
                            "ABUSE5250-ARIN",  
                            "ZG39-ARIN"  
                        ],  
                        "events": [  
                            {  
                                "action": "last changed",  
                                "actor": null,  
                                "timestamp": "2019-10-31T15:45:45-04:00"  
                            },  
                            {  
                                "action": "registration",  
                                "actor": null,  
                                "timestamp": "2000-03-30T00:00:00-05:00"  
                            }  
                        ],  
                        "events_actor": null,  
                        "handle": "GOGL",  
                        "links": [  
                            "https://rdap.arin.net/registry/entity/GOGL",  
                            "https://whois.arin.net/rest/org/GOGL"  
                        ],  
                        "notices": null,  
                        "raw": null,  
                        "remarks": [  
                            {  
                                "description": "Please note that the recommended way to file abuse complaints are located in the following links. \n\nTo report abuse and illegal activity: https://www.google.com/contact/\n\nFor legal requests: http://support.google.com/legal \n\nRegards, \nThe Google Team",  
                                "links": null,  
                                "title": "Registration Comments"  
                            }  
                        ],  
                        "roles": [  
                            "registrant"  
                        ],  
                        "status": null  
                    },  
                    "ZG39-ARIN": {  
                        "contact": {  
                            "address": [  
                                {  
                                    "type": null,  
                                    "value": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States"  
                                }  
                            ],  
                            "email": [  
                                {  
                                    "type": null,  
                                    "value": "arin-contact@google.com"  
                                }  
                            ],  
                            "kind": "group",  
                            "name": "Google LLC",  
                            "phone": [  
                                {  
                                    "type": [  
                                        "work",  
                                        "voice"  
                                    ],  
                                    "value": "+1-650-253-0000"  
                                }  
                            ],  
                            "role": null,  
                            "title": null  
                        },  
                        "entities": null,  
                        "events": [  
                            {  
                                "action": "last changed",  
                                "actor": null,  
                                "timestamp": "2021-11-10T10:26:54-05:00"  
                            },  
                            {  
                                "action": "registration",  
                                "actor": null,  
                                "timestamp": "2000-11-30T13:54:08-05:00"  
                            }  
                        ],  
                        "events_actor": null,  
                        "handle": "ZG39-ARIN",  
                        "links": [  
                            "https://rdap.arin.net/registry/entity/ZG39-ARIN",  
                            "https://whois.arin.net/rest/poc/ZG39-ARIN"  
                        ],  
                        "notices": [  
                            {  
                                "description": "By using the ARIN RDAP/Whois service, you are agreeing to the RDAP/Whois Terms of Use",  
                                "links": [  
                                    "https://www.arin.net/resources/registry/whois/tou/"  
                                ],  
                                "title": "Terms of Service"  
                            },  
                            {  
                                "description": "If you see inaccuracies in the results, please visit: ",  
                                "links": [  
                                    "https://www.arin.net/resources/registry/whois/inaccuracy_reporting/"  
                                ],  
                                "title": "Whois Inaccuracy Reporting"  
                            },  
                            {  
                                "description": "Copyright 1997-2022, American Registry for Internet Numbers, Ltd.",  
                                "links": null,  
                                "title": "Copyright Notice"  
                            }  
                        ],  
                        "raw": null,  
                        "remarks": null,  
                        "roles": [  
                            "technical",  
                            "administrative"  
                        ],  
                        "status": [  
                            "validated"  
                        ]  
                    }  
                },  
                "query": "209.85.218.44",  
                "raw": null  
            },  
            "date": "2022-02-03 11:29:11-08:00",  
            "delay": "*",  
            "from": "",  
            "from_ip_whois": {},  
            "time": "2022-02-03 19:29:11",  
            "with": "smtp"  
        },  
        {  
            "blacklist_info": [  
                {  
                    "blacklisted": true,  
                    "categories": "{'unknown'}",  
                    "detected_by": {  
                        "dnsbl.sorbs.net": [  
                            "unknown"  
                        ],  
                        "spam.dnsbl.sorbs.net": [  
                            "unknown"  
                        ]  
                    }  
                },  
                {  
                    "blacklisted": false,  
                    "categories": "set()",  
                    "detected_by": {}  
                }  
            ],  
            "blacklisted": true,  
            "by": "10.197.37.9",  
            "by_ip_whois": {},  
            "date": "2022-02-03 19:29:12+00:00",  
            "delay": 1.0,  
            "from": "mail-ej1-f44.google.com",  
            "from_geo": {  
                "city": "Mountain View",  
                "country": "US",  
                "ip_address": "209.85.218.44",  
                "latitude": 37.3893889,  
                "longitude": -122.0832101,  
                "region": "California"  
            },  
            "from_ip_whois": {  
                "asn": "15169",  
                "asn_cidr": "209.85.128.0/17",  
                "asn_country_code": "US",  
                "asn_date": "2006-01-13",  
                "asn_description": "GOOGLE, US",  
                "asn_registry": "arin",  
                "entities": [  
                    "GOGL"  
                ],  
                "network": {  
                    "cidr": "209.85.128.0/17",  
                    "country": null,  
                    "end_address": "209.85.255.255",  
                    "events": [  
                        {  
                            "action": "last changed",  
                            "actor": null,  
                            "timestamp": "2012-02-24T09:44:34-05:00"  
                        },  
                        {  
                            "action": "registration",  
                            "actor": null,  
                            "timestamp": "2006-01-13T13:42:45-05:00"  
                        }  
                    ],  
                    "handle": "NET-209-85-128-0-1",  
                    "ip_version": "v4",  
                    "links": [  
                        "https://rdap.arin.net/registry/ip/209.85.128.0",  
                        "https://whois.arin.net/rest/net/NET-209-85-128-0-1"  
                    ],  
                    "name": "GOOGLE",  
                    "notices": [  
                        {  
                            "description": "By using the ARIN RDAP/Whois service, you are agreeing to the RDAP/Whois Terms of Use",  
                            "links": [  
                                "https://www.arin.net/resources/registry/whois/tou/"  
                            ],  
                            "title": "Terms of Service"  
                        },  
                        {  
                            "description": "If you see inaccuracies in the results, please visit: ",  
                            "links": [  
                                "https://www.arin.net/resources/registry/whois/inaccuracy_reporting/"  
                            ],  
                            "title": "Whois Inaccuracy Reporting"  
                        },  
                        {  
                            "description": "Copyright 1997-2022, American Registry for Internet Numbers, Ltd.",  
                            "links": null,  
                            "title": "Copyright Notice"  
                        }  
                    ],  
                    "parent_handle": "NET-209-0-0-0-0",  
                    "raw": null,  
                    "remarks": null,  
                    "start_address": "209.85.128.0",  
                    "status": [  
                        "active"  
                    ],  
                    "type": "DIRECT ALLOCATION"  
                },  
                "nir": null,  
                "objects": {  
                    "ABUSE5250-ARIN": {  
                        "contact": {  
                            "address": [  
                                {  
                                    "type": null,  
                                    "value": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States"  
                                }  
                            ],  
                            "email": [  
                                {  
                                    "type": null,  
                                    "value": "network-abuse@google.com"  
                                }  
                            ],  
                            "kind": "group",  
                            "name": "Abuse",  
                            "phone": [  
                                {  
                                    "type": [  
                                        "work",  
                                        "voice"  
                                    ],  
                                    "value": "+1-650-253-0000"  
                                }  
                            ],  
                            "role": null,  
                            "title": null  
                        },  
                        "entities": null,  
                        "events": [  
                            {  
                                "action": "last changed",  
                                "actor": null,  
                                "timestamp": "2018-10-24T11:23:55-04:00"  
                            },  
                            {  
                                "action": "registration",  
                                "actor": null,  
                                "timestamp": "2015-11-06T15:36:35-05:00"  
                            }  
                        ],  
                        "events_actor": null,  
                        "handle": "ABUSE5250-ARIN",  
                        "links": [  
                            "https://rdap.arin.net/registry/entity/ABUSE5250-ARIN",  
                            "https://whois.arin.net/rest/poc/ABUSE5250-ARIN"  
                        ],  
                        "notices": [  
                            {  
                                "description": "By using the ARIN RDAP/Whois service, you are agreeing to the RDAP/Whois Terms of Use",  
                                "links": [  
                                    "https://www.arin.net/resources/registry/whois/tou/"  
                                ],  
                                "title": "Terms of Service"  
                            },  
                            {  
                                "description": "If you see inaccuracies in the results, please visit: ",  
                                "links": [  
                                    "https://www.arin.net/resources/registry/whois/inaccuracy_reporting/"  
                                ],  
                                "title": "Whois Inaccuracy Reporting"  
                            },  
                            {  
                                "description": "Copyright 1997-2022, American Registry for Internet Numbers, Ltd.",  
                                "links": null,  
                                "title": "Copyright Notice"  
                            }  
                        ],  
                        "raw": null,  
                        "remarks": [  
                            {  
                                "description": "Please note that the recommended way to file abuse complaints are located in the following links.\n\nTo report abuse and illegal activity: https://www.google.com/contact/\n\nFor legal requests: http://support.google.com/legal \n\nRegards,\nThe Google Team",  
                                "links": null,  
                                "title": "Registration Comments"  
                            },  
                            {  
                                "description": "ARIN has attempted to validate the data for this POC, but has received no response from the POC since 2019-10-24",  
                                "links": null,  
                                "title": "Unvalidated POC"  
                            }  
                        ],  
                        "roles": [  
                            "abuse"  
                        ],  
                        "status": null  
                    },  
                    "GOGL": {  
                        "contact": {  
                            "address": [  
                                {  
                                    "type": null,  
                                    "value": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States"  
                                }  
                            ],  
                            "email": null,  
                            "kind": "org",  
                            "name": "Google LLC",  
                            "phone": null,  
                            "role": null,  
                            "title": null  
                        },  
                        "entities": [  
                            "ABUSE5250-ARIN",  
                            "ZG39-ARIN"  
                        ],  
                        "events": [  
                            {  
                                "action": "last changed",  
                                "actor": null,  
                                "timestamp": "2019-10-31T15:45:45-04:00"  
                            },  
                            {  
                                "action": "registration",  
                                "actor": null,  
                                "timestamp": "2000-03-30T00:00:00-05:00"  
                            }  
                        ],  
                        "events_actor": null,  
                        "handle": "GOGL",  
                        "links": [  
                            "https://rdap.arin.net/registry/entity/GOGL",  
                            "https://whois.arin.net/rest/org/GOGL"  
                        ],  
                        "notices": null,  
                        "raw": null,  
                        "remarks": [  
                            {  
                                "description": "Please note that the recommended way to file abuse complaints are located in the following links. \n\nTo report abuse and illegal activity: https://www.google.com/contact/\n\nFor legal requests: http://support.google.com/legal \n\nRegards, \nThe Google Team",  
                                "links": null,  
                                "title": "Registration Comments"  
                            }  
                        ],  
                        "roles": [  
                            "registrant"  
                        ],  
                        "status": null  
                    },  
                    "ZG39-ARIN": {  
                        "contact": {  
                            "address": [  
                                {  
                                    "type": null,  
                                    "value": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States"  
                                }  
                            ],  
                            "email": [  
                                {  
                                    "type": null,  
                                    "value": "arin-contact@google.com"  
                                }  
                            ],  
                            "kind": "group",  
                            "name": "Google LLC",  
                            "phone": [  
                                {  
                                    "type": [  
                                        "work",  
                                        "voice"  
                                    ],  
                                    "value": "+1-650-253-0000"  
                                }  
                            ],  
                            "role": null,  
                            "title": null  
                        },  
                        "entities": null,  
                        "events": [  
                            {  
                                "action": "last changed",  
                                "actor": null,  
                                "timestamp": "2021-11-10T10:26:54-05:00"  
                            },  
                            {  
                                "action": "registration",  
                                "actor": null,  
                                "timestamp": "2000-11-30T13:54:08-05:00"  
                            }  
                        ],  
                        "events_actor": null,  
                        "handle": "ZG39-ARIN",  
                        "links": [  
                            "https://rdap.arin.net/registry/entity/ZG39-ARIN",  
                            "https://whois.arin.net/rest/poc/ZG39-ARIN"  
                        ],  
                        "notices": [  
                            {  
                                "description": "By using the ARIN RDAP/Whois service, you are agreeing to the RDAP/Whois Terms of Use",  
                                "links": [  
                                    "https://www.arin.net/resources/registry/whois/tou/"  
                                ],  
                                "title": "Terms of Service"  
                            },  
                            {  
                                "description": "If you see inaccuracies in the results, please visit: ",  
                                "links": [  
                                    "https://www.arin.net/resources/registry/whois/inaccuracy_reporting/"  
                                ],  
                                "title": "Whois Inaccuracy Reporting"  
                            },  
                            {  
                                "description": "Copyright 1997-2022, American Registry for Internet Numbers, Ltd.",  
                                "links": null,  
                                "title": "Copyright Notice"  
                            }  
                        ],  
                        "raw": null,  
                        "remarks": null,  
                        "roles": [  
                            "technical",  
                            "administrative"  
                        ],  
                        "status": [  
                            "validated"  
                        ]  
                    }  
                },  
                "query": "209.85.218.44",  
                "raw": null  
            },  
            "time": "2022-02-03 19:29:12",  
            "with": "smtps"  
        },  
        {  
            "blacklist_info": [  
                {  
                    "blacklisted": true,  
                    "categories": "{'unknown'}",  
                    "detected_by": {  
                        "bogons.cymru.com": [  
                            "unknown"  
                        ],  
                        "spambot.bls.digibase.ca": [  
                            "unknown"  
                        ]  
                    }  
                }  
            ],  
            "blacklisted": true,  
            "by": "atlas306.free.mail.bf1.yahoo.com",  
            "by_ip_whois": {},  
            "date": "2022-02-03 19:29:12+00:00",  
            "delay": 0.0,  
            "from": "10.197.37.9",  
            "from_ip_whois": {},  
            "time": "2022-02-03 19:29:12",  
            "with": "https"  
        }  
    ],  
    "SPF": {  
        "Auth": false,  
        "dns_lookups": 11,  
        "error": "Parsing the SPF record requires 11/10 maximum DNS lookups - https://tools.ietf.org/html/rfc7208#section-4.6.4",  
        "record": "v=spf1 a include:_spf.google.com include:mktomail.com include:mail.zendesk.com include:_spf.salesforce.com include:_spf.atlassian.net include:sent-via.netsuite.com ~all",  
        "valid": false,  
        "warnings": []  
    },  
    "SPFDomain": "siemplify.co",  
    "SourceServer": "atlas306.free.mail.bf1.yahoo.com",  
    "SourceServerIP": "10.197.37.9",  
    "StrongSPF": true,  
    "Subject": "string",  
    "To": "string"  
}
```



#### Parse Base64 Email
This action is an improved version of Parse EML Base64 blob.  It will parse EML and MSG files.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Stop Transport At Header|Stop processing the transport at this header field.|False|String|None|
|EML/MSG Base64 String|The base64 representation of an EML or MSG file.|True|Content|<insert base64 string>|
|Blacklisted Headers|Headers to exclude from the response.|False|String|None|
|Use Blacklist As Whitelist|To only include the listed headers.|False|Boolean|false|



##### JSON Results
```json
{  
    "attached_emails": [  
        {  
            "email": {  
                "body": [  
                    {  
                        "content": "string",  
                        "content_header": {  
                            "content-transfer-encoding": [  
                                "string"  
                            ],  
                            "content-type": [  
                                "string"  
                            ]  
                        },  
                        "content_type": "string",  
                        "domain": [  
                            "string"  
                        ],  
                        "email": [  
                            "string"  
                        ],  
                        "hash": "string"  
                    }  
                ],  
                "filename": "string",  
                "header": {  
                    "date": "string",  
                    "from": "string",  
                    "header": {  
                        "accept-language": [  
                            "string"  
                        ],  
                        "authentication-results": [  
                            "string"  
                        ],  
                        "content-language": [  
                            "string"  
                        ],  
                        "content-transfer-encoding": [  
                            "string"  
                        ],  
                        "content-type": [  
                            "string"  
                        ],  
                        "date": [  
                            "string"  
                        ],  
                        "from": [  
                            "string"  
                        ],  
                        "message-id": [  
                            "string"  
                        ],  
                        "mime-version": [  
                            "string"  
                        ],  
                        "received": [  
                            "string"  
                        ],  
                        "return-path": [  
                            "string"  
                        ],  
                        "subject": [  
                            "string"  
                        ],  
                        "thread-index": [  
                            "string"  
                        ],  
                        "thread-topic": [  
                            "string"  
                        ],  
                        "to": [  
                            "string"  
                        ],  
                        "x-forefront-antispam-report": [  
                            "string"  
                        ],  
                        "x-microsoft-antispam": [  
                            "string"  
                        ],  
                        "x-microsoft-antispam-mailbox-delivery": [  
                            "string"  
                        ],  
                        "x-microsoft-antispam-message-info": [  
                            "string"  
                        ],  
                        "x-ms-exchange-antispam-messagedata": [  
                            "string"  
                        ],  
                        "x-ms-exchange-crosstenant-authas": [  
                            "string"  
                        ],  
                        "x-ms-exchange-crosstenant-authsource": [  
                            "string"  
                        ],  
                        "x-ms-exchange-crosstenant-fromentityheader": [  
                            "string"  
                        ],  
                        "x-ms-exchange-crosstenant-id": [  
                            "string"  
                        ],  
                        "x-ms-exchange-crosstenant-mailboxtype": [  
                            "string"  
                        ],  
                        "x-ms-exchange-crosstenant-network-message-id": [  
                            "string"  
                        ],  
                        "x-ms-exchange-crosstenant-originalarrivaltime": [  
                            "string"  
                        ],  
                        "x-ms-exchange-crosstenant-userprincipalname": [  
                            "string"  
                        ],  
                        "x-ms-exchange-organization-authas": [  
                            "string"  
                        ],  
                        "x-ms-exchange-organization-authmechanism": [  
                            "string"  
                        ],  
                        "x-ms-exchange-organization-authsource": [  
                            "string"  
                        ],  
                        "x-ms-exchange-organization-expirationinterval": [  
                            "string"  
                        ],  
                        "x-ms-exchange-organization-expirationintervalreason": [  
                            "string"  
                        ],  
                        "x-ms-exchange-organization-expirationstarttime": [  
                            "string"  
                        ],  
                        "x-ms-exchange-organization-expirationstarttimereason": [  
                            "string"  
                        ],  
                        "x-ms-exchange-organization-messagedirectionality": [  
                            "string"  
                        ],  
                        "x-ms-exchange-organization-network-message-id": [  
                            "string"  
                        ],  
                        "x-ms-exchange-organization-scl": [  
                            "string"  
                        ],  
                        "x-ms-exchange-processed-by-bccfoldering": [  
                            "string"  
                        ],  
                        "x-ms-exchange-transport-crosstenantheadersstamped": [  
                            "string"  
                        ],  
                        "x-ms-exchange-transport-endtoendlatency": [  
                            "string"  
                        ],  
                        "x-ms-office365-filtering-correlation-id": [  
                            "string"  
                        ],  
                        "x-ms-oob-tlc-oobclassifiers": [  
                            "string"  
                        ],  
                        "x-ms-publictraffictype": [  
                            "string"  
                        ],  
                        "x-ms-tnef-correlator": [  
                            "string"  
                        ],  
                        "x-ms-traffictypediagnostic": [  
                            "string"  
                        ],  
                        "x-originating-ip": [  
                            "string"  
                        ]  
                    },  
                    "received": [  
                        {  
                            "by": [  
                                "string"  
                            ],  
                            "date": "string",  
                            "from": [  
                                "string"  
                            ],  
                            "src": "string",  
                            "with": "string"  
                        }  
                    ],  
                    "received_domain": [  
                        "string"  
                    ],  
                    "received_domains_internal": [],  
                    "received_ip": [  
                        "string"  
                    ],  
                    "receiving": [  
                        {  
                            "domains": [  
                                "string"  
                            ],  
                            "emails": [],  
                            "hosts": [  
                                "string"  
                            ],  
                            "ips": []  
                        },  
                        {  
                            "domains": [  
                                "string"  
                            ],  
                            "emails": [],  
                            "hosts": [  
                                "string"  
                            ],  
                            "ips": [  
                                "string"  
                            ]  
                        }  
                    ],  
                    "sending": [  
                        {  
                            "domains": [  
                                "string"  
                            ],  
                            "emails": [],  
                            "hosts": [  
                                "string"  
                            ],  
                            "ips": [  
                                "string"  
                            ]  
                        },  
                        {  
                            "domains": [  
                                "string"  
                            ],  
                            "emails": [],  
                            "hosts": [  
                                "string"  
                            ],  
                            "ips": []  
                        }  
                    ],  
                    "subject": "string",  
                    "to": [  
                        "string"  
                    ]  
                }  
            },  
            "filename": "string"  
        }  
    ],  
    "attachments": [  
        {  
            "content_header": {  
                "content-description": [  
                    "string"  
                ],  
                "content-disposition": [  
                    "string"  
                ],  
                "content-transfer-encoding": [  
                    "string"  
                ],  
                "content-type": [  
                    "string"  
                ]  
            },  
            "extension": "string",  
            "filename": "string",  
            "hash": {  
                "md5": "string",  
                "sha1": "string",  
                "sha256": "string",  
                "sha512": "string"  
            },  
            "raw": "string",  
            "size": 1111,  
            "subject": "string"  
        }  
    ],  
    "body": [  
        {  
            "content": "string",  
            "content_header": {  
                "content-transfer-encoding": [  
                    "string"  
                ],  
                "content-type": [  
                    "string"  
                ]  
            },  
            "content_type": "string",  
            "domain": [  
                "string"  
            ],  
            "email": [  
                "string"  
            ],  
            "hash": "string",  
            "uri": [  
                "string"  
            ]  
        },  
        {  
            "content": "string",  
            "content_header": {  
                "content-transfer-encoding": [  
                    "string"  
                ],  
                "content-type": [  
                    "string"  
                ]  
            },  
            "content_type": "string",  
            "domain": [  
                "string"  
            ],  
            "email": [  
                "string"  
            ],  
            "hash": "string"  
        }  
    ],  
    "domains": [  
        "string"  
    ],  
    "emails": [  
        "string"  
    ],  
    "header": {  
        "date": "string",  
        "from": "string",  
        "header": {  
            "accept-language": [  
                "string"  
            ],  
            "authentication-results": [  
                "string"  
            ],  
            "content-language": [  
                "string"  
            ],  
            "content-type": [  
                "string"  
            ],  
            "date": [  
                "string"  
            ],  
            "from": [  
                "string"  
            ],  
            "message-id": [  
                "string"  
            ],  
            "mime-version": [  
                "string"  
            ],  
            "received": [  
                "string"  
            ],  
            "subject": [  
                "string"  
            ],  
            "thread-index": [  
                "string"  
            ],  
            "thread-topic": [  
                "string"  
            ],  
            "to": [  
                "string"  
            ],  
            "x-forefront-antispam-report": [  
                "string"  
            ],  
            "x-microsoft-antispam": [  
                "string"  
            ],  
            "x-microsoft-antispam-mailbox-delivery": [  
                "string"  
            ],  
            "x-microsoft-antispam-message-info": [  
                "string"  
            ],  
            "x-ms-exchange-antispam-messagedata": [  
                "string"  
            ],  
            "x-ms-exchange-crosstenant-authas": [  
                "string"  
            ],  
            "x-ms-exchange-crosstenant-authsource": [  
                "string"  
            ],  
            "x-ms-exchange-crosstenant-fromentityheader": [  
                "string"  
            ],  
            "x-ms-exchange-crosstenant-id": [  
                "string"  
            ],  
            "x-ms-exchange-crosstenant-mailboxtype": [  
                "string"  
            ],  
            "x-ms-exchange-crosstenant-network-message-id": [  
                "string"  
            ],  
            "x-ms-exchange-crosstenant-originalarrivaltime": [  
                "string"  
            ],  
            "x-ms-exchange-crosstenant-userprincipalname": [  
                "string"  
            ],  
            "x-ms-exchange-organization-authmechanism": [  
                "string"  
            ],  
            "x-ms-exchange-organization-authsource": [  
                "string"  
            ],  
            "x-ms-exchange-organization-compliancelabelid": [  
                "string"  
            ],  
            "x-ms-exchange-organization-network-message-id": [  
                "string"  
            ],  
            "x-ms-exchange-organization-originalclientipaddress": [  
                "string"  
            ],  
            "x-ms-exchange-organization-originalserveripaddress": [  
                "string"  
            ],  
            "x-ms-exchange-organization-recordreviewcfmtype": [  
                "string"  
            ],  
            "x-ms-exchange-organization-submissionquotaskipped": [  
                "string"  
            ],  
            "x-ms-exchange-processed-by-bccfoldering": [  
                "string"  
            ],  
            "x-ms-exchange-transport-crosstenantheadersstamped": [  
                "string"  
            ],  
            "x-ms-exchange-transport-endtoendlatency": [  
                "string"  
            ],  
            "x-ms-has-attach": [  
                "string"  
            ],  
            "x-ms-office365-filtering-correlation-id": [  
                "string"  
            ],  
            "x-ms-oob-tlc-oobclassifiers": [  
                "string"  
            ],  
            "x-ms-publictraffictype": [  
                "string"  
            ],  
            "x-ms-traffictypediagnostic": [  
                "string"  
            ],  
            "x-originating-ip": [  
                "string"  
            ]  
        },  
        "received": [  
            {  
                "by": [  
                    "string"  
                ],  
                "date": "string",  
                "from": [  
                    "string"  
                ],  
                "src": "string",  
                "with": "string"  
            }  
        ],  
        "received_domain": [  
            "string"  
        ],  
        "received_domains_internal": [],  
        "received_ip": [  
            "string"  
        ],  
        "receiving": [  
            {  
                "domains": [  
                    "string"  
                ],  
                "emails": [],  
                "hosts": [  
                    "string"  
                ],  
                "ips": []  
            },  
            {  
                "domains": [  
                    "string"  
                ],  
                "emails": [],  
                "hosts": [  
                    "string"  
                ],  
                "ips": [  
                    "string"  
                ]  
            }  
        ],  
        "sending": [  
            {  
                "domains": [  
                    "string"  
                ],  
                "emails": [],  
                "hosts": [  
                    "string"  
                ],  
                "ips": [  
                    "string"  
                ]  
            },  
            {  
                "domains": [  
                    "string"  
                ],  
                "emails": [],  
                "hosts": [  
                    "string"  
                ],  
                "ips": []  
            }  
        ],  
        "subject": "string",  
        "to": [  
            "string"  
        ]  
    },  
    "ips": [  
        "string"  
    ],  
    "observed": {  
        "domains": [  
            "string"  
        ],  
        "emails": [  
            "string"  
        ],  
        "ips": [],  
        "urls": [  
            "string"  
        ]  
    },  
    "received": {  
        "domains": [  
            "string"  
        ],  
        "domains_internal": [],  
        "emails": [],  
        "foremail": [],  
        "ips": [  
            "string"  
        ]  
    },  
    "urls": [  
        "string"  
    ]  
}
```



#### Ping
Check connectivity
Timeout - 300 Seconds



##### JSON Results
```json
{}
```



#### Parse EML Base64 Blob
This action will decode a base64 string and attempt to parse it as an EML file.  It will return a list of parsed objects.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base64 EML Blob|A base64 encoded string of an EML file.|True|String|<base64encoded_string>|



##### JSON Results
```json
[  
  {  
    "Entity": "=?utf-8?q?Please_join_Zoom_meeting_in_progress?=",  
    "EntityResult": {  
      "base64_blob": "gxMjU0NjUwNDE3NTU4Nz09LS0K",  
      "headers": [  
        [  
          "Delivered-To",  
          "bbbbb@company.co"  
        ],  
        [  
          "Received",  
          "by 2002:a02:b105:0:0:0:0:0 with SMTP id r5csp394571jah;\n Mon, 25 May 2020 05:01:36 -0700 (PDT)"  
        ],  
        [  
          "X-Google-Smtp-Source",  
          "ABdhPJwRIPolXj6t9hz7uDhriCjaL3FX7ZCvEuj1yRKm3WIbPSxV+Sq7ndSNOgf1n9jnVIQeZLZ/"  
        ],  
        [  
          "X-Received",  
          "by 2002:aa7:8425:: with SMTP id q5mr15902257pfn.98.1590408095861; \n Mon, 25 May 2020 05:01:35 -0700 (PDT)"  
        ],  
        [  
          "ARC-Seal",  
          "i=1; a=rsa-sha256; t=1590408095; cv=none;\n d=google.com; s=arc-20160816;\n b=UI2usvi7Wzr15/jm30/LDWy2kNzh0KPb+5nipU+gloaJ0V6AtCgJeEKligz0DpqnnM\n V0ZOay+z7OsKqGAkgB2Fo9dOHwTFs+S9DU+ag18AFuLdx09Sj/AHcMOYEnyV+elsBl4D\n k80KBZfJ51b5l6QFulJlcCtBoOKXsa5bB+5XQy9UZA5YRLG+pIP+GDOu+8ejUjPz7XQ7\n 0DR/wiAkyYHeImnZ57bXMR35SjbP3jLhs6F5wY6oXPzN0j0Ljye1/0aJCgnaKu07Zv4t\n +CablS2sP8aKfhx+nUtL98BRWqoAM7CRR7BhpdDJmHO3f5AXVAEhf4OLJPMDhemPEztq\n tKsQ=="  
        ],  
        [  
          "ARC-Message-Signature",  
          "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com;\n s=arc-20160816; \n h=subject:reply-to:from:to:mime-version:message-id:date;\n bh=OCUn7dAzBq4ikkUWPM7zlRyznZDGSbzE8WOf3rs6Lfo=;\n b=FruVTsGq74a09NVaaVAQnSzpXHfok485GPyPlwhfGHtTrEZJ662VGLCc1pcjDx/SzM\n ++njkWuUjCV6Y7B7vPxYnXWHdFzdNYAEir4V0JDF3zPylYJemenwBaNZ54TN/24JyZ14\n egQupuAqMnfF7VZFHdVo0oCv3NCTDcQDEY8GOK3RrO2n+vNJM87ZTkfXg52apVsaSFHu\n sYY97MAV+tCNEeJqwIAQLPgq6H3uT1i+pbAZ6xv7d0XmxkI6yulc/eDB9Ii1cPHTk56s\n WRVRTTYHzgtBZpP6/6my8C9cuXBaAzTv4bmovzip0hB0KLN0Pz0sUfYQcCqoxbYNJdoy\n XhuQ=="  
        ],  
        [  
          "ARC-Authentication-Results",  
          "i=1; mx.google.com;\n spf=pass (google.com: domain of pawt@mailrelaysrv.com designates 18.184.247.15\n as permitted sender) smtp.mailfrom=pawt@mailrelaysrv.com"  
        ],  
        [  
          "Return-Path",  
          "<pawt@mailrelaysrv.com>"  
        ],  
        [  
          "Received",  
          "from mailstream-west.mxrecord.io\n (mailstream-uswest-egress002.mxrecord.io. [52.11.209.211])\n by mx.google.com with ESMTPS id lj8si13539801pjb.114.2020.05.25.05.01.35\n for <bbbbb@company.co>\n (version=TLS1_3 cipher=TLS_AES_256_GCM_SHA384 bits=256/256);\n Mon, 25 May 2020 05:01:35 -0700 (PDT)"  
        ],  
        [  
          "Received-SPF",  
          "pass (google.com: domain of pawt@mailrelaysrv.com designates\n 18.184.247.15 as permitted sender) client-ip=18.184.247.15; "  
        ],  
        [  
          "Authentication-Results",  
          "mx.google.com;\n spf=pass (google.com: domain of pawt@mailrelaysrv.com designates 18.184.247.15\n as permitted sender) smtp.mailfrom=pawt@mailrelaysrv.com"  
        ],  
        [  
          "Date",  
          "Mon, 25 May 2020 05:01:35 -0700 (PDT)"  
        ],  
        [  
          "Message-ID",  
          "<5ecbb39f.1c69fb81.ab8ef.0cfcSMTPIN_ADDED_MISSING@mx.google.com>"  
        ],  
        [  
          "Received",  
          "from mailstreamwest005.production.area1.internal (localhost\n [127.0.0.1])\n by mailstream-west.mxrecord.io (Postfix) with ESMTP id 49Vwg33HQWzNkJn\n for <bbbbb@company.co>; Mon, 25 May 2020 12:01:35 +0000 (UTC)"  
        ],  
        [  
          "Received-SPF",  
          "pass (mxrecord.io: mailrelaysrv.com designates 18.184.247.15 as\n permitted sender) client-ip=18.184.247.15; envelope-from=pawt@mailrelaysrv.com;\n helo=mail4.eu.mailrelaysrv.com; "  
        ],  
        [  
          "Authentication-Results",  
          "mailstream-west.mxrecord.io;\n dmarc=fail (p=none) header.from=company.co;\n spf=pass smtp.mailfrom=mailrelaysrv.com; dkim=none"  
        ],  
        [  
          "Received",  
          "from mailstream-west.mxrecord.io (localhost. [127.0.0.1])\n by localhost with SMTP (Area1Security-Mailstream 2.94.0) id KAMFVJZH\n for bbbbb@company.co; Mon, 25 May 2020 12:01:35 +0000 (GMT)"  
        ],  
        [  
          "Received",  
          "from mailrelaysrv.com (mail4.eu.mailrelaysrv.com [18.184.247.15])\n by mailstream-west.mxrecord.io (Postfix) with ESMTP id 49Vwg25XkYzNkHv\n for <bbbbb@company.co>; Mon, 25 May 2020 12:01:34 +0000 (UTC)"  
        ],  
        [  
          "Content-Type",  
          "multipart/mixed; boundary=\"===============2469812546504175587==\""  
        ],  
        [  
          "MIME-Version",  
          "1.0"  
        ],  
        [  
          "To",  
          "=?utf-8?q?hXKQ+fhuQ2u40+Sb+KBccg=3D=3D?= <bbbbb@company.co>"  
        ],  
        [  
          "From",  
          "=?utf-8?q?Maayan_Horenstain?= <aaaaa@company.co>"  
        ],  
        [  
          "Reply-To",  
          "<bbbbb@company.co>"  
        ],  
        [  
          "X-Area1Security-Disposition",  
          "SPOOF 49Vwg25XkYzNkHv-2020-05-25T12:01:35"  
        ],  
        [  
          "X-Area1Security-Origin",  
          "EXTERNAL 49Vwg25XkYzNkHv-2020-05-25T12:01:35"  
        ],  
        [  
          "X-Area1Security-Processed",  
          "f4822d4f5014edc3e32b57c850398246; 2; SPOOF;\n 2020-05-25T12:01:35"  
        ],  
        [  
          "Subject",  
          "=?utf-8?q?Please_join_Zoom_meeting_in_progress?="  
        ],  
        [  
          "X-PhishInsight",  
          "Trend Micro Phishing simulation"  
        ],  
        [  
          "X-PhishInsightTracking",  
          "This phishing simulation email was sent because\n bbbbb@company.co initiated a simulation campaign."  
        ],  
        [  
          "X-PhishInsightCampaignID",  
          ""  
        ]  
      ],  
      "sender": [  
        "aaaaa@company.co"  
      ],  
      "to": [  
        "bbbbb@company.co"  
      ],  
      "cc": [],  
      "bcc": [],  
      "subject": "=?utf-8?q?Please_join_Zoom_meeting_in_progress?=",  
      "date": "Mon, 25 May 2020 05:01:35 -0700 (PDT)",  
      "text_body": "",  
      "html_body": "<p style=\"padding-left: 30px;\">\n</p>\n<p style=\"padding-left: 30px;\">\n <span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">\n Hello\n </span>\n <span class=\"mceNonEditable\">\n <span class=\"mceNonEditable\">\n bbbbb\n </span>\n </span>\n <span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">\n ,\n </span>\n</p>\n<p style=\"padding-left: 30px;\">\n <span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">\n </span>\n</p>\n<p style=\"padding-left: 30px;\">\n <span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">\n Join your\n </span>\n <span class=\"mceNonEditable\">\n <span class=\"mceNonEditable\">\n \n </span>\n </span>\n <span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">\n CEO and Management Board Meeting\n </span>\n <br/>\n <span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">\n for all staffs on Zoom Meeting\n </span>\n</p>\n<p style=\"padding-left: 30px;\">\n <span style=\"font-family: helvetica, arial, sans-serif;\">\n </span>\n</p>\n<p style=\"padding-left: 30px;\">\n <span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">\n This is a reminder that your zoom meeting appointment with\n </span>\n <br/>\n <span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">\n <strong>\n H.R and Audit Head\n </strong>\n will start in few minutes.\n </span>\n <br/>\n <span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">\n Your presence is crucial to this meeting and equally\n </span>\n <br/>\n <span style=\"font-family: helvetica, arial, sans-serif; font-size: 12pt;\">\n required to commence this\n <strong>\n Q1 perfomance review meeting\n </strong>\n </span>\n <br/>\n <br/>\n</p>\n<p style=\"padding-left: 30px;\">\n</p>\n<table style=\"height: 71px; background-color: #3694f7; margin-left: 30px;\" width=\"208\">\n <tbody>\n <tr>\n <td style=\"width: 200px; height: 50px; text-align: center;\">\n <span style=\"font-family: tahoma, arial, helvetica, sans-serif;\">\n <strong>\n <span style=\"color: #ffffff;\">\n <a class=\"fakesitelink\" href=\"https://www.onlineservicetech.website/link/l/P70iPXzLzo2cEeD77GjmLWWqXFQCjsVQBYNKZZ346JqYYikTR6QGaMnqw4L-mxxYSStIHAeIicd-w1IUrFsBn6iuMCO4gwZ_1SBG-62fgIZQk3zPNIst9wGCbTW-62BxD-FJp7TcWFBSqKVUBeVYliF_DTc6oygMqfxdStFnDb_-CffKq4AzNFF13zwoNarj\" rel=\"noopener noreferrer\" style=\"color: #ffffff;\" target=\"_blank\">\n Join this live meeting\n </a>\n </span>\n </strong>\n </span>\n </td>\n </tr>\n </tbody>\n</table><img alt=\"\" src=\"https://www.onlineservicetech.website/link/t/KEDVs-MM3mp5milZ6YjdRdZjBbXiCMAKHKwUTCo7zkd4j2-iwl-RGhO3GIxnJDOk\"/><a href=\"https://www.onlineservicetech.website/link/b/KEDVs-MM3mp5milZ6YjdRdZjBbXiCMAKHKwUTCo7zkd4j2-iwl-RGhO3GIxnJDOk\"></a>",  
      "count": 1  
    }  
  }  
]
```



#### Parse Case Wall Email
This action will parse an EML or MSG file that has been attached to the case wall.
Timeout - 1200 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Entities|When enabled, this will create User entities out of the To and From headers and a Email Subject entity out of the Subject field. |False|Boolean|true|
|Exclude Entities Regex|Observed entities that match the supplied regex will not be created.|False|String||
|Original EML Only|Extract attachments from the original EML only.|False|Boolean|true|
|Create Observed Entities|Create Entities out of the observed entities in the email body.'All' will create URL, Email, IP, and Hash entities.|False|List|All|
|Save Attachments to Case Wall|Save the extracted attachments to the case wall.|False|Boolean|true|
|Fang Entities|When enabled, entities that are defanged (example.com => example[.]com) will be converted to fanged entities.|False|Boolean|true|
|Custom Entity Regexes|A JSON object that can parse out entities from body and subject.|False|Code|{ }|



##### JSON Results
```json
{  
    "parsed_emails": [  
        {  
            "attached_emails": [  
                {  
                    "attachments": [  
                        {  
                            "extension": "string",  
                            "filename": "string",  
                            "hash": {  
                                "md5": "string",  
                                "sha1": "string",  
                                "sha256": "string",  
                                "sha512": "string"  
                            },  
                            "level": 0,  
                            "mime_type": "string",  
                            "mime_type_short": "string",  
                            "size": 0  
                        }  
                    ],  
                    "body": [  
                        {  
                            "content": "string",  
                            "content_type": "string",  
                            "hash": "string"  
                        }  
                    ],  
                    "header": {  
                        "cc": "string",  
                        "date": "string",  
                        "from": "string",  
                        "header": {  
                            "authentication-results": [  
                                "string"  
                            ],  
                            "cc": [  
                                "string"  
                            ],  
                            "content-type": [  
                                "string"  
                            ],  
                            "date": [  
                                "string"  
                            ],  
                            "dkim-signature": [  
                                "string"  
                            ],  
                            "from": [  
                                "string"  
                            ],  
                            "message-id": [  
                                "string"  
                            ],  
                            "mime-version": [  
                                "string"  
                            ],  
                            "original-recipient": [  
                                "string"  
                            ],  
                            "received": [  
                                "string"  
                            ],  
                            "received-spf": [  
                                "string"  
                            ],  
                            "return-path": [  
                                "string"  
                            ],  
                            "subject": [  
                                "string"  
                            ],  
                            "to": [  
                                "string"  
                            ],  
                            "x-icloud-spam-score": [  
                                "string"  
                            ],  
                            "x-proofpoint-spam-details": [  
                                "string"  
                            ],  
                            "x-proofpoint-virus-version": [  
                                "string"  
                            ],  
                            "x-received": [  
                                "string"  
                            ]  
                        },  
                        "received": [  
                            {  
                                "by": [  
                                    "string"  
                                ],  
                                "date": "string",  
                                "from": [  
                                    "string"  
                                ],  
                                "src": "string",  
                                "with": "string"  
                            }  
                        ],  
                        "receiving": [  
                            {  
                                "domains": [  
                                    "string"  
                                ],  
                                "hosts": [  
                                    "string"  
                                ]  
                            }  
                        ],  
                        "sending": [  
                            {  
                                "domains": [  
                                    "string"  
                                ],  
                                "hosts": [  
                                    "string"  
                                ],  
                                "ips": [  
                                    "string"  
                                ]  
                            }  
                        ],  
                        "subject": "string",  
                        "to": [  
                            "string"  
                        ]  
                    },  
                    "level": 0,  
                    "source_file": "string"  
                }  
            ],  
            "attachment_id": 0,  
            "attachment_name": "string",  
            "attachments": [  
                {  
                    "content_header": {  
                        "content-disposition": [  
                            "string"  
                        ],  
                        "content-id": [  
                            "string"  
                        ],  
                        "content-transfer-encoding": [  
                            "string"  
                        ],  
                        "content-type": [  
                            "string"  
                        ],  
                        "x-attachment-id": [  
                            "string"  
                        ]  
                    },  
                    "extension": "string",  
                    "filename": "string",  
                    "hash": {  
                        "md5": "string",  
                        "sha1": "string",  
                        "sha256": "string",  
                        "sha512": "string"  
                    },  
                    "level": 0,  
                    "mime_type": "string",  
                    "mime_type_short": "string",  
                    "ole_data": [  
                        {  
                            "hide_if_false": 0,  
                            "id": "string",  
                            "name": "string",  
                            "risk": "string",  
                            "value": "string"  
                        }  
                    ],  
                    "size": 0  
                }  
            ],  
            "result": {  
                "attachments": [  
                    {  
                        "content_header": {  
                            "content-disposition": [  
                                "string"  
                            ],  
                            "content-id": [  
                                "string"  
                            ],  
                            "content-transfer-encoding": [  
                                "string"  
                            ],  
                            "content-type": [  
                                "string"  
                            ],  
                            "x-attachment-id": [  
                                "string"  
                            ]  
                        },  
                        "extension": "string",  
                        "filename": "string",  
                        "hash": {  
                            "md5": "string",  
                            "sha1": "string",  
                            "sha256": "string",  
                            "sha512": "string"  
                        },  
                        "level": 0,  
                        "mime_type": "string",  
                        "mime_type_short": "string",  
                        "ole_data": [  
                            {  
                                "hide_if_false": 0,  
                                "id": "string",  
                                "name": "string",  
                                "risk": "string",  
                                "value": "string"  
                            }  
                        ],  
                        "size": 0  
                    }  
                ],  
                "body": [  
                    {  
                        "content": "string",  
                        "content_type": "string",  
                        "hash": "string"  
                    }  
                ],  
                "header": {  
                    "date": "string",  
                    "from": "string",  
                    "header": {  
                        "content-type": [  
                            "string"  
                        ],  
                        "date": [  
                            "string"  
                        ],  
                        "from": [  
                            "string"  
                        ],  
                        "message-id": [  
                            "string"  
                        ],  
                        "mime-version": [  
                            "string"  
                        ],  
                        "subject": [  
                            "string"  
                        ],  
                        "to": [  
                            "string"  
                        ]  
                    },  
                    "received": [  
                        {  
                            "by": [  
                                "string"  
                            ],  
                            "date": "string",  
                            "from": [  
                                "string"  
                            ],  
                            "src": "string",  
                            "with": "string"  
                        }  
                    ],  
                    "receiving": [  
                        {  
                            "domains": [  
                                "string"  
                            ],  
                            "hosts": [  
                                "string"  
                            ]  
                        }  
                    ],  
                    "sending": [  
                        {  
                            "domains": [  
                                "string"  
                            ],  
                            "hosts": [  
                                "string"  
                            ],  
                            "ips": [  
                                "string"  
                            ]  
                        }  
                    ],  
                    "subject": "string",  
                    "to": [  
                        "string"  
                    ]  
                },  
                "level": 0,  
                "source_file": "string"  
            }  
        }  
    ]  
}
```



#### Analyze EML Headers
This actions gets a base64 EML or list of headers and extracts/analyses its headers
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base64 EML|Base64 string of an EML file.|False|String||
|Header List|Headers list in a JSON format.|False|String||



##### JSON Results
```json
{}
```






## Jobs



## Connectors


