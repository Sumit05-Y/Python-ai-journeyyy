"""Create a dict with your name, age, and a list of 3 skills
Save it to a file called profile.json using with open(...) and json.dump()
Load it back from profile.json using with open(...) and json.load()
Print all the values """

import json

user_details = { 
    "Name" : "RAM",
    "Age" : 21,
    "Skills" : ["Python","Ai","Machine learning"]

}
with open("profile.json","w") as f:
    json.dump(user_details,f,indent=4)


with open("profile.json","r") as f:
    data = json.load(f) 
    print(data)
