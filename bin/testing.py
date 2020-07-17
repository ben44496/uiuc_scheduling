import json
import re


def initialize(major):
    classes = {"CS 125", "CS 126", "CS 173"} ##
    if major is None:
        print("Major is null")
    print(major['credits'])
    print(major['min_t_gpa'])
    print(major['min_o_gpa'])
    print(requirement_completed(classes, major['AND']))

def requirement_completed(classes, requirement):
    try:
        if requirement.name is 'AND':
            AND(classes, requirement)
        elif requirement.name is 'OR':
            OR_regular(classes, requirement)
    except:
        print("Requirement not found")

def OR_regular(classes, requirement):
    if requirement is None:
        print("No requirement input")
        return
    number = requirement['choose']
    # unfinished = {}
    for i in requirement['classes']:                # Count how many classes fulfilled
        if number > 0:
            if i in classes:
                number -= 1
    if number > 0:                                  # If requirement unsatisfied, return req.
        return requirement


def AND(classes, requirement):
    # parse the classes, if there be any
    # then run requirement completed on each one, which will check for and and ors
    unfinished = {}
    unfinished['name'] = requirement['name']
    unfinished['description'] = requirement['description']
    if "classes" in requirement.keys():
        for i in requirement['classes']:
            if not i in classes:
                unfinished['classes'] = requirement['classes']
    for key, value in requirement.items():
        if re.search("OR_focus_area", key):
            ofa = OR_focus_area(classes, requirement["OR_focus_area"])
            if not ofa is None:
                unfinished[ofa['name']] = ofa
        if re.search("OR.+", key):
            o = OR_regular(classes, requirement[key])
            if not o is None:
                unfinished[o['name']] = o
        if re.search("AND", key):
            a = AND(classes, requirement[key])
            if not a is None:
                this_name = a['name']
                unfinished[this_name] = a
    return unfinished
    

def OR_focus_area(classes, requirement):
    number = requirement['choose']
    for i in requirement['groups']:
        if OR_regular() is None:
            number -= 1
        if number <= 0:
            return
    return requirement

def recur(classes, requirement):
    for i in requirement:
        if re.search("OR_focus_area", i):
            OR_focus_area(classes, requirement)
        if re.search("OR.+", i):
            OR_regular(classes, requirement)
        if re.search("AND", i):
            AND(classes, requirement)
    




classes = ["AE 202", "ENG 100", "PHYS 211", "PHYS 212", "MATH 221", "MATH 231", "MATH 241", "MATH 415", "CS 125", "CS 126", "CS 173", "CS 210", "CS 225", "CS 233", "CS 241", "CS 357", "CS 361", "CS 374", "CS 421"]

with open('testing.json') as f:
    data = json.load(f)

# a = OR_regular(classes, data['AND']['OR_science'])
b = AND(classes, data["AND"])
print(b)

with open('testing2.json', 'w') as outfile:
    json.dump(b, outfile)


    # for i in requirement.key():
    #     if re.search(r"OR.+", i) and not re.search(r"OR_focus_area", i):
    #         o = OR_regular(classes, i)
    #         unfinished[o['name']] = o
    #     elif re.search(r"OR_focus_area", i):
    #         OR_focus_area(classes, i)
    #     elif re.search(r"AND", i):
    #         AND(classes, i)
    # return unfinished