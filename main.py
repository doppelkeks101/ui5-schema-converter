# Script that fetches SAPUI5 API metadata and converts it to XSD schema files
# 
# UI5 API examples
# https://sapui5.hana.ondemand.com/test-resources/sap/ui/core/designtime/apiref/api.json
# https://sapui5.hana.ondemand.com/test-resources/sap/m/designtime/apiref/api.json

import requests
import json
import sys
import xml.etree.ElementTree as ET
from string import Template

TEMPLATE = Template("https://sapui5.hana.ondemand.com/test-resources$package/designtime/apiref/api.json")

api = TEMPLATE.substitute(package="/sap/m")
print("API: " + api)

response = requests.get(api)
json = response.json()

print(len(json["symbols"]))