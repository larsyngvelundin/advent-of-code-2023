def parse_data(example=False): #messy, but works hehe
    file_name = "data.txt"
    if example:
        file_name = "example_data.txt"
    data = {}
    state = "seeds"
    maps = []
    with open(f"days/5/{file_name}", 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            if (state == "maps"):
                if (line.find("map") > 0):
                    state = (line[:line.find("map")-1])
                    data[state] = []
                    maps.append(state)
            elif(state == "seeds"):
                data[state] = line[7:].split(" ")
                state = "maps"
            else:
                if(len(line) >1):
                    nums = (line.split(" "))
                    for i in range(0,3):
                        nums[i] = int(nums[i])
                    data[state].append(nums)
                else:
                    state = "maps"
    data['order'] = maps
    return data