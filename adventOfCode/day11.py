def paths(input_str: str) -> int:
    if len(input_str) == 0:
        return 0
    lines = input_str.splitlines()
    device_connections = {}
    for line in lines:
        in_and_out = line.split(': ')
        device_connections[in_and_out[0]] = in_and_out[1].split(' ')
    return paths_to_out('you', device_connections)

def paths_to_out(point: str, device_connections, additional_nodes = [], additional_nodes_found = []) -> int:
    if len(additional_nodes) > 0:
        if point in additional_nodes:
            additional_nodes_found[additional_nodes.index(point)] = True
    if point == 'out':
        all_hit = True
        for found in additional_nodes_found:
            all_hit = all_hit and found
        if all_hit:
            return 1
        else:
            return 0
    elif not point in device_connections:
        return 0
    else:
        paths = 0
        for next_point in device_connections[point]:
            paths += paths_to_out(next_point, device_connections, additional_nodes, additional_nodes_found.copy())
        return paths

def restricted_paths(input_str: str) -> int:
    if len(input_str) == 0:
        return 0
    lines = input_str.splitlines()
    device_connections = {}
    for line in lines:
        in_and_out = line.split(': ')
        device_connections[in_and_out[0]] = in_and_out[1].split(' ')
    return paths_to_out('svr', device_connections, ['dac','fft'],[False, False])