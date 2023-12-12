from parse import parse_data

data = parse_data(example=1)

all_chars = "|-LJ7F"


up, right, down, left = 0, 1, 2, 3
print(up, right, down, left)
directions = {
    '-': [False, True, False, True],
    '|': [True, False, True, False],
    'L': [True, True, False, False],
    'J': [True, False, False, True],
    '7': [False, False, True, True],
    'F': [False, True, True, False],
    '.': [False, False, False, False],
    'X': [False, False, False, False],
    'S': [True,True,True,True]
}
d = directions #for easier access

def check_if_matching_v(first,second):
    f, s = first, second
    if(d[f][right] and d[s][left]):
        return [True]
    if(d[f][right] and not d[s][left]):
        return [False, 1]
    if(not d[f][right] and d[s][left]):
        return [False, 2]
    if(not d[f][right] and not d[s][left]):
        return [False, None]
    return("something went wrong :(")

# 7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ

#['X', 'X', '7', 'J', 'J']
#X
#X
#7
#J
#J
def check_if_matching_h(first,second):
    f, s = first, second
    if(d[f][down] and d[s][up]):
        return [True]
    if(d[f][down] and not d[s][up]):
        return [False, 1]
    if(not d[f][down] and d[s][up]):
        return [False, 2]
    if(not d[f][down] and not d[s][up]):
        return [False, None]
    return("something went wrong :(")


for y in range(0, len(data)):
    data_test = list(data[y])
    x = 0
    while x < len(data_test)-1:
    # for x in range(0,len(data_test)-1):
        res = check_if_matching_v(data_test[x],data_test[x+1])
        # print(res)
        if (not res[0]):
            if (res[1]):
                data_test[x + res[1] - 1] = "X"
                # print(f"before{x}")
                x -= 2
                # print(f"after{x}")
        x += 1
    data[y] = "".join(data_test)

for row in data:
    print(row)

for x in range(0, len(data[0])):
    data_test = ""
    for y in range(0, len(data)):
        data_test += data[y][x]
    data_test = list(data_test)
    print(f"The data_Test in x is : {data_test}")
    y = 0
    print("NEW Y LOOP NEW Y LOOP NEW Y LOOP NEW Y LOOP NEW Y LOOP NEW Y LOOP ")
    while y < len(data_test)-1:
    # for x in range(0,len(data_test)-1):
        print("==================")
        print(f"Trying to check if valid:\n{data_test[y]}\n{data_test[y+1]}")
        res = check_if_matching_h(data_test[y],data_test[y+1])
        # print(res)
        if (not res[0]):
            if (res[1] and data_test[y + res[1] - 1] != "S"):
                data_test[y + res[1] - 1] = "X"
                print(f"data_test here: {data_test}")
                print(f"Tried to add X at {y + res[1] - 1}")
                # print(f"before{x}")
                y -= 2
                # print(f"after{x}")
        y += 1
    # data[y] = "".join(data_test)

# pivot_2d(data)


for row in data:
    print(row)
    # if data[]