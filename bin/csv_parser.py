import csv

name = '2019-fa.csv'

output = []

def initialize():
    global name
    output = []
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        col_name = 3
        col_number = 4
        for row in csv_reader:
            output.append(''+row[col_name] + ' ' + row[col_number])
    return output

def python_list_write(array):
    with open('uiuc_classes.txt', 'w') as filehandle:
        for listitem in array:
            filehandle.write('%s\n' % listitem)

def python_list_read(array):
    with open('uiuc_classes.txt', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            array.append(currentPlace)
    return array

if __name__ == "__main__":
    output = initialize()
    python_list_write(output)
    print(output)