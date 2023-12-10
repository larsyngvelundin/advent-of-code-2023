from parse import parse_data

data = parse_data(example = 1)

print(data)

# for seq in data:
#     print(f"###New sequence###")
#     end_values = []
#     current_range = 0
#     for i in range(0, len(seq)-1):
#         print(seq[i+1] - seq[i])


def get_new_list(seq):
    new_seq = []
    for i in range(0, len(seq)-1):
        new_seq.append(seq[i+1] - seq[i])
    return new_seq

def check_if_all_zero(seq):
    return seq == [0]*len(seq)

def main():
    for seq in data:
        while check_if_all_zero(seq) == False:
            print(f"Checking {seq}")
            seq = get_new_list(seq)
            input("")

if (__name__ == "__main__"):
    main()