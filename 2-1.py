from typing import Optional

with open("data/2.txt") as infile:
    lines = infile.read().splitlines()
lines = list(map(lambda report: report.split(" "), lines))
reports = list(map(lambda report: [int(number) for number in report], lines))


def is_safe(report:list[int]):
    prev_level = None
    is_increasing: Optional[bool] = None
    for level in report:
        if prev_level is None:
            # first in report, just set prev_level and move on
            prev_level = level
            continue
        if is_increasing is None:
            # we are on the second level in the report if we reach here
            is_increasing = (level > prev_level)
        else:
            if is_increasing != (level > prev_level):
                return False

        difference = abs(level - prev_level)
        if difference < 1 or difference > 3:
            return False
        
        # this level is fine if it reaches this far
        prev_level = level
        
    return True

num_safe = 0

for report in reports:
    if is_safe(report):
        num_safe += 1
print(num_safe)


        

pass