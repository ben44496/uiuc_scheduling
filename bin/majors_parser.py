import json
import re

file_name = 'majors.json'

def open_json(name):
    try: 
        with open(name, 'r') as json_file:
            return json.load(json_file)
    except:
        print("File not found")

"""
    1. request major,
    2. do recursive check for 
"""

def initialize(major):
    classes = {"CS 125", "CS 126", "CS 173"} ##
    if major is None:
        print("Major is null")
    print(major['credits'])
    print(major['min_t_gpa'])
    print(major['min_o_gpa'])
    print(requirement_completed(classes, major['AND']))

def add_to_dict(requirement):
      name = requirement['name']
      

def OR_regular(classes, requirement):
    number = requirement['choose']
    unfinished = {}
    for i in requirement['classes']:                # Count how many classes fulfilled
        if number >= 0:
            if i in classes:
                number -= 1
    if number > 0:                                  # If there remains at least one class unfulfilled, we have to return the req.
        # name = requirement.name
        # for key, value in requirement.__dict__.items():
        #     unfinished[key] = value # add requirement to unfinished
        unfinished.


def AND(classes, requirement):
    # parse the classes, if there be any
    # then run requirement completed on each one, which will check for and and ors
    unfinished = {}
    if not requirement['classes'] is None:
        for i in requirement['classes']:
            if not i in classes:
                unfinished['classes'] = requirement
                break
    for key, value in requirement.__dict__.items():
        if re.search("OR.+", key):
            OR_regular(classes, i)

def requirement_completed(classes, requirement):
    if requirement.name is 'AND':
        AND(classes, requirement)
    elif requirement.name is 'OR':
        OR_regular(classes, requirement)

data = open_json(file_name)
initialize(data['computer_science'])
