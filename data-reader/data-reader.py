#!/usr/bin/env python3

import click
import xml.etree.ElementTree as ET
from pathlib import Path
from ip_checker import IPAddress


@click.command()
@click.option("-s", "--source-ip", type = IPAddress(), help = "Set the source IP address")
@click.option("-p", "--source-port", type = int, help = "Set the source Port number")
@click.option("-d", "--dest-ip", type = IPAddress(), help = "Set the destination IP address")
@click.option("-P", "--dest-port", type = int, help="Set the destination Port number")
@click.option("--home", envvar = "HOME", hidden = True)
def connection(home, source_ip, source_port, dest_ip, dest_port):
	"""this function reads input arguments and stores data in xml config file."""
	
	xml_file_path = home + "/gitlab/python-click-cli/data-reader/ims_config.xml"
	xml_file = ET.parse(xml_file_path)
	xml_tree = xml_file.getroot()
	if xml_tree.tag != "ims":
		raise RuntimeError(f"{xml_file_path} is not an ims configurations file.")

	if source_ip:
		sourceIP = xml_tree.find("connection/sourceIP")
		sourceIP.text = source_ip
	
	if source_port:
		sourcePort = xml_tree.find("connection/sourcePort")
		sourcePort.text = str(source_port)
	
	if destination_ip:
		destinationIP = xml_tree.find("connection/destinationIP")
		destinationIP.text = dest_ip

	if destination_port:
		destinationPort = xml_tree.find("connection/destinationPort")
		destinationPort.text = str(dest_port)

	# if xml file consists elements with attributes
	# use this command:
	# 	xml_tree.find("connection/test").attrib['name'] = 'value'


	xml_file.write(xml_file_path, encoding="UTF-8", xml_declaration=True)

if __name__ == "__main__":
	connection()
