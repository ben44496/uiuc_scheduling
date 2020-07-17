

# the purpose of this code is to list out the courses that need to be completed from the user's already completed courses

already_completed_courses = []

def xor(completed, req_courses):
    still_todo = req_courses
    for course in req_courses:
        var = check_req(completed, course)
        still_todo.remove(var)


def check_req(completed, requirement):
    if requirement in completed:
        return requirement
    else:
        return None

