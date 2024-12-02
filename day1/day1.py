# puzzle 1 day 1 of advent of code 2024
import numpy as np

def preprocess(filename):

    list = np.loadtxt(filename, dtype=int)
    # print(list.shape)
    list1, list2 = [], []
    for i in list:
        list1.append(i[0]), list2.append(i[1])

    list1.sort()
    list2.sort()
    return list1, list2

def part1(list1, list2):
    print(sum([abs(i-j) for i, j in zip(list1, list2)]))

def part2(list1, list2):
    list2_freq = {}

    for i in list2:
        if i in list2_freq:
            list2_freq[i] += 1
        else:
            list2_freq[i] = 1

    sum = 0
    # for i in list1:
    for i in list1:
        if i not in list2_freq.keys():
            freq = 0
        else:
            freq = list2_freq[i]
        
        sum+= i*freq
        

    print(sum)


list1, list2 = preprocess("input-real.txt")

# part1(list1, list2)
part2(list1, list2)


# sum = sum([abs(i-j) for i, j in zip(list1, list2)])