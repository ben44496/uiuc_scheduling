import json

with open('major.json') as config_file:
    data = json.load(config_file)


# Must past in an array for it to work
def major(args):
    if args is None: 
        print("No major was entered. [libray.py]")
    else :
        for a in args:
            print(a, sep=', ', end='\n'); # debug
    return args
        

def major_conflicts(args):
    # We want to do hashtable of "core", and somehow eliminate redundancies

    if args is None: 
        print("No major was entered. [libray.py]")
    

    # for each major that we have, we want to take the credits, and compare it to what our max credits is.
    # if it is greater than we replace it with our existing value. at end we print out value.
    info = {
        "credits" : 0,
        "science_electives" : 0,
        "technical_electives" : 0,
        "electives" : 0,
        "min_t_gpa" : 0,
        "min_o_gpa" : 0,
        "core" : []
    }
    
    for maj in args:
        if data['majors'][maj]['credits'] > info["credits"]: # max credits
            info["credits"] = data['majors'][maj]['credits']
        
        if data['majors'][maj]['science_electives'] > info["science_electives"]: # max science_electives
            info["science_electives"] = data['majors'][maj]['science_electives']
        
        info["technical_electives"] += data['majors'][maj]['technical_electives'] # total technical electives
        
        if data['majors'][maj]['min_t_gpa'] > info["min_t_gpa"]: # max technical gpa
            info["min_t_gpa"] = data['majors'][maj]['min_t_gpa']
        
        if data['majors'][maj]['min_o_gpa'] > info["min_o_gpa"]: # max overall gpa
            info["min_o_gpa"] = data['majors'][maj]['min_o_gpa']

        for c in data['majors'][maj]['core']:
            var = []                            # Empty list for groupings
            satisfied = 1                       # This int will tell us if one of the requirements are already satisfied
            if isinstance(c, str):              # If it is a string and single, it will convert to a list
                var.append(c)
            else:                               # If it is already a list (in a grouping), reassigns pointer
                var = c
            
            for i in var:
                if i in info["core"]:
                    satisfied -= 1
            if satisfied > 0:
                info["core"].append(c) #### right now it does not account for the fact that there may be repeated version of groupings
                    
                
            
    return info
            
# completed - an array of classes that have been completed
# majors - what majors you are doing. 
# def tobe_completed(completed, majors):
    
    
    
    