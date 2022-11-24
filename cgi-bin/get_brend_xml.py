import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import db
import cgi
import xml.etree.ElementTree as ET

brends = db.get_all_brend_joined()

root = ET.Element('brends')
for brend in brends:
    brend_element = ET.SubElement(root, 'brend')
    brend_name = ET.SubElement(brend_element, 'name_brend')
    brend_name.text = brend[1]
    brend_country = ET.SubElement(brend_element, 'country')
    brend_country.text = brend[2]

tree = ET.ElementTree(root)
ET.indent(tree)

print(f'Content-Type: application/octet-stream; name="brends.xml"\n')
ET.dump(tree)