import fileinput
from itertools import zip_longest

from sortedcontainers import SortedSet


def read_disk():
    compacted = fileinput.input().readline().strip()
    return [int(block_length) for block_length in compacted]


def compact_disk(disk):
    occupied_blocks = disk[::2]
    free_blocks = disk[1::2]

    occupied_blocks_indexed_reversed = SortedSet(
        enumerate(occupied_blocks), key=lambda t: -t[0]
    )

    free_blocks_after_moves = []
    for free_block_idx, free_block in enumerate(free_blocks):
        moved_blocks = []
        for occupied_block_idx, occupied_block in occupied_blocks_indexed_reversed:
            if occupied_block_idx <= free_block_idx:
                # the free block is to the right from the occupied block
                break
            if occupied_block > free_block:
                continue
            free_block -= occupied_block
            moved_blocks.append((occupied_block_idx, occupied_block))

        for moved_block in moved_blocks:
            occupied_blocks_indexed_reversed.remove(moved_block)

        free_blocks_after_moves.append(moved_blocks)

    disk = []
    processed_occupied_blocks = set()
    for i, (occupied_block, free_block, blocks_moved_into_free) in enumerate(
        zip_longest(occupied_blocks, free_blocks, free_blocks_after_moves)
    ):
        occupied_block = occupied_block or 0
        free_block = free_block or 0
        blocks_moved_into_free = blocks_moved_into_free or []

        if i not in processed_occupied_blocks:
            processed_occupied_blocks.add(i)
            disk += [i for _ in range(occupied_block)]
        else:
            disk += [None for _ in range(occupied_block)]

        for moved_block_idx, moved_block in blocks_moved_into_free:
            free_block -= moved_block
            disk += [moved_block_idx for _ in range(moved_block)]
            processed_occupied_blocks.add(moved_block_idx)

        disk += [None for _ in range(free_block)]

    return disk


def compute_hash(disk):
    return sum(i * value for i, value in enumerate(disk) if value is not None)


def main():
    disk = read_disk()
    disk = compact_disk(disk)
    print(compute_hash(disk))


if __name__ == "__main__":
    main()
