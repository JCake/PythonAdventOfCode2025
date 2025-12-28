from functools import reduce
import re

class NumAndOp:
    def __init__(self, op):
        self.nums = []
        self.op = op

    def calculate(self):
        if self.op == '+':
            return reduce(lambda x, y : x + y, self.nums)
        else:
            return reduce(lambda x, y : x * y, self.nums, 1)

def math(input_str: str) -> int:
    lines = input_str.splitlines()
    numbers_and_operations = []
    operations = re.split(r'\s+', lines[-1].strip())
    for operation in operations:
        numbers_and_operations.append(NumAndOp(operation))
    for li, line in enumerate(lines):
        if li == len(lines) - 1:
            continue
        numbers = re.split(r'\s+', line.strip())
        for i, n in enumerate(numbers):
            numbers_and_operations[i].nums.append(int(n))
    grand_total = 0
    for num_and_op in numbers_and_operations:
        grand_total += num_and_op.calculate()
    return grand_total
