# this program uses the openweathermap.org API to get today's weather for a given city.

# sample api output by city for today's weather API looks like:

"""
...
u'name': u'Seattle',
 u'sys': {u'country': u'US',
          u'id': 2949,
          u'message': 0.1652,
          u'sunrise': 1513612396,
          u'sunset': 1513642748,
          u'type': 1},
 u'visibility': 16093,
 u'weather': [{u'description': u'light rain',
               u'icon': u'10n',
               u'id': 500,
               u'main': u'Rain'}],
 u'wind': {u'deg': 190, u'gust': 9.8, u'speed': 5.7}}
 ...
 """

from pprint import pprint
import json
import requests

# we get this URL from openweather site in the API section, the %appid is the API key necessary to query the data
# you get this key once you register on the site
url = 'http://api.openweathermap.org/data/2.5/weather?q=Seattle,us&appid=53b2d8d20b123f16babfd6d100da8ea6'

# we read the URL using the request module
response = requests.get(url)

# since the API data is in a json format, we need to convert it to a python file
# using json.loads method, which returns the data as a dictionary
jsonDataAsPythonValue = json.loads(response.text)

#pprint simply stands for pretty print, where it shows all the data in a nice, structred way
pprint(jsonDataAsPythonValue)

# gets the name of the city by referencing the name key in the API dictionary
print "the weather in %s today is:" % jsonDataAsPythonValue['name']

# prints the main weather status as well as the description by referencing relevant API keys
# the 0 inbetween weather & main is necessary because once you get into weather, everything else
# is in a list as one big value, so you reference that value first, and then the other key
print jsonDataAsPythonValue['weather'][0]['main'], '-', jsonDataAsPythonValue['weather'][0]['description'] 




