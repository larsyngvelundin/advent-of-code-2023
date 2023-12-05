from parse import parse_data

drs = 0
srs = 1
rl = 2

data = parse_data(example=False)

mini = 99999999999999
for seed in data["seeds"]:
  curr = int(seed)
  for map in data['order']:
    for set in data[map]:
      if(curr >= set[srs]
      and curr <= set[srs] + set[rl]):
        curr += set[drs] - set[srs]
        break
  if (curr < mini):
    mini = curr
print(f"Lowest is {mini}")