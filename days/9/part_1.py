from parse import parse_data

data = parse_data(example = 0)

def get_new_list(seq):
    new_seq = []
    for i in range(0, len(seq)-1):
        new_seq.append(seq[i+1] - seq[i])
    return new_seq

def check_if_all_zero(seq):
    return seq == [0]*len(seq)

def main():
    total = 0
    for seq in data:
        seq_total = 0
        while check_if_all_zero(seq) == False:
            seq_total += seq[-1]
            seq = get_new_list(seq)
        total += seq_total
    print(f"Full total: {total}")

if (__name__ == "__main__"):
    main()