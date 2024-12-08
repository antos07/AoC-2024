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

    possible_antinodes = [
        (antenna1[0] + dh, antenna1[1] + dw),
        (antenna2[0] - dh, antenna2[1] - dw),
    ]
    if dh % 3 == 0 and dw % 3 == 0:
        possible_antinodes += [
            (antenna1[0] + dh // 3, antenna1[1] + dw // 3),
            (antenna2[0] - dh // 3, antenna2[1] - dw // 3),
        ]

    def is_valid_antinode(pos):
        d1 = math.dist(pos, antenna1)
        d2 = math.dist(pos, antenna2)
        return (
            0 <= pos[0] < map_h
            and 0 <= pos[1] < map_w
            and (math.isclose(d1, 2 * d2) or math.isclose(2 * d1, d2))
        )

    return [pos for pos in possible_antinodes if is_valid_antinode(pos)]


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
