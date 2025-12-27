def accessible_paper(input_str: str) -> int:
    if input_str == '':
        return 0
    return len(removable_spots(input_str.splitlines()))

def accessible_paper_continuing(input_str: str) -> int:
    lines = input_str.splitlines()
    to_remove = removable_spots(lines)
    total_count = 0
    while len(to_remove) > 0:
        total_count += len(to_remove)
        for spot in to_remove:
            this_line = lines[spot[0]]
            new_line = ''
            for j in range(len(this_line)):
                if j == spot[1]:
                    new_line += '.'
                else:
                    new_line += this_line[j]
            lines[spot[0]] = new_line
        to_remove = removable_spots(lines)
    return total_count

def removable_spots(lines: list[str]) -> list[list[int]]:
    num_lines = len(lines)
    num_columns = len(lines[0])
    accessible_spots = []
    for i in range(num_lines):
        for j in range(num_columns):
            if lines[i][j] == '@':
                neighbors = 0
                for i_n in range(i-1, i+2):
                    for j_n in range(j-1, j+2):
                        if 0 <= i_n < num_lines and 0 <= j_n < num_columns:
                            if lines[i_n][j_n] == '@':
                                neighbors += 1
                if neighbors <= 4:
                    accessible_spots.insert(0, [i,j])
    return accessible_spots
