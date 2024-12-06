def count_obstructions(grid: list[str]) -> int:
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
    
    def get_possible_obstructions() -> list[tuple[int]]:
        x, y, dirX, dirY = find_initial_position()

        travelled_positions = [[(i,j) == (x,y) for j in range(width)] for i in range(height)]

        while True:
            if not is_in_grid(x+dirX, y+dirY):
                break
            while grid[x+dirX][y+dirY] == "#":
                dirX, dirY = next_direction(dirX,dirY)
            x, y = x+dirX, y+dirY
            travelled_positions[x][y] = True

        return [(i,j) for i in range(height) for j in range(width) if travelled_positions[i][j]]

    
    def is_in_infinite_loop(grid: list[str]) -> bool:
        x, y, dirX, dirY = find_initial_position()

        travelled_positions_with_direction = [[[False] * 4 for j in range(width)] for i in range(height)]

        while True:
            if not is_in_grid(x+dirX, y+dirY):
                return False
            while grid[x+dirX][y+dirY] == "#":
                dirX, dirY = next_direction(dirX,dirY)
            x, y = x+dirX, y+dirY
            if travelled_positions_with_direction[x][y][directions.index((dirX,dirY))]:
                return True
            travelled_positions_with_direction[x][y][directions.index((dirX,dirY))] = True

    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    number_of_obstructions = 0
    for i,j in get_possible_obstructions():
        if grid[i][j] == ".": # just to avoid the initial position
            grid[i] = grid[i][:j] + "#" + grid[i][j+1:]
            if is_in_infinite_loop(grid):
                number_of_obstructions += 1
            grid[i] = grid[i][:j] + "." + grid[i][j+1:]
    return number_of_obstructions


def main():
    grid = []
    with open("06/input.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            grid.append(line[:-1]) # remove the "\n"
    print(count_obstructions(grid))


if __name__ == "__main__":
    main()