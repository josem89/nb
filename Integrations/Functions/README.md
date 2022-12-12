
# Functions

A set of math and data manipulation actions created for Siemplify Community to power up playbook capabilities.  

Python Version - 2



## Actions
#### Time Duration Calculator
The Time Duration Calculator will calculate the time that has elapsed/difference between two dates with time.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Input DateTime 1|The first input datetime value.  Supports either strftime format or "now" for the current time.|True|String||
|Input DateTime 1 Format|The strftime format of the DateTime string.https://strftime.org/|True|String|%Y-%m-%dT%H:%M:%S%z|
|Input DateTime 2|The second input datetime value.  Supports either strftime format or "now" for the current time.|True|String|now|
|Input DateTime 2 Format|The strftime format of Input DateTime 2.|True|String|%Y-%m-%dT%H:%M:%S%z|



##### JSON Results
```json
{}
```



#### Convert Time Format
Convert a datetime value from one format to another format.  
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Input|The input datetime value that will be converted.|True|String|<input val>|
|From Format|The datetime format the input string is in.  https://strftime.org/|True|String|X|
|To Format|The desired time format of the output.  Use Arrow time format.  https://arrow.readthedocs.io/en/stable/#supported-tokens|True|String|YYYY/MM/DD|
|Time Delta In Seconds|Shift parameter that allows to change the output actual time to either the future (positive) or past (negative). This shift is measured in seconds|True|String|0|
|Timezone|Output timezone|False|String||



##### JSON Results
```json
{}
```



#### SanitizeHTML
Given a fragment of HTML, SantizeHTML will parse it according to the HTML5 parsing algorithm and sanitize any disallowed tags or attributes. This algorithm also takes care of things like unclosed and (some) misnested tags.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Tags|Tags is the allowed set of HTML tags. Comma separated list. HTML tags not in this list will be escaped or stripped. |False|String|a,abbr,acronym,b,blockquote,code,em,i,li,ol,strong,ul,table,tr,td,th,h1,h2,h3,body,tbody,thead,div,footer,head,header,html,img,option,p,section,span,strong,svg|
|Attributes|Attributes lets you specify which attributes are allowed. Value should be a comma separated list.Default  {'a': ['href', 'title'], 'abbr': ['title'],|False|String|None|
|Styles|If you allow the style attribute, specify the allowed styles set, for example color and background-color. Value should be comma separated list.|False|String|None|
|Allow All Attributes|Set to True to allow all attributes.|False|Boolean|false|
|Input HTML|The HTML fragment that will be sanitized.|True|String||



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



#### Run JSONPath Query
The action runs an JSONPath Query on a given json and extracts values according to the expression.
View https://github.com/h2non/jsonpath-ng for more information on JSONPath
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Json|Json input|True|Code|None|
|JSONPath Expression|JSONPath expressions always refers to a JSON structure in the same way as XPath expressions are used in combination with an XML document.|True|String|None|



##### JSON Results
```json
{}
```



#### String Functions
This action includes basic Pythonic string functions as mentioned below - 
Lower - converts a string into lower case.
Upper - converts a string into upper case.
Count - returns the number of times a specified value occurs in a string.
Find - searches the string for a specified value and returns the position of where it was found.
IsAlpha - returns "True" if all characters in the string are in the alphabet.
IsDigit - returns "True" if all characters in the string are digits.
Replace - returns a string where a specified value is replaced with a specified value.
Strip - returns a trimmed version of the string.
Title - converts the first character of each word to uppercase.
Split - Splits the input string into a list using Param 1 as the separator.  Defaults to comma.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Param 2|The second parameter (this is an optional parameter as some functions require only 1 param)|False|String| |
|Param 1|The first parameter (this is an optional parameter as some functions require only 1 param)|False|String|None|
|Input|The input for the current fuction|True|String|Example|
|Function|Select the function you would like to run from the list|True|List|Lower|



##### JSON Results
```json
{}
```



#### XMLtoJson
Convert XML formatted data to JSON.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|xml|Convert XML to JSON|True|String|<e> <a>text</a> <a>text</a> </e>|



##### JSON Results
```json
{}
```



#### IP to Integer
Converts an IP address or list of IP addresses to integers or longs.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IP Addresses|Comma separated list of IP addresses to be converted into integers.|True|String||



##### JSON Results
```json
{}
```



#### Math Functions
A set of built-in Python functions - 
Abs - returns the absolute value of a number
Float - returns a floating point number
Display - converts the number to include commas where needed
Hex - converts a number into a hexadecimal value
Int - returns an integer number
Max - returns the largest item in an iterable 
Min - returns the smallest item in an iterable
Round - rounds a number
Sort - returns a sorted number
Sum - sums the items of an iterator
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Function|Select the Math Function you would like to run on the number|True|List|Max|
|Numbers|The numbers you would like to run the Math function on.|True|String|13.5,-90,566,11.32|



##### JSON Results
```json
{}
```



#### Math Arithmetic
A set of built in math operators:
Plus - returns a result for the sum of 2 arguments
Sub - returns a result for 1 argument minus the other
Multi - returns a result for 1 argument multiplied by the other
Div - returns a result for 1 argument divided by the other
Mod - returns the result of the percentage between 2 arguments
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Function|The function you would like to run on 2 given arguments |True|List|Plus|
|Arg 2|The second argument |True|String|{}|
|Arg 1|The first argument|True|String|{}|



##### JSON Results
```json
{}
```



#### Create Thumbnail
Creates a Base64 Thumbnail of an image.
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base64 Image|The Base64 string of the image.|False|String||
|Thumbnail Size|Comma separated.  Pixels.   X , Y|True|String|250,250|
|Input JSON|Input JSON|False|String||
|Image Key Path|If using Input JSON, the keypath for the image field.|False|String||



##### JSON Results
```json
{}
```






## Jobs



## Connectors


