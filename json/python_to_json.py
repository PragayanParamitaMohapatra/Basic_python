import json
dict={"name":"guddi","age":25,"addr":"bnj"}
print(type(dict))
print(dict)
json_data=json.dumps(dict)
print(type(json_data))
print(json_data)