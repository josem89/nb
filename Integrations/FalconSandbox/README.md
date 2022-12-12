
# FalconSandbox

Falcon Sandbox is a high end malware analysis framework with a very agile architecture.

Python Version - 1
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|String|https://<server-address>/api/v2|
|Api Key|None|True|Password|None|
|Threshold|None|True|Integer|50.0|



## Actions
#### Search
Search Falcon databases for existing scan reports and information about files, and file Urls
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Name|Filename e.g. invoice.exe|False|String||
|File Type|e.g. docx|False|String||
|File Type Description|e.g. PE32 executable|False|String||
|Verdict|e.g. 1 (1=whitelisted, 2=no verdict, 3=no specific threat, 4=suspicious, 5=malicious)|False|String||
|AV Multiscan Range|e.g. 50-70 (min 0, max 100)|False|String||
|AV Family Substring|e.g. Agent.AD, nemucod|False|String||
|Hashtag|e.g. ransomware|False|String|None|
|Port|e.g. 8080|False|String|None|
|Host|x.x.x.x|False|String|None|
|Domain|e.g. checkip.dyndns.org|False|String|None|
|HTTP Request Substring|e.g. google|False|String|None|
|Similar Samples|e.g. <sha256>|False|String|None|
|Sample Context|e.g. <sha256>|False|String|None|



##### JSON Results
```json
[{"environment_id": 120, "job_id": "5c441f357ca3e158b964fee3", "analysis_start_time": "2019-01-20 08:23:00", "vx_family": "Trojan.Generic", "av_detect": "70", "threat_score": 98, "environment_description": "Windows 7 64 bit", "verdict": "malicious", "submit_name": "original.bin", "sha256": "8bade22161bf71a49955a66ec69809affbd2dde09dc84b94ede57e0d027e82e4", "type": null, "type_short": "service", "size": 43520}]
```



#### Wait For Job and Fetch Report
Wait for a scan job to complete and fetch the scan report.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Job ID|The job id to fetch report for. For multiple, use comma separated values.|True|String||



##### JSON Results
```json
{"5f21459cb80c2d0a182b7967": {"environment_id": 300, "threat_score": 0, "target_url": null, "total_processes": 0, "threat_level": 3, "size": 26505, "submissions": [{"url": null, "submission_id": "5f267a34e3e6784e4f180936", "created_at": "2020-08-02T08:32:52+00:00", "filename": "Test.py"}, {"url": null, "submission_id": "5f2146381a5f6253f266fed9", "created_at": "2020-07-29T09:49:44+00:00", "filename": "Test.py"}, {"url": null, "submission_id": "5f21461360cae26e4719a6c9", "created_at": "2020-07-29T09:49:07+00:00", "filename": "Test.py"}, {"url": null, "submission_id": "5f21459cb80c2d0a182b7968", "created_at": "2020-07-29T09:47:08+00:00", "filename": "Test.py"}], "job_id": "5f21459cb80c2d0a182b7967", "vx_family": null, "interesting": false, "error_type": null, "state": "SUCCESS", "mitre_attcks": [], "certificates": [], "hosts": [], "sha256": "fa636febca412dd9d1f2e7f7ca66462757bce24adb7cb5fffd2e247ce6dcf7fe", "sha512": "62c6d5c16d647e1361a761553fb1adfa92df3741e53a234fab28d08d3d003bdb4b2a7d7c5a050dc2cdba7b1d915f42d3c56f9694053fa75adae82c1b20e03b02", "compromised_hosts": [], "extracted_files": [], "analysis_start_time": "2020-07-29T09:47:17+00:00", "tags": [], "imphash": "Unknown", "total_network_connections": 0, "av_detect": null, "classification_tags": [], "submit_name": "Test.py", "ssdeep": "384:lRGs3v2+nSZUpav/+GUYERs0vZfyh/fyChIRpyCCLqa09NdyDRax9XSmxTAf:lR3fKZUoGGX0xfm/Duyoa09x9+", "md5": "bfec680af21539eb0a9f349038c68220", "error_origin": null, "total_signatures": 0, "processes": [], "sha1": "0a4e78bb8df401197e925b2643ceabf5b670df17", "url_analysis": false, "type": "Python script, ASCII text executable, with CRLF line terminators", "file_metadata": null, "environment_description": "Linux (Ubuntu 16.04, 64 bit)", "verdict": "no verdict", "domains": [], "type_short": ["script", "python"]}}
```



#### Submit File
Submit files for analysis
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Path|The full path of the file to analyze. For multiple, use comma separated values.|True|String||
|Environment|The environment to use for the scan.|True|List|Linux (Ubuntu 16.04, 64 bit)|



##### JSON Results
```json
[{"EntityResult": {"sha256": "fa636febca412dd9d1f2e7f7ca66462757bce24adb7cb5fffd2e247ce6dcf7fe", "job_id": "5f21459cb80c2d0a182b7967"}, "Entity": "/temp/test.txt"}]
```



#### Ping
Test connectivity to Falcon Sandbox
Timeout - 600 Seconds



