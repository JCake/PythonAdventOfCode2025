def min_presses(input_str: str) -> int:
    lines = input_str.splitlines()
    total_presses = 0
    for line in lines:
        total_presses += min_presses_for_line(line)
    return total_presses

def min_presses_for_line(line: str) -> int:
    lights_and_rest = line.split('] ')
    lights = lights_and_rest[0].replace('[','')
    goal_light_status = []
    for light in lights:
        goal_light_status.append('#' == light)
    button_strs = lights_and_rest[1].split(' {')[0].split(' ')
    buttons = []
    for button_str in button_strs:
        lights_for_button = button_str.replace('(','').replace(')','').split(',')
        lights_list = []
        for light in lights_for_button:
            lights_list.append(int(light))
        buttons.append(lights_list)

    total_presses_to_try = 0
    success = False
    while not success:
        total_presses_to_try += 1
        success = press_choice(buttons, 0, True, [False] * len(lights), goal_light_status, total_presses_to_try, 0)
        if not success:
            success = press_choice(buttons, 0, False, [False] * len(lights), goal_light_status, total_presses_to_try, 0)
    return total_presses_to_try


def press_choice(buttons: list[list[int]], current_button_index: int, press: bool, light_status, goal_light_status, presses_remaining, skipped_presses) -> bool:
    if presses_remaining == 0:
        return light_status == goal_light_status
    if press:
        for impacted_light in buttons[current_button_index]:
            light_status[impacted_light] = not light_status[impacted_light]
        presses_remaining -= 1
        skipped_presses = 0
    else:
        skipped_presses += 1
    press_next = press_choice(buttons, (current_button_index + 1) % len(buttons), True, light_status.copy(), goal_light_status, presses_remaining, skipped_presses)
    no_press_next = False
    if skipped_presses < len(buttons):
        no_press_next = press_choice(buttons, (current_button_index + 1) % len(buttons), False, light_status.copy(), goal_light_status, presses_remaining, skipped_presses)
    return press_next or no_press_next

def min_presses_joltage(input_str: str) -> int:
    lines = input_str.splitlines()
    total_presses = 0
    for line in lines:
        total_presses += min_presses_for_line_joltage(line)
    return total_presses

def min_presses_for_line_joltage(line: str) -> int:
    buttons_and_joltage = line.split('] ')[1].split(' {')
    button_strs = buttons_and_joltage[0].strip().split(' ')
    buttons = []
    for button_str in button_strs:
        lights_for_button = button_str.replace('(','').replace(')','').split(',')
        lights_list = []
        for light in lights_for_button:
            lights_list.append(int(light))
        buttons.append(lights_list)
    joltage = []
    joltage_strs = buttons_and_joltage[1].strip('}').split(',')
    for joltage_str in joltage_strs:
        joltage.append(int(joltage_str))

    total_presses_to_try = 0
    success = False
    while not success:
        total_presses_to_try += 1
        success = press_choice_joltage(buttons, 0, joltage.copy(), total_presses_to_try)
    return total_presses_to_try


# TODO improve efficiency by looking more closely at possible values
def press_choice_joltage(buttons: list[list[int]], current_index: int, joltage_status: list[int], presses_remaining) -> bool:
    if presses_remaining == 0:
        return all_zero(joltage_status)
    if current_index >= len(buttons):
        return False
    current_button = buttons[current_index]
    max_presses = presses_remaining
    for j in current_button:
        if joltage_status[j] < max_presses:
            max_presses = joltage_status[j]
    # no presses:
    if press_choice_joltage(buttons, current_index + 1, joltage_status.copy(), presses_remaining):
        return True
    # at least one press:
    for i in range(1,max_presses+1):
        for j in current_button:
            joltage_status[j] = joltage_status[j] - 1
        if press_choice_joltage(buttons, current_index+1, joltage_status.copy(), presses_remaining - i):
            return True
    return False


def all_zero(joltage_status: list[int]):
    for i in range(len(joltage_status)):
        if joltage_status[i] > 0:
            return False
    return True

