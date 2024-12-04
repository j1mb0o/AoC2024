import re

pattern = r"mul\(\d{1,3},\d{1,3}\)"

with open("input-text.txt", "r") as file:
    text = file.read()

text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"



# matches = re.findall(pattern, text)

# # ['mul(2,4)', 'mul(32,64)', 'mul(11,8)', 'mul(8,5)']
# # turn into multiplication 
# # print(matches)  
# result = 0
# for match in matches:
#     numbers = re.findall(r"\d{1,3}", match)
#     print(numbers)
#     num1 = int(numbers[0])
#     num2 = int(numbers[1])
#     result += num1 * num2
# #     text = text.replace(match, str(result))

# print(result)
# # print(text)