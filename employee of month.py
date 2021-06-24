work_hours = [('Bhanu',10000),('Sai',300),('Harshitha',990)]


def employee_check(work_hours):
    current_high = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_high:
            current_high = hours
            employee_of_month = employee
        else:
            pass
    print (employee_of_month, current_high)


employee_check(work_hours)





