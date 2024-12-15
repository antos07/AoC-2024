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


WIDE_BOX_LEFT_CELL = "["
WIDE_BOX_RIGHT_CELL = "]"
WIDE_BOX_CELLS = [WIDE_BOX_LEFT_CELL, WIDE_BOX_RIGHT_CELL]


def widen_the_map(warehouse_map):
    new_warehouse_map = {}
    for (y, x), symbol in warehouse_map.items():
        if symbol in [WALL_CELL, EMPTY_CELL]:
            new_warehouse_map[y, 2 * x] = symbol
            new_warehouse_map[y, 2 * x + 1] = symbol
        elif symbol == ROBOT_CELL:
            new_warehouse_map[y, 2 * x] = ROBOT_CELL
            new_warehouse_map[y, 2 * x + 1] = EMPTY_CELL
        else:
            new_warehouse_map[y, 2 * x] = WIDE_BOX_LEFT_CELL
            new_warehouse_map[y, 2 * x + 1] = WIDE_BOX_RIGHT_CELL

    return new_warehouse_map


def main():
    warehouse_map, instructions = parse_input()
    warehouse_map = widen_the_map(warehouse_map)

    print_map(warehouse_map)

    robot_position = find_robot(warehouse_map)
    instruction2offset = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
    for instruction in instructions:
        robot_y, robot_x = robot_position
        dy, dx = instruction2offset[instruction]

        # When moving horizontally, nothing changes from task 1
        if dy == 0:
            # Finding there a box stack ends
            last_box_y, last_box_x = robot_y + dy, robot_x + dx
            while warehouse_map[last_box_y, last_box_x] in WIDE_BOX_CELLS:
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

        # Vertical moves have new logic
        else:
            new_layer = {robot_position}
            cells_to_move = []
            can_move = True
            while can_move and new_layer:
                cells_to_move.append(new_layer)
                new_layer = set()

                for y, x in cells_to_move[-1]:
                    if warehouse_map[y + dy, x + dx] == WALL_CELL:
                        can_move = False
                        break
                    elif warehouse_map[y + dy, x + dx] == WIDE_BOX_LEFT_CELL:
                        new_layer |= {(y + dy, x + dx), (y + dy, x + dx + 1)}
                    elif warehouse_map[y + dy, x + dx] == WIDE_BOX_RIGHT_CELL:
                        new_layer |= {(y + dy, x + dx), (y + dy, x + dx - 1)}

            if not can_move:
                continue

            for layer in reversed(cells_to_move):
                for y, x in layer:
                    warehouse_map[y + dy, x + dx] = warehouse_map[y, x]
                    warehouse_map[y, x] = EMPTY_CELL

        robot_position = robot_y + dy, robot_x + dx

    answer = sum(
        y * 100 + x
        for (y, x), symbol in warehouse_map.items()
        if symbol == WIDE_BOX_LEFT_CELL
    )
    print(answer)


if __name__ == "__main__":
    main()
