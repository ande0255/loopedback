import xml.etree.ElementTree as ET

tree = ET.parse('AwesomeFood.xml')

root = tree.getroot()

for child in root:
    print(child.tag)
    print(child.attrib)
    for subelem in child:
        print(subelem.text)