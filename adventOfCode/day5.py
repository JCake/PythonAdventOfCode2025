def ingredient_count(input_str: str) -> int:
    parts = input_str.split('\n\n')
    fresh_ranges = find_fresh_ranges(input_str)
    count = 0
    available_ingredients = parts[1].splitlines()
    for ingredient in available_ingredients:
        found = False
        for fresh_range in fresh_ranges:
            if fresh_range[0] <= int(ingredient) <= fresh_range[1]:
                found = True
                break
        if found:
            count += 1
    return count

def find_fresh_ranges(input_str: str) -> list:
    parts = input_str.split('\n\n')
    ranges = parts[0].splitlines()
    fresh_ranges = []
    for r in ranges:
        min_and_max = r.split('-')
        min_p = int(min_and_max[0])
        max_p = int(min_and_max[1])
        fresh_ranges.append([min_p, max_p])
    return fresh_ranges

def possible_fresh_count(input_str: str) -> int:
    fresh_ranges = find_fresh_ranges(input_str)
    fresh_ranges = sorted(fresh_ranges, key=lambda x: x[0])
    no_overlaps = [fresh_ranges[0]]
    for i in range(1, len(fresh_ranges)):
        comparison_range = fresh_ranges[i]
        if comparison_range[0] <= no_overlaps[len(no_overlaps)-1][1] <= comparison_range[1]:
            no_overlaps[len(no_overlaps)-1][1] = comparison_range[1]
        elif comparison_range[0] > no_overlaps[len(no_overlaps)-1][1]:
            no_overlaps.append(comparison_range)
    total = 0
    for no_overlap in no_overlaps:
        total += (no_overlap[1] - no_overlap[0] + 1)
    return total

def first_num(li: list[int]) -> int:
    return li[0]
