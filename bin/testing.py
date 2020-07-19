import json
import re
import traceback

            

def major_check(classes, major):
    output = {}
    if major is None:
        print("Major is null")
        return None
    try:
        output['credits'] = major['credits']
        output['credits'] = major['credits']
        output['min_t_gpa'] = major['min_t_gpa']
        output['min_o_gpa'] = major['min_o_gpa']
        output['min_o_gpa'] = major['min_o_gpa']
        output['AND'] = AND(classes, major["AND"])
        return output
    except Exception as exp:
        print("Something went wrong (major_check())")
        # print(type(exp))
        # print(exp)
        traceback.print_exc()
        return None
    return None

# def requirement_completed(classes, requirement):
#     try:
#         if requirement.name is 'AND':
#             AND(classes, requirement)
#         elif requirement.name is 'OR':
#             OR_regular(classes, requirement)
#     except:
#         print("Requirement not found")

def OR_regular(classes, requirement):
    if requirement is None:
        print("No requirement input")
        return
    number = requirement['choose']
    # unfinished = {}
    print(requirement)
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
    unfinished['key'] = requirement['key']
    unfinished['description'] = requirement['description']
    if "classes" in requirement.keys():
        for i in requirement['classes']:
            if not i in classes:
                unfinished['classes'] = requirement['classes']
    # return recur(unfinished, classes, requirement)
    for key, value in requirement.items():
        if re.search("OR_focus_area", key):
            ofa = OR_focus_area(classes, requirement["OR_focus_area"])
            if not ofa is None:
                unfinished[ofa['key']] = ofa
        if not re.search("OR_focus_area", key) and re.search("OR.+", key):
            o = OR_regular(classes, requirement[key])
            if not o is None:
                unfinished[o['key']] = o
        if re.search("AND", key):
            a = AND(classes, requirement[key])
            if not a is None:
                this_name = a['key']
                unfinished[this_name] = a
    return unfinished

def OR_focus_area(classes, requirement):
    number = requirement['choose']
    for key, value in requirement['groups'].items():
        print(value)
        if OR_regular(classes, value["OR"]) is None:
            number -= 1
        if number <= 0:
            return
    return requirement

# def recur(input, classes, requirement):
#     unfinished = input 
#     for key, value in requirement.items():
#         if re.search("OR_focus_area", key):
#             ofa = OR_focus_area(classes, requirement["OR_focus_area"])
#             if not ofa is None:
#                 unfinished[ofa['key']] = ofa
#         if re.search("OR.+", key):
#             o = OR_regular(classes, requirement[key])
#             if not o is None:
#                 unfinished[o['key']] = o
#         if re.search("AND", key):
#             a = AND(classes, requirement[key])
#             if not a is None:
#                 this_name = a['key']
#                 unfinished[this_name] = a
#     return unfinished
    



# ENG 100, IB 150
classes = ["MATH 347", "CS 427", "CS 440", "CS 446", "CS 543", "IB 150", "PHYS 211", "PHYS 212", "MATH 221", "MATH 231", "MATH 241", "MATH 415", "CS 125", "CS 126", "CS 173", "CS 210", "CS 225", "CS 233", "CS 241", "CS 357", "CS 361", "CS 374", "CS 421"]
majors = ["computer_science", "mathematics"]

def run(classes, args, input_fname, output_fname):
    with open(input_fname) as f:
        data = json.load(f)
    out = {}
    for i in args:
        try:
            out[i] = major_check(classes, data[i])
        except:
            print("Invalid major entered: ", i)
    with open(output_fname, 'w') as fi:
        json.dump(out, fi)

run(classes, majors, 'majors.json', 'testing2.json')



