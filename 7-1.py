from math import prod
with open("data/7.txt") as infile:
    lines = infile.read().splitlines()

def solves_equation(answer: int, nums: list[int], operations: list[bool]) -> bool:
    cumulative = nums[0]
    for i in range(len(nums) - 1 ):
        if operations[i]:
            cumulative *= nums[i + 1]
        else:
            cumulative += nums[i + 1]
        
        if cumulative == answer:
            return True
        if cumulative > answer:
            return False

    # and if the whole lot is less than the answer it gets here
    
    return False

def is_solvable(answer, nums):
    num_operations = (len(nums) -1)
    for i in range(2 * num_operations + 1):
        operations = [bool((i >> bit) & 1) for bit in range(num_operations - 1, -1, -1)]
        if solves_equation(answer, nums, operations):
            return True
    assert prod(nums) < answer, "test"
    return False


sum_of_solvable_equations = 0
for line in lines:
    answer, equation = line.split(":")
    answer = int(answer)
    nums = list(map(lambda num: int(num), equation.strip().split(" ")))
    if is_solvable(answer, nums):
        sum_of_solvable_equations += answer

print(sum_of_solvable_equations)