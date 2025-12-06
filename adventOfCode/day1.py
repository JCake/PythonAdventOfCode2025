def password(inputStr: str, part2: bool = False):
    commands = inputStr.splitlines()
    zero_count = 0
    loc = 50
    for command in commands:
        direction = command[0]
        distance = int(command[1:])
        # TODO make this less dumb... my math was not working
        for i in range(0, distance):
            if direction == 'L':
                loc -= 1

            if direction == 'R':
                loc += 1

            loc = loc % 100
            if part2 and loc == 0:
                zero_count += 1

        loc = loc % 100
        if not part2 and loc == 0:
            zero_count += 1

    return zero_count