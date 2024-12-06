
import numpy as np
import re 
import sys

with open (sys.argv[1], "r") as file:
    file_contents = file.read()


rule_pattern = r"\d{1,3}\|\d{1,3}"
rules = re.findall(rule_pattern, file_contents)

no_rules = re.sub(rule_pattern, "", file_contents)

no_rules = no_rules.lstrip().split("\n")

no_rules_int = [list(map(int, rule.split(','))) for rule in no_rules]


ruleset = {}
for rule in rules:
    before, after = (rule.split("|"))
    before, after = int(before), int(after)
    if before not in ruleset:
        ruleset[int(before)] = []
    ruleset[int(before)].append(int(after))

def get_good_bad_lines(lines):

    good_lines = [] 
    bad_lines = []
    for line in no_rules_int:
        line_good = True
        
        for i in range(len(line)):

            if line[i] in ruleset.keys():
                # 
                numbers_before = line[:i]
                if np.isin(np.array(numbers_before), np.array(ruleset[line[i]])).any():
                    # 
                    line_good = False
                    break
        if line_good:
            good_lines.append(line)
        else:
            bad_lines.append(line)

    
    return good_lines, bad_lines

def fix_line(line):
    i = 0
    while i < len(line):
        if line[i] in ruleset.keys():
            numbers_before = line[:i]
            if np.isin(np.array(numbers_before), np.array(ruleset[line[i]])).any():
                # 
                fault = np.isin(np.array(numbers_before), np.array(ruleset[line[i]]))
                fault_index = np.where(fault == True)[0][0]
                # print(fault)
                # print(fault_index)
                # print(f"Before {line}")
                line[fault_index], line[i] = line[i], line[fault_index]
                # print(f"After {line}")
                i = 0
                continue
        i += 1

    return line

# first sort
good_lines, bad_lines = get_good_bad_lines(no_rules_int)

fixed_sum = 0
fixed = []
# while len(bad_lines) > 0:

for line in bad_lines:
    # print(f"Before fixing: {line}")    
    # print(f"After  fixing: {fix_line(line)}")
    fixed.append(fix_line(line))
    # print(line)
# print(bad_lines)
# good_lines.clear()
# new_good_lines, bad_lines = get_good_bad_lines(bad_lines)

# fixed_sum += sum(middle_good)



fixed

middle_fixed = [i[len(i)//2] for i in fixed]
middle_fixed
print(sum(middle_fixed))

