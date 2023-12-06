import re

def parse_data(example=False): #messy, but works hehe
    file_name = "data.txt"
    if example:
        file_name = "example_data.txt"
    times = []
    records = []
    with open(f"days/6/{file_name}", 'r') as file:
        first_line = True
        for line in file:
            line = line.rstrip('\n')
            line = re.sub(' +', ' ', line)
            if(first_line):
                first_line = False
                times = line[6:].split(" ")
                for i in range(0,len(times)):
                    times[i] = int(times[i])
            else:
                records = line[10:].split(" ")
                for i in range(0,len(records)):
                    records[i] = int(records[i])
                break
    return times, records


def parse_data_2(example=False): #messy, but works hehe
    file_name = "data.txt"
    if example:
        file_name = "example_data.txt"
    time = 0
    record = 0
    with open(f"days/6/{file_name}", 'r') as file:
        first_line = True
        for line in file:
            line = line.rstrip('\n')
            line = re.sub(' +', '', line)
            if(first_line):
                first_line = False
                time = int(line[5:])
            else:
                record = int(line[9:])
    return time, record
