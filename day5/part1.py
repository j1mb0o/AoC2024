import re 
import sys
import numpy as np

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

good_lines = [] 
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

res = np.sum([line[len(line)//2] for line in good_lines])
print(res)


