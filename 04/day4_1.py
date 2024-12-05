def count_xmas(lines: list[str]) -> int:
    height = len(lines)
    width = len(lines[0]) - 1 # Assume at least one line and all lines have the same length, -1 for the '\n'

    def is_in_tab(i: int,j: int) -> bool:
        return 0 <= i < height and 0 <= j < width
    
    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

    number_of_xmas = 0
    for x in range(height):
        for y in range(width):
            if lines[x][y] == "X":
                for dx, dy in directions:
                    if is_in_tab(x+dx,y+dy) and lines[x+dx][y+dy] == "M" and is_in_tab(x+2*dx,y+2*dy) and lines[x+2*dx][y+2*dy] == "A" and is_in_tab(x+3*dx,y+3*dy) and lines[x+3*dx][y+3*dy] == "S":
                        number_of_xmas += 1

    return number_of_xmas

def main():
    with open("04/input.txt", "r") as f:
        lines = f.readlines()
    print(count_xmas(lines))


if __name__ == "__main__":
    main()