import math

def invalid_sum(input_str: str, any_num_repeats = False):
    sum_of_invalid = 0
    range_pairs = input_str.split(',')
    for rangePair in range_pairs:
        [start, end] = rangePair.split('-')
        for i in range(int(start), int(end) + 1):
           i_str = f'{i}'
           str_len = int(len(i_str))
           if not any_num_repeats and str_len % 2 == 0:
               half = int(str_len / 2)
               if i_str[0:half] == i_str[half:str_len]:
                   sum_of_invalid += i
           elif any_num_repeats and has_any_repeats(i_str,str_len):
               sum_of_invalid += i

    return sum_of_invalid

def has_any_repeats(i_str: str, str_len: int):
    for repeats in range(2, str_len + 1):
        if str_len % int(repeats) == 0:
            if has_repeats(i_str, repeats, str_len):
                return True
    return False

def has_repeats(i_str: str, repeats: int, str_len: int) -> bool:
    substr_size = int(str_len / repeats)
    prev_compare = i_str[0:substr_size]
    for segmentNum in range(1, repeats):
        compare = i_str[substr_size * segmentNum:substr_size * (segmentNum + 1)]
        if prev_compare != compare:
            return False
        prev_compare = compare
    return True