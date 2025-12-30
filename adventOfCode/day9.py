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

def limited_area(input_str: str) -> int:
    lines = input_str.splitlines()
    red_coords = []
    for line in lines:
        x_and_y = line.split(',')
        red_coords.append(Coord(int(x_and_y[0]), int(x_and_y[1])))
    green_lines_y_to_xs = {}
    green_lines_x_to_ys = {}
    for i, red_coord in enumerate(red_coords):
        next_i = i + 1
        if i == len(red_coords) - 1:
            next_i = 0
        red_coord2 = red_coords[next_i]
        if red_coord.x == red_coord2.x:
            start_y = min(red_coord.y, red_coord2.y)
            end_y = max(red_coord.y, red_coord2.y) + 1
            if red_coord.x not in green_lines_x_to_ys:
                green_lines_x_to_ys[red_coord.x] = []
            green_lines_x_to_ys[red_coord.x].append(start_y)
            green_lines_x_to_ys[red_coord.x].append(end_y)
            for y in range(start_y, end_y):
                if y not in green_lines_y_to_xs:
                    green_lines_y_to_xs[y] = []
                green_lines_y_to_xs[y].append(red_coord.x)
        elif red_coord.y == red_coord2.y:
            start_x = min(red_coord.x, red_coord2.x)
            end_x = max(red_coord.x, red_coord2.x) + 1
            if red_coord.y not in green_lines_y_to_xs:
                green_lines_y_to_xs[red_coord.y] = []
            green_lines_y_to_xs[red_coord.y].append(start_x)
            green_lines_y_to_xs[red_coord.y].append(end_x)
            for x in range(start_x, end_x):
                if x not in green_lines_x_to_ys:
                    green_lines_x_to_ys[x] = []
                green_lines_x_to_ys[x].append(red_coord.y)
    area = 0
    for i1 in range(len(red_coords)):
        for i2 in range(i1 + 1, len(red_coords)):
            new_area = abs(red_coords[i1].x - red_coords[i2].x + 1) * abs(red_coords[i1].y - red_coords[i2].y + 1)
            if new_area > area and all_red_or_green(red_coords[i1], red_coords[i2], green_lines_y_to_xs, green_lines_x_to_ys):
                area = new_area
    return area

def all_red_or_green(coord1, coord2, green_lines_y_to_xs, green_lines_x_to_ys):
    coord1_x_in = min(green_lines_y_to_xs[coord2.y]) <= coord1.x <= max(green_lines_y_to_xs[coord2.y])
    if coord1_x_in:
        return min(green_lines_y_to_xs[coord1.y]) <= coord2.x <= max(green_lines_y_to_xs[coord1.y])
    return False
