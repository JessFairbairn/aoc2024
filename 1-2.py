

with open("1.txt") as infile:
    lines = infile.read().splitlines()
pairs = [raw.split("   ") for raw in lines]
list1, list2 = zip(*pairs)
list1 = list(list1)
list2 = list(list2)

cumulative_score = 0
for num in list1:
    instance_in_list2 = len(list(filter(lambda num2: num2 == num, list2)))
    cumulative_score += int(num) * instance_in_list2
print(cumulative_score)