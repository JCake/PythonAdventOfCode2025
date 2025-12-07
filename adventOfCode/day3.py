def joltage(input_str: str) -> int:
    banks = input_str.splitlines()
    total_joltage = 0
    for bank in banks:
        digits = []
        for digit in bank:
            digits.append(int(digit))
        size = int(len(digits))
        first_digit = max(digits[:size - 1])
        first_index = digits.index(first_digit)
        second_digit = max(digits[first_index + 1:])
        total_joltage += int(first_digit * 10 + second_digit)
    return total_joltage

def extra_joltage(input_str: str) -> int:
    banks = input_str.splitlines()
    total_joltage = 0
    for bank in banks:
        digits = []
        for digit in bank:
            digits.append(int(digit))
        size = int(len(digits))
        this_joltages = 0
        index = -1
        for i in range(1,13):
            sub_digits = digits[index + 1:size - (12-i)]
            digit = max(sub_digits)
            index += (1 + sub_digits.index(digit))
            this_joltages += (int(digit) * 10 ** (12-i))
        total_joltage += this_joltages
    return total_joltage
