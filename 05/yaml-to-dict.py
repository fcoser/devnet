import yaml

with open("sample.yaml") as data:
    yaml_sample = data.read()

yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)

print(type(yaml_dict))

print(yaml_dict)

yaml_dict["interface"]["name"] = "GigabitEthernet1"

print(yaml.dump(yaml_dict, default_flow_style=False))


#escrever mudanças no arquivo

with open("sample.yaml", "w") as data:
    data.write(yaml.dump(yaml_dict, default_flow_style=False))
