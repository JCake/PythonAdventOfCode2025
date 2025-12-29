import math

class Coord:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class CoordConnection:
    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2
        self.dist = -1

    def distance(self):
        if self.dist == -1:
            self.dist = math.sqrt((self.coord1.x - self.coord2.x)**2 + (self.coord1.y - self.coord2.y)**2 + (self.coord1.z - self.coord2.z)**2)
        return self.dist

def build_coord_connections(input_str: str) -> list[CoordConnection]:
    lines = input_str.splitlines()
    coords = []
    for line in lines:
        coord = line.split(',')
        coords.append(Coord(int(coord[0]),int(coord[1]),int(coord[2])))
    coord_connections = []
    for index, coord in enumerate(coords):
        for index_2 in range(index + 1, len(coords)):
            coord_connection = CoordConnection(coord, coords[index_2])
            coord_connections.append(coord_connection)
    coord_connections.sort(key=lambda c: c.distance())
    return coord_connections

def circuit(input_str: str, pairs: int) -> int:
    coord_connections = build_coord_connections(input_str)
    chains = []
    for p in range(pairs):
        matched = False
        coord_connection = coord_connections[p]
        for chain in chains:
            if coord_connection.coord1 in chain or coord_connection.coord2 in chain:
                chain.add(coord_connection.coord1)
                chain.add(coord_connection.coord2)
                matched = True
                break
        if not matched:
            new_chain = set()
            new_chain.add(coord_connections[p].coord1)
            new_chain.add(coord_connections[p].coord2)
            chains.append(new_chain)

    combined = False
    while True:
        combined = False
        for i, chain in enumerate(chains):
            for c2i in range(i+1,len(chains)):
                if c2i < len(chains) and len(chain & chains[c2i]) > 0:
                    chain.update(chains[c2i])
                    chains[c2i] = set() # clear it out since it's been combined
                    combined = True
        if not combined:
            break

    chains.sort(key=lambda c: len(c))
    return len(chains[-1]) * len(chains[-2]) * len(chains[-3])