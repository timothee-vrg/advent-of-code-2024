GRID_HEIGHT = 101
GRID_WIDTH = 103

def parse_line(line: str) -> list[int]:
    position, velocity = line.split()
    _, position_values = position.split("=")
    p_x, p_y = list(map(int, position_values.split(",")))
    _, velocity_values = velocity.split("=")
    v_x, v_y = list(map(int, velocity_values.split(",")))
    return [p_x,p_y,v_x,v_y]

def safety_factor(robots: list[int]) -> int:
    
    def final_positions(p_x: int, p_y: int, v_x: int, v_y: int, numbers_of_seconds:int) -> tuple[int,int]:
        return (p_x + number_of_seconds*v_x) % GRID_HEIGHT, (p_y + number_of_seconds*v_y) % GRID_WIDTH
    
    def check_tree() -> bool:
        for x,y in positions:
            if all([(x+i, y) in positions for i in range(10)]):
                return True
        return False

    def display_grid() -> None:
        grid = [[" " for j in range(GRID_HEIGHT)] for i in range(GRID_WIDTH)]
        for x,y in positions:
            grid[y][x] = "*"
        for line in grid:
            print(*line)

    number_of_seconds = 0
    while True:
        positions = set()
        for p_x,p_y,v_x,v_y in robots:
            p_xf, p_yf = final_positions(p_x,p_y,v_x,v_y,number_of_seconds)
            positions.add((p_xf, p_yf))
        if check_tree():
            display_grid()
            break
        number_of_seconds += 1
    return number_of_seconds

def main():
    robots = []
    with open("14/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            robots.append(parse_line(line.strip()))
    print(safety_factor(robots))


if __name__ == "__main__":
    main()