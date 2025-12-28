def splitter(input_str: str) -> int:
    lines = input_str.splitlines()
    x_indices = set()
    x_indices.add(lines[0].find('S'))
    split_spots = set()
    for y in range(1, len(lines)):
        new_x_indices = set()
        for x in x_indices:
            if lines[y][x] == '.':
                new_x_indices.add(x)
            elif lines[y][x] == '^':
                new_x_indices.add(x-1)
                new_x_indices.add(x+1)
                split_spots.add(f'{x},{y}')
        x_indices = new_x_indices
    return len(split_spots)

