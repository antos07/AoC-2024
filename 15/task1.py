import fileinput


def parse_input():
    lines = iter(fileinput.input())
    lines = [line.strip() for line in lines]
    empty_line_idx = lines.index("")
    warehouse_map, instructions = lines[:empty_line_idx], lines[empty_line_idx + 1 :]
    warehouse_map = {
        (i, j): value
        for i, line in enumerate(warehouse_map)
        for j, value in enumerate(line)
    }
    instructions = "".join(instructions)
    return warehouse_map, instructions


ROBOT_CELL = "@"
EMPTY_CELL = "."
BOX_CELL = "O"
WALL_CELL = "#"


def find_robot(warehouse_map):
    return next(
        position for position, symbol in warehouse_map.items() if symbol == ROBOT_CELL
    )


def print_map(warehouse_map):
    map_h = max(y for y, _ in warehouse_map) + 1
    map_w = max(x for _, x in warehouse_map) + 1

    lines = [[None] * map_w for _ in range(map_h)]
    for (y, x), symbol in warehouse_map.items():
        lines[y][x] = symbol

    lines = ["".join(line) for line in lines]
    lines = "\n".join(lines)
    lines = "\n" + lines + "\n"
    print(lines)


def main():
    warehouse_map, instructions = parse_input()

    robot_position = find_robot(warehouse_map)
    instruction2offset = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
    for instruction in instructions:
        robot_y, robot_x = robot_position
        dy, dx = instruction2offset[instruction]

        # Finding there a box stack ends
        last_box_y, last_box_x = robot_y + dy, robot_x + dx
        while warehouse_map[last_box_y, last_box_x] == BOX_CELL:
            last_box_y, last_box_x = last_box_y + dy, last_box_x + dx

        # If the boxes are stuck, the robot can't move
        if warehouse_map[last_box_y, last_box_x] == WALL_CELL:
            continue

        # Moving the boxes from the last to the firs one and then moving the robot.
        while (last_box_y, last_box_x) != (robot_y, robot_x):
            warehouse_map[last_box_y, last_box_x] = warehouse_map[
                last_box_y - dy, last_box_x - dx
            ]
            warehouse_map[last_box_y - dy, last_box_x - dx] = EMPTY_CELL
            last_box_y, last_box_x = last_box_y - dy, last_box_x - dx

        robot_position = robot_y + dy, robot_x + dx

    answer = sum(
        y * 100 + x for (y, x), symbol in warehouse_map.items() if symbol == BOX_CELL
    )
    print(answer)


if __name__ == "__main__":
    main()
