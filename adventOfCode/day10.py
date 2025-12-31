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

