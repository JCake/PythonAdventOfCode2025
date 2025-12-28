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
    numbers_and_operations = numbers_and_operations = build_ops(lines)
    for li, line in enumerate(lines):
        if li == len(lines) - 1:
            continue
        numbers = re.split(r'\s+', line.strip())
        for i, n in enumerate(numbers):
            numbers_and_operations[i].nums.append(int(n))
    return calc_grand_total(numbers_and_operations)

def ceph_math(input_str: str) -> int:
    lines = input_str.splitlines()
    numbers_and_operations = build_ops(lines)
    num_and_op_i = 0
    for col in range(len(lines[0])):
        num = ''
        for li, line in enumerate(lines):
            if li == len(lines) - 1:
                continue
            num += line[col]
        trimmed_num = num.strip()
        if trimmed_num == '':
            num_and_op_i += 1
            continue
        else:
            numbers_and_operations[num_and_op_i].nums.append(int(trimmed_num))
    return calc_grand_total(numbers_and_operations)

def build_ops(lines: list[str]):
    numbers_and_operations = []
    operations = re.split(r'\s+', lines[-1].strip())
    for operation in operations:
        numbers_and_operations.append(NumAndOp(operation))
    return numbers_and_operations

def calc_grand_total(numbers_and_operations: list[NumAndOp]):
    grand_total = 0
    for num_and_op in numbers_and_operations:
        grand_total += num_and_op.calculate()
    return grand_total
