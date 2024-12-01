

with open("1.txt") as infile:
    lines = infile.read().splitlines()
pairs = [raw.split("   ") for raw in lines]
list1, list2 = zip(*pairs)
list1 = sorted(list(list1))
list2 = sorted(list(list2))

cumulative_distance = 0
for pair in zip(list1, list2):
    cumulative_distance += abs(int(pair[0])-int(pair[1]))
print(cumulative_distance)