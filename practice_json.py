# JavaScript Object Notation (JSON) is a popular way to format data as a single human-readable string.
# Many websites offer JSON content as a way for programs to interact with the website.
# This is known as providing an application programming interface (API).
# Here is an example of data formatted as JSON:

"""{"name": "Zophie", "isCat": true,
 "miceCaught": 0, "napsTaken": 37.5,
 "felineIQ": null}"""

# json module handles all the details of translating between a string with JSON data and 
# Python values for the json.loads() and json.dumps() functions. 
import json

def example1():

	jsonData = '{"name": "Sophie", "isCat" : true, "miceCaught" : 0, "felineIQ": null}'

	# jsonDataAsPythonValue variable now holds: {'isCat': True, 'miceCaught': 0, 'name': 'Sophie', 'felineIQ': None}
	# loads stands for load string, it translates JSON data into a Python value, returning it as a dictionary
	jsonDataAsPythonValue = json.loads(jsonData)

	print jsonDataAsPythonValue

def example2():

	pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

	# The json.dumps() function (dump string) will translate a Python value into a string
	# of JSON-formatted data. Returns: '{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'
	stringOfJsonData = json.dumps(pythonValue)

	print stringOfJsonData

example1()
example2()

