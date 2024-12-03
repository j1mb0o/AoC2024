import numpy as np
def process_input(input_file):
    # return [line.split() for line in input.splitlines()]
    with open(input_file) as f:
        reports = f.readlines()
    # print(reports)
    # x = "a b c"
    # reports = x.split()
    reports = [list(map(int, report.split()))  for report in reports ]

    return reports


def part1(reports):
    safe_reports = 0
    for report in reports:
        
        report_status, problem_level = safe(report=report)

        if report_status == 0 and problem_level != -100:
            print(f"Problematic report {report}")
            report.pop(problem_level)
            print(f"Before correction: {report_status=} {problem_level=}")
            report_status, problem_level = safe(report=report)
            print(f"After corection: {report_status=} {problem_level=}")
            safe_reports+=report_status
            # print(report_status, problem_level)
        else:
            safe_reports += report_status

        print()

    print(safe_reports)
        

def safe(report):
    if (
        not (report == np.sort(report)).all() and
        not (report == np.sort(report)[::-1]).all()
    ):
        return 0, -100 # can't be fixed
    
    for i in range(len(report)-1):
        if (np.abs(report[i] - report[i+1]) < 1 or 
            np.abs(report[i] - report[i+1]) >3):
            return 0, i
    
    return 1, 100 # all good

# def part2(reports):
#     safe_reports = 0
#     for report in reports:
#         if (
#             not (report == np.sort(report)).all() and
#             not (report == np.sort(report)[::-1]).all()
#         ):
#             continue
        
#         report_safe = True
#         fault_tol = 1
#         for i in range(len(report)-1):
#             if (np.abs(report[i] - report[i+1]) < 1 or 
#                 np.abs(report[i] - report[i+1]) >3):
#                 if fault_tol == 0:
#                     report_safe = False
#                     break
#                 fault_tol -= 1


#         if not report_safe:
#             continue
#         safe_reports+=1
#         print(report)
#     print(safe_reports)
    


if __name__ == "__main__":
    reports = process_input("input-sample.txt")
    # print(reports)
    part1(reports)
    # part2(reports)

