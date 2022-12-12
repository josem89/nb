# GitSync

## Integrations
|Name|Description|
|----|-----------|
|Any.Run|Interactive online malware analysis service for dynamic and static research of most types of threats using any environments.|
|Arnaud Email Utilities||
|Connectors|A set of custom connectors created for Siemplify Community to power up automation capabilities.|
|EmailUtilities|A set of utility actions to assist with working with emails.  Includes actions to parse EMLs and analyze email headers.|
|Enrichment|A set of entity enrichment actions to assist in the managing of entity attributes.|
|Exchange|Integration provides support for Microsoft Exchange 2010 - 2019 and Microsoft Office365 mail servers. Integration uses Exchange Web Services (EWS) for communication. Integration includes a series of actions to send out emails and work with received emails, along with a connector to monitor specific mailboxes and ingest emails from that mailboxes as alerts to Siemplify for further analysis.|
|Exchange Extension Pack|Exchange Extension Pack integration works on Exchange Management Shell. The Exchange Management Shell is built on Windows PowerShell technology and provides a powerful command-line interface that enables the automation of Exchange administration tasks.|
|Falcon Sandbox|Falcon Sandbox is a high end malware analysis framework with a very agile architecture.|
|FileUtilities|A set of file utility actions created for Siemplify Community to power up playbook capabilities.  |
|Functions|A set of math and data manipulation actions created for Siemplify Community to power up playbook capabilities.  |
|Insights|A set of insight actions created for Siemplify Community to power up playbook capabilities.  |
|Lists|A set of tools to facilitate managing custom lists within Siemplify|
|Microsoft Azure Sentinel|Microsoft Azure Sentinel is a scalable, cloud-native, security information event management (SIEM) and security orchestration automated response (SOAR) solution. Azure Sentinel delivers intelligent security analytics and threat intelligence across the enterprise, providing a single solution for alert detection, threat visibility, proactive hunting, and threat response.|
|Microsoft Graph Mail|Microsoft 365 and Office 365 deliver the power of cloud productivity to businesses of all sizes, helping save time, money, and free up valued resources. The Microsoft 365 and Office 365 plans combine the familiar Microsoft Office desktop suite with cloud-based versions of Microsoft's next-generation communications and collaboration services (including Office for the web, Microsoft Exchange Online, Microsoft Teams, and Microsoft SharePoint Online) to help users be productive from virtually anywhere through the Internet. This integration uses Microsoft Graph Mail API to communicate with Microsoft 365 and Office 365 services.|
|Microsoft Teams|Microsoft Teams is a platform that combines workplace chat, meetings, notes, and attachmentsQuick Guide: you must first register your app at Microsoft App Registration Portal, Configure Microsoft Teams Integration, Run the action 'Get Authorization', Run the action 'Generate Token'.|
|TemplateEngine|Template Engine integration provides the ability to render templates using Jinja2. Jinja2 provide fast and flexible ways to create rich templates. These templates can be used in entity insights, emails, ticketing systems, or any action that can take in a text string.Jinja2 documentation can be found at https://jinja.palletsprojects.com/en/2.11.x/ |
|Threat Connect|Identify Manage and Block Threats Faster with Intelligence. Make informed decisions with ThreatConnect's in-platform analytics and automation.|
|Tools|A set of utility actions for data manipulation and common platform tasks to power up playbook capabilities. |
|UnshortenMe|Unshorten.me is a free service to Un-Shorten the URLs created by URL shortening services. Unshorten.me can un-shorten URLs created by different services like goo.gl (Google), fb.me (Facebook), t.co (Twitter), bit.ly, TinyURL, ow.ly among others.|
|VirusTotalV3|VirusTotal was founded in 2004 as a free service that analyzes files and URLs for viruses, worms, trojans and other kinds of malicious content. Our goal is to make the internet a safer place through collaboration between members of the antivirus industry, researchers and end users of all kinds. Fortune 500 companies, governments and leading security companies are all part of the VirusTotal community, which has grown to over 500,000 registered users.This integration was created using the 3rd iteration of VT API.|


## Connectors
|Name|Description|Has Mappings|
|----|-----------|------------|
|Microsoft Azure Sentinel Incident Connector v2|Fetches Incidents from Azure Sentinel.|True|
|Microsoft Graph Mail Connector|Connector can be used to fetch emails from the Microsoft Graph Mail service. Connector dynamic list can be used to filter specific values from the email body and subject parts using regexes. By default, regex is used to filter out the urls from the email.|True|
|Microsoft Graph Mail Connector 2|Connector can be used to fetch emails from the Microsoft Graph Mail service. Connector dynamic list can be used to filter specific values from the email body and subject parts using regexes. By default, regex is used to filter out the urls from the email.|True|


## Playbooks
|Name|Description|
|----|-----------|
|Process Azure Sentinel|An embedded workflow that can receive inputs and return an output.|
|Azure Sentinel||
|Entity Triage|An embedded workflow that can receive inputs and return an output.|
|Manual Case Enrichment||
|Process Attachments|An embedded workflow that can receive inputs and return an output.|
|Submit Files For analysis|An embedded workflow that can receive inputs and return an output.|
|Update Priority From Score|An embedded workflow that can receive inputs and return an output.|
|Analyze Headers|Block will analyze headers. |
|Attachments|An embedded workflow that can receive inputs and return an output.|
|Body Analysis|This block will scan the body string for spelling errors and ...|
|Certificate Check|An embedded workflow that can receive inputs and return an output.|
|Domain Investigation|Enriches URLs, Emails, Domains, and IP addresses with WHOIS information.  Will create domain entities and link to URLs and Emails.  Will set any domain that is less than 180 days old as suspicious.  Checks to see if domains are look a like domains. |
|Email Analysis Playbook||
|Sanitization|An embedded workflow that can receive inputs and return an output.|


## Jobs
|Name|Description|
|----|-----------|
|Push Content|Push all content of this platform to git|
|Sync AS Incidents Update||
|Sync AS Incidents||
|Sync Azure Sentinel Entities|Will create new entities in Siemplify Alerts from AS incidents|

