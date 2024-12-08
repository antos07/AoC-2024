import fileinput
import itertools
import math
from collections import defaultdict

EMPTY_CELL = "."


def read_map():
    antenna_positions = defaultdict(list)

    for i, line in enumerate(fileinput.input()):
        for j, cell in enumerate(line.strip()):
            if cell != EMPTY_CELL:
                antenna_positions[cell].append((i, j))

    # returning map dimensions and antenna positions
    return i + 1, j + 1, antenna_positions


def calculate_antinodes(antenna1, antenna2, map_h, map_w):
    dh = antenna1[0] - antenna2[0]
    dw = antenna1[1] - antenna2[1]

    # as the distance doesn't play any role, I can simply find the lowest
    # possible dh and dw and iterate through all cells on the line
    # by adding or subtracting them.
    gcd = math.gcd(dh, dw)
    dh //= gcd
    dw //= gcd

    def is_valid_antinode(pos):
        return 0 <= pos[0] < map_h and 0 <= pos[1] < map_w

    possible_nodes = []
    for pos in zip(itertools.count(antenna1[0], dh), itertools.count(antenna1[1], dw)):
        if not is_valid_antinode(pos):
            # ran out of bounds
            break
        possible_nodes.append(pos)
    for pos in zip(itertools.count(antenna1[0], -dh), itertools.count(antenna1[1], -dw)):
        if not is_valid_antinode(pos):
            # ran out of bounds
            break
        possible_nodes.append(pos)

    return set(possible_nodes)


def main():
    map_h, map_w, antenna_positions = read_map()

    unique_antinodes = set()
    for same_frequency_antennas in antenna_positions.values():
        for a1, a2 in itertools.product(same_frequency_antennas, repeat=2):
            if a1 != a2:
                unique_antinodes |= set(calculate_antinodes(a1, a2, map_h, map_w))
    print(len(unique_antinodes))


if __name__ == "__main__":
    main()
