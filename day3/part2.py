import re

def process_text(text):
    result = 0
    enbale = True
    for a,b, instruct in re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do(?:n\'t)?)\(\)', text):
        # print(a,b, instruct)
        if instruct == 'don\'t':
            enbale = False
        elif instruct == 'do':
            enbale = True
        elif enbale:
            yield int(a) * int(b)
            
    return result


with open("input-text.txt", "r") as file:
    text = file.read()


print(sum(process_text(text)))

# print(process_text(text))