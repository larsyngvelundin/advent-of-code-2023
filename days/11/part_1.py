example = 0
file_name = "days/11/data.txt"
if example:
    file_name = "days/11/example_data.txt"

file = open(file_name, "r")

data = []

def printm(data):
    for line in data:
        print(line)

for line in file:
    line = line.rstrip("\n")
    print(line)
    data.append(line)
    
#print(data)
def flip_map(data):
    new_data = [""] * len(data[0])
    print (new_data)
    for row in data:
        for i in range(0, len(row)):
            new_data[i] += row[i]
    return new_data

#duplicate all horizontal rows with only space 
def fix_expanse(data):
    y = 0
    while y < len(data):
        if(data[y] == "."*len(data[y])):
            data.insert(y, data[y])
            print(f"Inserting {data[y]} at {y}")
            y += 1
        y += 1
    return data
data = fix_expanse(data)
#printm (data)

data= flip_map(data)
#printm(data)

data = fix_expanse(data)
data = flip_map(data)
#printm(data)
#duplicate all vertical rows with only

galaxies = []

for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if data[y][x] == "#":
            galaxies.append([x,y])


print(galaxies)
g = galaxies

t = 0

for i in range(0, len(g)-1):
    #print("new i")
    for j in range(i+1, len(g)):
        #print(f"comparing {g[i]} and {g[j]}")
        dist = 0
        dist += (abs(g[i][0] - g[j][0]))
        dist += (abs(g[i][1] - g[j][1]))
        t += dist

print(t)