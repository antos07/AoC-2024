import fileinput
import re
from collections import deque
from dataclasses import dataclass


@dataclass(unsafe_hash=True)
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


BARRIER = "-" * 20


def main():
    lines = iter(fileinput.input())
    w, h = map(int, next(lines).strip().split())
    assert w % 2 == 1
    assert h % 2 == 1
    robots = [Robot.from_str(line.strip()) for line in lines]

    for i in range(1000):
        # updating robots
        for robot in robots:
            robot.pos = (
                (robot.pos[0] + robot.vel[0]) % w,
                (robot.pos[1] + robot.vel[1]) % h,
            )

        # drawing robots
        if is_christmas_tree(w, h, robots):
            print(BARRIER)
            print(f"Iteration {i}")
            print(BARRIER)
            draw_robots(w, h, robots)
            print(BARRIER)


def is_christmas_tree(w, h, robots):
    try:
        first_robot = next(robot for robot in robots if robot.pos == (w // 2, h // 2))
    except StopIteration:
        return False

    unused_robots = set(robots) - {first_robot}
    assert len(unused_robots) == len(robots) - 1
    robots_to_try = deque([first_robot])
    while robots_to_try:
        robot = robots_to_try.popleft()

        used_robots = set()
        for another_robot in unused_robots:
            if all(abs(robot.pos[i] - another_robot.pos[i]) <= 1 for i in range(2)):
                used_robots.add(another_robot)

        unused_robots -= used_robots
        robots_to_try.extend(used_robots)

    return len(robots) - len(unused_robots) >= len(robots) * 0.2


def draw_robots(screen_w, screen_h, robots):
    lines = [[" "] * screen_w for _ in range(screen_h)]
    for robot in robots:
        lines[robot.pos[1]][robot.pos[0]] = "#"
    for line in lines:
        print("".join(line))


if __name__ == "__main__":
    main()
