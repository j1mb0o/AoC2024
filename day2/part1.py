import numpy as np
import sys

def process_input(input_file):
    # return [line.split() for line in input.splitlines()]
    with open(input_file) as f:
        reports = f.readlines()
    # print(reports)
    # x = "a b c"
    # reports = x.split()
    reports = [list(map(int, report.split()))  for report in reports ]

    return reports

def safe(report):
    if (
        not (report == np.sort(report)).all() and
        not (report == np.sort(report)[::-1]).all()
    ):
        return False # can't be fixed
    
    for i in range(len(report)-1):
        if (np.abs(report[i] - report[i+1]) < 1 or 
            np.abs(report[i] - report[i+1]) >3):
            return False
    
    return True


reports = process_input(sys.argv[1])
print(sum([safe(report) for report in reports]))