
# Lists

A set of tools to facilitate managing custom lists within Siemplify

Python Version - 2



## Actions
#### Ping
Check connectivity
Timeout - 300 Seconds



##### JSON Results
```json
{}
```



#### Add String to Custom List
The action adds a string to a custom list.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|ListItem|The list item string to add to the custom list.|True|String|cajs3i|
|Category|Custom list Category|True|String|WhiteList|



##### JSON Results
```json
[  
    {  
        "Entity": "1.2.3.4",  
        "EntityResult": false  
    },  
    {  
        "Entity": "google.com",  
        "EntityResult": true  
    },  
    {  
        "Entity": "yahoo.co.uk",  
        "EntityResult": false  
    }  
]
```



#### Is String In Custom List
The action checks if a specific string exists in a custom list
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IdentifierList|A list of "strings" to compare against the custom list (for the current environment) in a specific category |True|String|1.2.3.4,google.com,yahoo.co.uk|
|Category|Custom list Category|True|String|WhiteList|



##### JSON Results
```json
[  
    {  
        "Entity": "1.2.3.4",  
        "EntityResult": false  
    },  
    {  
        "Entity": "google.com",  
        "EntityResult": true  
    },  
    {  
        "Entity": "yahoo.co.uk",  
        "EntityResult": false  
    }  
]
```



#### Remove String from Custom List
The action removes a string from a custom list.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|ListItem|The list item string to add to the custom list.|True|String|cajs3i|
|Category|Custom list Category|True|String|WhiteList|



##### JSON Results
```json
[  
    {  
        "Entity": "1.2.3.4",  
        "EntityResult": false  
    },  
    {  
        "Entity": "google.com",  
        "EntityResult": true  
    },  
    {  
        "Entity": "yahoo.co.uk",  
        "EntityResult": false  
    }  
]
```






## Jobs



## Connectors