#### Analyze File
Submit a file for analysis and fetch report
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Path|The full path of the file to analyze|True|String||
|Environment|Environment ID. e.g. 100 (100=Windows 7 32 bit)|True|String||
|Include Report|If enabled, action will fetch report related to the attachment. Note: this feature requires a premium key.|False|Boolean|true|



##### JSON Results
```json
[{"target_url": null, "threat_score": null, "environment_id": 100, "total_processes": 0, "threat_level": null, "size": 31261, "job_id": "5c4435ef7ca3e109e640b709", "vx_family": null, "interesting": false, "error_origin": null, "state": "IN_QUEUE", "mitre_attcks": [], "certificates": [], "hosts": [], "sha256": "26d3c8656a83b06b293b15251617fe2c2c493f842a95b3d9b2ee45b3209d5fac", "type": "PNG image data, 1200 x 413, 8-bit/color RGBA, non-interlaced", "compromised_hosts": [], "extracted_files": [], "analysis_start_time": "2019-01-20T02:50:01-06:00", "tags": [], "imphash": null, "total_network_connections": 0, "av_detect": null, "total_signatures": 0, "submit_name": "Proofpoint_R_Logo (1).png", "ssdeep": null, "classification_tags": [], "md5": "48703c5d4ea8dc2099c37ea871b640ef", "processes": [], "sha1": "5b30e297b54ef27ffcda06aa212b5aa6c5424e1c", "url_analysis": false, "sha512": "01f48fa1671cdc9e4d6866b9b237430f1b9b7093cbbed57fb010dc3db84a754a7a0457c5fd968d4e693ca74bdc1c7f15efb55f2af2ea236354944cffc8d4efd8", "file_metadata": null, "environment_description": "Windows 7 32 bit", "verdict": null, "domains": [], "error_type": null, "type_short": ["img"]}]
```



#### Analyze File Url
Submit a file by URL for analysis and fetch report
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Url|The url to the file to analyze. e.g. http://tamzamaninda.net/office/Document.zip|True|String||
|Environment|Environment ID. e.g. 100 (100=Windows 7 32 bit)|True|String||



##### JSON Results
```json
[{"target_url": null, "threat_score": null, "environment_id": 100, "total_processes": 0, "threat_level": null, "size": 31261, "job_id": "5c4435ef7ca3e109e640b709", "vx_family": null, "interesting": false, "error_origin": null, "state": "IN_QUEUE", "mitre_attcks": [], "certificates": [], "hosts": [], "sha256": "26d3c8656a83b06b293b15251617fe2c2c493f842a95b3d9b2ee45b3209d5fac", "type": "PNG image data, 1200 x 413, 8-bit/color RGBA, non-interlaced", "compromised_hosts": [], "extracted_files": [], "analysis_start_time": "2019-01-20T02:50:01-06:00", "tags": [], "imphash": null, "total_network_connections": 0, "av_detect": null, "total_signatures": 0, "submit_name": "Proofpoint_R_Logo (1).png", "ssdeep": null, "classification_tags": [], "md5": "48703c5d4ea8dc2099c37ea871b640ef", "processes": [], "sha1": "5b30e297b54ef27ffcda06aa212b5aa6c5424e1c", "url_analysis": false, "sha512": "01f48fa1671cdc9e4d6866b9b237430f1b9b7093cbbed57fb010dc3db84a754a7a0457c5fd968d4e693ca74bdc1c7f15efb55f2af2ea236354944cffc8d4efd8", "file_metadata": null, "environment_description": "Windows 7 32 bit", "verdict": null, "domains": [], "error_type": null, "type_short": ["img"]}]
```



#### Scan URL
Scan URL/domain for analysis.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Threshold|Mark entity as suspicious if number of av detection is equal or above the given threshold|True|String||
|Environment|The environment to use for the scan.|True|List|Linux (Ubuntu 16.04, 64 bit)|



