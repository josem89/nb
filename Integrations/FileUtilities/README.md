
# FileUtilities

A set of file utility actions created for Siemplify Community to power up playbook capabilities.  

Python Version - 2



## Actions
#### Count Files
The action counts files in a given folder path according to a specific file extension
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Extension|Count the files that include a specific file extension|False|String|*.txt|
|Folder|The folder path from which you would like to count the files|True|String|/tempFolder|
|Is Recursive|If enabled, this will recursively count all files in the directory.|False|Boolean|false|



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



#### Get Files as Base64
Converts local files to base64 strings.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Paths|A comma delimited list of files, including their path.|True|String|/path/file.exe|



##### JSON Results
```json
{  
  "filenames": [  
    "/opt/siemplify/siemplify_server/Scripting/Phishing_.eml",  
    "/opt/siemplify/siemplify_server/Scripting/Logo.png"  
  ],  
  "data": [  
    {  
      "path": "/opt/siemplify/siemplify_server/Scripting",  
      "filename": "Phishing_.eml",  
      "extension": ".eml",  
      "base64": "XXXX"  
    },  
    {  
      "path": "/opt/siemplify/siemplify_server/Scripting",  
      "filename": "Logo.png",  
      "extension": ".png",  
      "base64": "iVBORw0KGgoAAAANSUhEUgAAAY8AAABdCAYAAABdG+"  
    }  
  ]  
}
```



#### Add Entity to File
This action will add the identifier of a target entity to a local file.  It will only add one occurance of the entity to the file and will return False if the entity already exists.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filename|The name of the file to write the entities to.|True|String|<filename.out>|



##### JSON Results
```json
{}
```



#### Extract Zip Files
This action will extract files from a ZIP archive.  It has the ability to extract password protected files by either a supplied password or bruteforce. Requires FILENAME entity to have attachment_id attribute to download file from Case Wall.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Include Data In JSON Result|Include the data from the extracted files as base64 encoded values in the JSON result of the action.|False|Boolean|false|
|Create Entities|Create entities out of the extracted files.|False|Boolean|true|
|Zip File Password|If the zip file is password protected, use this password to extract.|False|String||
|BruteForce Password|When enabled, the action will attempt to brute force any password protected Zip files.|False|Boolean|false|
|Add to Case Wall|Add the extracted files to the case wall.|False|Boolean|true|
|Zip Password List Delimiter|This is character that separates multiple passwords in the Zip File Password parameter.|True|String|,|



##### JSON Results
```json
{}
```



#### Get Attachment
The actions gets an attachment from the case wall (the result is presented as a Base64)
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attachment Scope|The scope of the attachment that needs to be retrieved - case or alert|True|List|Alert|



##### JSON Results
```json
[  
  {  
    "evidenceName": "Siemplify Picture",  
    "description": "Original email attachment",  
    "evidenceThumbnailBase64": "",  
    "evidenceId": 4,  
    "fileType": ".png",  
    "creatorUserId": "EmailV2",  
    "id": 4,  
    "type": 4,  
    "caseId": 11,  
    "isFavorite": false,  
    "modificationTimeUnixTimeInMs": 1592991920239,  
    "creationTimeUnixTimeInMs": 1592991920239,  
    "alertIdentifier": "9069-4D83-BBB1-D37C0D494A36",  
    "base64_blob": "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"  
  }  
]
```



#### Copy of Extract Zip Files
This action will extract files from a ZIP archive.  It has the ability to extract password protected files by either a supplied password or bruteforce. Requires FILENAME entity to have attachment_id attribute to download file from Case Wall.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Include Data In JSON Result|Include the data from the extracted files as base64 encoded values in the JSON result of the action.|False|Boolean|false|
|Create Entities|Create entities out of the extracted files.|False|Boolean|true|
|Zip File Password|If the zip file is password protected, use this password to extract.|False|String||
|BruteForce Password|When enabled, the action will attempt to brute force any password protected Zip files.|False|Boolean|false|
|Add to Case Wall|Add the extracted files to the case wall.|False|Boolean|true|
|Zip Password List Delimiter|This is character that separates multiple passwords in the Zip File Password parameter.|True|String|,|



##### JSON Results
```json
{}
```



#### Remove Entity from File
This action will remove the identifier of a target entity from a local file. It will return False if it failed to remove all entities or an entity does not exist.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filename|The name of the file to write the entities to.|True|String|<filename.out>|



##### JSON Results
```json
{}
```



