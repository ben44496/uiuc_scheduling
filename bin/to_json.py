import uiuc_api as ua
import json
import csv

name = '2019-fa.csv'
csv_classes = []

def csv_parser():
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        col_name = 3
        col_number = 4
        for row in csv_reader:
            csv_classes.append(''+row[col_name] + ' ' + row[col_number])

def make_json(arr):
    out = {}
    for i in arr:
        out[i] = make_json_object(i)
        if out[i] == None:
            out.pop(i)
        print(i)
    return out

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

def make_json_object(strings):
    info = {}
    try:
        myclass = ua.get_course(strings)
        name = myclass.name
        for key, value in myclass.__dict__.items():
            if key == 'standing' and not value is None:
                info[str(key)] = str(value.name)
            else: 
                info[str(key)] = value
    except:
        return 
    return info


csv_parser()


with open('output.json', 'w') as json_file:
    json.dump(make_json(csv_classes), json_file, default=set_default) 

