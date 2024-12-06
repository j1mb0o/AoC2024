# have M as the center, and then check all 8 directions for the other letters
import re
import sys


with open (sys.argv[1]) as f:
    lets = [[y for y in x] for x in f.read().split('\n')]
    

horizontal = ["".join(x) for x in lets]

vertical = ["".join(x) for x in zip(*lets)]

def get_diagonals(matrix):
    n = len(matrix)
    diagonals = []

    # Top-left to bottom-right diagonals
    for d in range(2 * n - 1):
        diagonal = []
        for i in range(max(0, d - n + 1), min(d + 1, n)):
            diagonal.append(matrix[i][d - i])
        diagonals.append(''.join(diagonal))

    # Top-right to bottom-left diagonals
    for d in range(2 * n - 1):
        diagonal = []
        for i in range(max(0, d - n + 1), min(d + 1, n)):
            diagonal.append(matrix[i][n - 1 - (d - i)])
        diagonals.append(''.join(diagonal))

    return diagonals
# Get diagonal strings
diagonal_strings = get_diagonals(lets)

every = horizontal + vertical + diagonal_strings

pattern  = r"(?=(XMAS|SAMX))"
cnt = 0

cnt = sum([int(len(re.findall(pattern, x))) for x in every])
# for x in every:
#     match = re.findall(pattern, x)
#     # if match:
#     cnt += int(len(match))
        # print(match)
print(cnt)