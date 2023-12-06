from parse import parse_data
from time import time

times, records = parse_data(example=0)

def main_brute():
    winners = [0] * len(times)
    for i in range(0,len(times)):
        for start in range(0, times[i]):
            time_after_start = times[i] - start
            race_time = time_after_start * start
            if(race_time > records[i]):
                winners[i] += 1
    multsum = winners[0]
    for i in range(1, len(winners)):
        multsum *= winners[i]
    print(f"Result: {multsum}")

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