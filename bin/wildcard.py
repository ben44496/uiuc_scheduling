"""
We want to read for input like the following:
- CS * 
- CS 1*
- * 100             # Means all major's 100 courses
- *                 # Means all classes at uiuc
"""
import uiuc_api as ua
import re
import json
import csv_parser as cp
import sys

# Queries api with argument array
def query_api(argument):
    info = {}
    for i in argument:
        try:
            myclass = ua.get_course(i)
            name = myclass.name
            for key, value in myclass.__dict__.items():
                if key == 'standing' and not value is None:
                    info[str(key)] = str(value.name)
                else: 
                    info[str(key)] = value
        except:
            print("Class not found:", i)
    return info

# Queries your json file of all the classes
def query_json(argument, jfile):
    classes = {}
    info = {}
    with open(jfile) as f:
        classes = json.load(jfile)
    for i in argument:
        try: 
            info[i] = classes[i]
        except:
            print("Class not found:", i)
    return info

        
def parse_wildcard(input):
    classes = cp.initialize() # Initializes an array of all possible classes
    input_array = [] # This array is for separating class name and class number
    output = {} # This dictionary is what we will output at the end
    s = "\A"
    if input is None:
        print("Input is null")
        return
    else: ### maybe we don't need to split it and parse it as a string into regex
        input_array = input.split(" ")
        try: 
            for i in input_array[0]:
                if i is "*":
                    s = s + ".+"
                else:
                    s = s + i
        
            s = s + "\s"
            for i in input_array[1]:
                if i is "*":
                    s = s + ".+"
                else:
                    s = s + i
        except:
            print("If you want all classes, do '* *'\nYou need to have two arguments for this to work.")
        s = s + "\Z"
    parse(s)

def parse(input):
    classes = cp.initialize()
    output = []
    for class_name in classes:
        if re.search(input, class_name):
            output.append(class_name)
    print(output)
    return output

#parse_wildcard("CS 22*")

if __name__ == "__main__":
    for i in sys.argv[1:]:
        parse_wildcard(i)

# r"\ACS\s" => CS *
# r"\s1.+\Z" => * 1--
# r"\s21.+\Z" => * 21-
# r"\ACS\S2.+\Z" => CS 2--
