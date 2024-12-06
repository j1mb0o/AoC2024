import numpy as np

with open("input-real.txt", "r") as file:
    data =  [[y for y in x] for x in file.read().split('\n')]

npdata = np.array(data)

x_limits, y_limits= (1, npdata.shape[0]-1), (1, npdata.shape[1]-1) 

pos_list = ["MAS", "SAM"]
cnt = 0
for x in range(npdata.shape[0]):
    for y in range(npdata.shape[1]):
        if npdata[x, y] == "A":
            if npdata[x-1:x+2, y-1:y+2].size != 9:
                continue
            sub_array = npdata[x-1:x+2, y-1:y+2]
            # print(sub_array)
            diag1 = "".join(sub_array.diagonal())
            diag2 = "".join(np.fliplr(sub_array).diagonal())
            # print(diag1, diag2)
            if (diag1 in pos_list) and (diag2 in pos_list):
                cnt+=1
                # print(npdata[x-1:x+2, y-1:y+2])

print(cnt)