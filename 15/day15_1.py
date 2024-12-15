def move_grid(grid: list[list[str]], arrows: str) -> None:
    height = len(grid)
    width = len(grid[0])

    arrow_to_direction = {"<": (0,-1), ">": (0,1), "^": (-1,0), "v": (1,0)}

    def find_robot() -> tuple[int,int]:
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "@":
                    return i,j
        raise Exception("Robot not found")
    
    def move_if_possible(x: int, y: int, dx: int, dy: int) -> tuple[int,int]:
        distance = 1
        while grid[x+distance*dx][y+distance*dy] == "O":
            distance += 1
        if grid[x+distance*dx][y+distance*dy] == "#":
            return x, y
        while distance >= 2:
            grid[x+distance*dx][y+distance*dy] = "O"
            distance -= 1
        grid[x][y], grid[x+dx][y+dy] = ".", "@"
        return x+dx,y+dy
    
    x_robot, y_robot = find_robot()
    for arrow in arrows:
        dx, dy = arrow_to_direction[arrow]
        x_robot, y_robot = move_if_possible(x_robot, y_robot, dx, dy)

def gps_sum(grid: list[list[str]]) -> int:
    height = len(grid)
    width = len(grid[0])

    res = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "O":
                res += i*100 + j
    return res

def main():
    grid = []
    with open("15/input.txt", "r") as f:
        PARSE_GRID = 1
        PARSE_ARROWS = 2
        lines = f.readlines()
        parse_type = PARSE_GRID
        for line in lines:
            if line == "\n":
                parse_type = PARSE_ARROWS
            elif parse_type == PARSE_GRID:
                grid.append(list(line.strip()))
            elif parse_type == PARSE_ARROWS:
                move_grid(grid, line.strip())
    print(gps_sum(grid))


if __name__ == "__main__":
    main()