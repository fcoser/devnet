import json

with open("sample.json") as data:
    json_data = data.read()

json_dict = json.loads(json_data)

print(type(json_dict))


print(json_dict)

json_dict["interface"]["description"] = "Backup Link"

print(json_dict)

with open("sample.json", "w") as data:
    json.dump(json_dict, data, indent = 4)

with open("sample.json") as data:
    json_data = data.read()
    print(json_data)