##### JSON Results
```json
[{"EntityResult": {"environment_id": 100, "threat_score": 13, "target_url": null, "total_processes": 3, "threat_level": 0, "size": null, "submissions": [{"url": "http://google.com/", "submission_id": "5f4925f00da24603010641be", "created_at": "2020-08-28T15:42:40+00:00", "filename": null}, {"url": "http://google.com/", "submission_id": "5f48c011f86f36448901d054", "created_at": "2020-08-28T08:28:01+00:00", "filename": null}], "job_id": "5f1332c48161bb7d5b6c9663", "vx_family": "Unrated site", "interesting": false, "error_type": null, "state": "SUCCESS", "mitre_attcks": [], "certificates": [], "hosts": ["172.217.11.67", "172.217.5.67", "172.217.4.162", "142.250.68.99", "142.250.68.98", "172.217.14.78", "172.217.4.174", "172.217.11.163"], "sha256": "6982da0e6956768fdc206317d429c6b8313cf4ebf298ec0aa35f0f03f07cec6a", "sha512": "c2e12fee8e08b387f91529aaada5c78e86649fbb2fe64d067b630e0c5870284bf0ca22654211513d774357d37d4c9729ea7ddc44bf44144252959004363d7da9", "compromised_hosts": [], "extracted_files": [{"av_label": null, "sha1": "0da5de8165c50f6ace4660a6b38031f212917b17", "threat_level": 0, "name": "rs_ACT90oEMCn26rBYSdHdZAoXYig7gRwLYBA_1_.js", "threat_level_readable": "no specific threat", "type_tags": ["script", "javascript"], "description": "ASCII text, with very long lines", "file_available_to_download": false, "av_matched": null, "runtime_process": null, "av_total": null, "file_size": 566005, "sha256": "d41f46920a017c79fe4e6f4fb0a621af77169168c8645aa4b5094a1e67e127a0", "file_path": null, "md5": "c8c8076fd2390d47c8bf4a40f4885eeb"}], "analysis_start_time": "2020-07-18T17:35:09+00:00", "tags": ["tag", "the"], "imphash": "Unknown", "total_network_connections": 8, "av_detect": 0, "classification_tags": [], "submit_name": "http://google.com/", "ssdeep": "Unknown", "md5": "e6f672151804707d11eb4b840c3ec635", "error_origin": null, "total_signatures": 14, "processes": [{"process_flags": [], "av_label": null, "mutants": [], "uid": "00083159-00001692", "icon": null, "script_calls": [], "pid": null, "handles": [], "command_line": "\"%WINDIR%\\System32\\ieframe.dll\",OpenURL C:\\6982da0e6956768fdc206317d429c6b8313cf4ebf298ec0aa35f0f03f07cec6a.url", "file_accesses": [], "parentuid": null, "normalized_path": "%WINDIR%\\System32\\rundll32.exe", "av_matched": null, "streams": [], "registry": [], "av_total": null, "sha256": "3fa4912eb43fc304652d7b01f118589259861e2d628fa7c86193e54d5f987670", "created_files": [], "name": "rundll32.exe"}, {"process_flags": [], "av_label": null, "mutants": [], "uid": "00083319-00003012", "icon": null, "script_calls": [], "pid": null, "handles": [], "command_line": "http://google.com/", "file_accesses": [], "parentuid": "00083159-00001692", "normalized_path": "%PROGRAMFILES%\\Internet Explorer\\iexplore.exe", "av_matched": null, "streams": [], "registry": [], "av_total": null, "sha256": "8abc7daa81c8a20bfd88b6a60ecc9ed1292fbb6cedbd6f872f36512d9a194bba", "created_files": [], "name": "iexplore.exe"}, {"process_flags": [], "av_label": null, "mutants": [], "uid": "00083353-00002468", "icon": null, "script_calls": [], "pid": null, "handles": [], "command_line": "SCODEF:3012 CREDAT:275457 /prefetch:2", "file_accesses": [], "parentuid": "00083319-00003012", "normalized_path": "%PROGRAMFILES%\\Internet Explorer\\iexplore.exe", "av_matched": null, "streams": [], "registry": [], "av_total": null, "sha256": "8abc7daa81c8a20bfd88b6a60ecc9ed1292fbb6cedbd6f872f36512d9a194bba", "created_files": [], "name": "iexplore.exe"}], "sha1": "0a0bec39293c168288c04f575a7a317e29f1878f", "url_analysis": true, "type": null, "file_metadata": null, "environment_description": "Windows 7 32 bit", "verdict": "no specific threat", "domains": ["fonts.gstatic.com", "googleads.g.doubleclick.net", "ocsp.pki.goog", "ssl.gstatic.com", "www.gstatic.com"], "type_short": []}, "Entity": "google.com"}]
```



#### Get Hash Scan Report
Fetch hybrid analysis reports and enrich file hash entities
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": [{"classification_tags": [], "environment_id": 100, "total_processes": 0, "threat_level": null, "size": 31261, "job_id": "5c4435ef7ca3e109e640b709", "target_url": null, "interesting": false, "error_type": null, "state": "IN_QUEUE", "environment_description": "Windows 7 32 bit", "mitre_attcks": [], "certificates": [], "hosts": [], "sha256": "26d3c8656a83b06b293b15251617fe2c2c493f842a95b3d9b2ee45b3209d5fac", "sha512": "01f48fa1671cdc9e4d6866b9b237430f1b9b7093cbbed57fb010dc3db84a754a7a0457c5fd968d4e693ca74bdc1c7f15efb55f2af2ea236354944cffc8d4efd8", "compromised_hosts": [], "extracted_files": [], "analysis_start_time": "2019-01-20T02:50:01-06:00", "tags": [], "imphash": null, "total_network_connections": 0, "av_detect": null, "total_signatures": 0, "submit_name": "Proofpoint_R_Logo (1).png", "ssdeep": null, "md5": "48703c5d4ea8dc2099c37ea871b640ef", "error_origin": null, "processes": [], "sha1": "5b30e297b54ef27ffcda06aa212b5aa6c5424e1c", "url_analysis": false, "type": "PNG image data, 1200 x 413, 8-bit/color RGBA, non-interlaced", "file_metadata": null, "vx_family": null, "threat_score": null, "verdict": null, "domains": [], "type_short": ["img"]}], "Entity": "26d3c8656a83b06b293b15251617fe2c2c493f842a95b3d9b2ee45b3209d5fac"}]
```






## Jobs



## Connectors


