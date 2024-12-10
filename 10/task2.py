import fileinput


def read_map():
    return {
        (i, j): int(symbol)
        for i, line in enumerate(fileinput.input())
        for j, symbol in enumerate(line.strip())
    }


def count_starting_trails(island_map, position):
    def count(current_position, height):
        if island_map.get(current_position) != height:
            return 0
        if height == 9:
            return 1

        possible_next_positions = [
            (current_position[0] + 1, current_position[1]),
            (current_position[0] - 1, current_position[1]),
            (current_position[0], current_position[1] + 1),
            (current_position[0], current_position[1] - 1),
        ]
        return sum(
            count(next_position, height + 1)
            for next_position in possible_next_positions
        )

    return count(position, 0)


def main():
    island_map = read_map()

    answer = sum(count_starting_trails(island_map, position) for position in island_map)
    print(answer)


if __name__ == "__main__":
    main()
