import fileinput
import operator
import re
from collections import Counter
from dataclasses import dataclass
from functools import reduce


@dataclass
class Robot:
    pos: tuple[int, int]
    vel: tuple[int, int]

    @classmethod
    def from_str(cls, s):
        m = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", s)
        assert m

        return cls(
            pos=(int(m.group(1)), int(m.group(2))),
            vel=(int(m.group(3)), int(m.group(4))),
        )


SIMULATION_TIME_S = 100


def main():
    lines = iter(fileinput.input())
    w, h = map(int, next(lines).strip().split())
    assert w % 2 == 1
    assert h % 2 == 1
    robots = [Robot.from_str(line.strip()) for line in lines]

    final_positions = [
        (
            (robot.pos[0] + robot.vel[0] * SIMULATION_TIME_S) % w,
            (robot.pos[1] + robot.vel[1] * SIMULATION_TIME_S) % h,
        )
        for robot in robots
    ]
    quadrants_counter = Counter()

    for position in final_positions:
        if position[0] == w // 2 or position[1] == h // 2:
            continue

        quadrants_counter[position[0] < w // 2, position[1] < h // 2] += 1
    answer = reduce(operator.mul, quadrants_counter.values(), 1)
    print(answer)


if __name__ == "__main__":
    main()
