
# TemplateEngine

Template Engine integration provides the ability to render templates using Jinja2. Jinja2 provide fast and flexible ways to create rich templates. These templates can be used in entity insights, emails, ticketing systems, or any action that can take in a text string.
Jinja2 documentation can be found at https://jinja.palletsprojects.com/en/2.11.x/ 

Python Version - 2



## Actions
#### Ping
Check connectivity
Timeout - 600 Seconds



##### JSON Results
```json
{}
```



#### Entity Insight
This action will use a Jinja2 template to create Entity Insights from a JSON object.  The input JSON object must be in the format of EntityResult.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|JSON Object|The raw JSON object that will be used to render the template.  |True|Content|{}|
|Template|The Jinja2 template to display.  Can be a HTML template from "Settings->Environment" or added in content box.|False|Email Content||
|Triggered By|The name of the integration that triggered this entity insight.|True|String|Siemplify|
|Remove BRs|Remove all <br> tags from the rendered template.|False|Boolean|false|
|Create Insight|When enabled, the action will create entity insights.  Default value of true.|False|Boolean|true|



##### JSON Results
```json
{}
```



#### Render Template
This action will render a Jinja2 template using a JSON input.  
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|JSON Object|The raw JSON object that will be used to render the template.  This value is available as the variable input_json in the Jinja template.|False|Content|{}|
|Jinja|The Jinja template code to be rendered.  Will override Template parameter. Append |safe to disable HTML encoding.|False|Code||
|Include Case Data|When enabled, entity attributes and event data are available under the variables input_json['SecurityEvents'] and input_json['SecurityEntities']|False|Boolean|false|
|Template|The Jinja2 template to be rendered.  Can be a HTML template from "Settings->Environment" or added in content box.|False|Email Content||



##### JSON Results
```json
{}
```






## Jobs



## Connectors


