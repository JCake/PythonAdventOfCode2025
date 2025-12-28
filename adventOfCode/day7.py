class Splits:
    def __init__(self, splits, timelines):
        self.splits = splits
        self.timelines = timelines

def splitter(input_str: str) -> Splits:
    lines = input_str.splitlines()
    x_indices = set()
    x_indices.add(lines[0].find('S'))
    split_spots = set()
    timeline_counts = {lines[0].find('S'): 1}
    for y in range(1, len(lines)):
        new_x_indices = set()
        for x in x_indices:
            if lines[y][x] == '.':
                new_x_indices.add(x)
            elif lines[y][x] == '^':
                new_x_indices.add(x-1)
                new_x_indices.add(x+1)
                split_spots.add(f'{x},{y}')
                coming_in = int(timeline_counts[x])
                timeline_counts[x] = 0
                timeline_counts[x-1] = timeline_counts.get(x-1, 0) + coming_in
                timeline_counts[x+1] = timeline_counts.get(x+1, 0) + coming_in
        x_indices = new_x_indices
    total_timelines = 0
    for t in timeline_counts.values():
        total_timelines += t
    return Splits(len(split_spots), total_timelines)
