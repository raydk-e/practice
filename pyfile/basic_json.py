import json

# A json
x = '{"name":"tipu", "age":40, "location": "kolkata"}'

# parsing json by load method
y = json.loads(x)

print(y["location"])

# A python dict
p = [{"name":"titu", "age":37, "location": "jamshedpur"},
     {"name":"tikina", "age":35, "location": "dhamnagar"},
     {"name":"papuna", "age":12, "location": "bhubaneswar"}]



#making json
q = json.dumps(p)

file_name  = "/home/deepak/projects/practice/practice/datafile/basic_json.json"

with open(file_name, "w") as json_f:
    json.dump(q, json_f, indent=4)
