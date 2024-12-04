
with open("test.txt", "r") as file:
    text = file.read()

print(''.join(text.split('\n')))