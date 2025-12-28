def splitter(input_str: str) -> int:
    return full_split(input_str)[0]

def timelines(input_str: str) -> int:
    return full_split(input_str)[1]

def full_split(input_str: str) -> list[int]:
    lines = input_str.splitlines()
    split_spots = set()
    paths = set()
    paths.add(f'{lines[0].find('S')}')
    for y in range(1, len(lines)):
        new_paths = set()
        for path in paths:
            x = int(path.split(',')[-1])
            if lines[y][x] == '.':
                new_paths.add(f'{path},{x}')
            elif lines[y][x] == '^':
                new_paths.add(f'{path},{x-1}')
                new_paths.add(f'{path},{x+1}')
                split_spots.add(f'{x},{y}')
        paths = new_paths
    return [len(split_spots), len(paths)]



