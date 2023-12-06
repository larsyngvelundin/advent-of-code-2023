from parse import parse_data_2 as parse_data
from time import time

time_to_race, record = parse_data(example=0)
print(f"time: {time_to_race}")
print(f"record: {record}")

def main_brute():
    winners = 0
    for start in range(0, time_to_race):
        time_after_start = time_to_race - start
        race_time = time_after_start * start
        if(race_time > record):
            winners += 1
    print(f"Result: {winners}")

def main_binary():
    print(f"not done")

if __name__ == '__main__':
    start_time_total = time()
    main_brute()
    end_time = time()
    elapsed_time = end_time - start_time_total
    print(f"- Total time: {elapsed_time:.8f}")

    start_time_total = time()
    main_binary()
    end_time = time()
    elapsed_time = end_time - start_time_total
    print(f"- Total time: {elapsed_time:.8f}")