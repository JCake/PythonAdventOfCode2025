def paths(input_str: str) -> int:
    if len(input_str) == 0:
        return 0
    lines = input_str.splitlines()
    device_connections = {}
    for line in lines:
        in_and_out = line.split(': ')
        device_connections[in_and_out[0]] = in_and_out[1].split(' ')
    return paths_to('you', device_connections, 'out')

def paths_to(point: str, device_connections, goal:str, exclude = []) -> int:
    if point in exclude:
        return 0
    if point == goal:
        return 1
    if not point in device_connections:
        return 0
    paths = 0
    for next_point in device_connections[point]:
        paths += paths_to(next_point, device_connections, goal)
    return paths

def restricted_paths(input_str: str) -> int:
    if len(input_str) == 0:
        return 0
    lines = input_str.splitlines()
    device_connections = {}
    for line in lines:
        in_and_out = line.split(': ')
        device_connections[in_and_out[0]] = in_and_out[1].split(' ')
    svr_to_dac = 0
    svr_to_fft = 0
    for point in device_connections['svr']:
        svr_to_dac += paths_to(point, device_connections, 'dac', ['svr','fft','out'])
        svr_to_fft += paths_to(point, device_connections, 'fft', ['svr','dac','out'])
    dac_to_fft = 0
    dac_to_out = 0
    for point in device_connections['dac']:
        dac_to_fft += paths_to(point, device_connections, 'fft', ['out','dac','svr'])
        dac_to_out += paths_to(point, device_connections, 'out', ['svr','dac','fft'])
    fft_to_out = 0
    fft_to_dac = 0
    for point in device_connections['fft']:
        fft_to_out += paths_to(point, device_connections, 'out', ['svr','fft','dac'])
        fft_to_dac += paths_to(point, device_connections, 'dac', ['svr','fft','out'])

    return svr_to_dac * dac_to_fft * fft_to_out + svr_to_fft * fft_to_dac * dac_to_out