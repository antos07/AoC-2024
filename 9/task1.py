import fileinput


def read_disk():
    compacted = fileinput.input().readline().strip()
    return [
        # every 2nd number is an empty block
        block_id // 2 if block_id % 2 == 0 else None
        for block_id, block_length in enumerate(compacted)
        for _ in range(int(block_length))
    ]


def compact_disk(disk):
    free_positions = (i for i, value in enumerate(disk) if value is None)
    occupied_positions = [i for i, value in enumerate(disk) if value is not None]

    disk = list(disk)
    for free_pos, occupied_pos in zip(free_positions, reversed(occupied_positions)):
        if free_pos > occupied_pos:
            # it's impossible to compact any further
            break

        disk[free_pos], disk[occupied_pos] = disk[occupied_pos], disk[free_pos]
    return disk


def compute_hash(disk):
    return sum(i * value for i, value in enumerate(disk) if value is not None)


def main():
    disk = read_disk()
    disk = compact_disk(disk)
    print(compute_hash(disk))


if __name__ == "__main__":
    main()
