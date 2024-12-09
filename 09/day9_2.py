def generate_blocks(line: str) -> list[str]:
    length = len(line)
    blocks = []
    for i in range(length):
        if i%2 == 0:
            blocks.extend([str(i//2)]*int(line[i]))
        else:
            blocks.extend(['.']*int(line[i]))
    return blocks

def compact_blocks(blocks: list[str]) -> list[str]:
    length = len(blocks)
    pos = length - 1

    while blocks[pos] == ".":
        pos -= 1
    block_id = int(blocks[pos])

    while block_id > 0:
        while blocks[pos] != str(block_id):
            pos -= 1
        block_size = 1
        pos -= 1
        while blocks[pos] == str(block_id):
            pos -= 1
            block_size += 1

        free_space = ["."] * block_size
        for i in range(min(pos, length-block_size)):
            if blocks[i:i+block_size] == free_space:
                blocks[i:i+block_size], blocks[pos+1:pos+1+block_size] = blocks[pos+1:pos+1+block_size], blocks[i:i+block_size]
                break
        block_id -= 1
    
    return blocks

def compute_checksum(blocks: list[str]) -> int:
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] != ".":
            checksum += i*int(blocks[i])
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