#### Create Archive
Creates an archive file from a list of provided files or a directories.  Supports: zip, tar, gztar, bztar, xtar.
Returns the location of the archive file.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Archive Type|The type of archive to create.  Supports: zip,uncompressed tar-filegzip'ed tar-filebzip2'ed tar-filexz'ed tar-file|True|List|zip|
|Archive Base Name|The name of the archive file that will be created without the extension.|True|String|<filename>|
|Archive Input|Either a comma delimited list of files or a directory path.|True|String|<archive input>|



##### JSON Results
```json
{  
    "success": true,  
    "archive": "/opt/siemplify/siemplify_server/Scripting/FileUtilities/Archives/testarchive.zip"  
}
```



#### Extract Archive
Extracts an archive file to a directory..  Supports: zip, tar, gztar, bztar, xtar.
Returns the extracted path and files.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Archive|The  path of the archive to be extracted.  Supports comma delimitedExample: /opt/siemplify/siemplify_server/Scripting/FileUtilities//file.zip|True|String|<archive file with path>|



##### JSON Results
```json
{  
  "archives": [  
    {  
      "success": true,  
      "archive": "testarchive.zip",  
      "folder": "/opt/siemplify/siemplify_server/Scripting/FileUtilities/Extract/testarchive",  
      "files_with_path": [  
        "/opt/siemplify/siemplify_server/Scripting/FileUtilities/Extract/testarchive/Archives/testarchive.zip",  
        "/opt/siemplify/siemplify_server/Scripting/FileUtilities/Extract/testarchive/Archives/file1",  
        "/opt/siemplify/siemplify_server/Scripting/FileUtilities/Extract/testarchive/Archives/file2"  
      ],  
      "files_list": ["testarchive.zip", "file1", "file2"],  
      "files": {  
        "name": "testarchive",  
        "type": "directory",  
        "children": [  
          {  
            "name": "Archives",  
            "type": "directory",  
            "children": [  
              {  
                "name": "testarchive.zip",  
                "type": "file"  
              },  
              {  
                "name": "file1",  
                "type": "file"  
              },  
              {  
                "name": "file2",  
                "type": "file"  
              }  
            ]  
          }  
        ]  
      }  
    }  
  ]  
}
```



#### Save Base64 to File
The action saves a base64 string to a file.  It supports comma separated lists for Filename and Base64 Input.  The optional File Extension parameter is used to add an extension to the output filename.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Extension|Optional: this will add the supplied extension to the filename.|False|String|None|
|Base64 Input|The base64 string that will be converted to a file.  Supports comma separation. |True|String|<base64_encoded_string>|
|Filename|The filename the base64 string will be saved as.|True|String||



##### JSON Results
```json
{  
  "files": [  
    {  
      "file_name": "ABCDE.COM",  
      "file_path": "/opt/siemplify/siemplify_server/Scripting/downloads/HTTPSACCOUNT.LIVE.COMSECURITYNOTIFICATIONSUPDATE",  
      "extension": ".COM"  
    },  
    {  
      "file_name": "archive1.zip",  
      "file_path": "/opt/siemplify/siemplify_server/Scripting/downloads/archive1.zip",  
      "extension": ".zip"  
    }  
  ]  
}
```



#### Add Attachment
The action adds an attachment to the case wall (similar to attach evidence)
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Name|The name of the attachment|True|String|Name|
|IsFavorite|Is the attachment marked as favorite in the case wall |False|Boolean|false|
|Base64 Blob|The attachment's content in Base64|True|String|<Base64 here>|
|Type|Attachment Type|True|String|.txt|
|Description|The description of the attachment |True|String|Description|



##### JSON Results
```json
{  
  "evidenceName": "Description",  
  "description": "Name",  
  "evidenceThumbnailBase64": "",  
  "evidenceId": 30,  
  "fileType": ".txt",  
  "creatorUserId": "No user context",  
  "id": 30,  
  "type": 4,  
  "caseId": 25,  
  "isFavorite": false,  
  "modificationTimeUnixTimeInMs": 1593151675450,  
  "creationTimeUnixTimeInMs": 1593151675450,  
  "alertIdentifier": null  
}
```



#### Decode Base64
The action decodes base64 input string and returns the json object.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base64 Input|Base64 Input string you would like to decode|True|String| |
|Encoding|Choose the encoding option from the list|True|List|UTF-8|



##### JSON Results
```json
{  
    "decoded_content":"Example output data"  
}
```






## Jobs



## Connectors


