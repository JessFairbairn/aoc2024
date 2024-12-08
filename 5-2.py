with open("5.txt") as infile:
    lines = iter(infile.read().splitlines())

# process rules
rules = []
for line in lines:
    if line == "":
        break
    pair = [int(x) for x in line.split("|")]
    rules.append(pair)

print("END OF RULES")
updates: list[list[int]] = []
for line in lines:
    update = [int(x) for x in line.split(",")]
    updates.append(update)


def is_update_legal(update) -> bool:
    for i in range(len(update)):
        page_num = update[i]

        for j in range(len(update)):
            other_page_num = update[j]
            if j > i:
                # other_page_num before page_num
                if any(list(map(lambda pair: pair[0] == other_page_num and pair[1] == page_num, rules))):
                    return False
            elif j < i:
                # other_page_num after page_num
                if any(list(map(lambda pair: pair[0] == page_num and pair[1] == other_page_num, rules))):
                    return False
    return True

illegal_updates: list[list[int]] = []
for update in updates:
    if not is_update_legal(update):
        illegal_updates.append(update)

# NOW FIX EM
fixed_updates = []
def swap_first_error(update):
    for i in range(len(update)):
        page_num = update[i]

        for j in range(len(update)):
            other_page_num = update[j]
            if j > i:
                    # other_page_num before page_num
                if any(list(map(lambda pair: pair[0] == other_page_num and pair[1] == page_num, rules))):
                    update[i], update[j] = update[j], update[i]
                    return
            elif j < i:
                    # other_page_num after page_num
                if any(list(map(lambda pair: pair[0] == page_num and pair[1] == other_page_num, rules))):
                    update[i], update[j] = update[j], update[i]
                    return
num_fixed = 0
for update in illegal_updates:
    while True:
        if is_update_legal(update):
            num_fixed += 1
            print(f"{num_fixed} of {len(illegal_updates)} fixed")
            fixed_updates.append(update)
            break
        swap_first_error(update)
    




sum_of_middles = sum(map(lambda update:update[int((len(update) +1 )/2 - 1)], fixed_updates))

print(f"Sum of middles: {sum_of_middles}")

pass