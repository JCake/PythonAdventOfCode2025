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