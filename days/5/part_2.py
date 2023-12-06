from parse import parse_data
from time import time
import sys

drs = 0
srs = 1
rl = 2

data = parse_data(example=True)

for i in range(0, len(data['seeds'])):
  data['seeds'][i] = int(data['seeds'][i])

mini = 999999999999999

start_time_total = time()


def print_progress_bar(total, done, bar_length=50):
    """
    Prints a progress bar to the console given `total` and `done` values. :param total: The total amount (the value representing 100% completion)
    :param done: The amount of work done so far
    :param bar_length: The character length of the bar on the screen
    """
    percent = float(done) / total
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))
    end_time = time()
    elapsed_time = end_time - start_time_total
    # print(f"- Total time: {elapsed_time:.2f}")
    time_str = f"{elapsed_time:.2f}"

    sys.stdout.write("\rProgress: [{0}] {1}% {2}/{3} {4}".format(arrow + spaces, int(round(percent * 100)),done, total,time_str))
    sys.stdout.flush()

#calculate total amount of seeds
total_seeds = 0
for i in range(1, len(data['seeds']), +2):
  total_seeds += data['seeds'][i]

input(total_seeds)
done = 0

for i in range(0, len(data['seeds']), +2):
  for seed in range(data['seeds'][i], data['seeds'][i]+data['seeds'][i+1]):
    # input(f"Checking {data['seeds'][i]} to {data['seeds'][i] + data['seeds'][i + 1]}\nCurrently on {seed}")
    curr = int(seed)
    for map in data['order']:
      for set in data[map]:
        if(curr >= set[srs]
        and curr <= set[srs] + set[rl]):
          curr += set[drs] - set[srs]
          break
    if (curr < mini):
      mini = curr
    done += 1
    if (done % 1000000 == 0):
      print_progress_bar(total_seeds, done)
print(f"Lowest is {mini}")