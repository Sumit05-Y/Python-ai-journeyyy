"""Create a dict with your name, age, and a list of 3 skills
Convert it to a JSON string using json.dumps()
Print the string and its type (should be str)
Convert that string back into a dict using json.loads()
Print the result and its type (should be dict)"""


import json

user_details = { 
    "Name" : "RAM",
    "Age" : 21,
    "Skills" : ["Python","Ai","Machine learning"]

}

data = json.dumps(user_details)
print(f"{type(data)} is the DATA TYPE after using dumps.")

data1=json.loads(data)
print(data1)
print(f"{type(data1)} is the DATA TYPE after using loads.")

