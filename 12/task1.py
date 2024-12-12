import fileinput
from collections import deque


def read_map():
    return {
        (i, j): value
        for i, line in enumerate(fileinput.input())
        for j, value in enumerate(line.strip())
    }


def visit_region(garden_map, start_position):
    visited = set()
    perimeter = 0
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
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
        ]
        for next_position in possible_moves:
            if garden_map.get(next_position) != plant:
                # there is a border at this direction
                perimeter += 1
            elif (
                next_position not in visited and garden_map.get(next_position) == plant
            ):
                visit_queue.appendleft(next_position)

    return perimeter, area, visited


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
