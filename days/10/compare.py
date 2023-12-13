import part_1_str
import part_1_xy
from time import time



def main():
    
    start_time_total = time()
    part_1_str.main()
    end_time = time()
    elapsed_time = end_time - start_time_total
    print(f"- Total time STR: {elapsed_time:.8f}")
    start_time_total = time()
    part_1_xy.main()
    end_time = time()
    elapsed_time = end_time - start_time_total
    print(f"- Total time XY: {elapsed_time:.8f}")

if __name__ == "__main__":
    main()

