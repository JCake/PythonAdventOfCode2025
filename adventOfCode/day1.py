import math


def password(inputStr: str, part2: bool = False):
    commands = inputStr.splitlines()
    zero_count = 0
    loc = 50
    for command in commands:
        starting_loc = loc
        direction = command[0]
        distance = int(command[1:])
        if direction == 'L':
            loc -= distance
            if part2 and distance > 0:
                if loc == 0:
                    zero_count += 1
                elif loc < 0:
                    if starting_loc == 0:
                        zero_count += math.floor(distance / 100)
                    else:
                        zero_count += (math.floor(loc / -100) + 1)
        if direction == 'R':
            loc += distance
            if part2 and distance > 0:
                if loc == 100:
                    zero_count += 1
                elif loc > 100:
                    if starting_loc == 0:
                        zero_count += math.floor(distance / 100)
                    else:
                        zero_count += math.floor(loc / 100)

        loc = loc % 100
        if not part2 and loc == 0:
            zero_count += 1

    return zero_count