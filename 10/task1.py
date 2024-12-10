import fileinput


def read_map():
    return {
        (i, j): int(symbol)
        for i, line in enumerate(fileinput.input())
        for j, symbol in enumerate(line.strip())
    }


def count_starting_trails(island_map, position):
    visited_tops = set()

    def count(current_position, height):
        if island_map.get(current_position) != height:
            return
        if height == 9:
            visited_tops.add(current_position)
            return

        possible_next_positions = [
            (current_position[0] + 1, current_position[1]),
            (current_position[0] - 1, current_position[1]),
            (current_position[0], current_position[1] + 1),
            (current_position[0], current_position[1] - 1),
        ]
        for next_position in possible_next_positions:
            count(next_position, height + 1)

    count(position, 0)
    return len(visited_tops)


def main():
    island_map = read_map()

    answer = sum(count_starting_trails(island_map, position) for position in island_map)
    print(answer)


if __name__ == "__main__":
    main()
