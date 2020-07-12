import xml.etree.ElementTree as ET

tree = ET.parse('AwesomeFood.xml')

root = tree.getroot()

for child in root:
    print(root.text)
    print(child.tag)
    for subelem in child:
        print(subelem.text)
    print()
    