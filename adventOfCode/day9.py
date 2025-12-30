class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def max_area(input_str: str) -> int:
    lines = input_str.splitlines()
    coords = []
    for line in lines:
        x_and_y = line.split(',')
        coords.append(Coord(int(x_and_y[0]), int(x_and_y[1])))
    area = 0
    for i1 in range(len(coords)):
        for i2 in range(i1 + 1, len(coords)):
            new_area = abs(coords[i1].x - coords[i2].x + 1) * abs(coords[i1].y - coords[i2].y + 1)
            if new_area > area:
                area = new_area
    return area

class MinAndMax:
    def __init__(self, a, b):
        self.min = min(a, b)
        self.max = max(a, b)

    def contains(self, x) -> bool:
        return self.min < x < self.max

def limited_area(input_str: str) -> int:
    lines = input_str.splitlines()
    red_coords = []
    for line in lines:
        x_and_y = line.split(',')
        red_coords.append(Coord(int(x_and_y[0]), int(x_and_y[1])))
    horizontal_lines_x_indexed = {}
    horizontal_lines_y_indexed = {}
    vertical_lines_y_indexed = {}
    vertical_lines_x_indexed = {}
    for i, red_coord in enumerate(red_coords):
        next_i = i + 1
        if i == len(red_coords) - 1:
            next_i = 0
        red_coord2 = red_coords[next_i]
        if red_coord.x == red_coord2.x:
            min_and_max = MinAndMax(red_coord.y, red_coord2.y)
            if red_coord.x not in vertical_lines_x_indexed:
                vertical_lines_x_indexed[red_coord.x] = []
            for y in range(min_and_max.min, min_and_max.max + 1):
                if y not in vertical_lines_y_indexed:
                    vertical_lines_y_indexed[y] = []
                vertical_lines_y_indexed[y].append(red_coord.x)
                vertical_lines_x_indexed[red_coord.x].append(y)
        elif red_coord.y == red_coord2.y:
            min_and_max = MinAndMax(red_coord.x, red_coord2.x)
            if red_coord.y not in horizontal_lines_y_indexed:
                horizontal_lines_y_indexed[red_coord.y] = []
            for x in range(min_and_max.min, min_and_max.max + 1):
                if x not in horizontal_lines_x_indexed:
                    horizontal_lines_x_indexed[x] = []
                horizontal_lines_x_indexed[x].append(red_coord.y)
                horizontal_lines_y_indexed[red_coord.y].append(x)
    area = 0
    for i1 in range(len(red_coords)):
        for i2 in range(i1 + 1, len(red_coords)):
            new_area = abs(red_coords[i1].x - red_coords[i2].x + 1) * abs(red_coords[i1].y - red_coords[i2].y + 1)
            if new_area > area and all_red_or_green(red_coords[i1], red_coords[i2], horizontal_lines_x_indexed, horizontal_lines_y_indexed, vertical_lines_y_indexed, vertical_lines_x_indexed):
                area = new_area
    return area

def all_red_or_green(coord1, coord2, horizontal_lines_x_indexed, horizontal_lines_y_indexed, vertical_lines_y_indexed, vertical_lines_x_indexed):
    horizontal_line_xs = MinAndMax(coord1.x, coord2.x)
    horizontal_good = True
    if coord1.y in vertical_lines_y_indexed:
        for x in vertical_lines_y_indexed[coord1.y]:
            if horizontal_line_xs.contains(x):
                horizontal_good = False
    if coord2.y in vertical_lines_y_indexed:
        for x in vertical_lines_y_indexed[coord2.y]:
            if horizontal_line_xs.contains(x):
                horizontal_good = False

    vertical_line_ys = MinAndMax(coord1.y, coord2.y)
    vertical_good = True
    if coord1.x in horizontal_lines_x_indexed:
        for y in horizontal_lines_x_indexed[coord1.x]:
            if vertical_line_ys.contains(y):
                vertical_good = False
    if coord2.x in horizontal_lines_x_indexed:
        for y in horizontal_lines_x_indexed[coord2.x]:
            if vertical_line_ys.contains(y):
                vertical_good = False

    return horizontal_good and vertical_good

def areas_in_range(input_str: str, min_area: int, max_area: int) -> list[int]:
    lines = input_str.splitlines()
    coords = []
    for line in lines:
        x_and_y = line.split(',')
        coords.append(Coord(int(x_and_y[0]), int(x_and_y[1])))
    areas = []
    for i1 in range(len(coords)):
        for i2 in range(i1 + 1, len(coords)):
            new_area = abs(coords[i1].x - coords[i2].x + 1) * abs(coords[i1].y - coords[i2].y + 1)
            if min_area < new_area < max_area:
                areas.append(new_area)
    areas.sort()
    return areas
