import xml.etree.ElementTree as ET

stream = open('AwesomeFood.xml', 'r') # This opens the XML File 'AwesomeFood' I created for parsing

xml = ET.parse(stream) # This tell the script to Parse data into an Element Tree Object

root = xml.getroot() # This gets the "Root" Element of each Element Tree (The Parent!)

for e in root:
    print(ET.tostring(e))
    print(**)
    print(e.get(*Id*))