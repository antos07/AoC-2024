import enum
import fileinput
from collections import deque
from functools import reduce
from itertools import pairwise


def read_map():
    return {
        (i, j): value
        for i, line in enumerate(fileinput.input())
        for j, value in enumerate(line.strip())
    }


class Directions(enum.Enum):
    UP = enum.auto()
    DOWN = enum.auto()
    LEFT = enum.auto()
    RIGHT = enum.auto()


def visit_region(garden_map, start_position):
    visited = set()
    border_positions = []
    area = 0

    plant = garden_map[start_position]
    visit_queue = deque([start_position])
    while visit_queue:
        row, col = position = visit_queue.popleft()

        if position in visited:
            continue

        visited.add(position)
        area += 1

        possible_moves = [
            ((row + 1, col), Directions.DOWN),
            ((row - 1, col), Directions.UP),
            ((row, col + 1), Directions.RIGHT),
            ((row, col - 1), Directions.LEFT),
        ]
        for next_position, direction in possible_moves:
            if garden_map.get(next_position) != plant:
                # there is a border at this direction
                border_positions.append((next_position, direction))
            elif (
                next_position not in visited and garden_map.get(next_position) == plant
            ):
                visit_queue.appendleft(next_position)

    # counting horizontal sides
    sides = reduce(
        lambda total, positions: total
        + int(
            not (
                positions[0][0] == positions[1][0]  # are on the same line
                and positions[0][1] + 1 == positions[1][1]  # are subsequent tiles
            )
        ),
        pairwise(
            sorted(
                pos
                for pos, direction in border_positions
                if direction == Directions.DOWN
            )
            + sorted(
                pos for pos, direction in border_positions if direction == Directions.UP
            )
        ),
        1,
    )

    # counting vertical sides
    sides += reduce(
        lambda total, positions: total
        + int(
            not (
                positions[0][1] == positions[1][1]  # are on the same line
                and positions[0][0] + 1 == positions[1][0]  # are subsequent tiles
            )
        ),
        pairwise(
            sorted(
                (
                    pos
                    for pos, direction in border_positions
                    if direction == Directions.LEFT
                ),
                key=lambda pos: pos[::-1],
            )
            + sorted(
                (
                    pos
                    for pos, direction in border_positions
                    if direction == Directions.RIGHT
                ),
                key=lambda pos: pos[::-1],
            )
        ),
        1,
    )

    return sides, area, visited


def main():
    garden_map = read_map()

    answer = 0
    visited = set()
    for position in garden_map:
        if position not in visited:
            perimeter, area, newly_visited = visit_region(garden_map, position)
            answer += perimeter * area
            visited |= newly_visited
    print(answer)


if __name__ == "__main__":
    main()
