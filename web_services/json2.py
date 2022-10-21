import json


data='''
[
    {
        "name" : "Chuck",
        "ID" : "001",
        "x" : "2"
    },
    {
        "name" : "Chuck",
        "ID" : "009",
        "x" : "7"
    }
]'''

info= json.loads(data)
print('User count: ', len(info))

for items in info:
    print('Name: ', items["name"])
    print('ID: ', items["ID"])
    print('Attribute: ', items["x"])