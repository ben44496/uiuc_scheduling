"""
    Author: Benjamin Nguyen
    Linkedin: linkedin.com/in/benjamin-khac-nguyen

    This code is meant to query for a class (ie. "CS 125") and output it into a file
    named 'output.json'. This uses the uiuc_api library and is intended to supplement 
    information provided in the library for better user comprehension.
"""

import uiuc_api as ua                                       # Here we import the uiuc_api provided
import json                                                 # Import json for the json python library

args = ['CS 125']                                           # This is a list of classes we want to query (ex: Query for CS 125 info)

# This function concatenates all the classes you may want into a json line
def make_json(arr):
    out = {}
    for i in arr:
        out[i] = make_json_object(i)
        if out[i] == None:
            out.pop(i)
        print(i)
    return out

# This function makes sure everything is parsable to json file format
def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

# This function retrieves the info for each class
def make_json_object(strings):
    info = {}
    try:                                                    # Try/Except is added in case the class entered is invalid
        myclass = ua.get_course(strings)
        name = myclass.name
        for key, value in myclass.__dict__.items():
            if key == 'standing' and not value is None:     # This is to account for the enum "standing" from uiuc_api, only parsing if null
                info[str(key)] = str(value.name)
            else: 
                info[str(key)] = value
    except:
        return 
    return info

# This outputs all the class information and writes it to a new json file called 'output.json'
with open('output.json', 'w') as json_file:
    json.dump(make_json(args), json_file, default=set_default) 

