def generate_blocks(line: str) -> list[str]:
    length = len(line)
    blocks = []
    for i in range(length):
        if i%2 == 0:
            blocks.extend([str(i//2)]*int(line[i]))
        else:
            blocks.extend(['.']*int(line[i]))
    return blocks

def compact_blocks(blocks: list[str]) -> list[int]:
    length = len(blocks)
    beg, end = 0, length
    
    while beg < end:
        end -= 1
        while blocks[end] == ".":
            end -= 1
        while blocks[beg] != ".":
            beg += 1
        if beg < end:
            blocks[beg], blocks[end] = blocks[end], blocks[beg]
    
    return list(map(int,blocks[:beg]))

def compute_checksum(blocks: list[int]) -> int:
    checksum = 0
    for i in range(len(blocks)):
        checksum += i*blocks[i]
    return checksum

def main():
    with open("09/input.txt", "r") as f:
        line = f.readline()

        blocks = generate_blocks(line)
        compacted_blocks = compact_blocks(blocks)
        checksum = compute_checksum(compacted_blocks)

        print(checksum)


if __name__ == "__main__":
    main()