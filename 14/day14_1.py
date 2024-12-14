GRID_HEIGHT = 101
GRID_WIDTH = 103
NUMBER_OF_SECONDS = 100

def parse_line(line: str) -> list[int]:
    position, velocity = line.split()
    _, position_values = position.split("=")
    p_x, p_y = list(map(int, position_values.split(",")))
    _, velocity_values = velocity.split("=")
    v_x, v_y = list(map(int, velocity_values.split(",")))
    return [p_x,p_y,v_x,v_y]


def safety_factor(robots: list[int]) -> int:
    
    def final_positions(p_x: int, p_y: int, v_x: int, v_y: int) -> tuple[int,int]:
        return (p_x + NUMBER_OF_SECONDS*v_x) % GRID_HEIGHT, (p_y + NUMBER_OF_SECONDS*v_y) % GRID_WIDTH
    
    def add_to_quarter(x: int, y: int) -> None:
        if x < GRID_HEIGHT//2 and y < GRID_WIDTH//2:
            quarters[0] += 1
        elif x < GRID_HEIGHT//2 and y > GRID_WIDTH//2:
            quarters[1] += 1
        elif x > GRID_HEIGHT//2 and y < GRID_WIDTH//2:
            quarters[2] += 1
        elif x > GRID_HEIGHT//2 and y > GRID_WIDTH//2:
            quarters[3] += 1
    
    def prod(tab: list[int]) -> int:
        res = 1
        for elmt in tab:
            res *= elmt
        return res

    quarters = [0,0,0,0]

    for p_x,p_y,v_x,v_y in robots:
        p_xf, p_yf = final_positions(p_x,p_y,v_x,v_y)
        add_to_quarter(p_xf, p_yf)
    return prod(quarters)

def main():
    robots = []
    with open("14/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            robots.append(parse_line(line.strip()))
    print(safety_factor(robots))


if __name__ == "__main__":
    main()