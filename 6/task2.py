import enum
import sys

START_SYMBOL = "^"
WALL_SYMBOL = "#"
FREE_SYMBOL = "."


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


def check_loop(situation_map):
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
            return False

        cur_position = i + di, j + dj
    return True


def main():
    situation_map = read_map()

    answer = 0
    # Here I use the dumbest solution possible: I check all possible alterations.
    # This, of course, is totally ineffective and there's probably a better solution
    # but who cares.
    #
    # As a better idea, we can check only the positions that are actually on
    # the guard's original way. And there are some more optimizations, which
    # we can perform.
    for position, value in situation_map.items():
        if value != FREE_SYMBOL:
            continue

        altered_map = situation_map.copy()
        altered_map[position] = WALL_SYMBOL
        if check_loop(altered_map):
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
