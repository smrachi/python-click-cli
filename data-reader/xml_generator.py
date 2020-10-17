"""Creating an XML file

this program creates an xml file and saves it including the xml 
declaration line.
"""

import xml.etree.ElementTree as ET

tree = ET.ElementTree("tree")

document = ET.Element("outer")
node1 = ET.SubElement(document, "inner")
node1.text = "text"

tree._setroot(document)
tree.write("./output.xml", encoding="UTF-8", xml_declaration=True)	