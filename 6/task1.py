import enum
import sys


START_SYMBOL = "^"
WALL_SYMBOL = "#"


def read_map():
    raw_input = [line for line in sys.stdin]
    return {
        (i, j): value
        for i, line in enumerate(raw_input)
        for j, value in enumerate(line)
    }


def find_start_position(situation_map):
    for k, v in situation_map.items():
        if v == START_SYMBOL:
            return k
    raise RuntimeError("Start position not found")


class Directions(tuple, enum.Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    def turn_right(self):
        all_dirs = list(self.__class__)
        return all_dirs[(all_dirs.index(self) + 1) % len(all_dirs)]


def main():
    situation_map = read_map()

    cur_position = find_start_position(situation_map)
    cur_direction = Directions.UP
    visited_with_directions = set()
    while (cur_position, cur_direction) not in visited_with_directions:
        visited_with_directions.add((cur_position, cur_direction))

        i, j = cur_position
        di, dj = cur_direction
        try:
            while situation_map[i + di, j + dj] == WALL_SYMBOL:
                cur_direction = cur_direction.turn_right()
                di, dj = cur_direction
        except KeyError:
            # the guard leaved the mapped area
            break

        cur_position = i + di, j + dj

    answer = len({position for position, _ in visited_with_directions})
    print(answer)


if __name__ == "__main__":
    main()
