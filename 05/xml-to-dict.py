import xmltodict

with open("sample.xml") as data:
    xml_example = data.read()

xml_dict = xmltodict.parse(xml_example)

print(xml_dict)

xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.55.3"

print(xmltodict.unparse(xml_dict, pretty=True))

with open("sample.xml", "w") as data:
    data.write(xmltodict.unparse(xml_dict, pretty=True))
