def count_distinct_position(grid: list[str]) -> int:
    height = len(grid)
    width = len(grid[0])
    
    def is_in_grid(i: int,j: int) -> bool:
        return 0 <= i < height and 0 <= j < width
    
    def find_initial_position() -> tuple[int]:
        for i in range(height):
            for j in range(width):
                match grid[i][j]:
                    case ">":
                        return i,j,0,1
                    case "<":
                        return i,j,0,-1
                    case "v":
                        return i,j,1,0
                    case "^":
                        return i,j,-1,0
                    case _:
                        continue
        raise Exception("No initial position found.")
    
    def next_direction(dirX: int, dirY: int) -> tuple[int]:
        return directions[(directions.index((dirX,dirY))+1)%len(directions)]
    
    x, y, dirX, dirY = find_initial_position()
    directions = [(-1,0), (0,1), (1,0), (0,-1)]

    number_of_distinct_position = 1 # the initial position
    travelled_positions = [[(i,j) == (x,y) for j in range(width)] for i in range(height)]

    while True:
        if not is_in_grid(x+dirX, y+dirY):
            break
        while grid[x+dirX][y+dirY] == "#":
            dirX, dirY = next_direction(dirX,dirY)
        x, y = x+dirX, y+dirY
        if not travelled_positions[x][y]:
            number_of_distinct_position += 1
        travelled_positions[x][y] = True

    return number_of_distinct_position

def main():
    grid = []
    with open("06/input.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            grid.append(line[:-1]) # remove the "\n"
    print(count_distinct_position(grid))


if __name__ == "__main__":
    main()