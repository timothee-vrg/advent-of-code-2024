def resize_line(line: str) -> str:
    resized_char = {"@": "@.", ".": "..", "#": "##", "O": "[]"}

    res = ""
    for char in line:
        res += resized_char[char]
    return res

def move_grid(grid: list[list[str]], arrows: str) -> None:
    height = len(grid)
    width = len(grid[0])

    arrow_to_direction = {"<": {"direction": -1, "is_vertical" : False}, 
                          ">": {"direction": 1, "is_vertical" : False}, 
                          "^": {"direction": -1, "is_vertical" : True}, 
                          "v": {"direction": 1, "is_vertical" : True}}

    def find_robot() -> tuple[int,int]:
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "@":
                    return i,j
        raise Exception("Robot not found")
    
    def move_if_possible(x: int, y: int, direction: int, is_vertical: bool) -> tuple[int,int]:
        if is_vertical:
            return move_vertical_if_possible(x, y, direction)
        return move_horizontal_if_possible(x, y, direction)
    
    def move_horizontal_if_possible(x: int, y: int, dy: int) -> tuple[int,int]:
        distance = 1
        bracket = "[" if dy == 1 else "]"
        while grid[x][y+distance*dy] == bracket:
            distance += 2
        if grid[x][y+distance*dy] == "#":
            return x, y
        if dy == 1: distance-=1
        while distance >= 2:
            grid[x][y+distance*dy:y+distance*dy+2] = ["[","]"]
            distance -= 2
        grid[x][y], grid[x][y+dy] = ".", "@"
        return x, y+dy
    
    def move_vertical_if_possible(x: int, y: int, dx: int) -> tuple[int,int]:
        if grid[x+dx][y] == '.':
            grid[x][y], grid[x+dx][y] = ".", "@"
            return x+dx, y
        elif grid[x+dx][y] == "#":
            return x, y
        elif grid[x+dx][y] == "[":
            boxes = [(x+dx, y)]
        else:
            boxes = [(x+dx, y-1)]
        
        all_boxes = boxes.copy()
        while boxes:
            x_box, y_box = boxes.pop()
            new_boxes = []
            if grid[x_box+dx][y_box] == '[':
                new_boxes.append((x_box+dx, y_box))
            elif grid[x_box+dx][y_box] == "]":
                new_boxes.append((x_box+dx, y_box-1))
            elif grid[x_box+dx][y_box] == "#":
                return x,y
            if grid[x_box+dx][y_box+1] == '[':
                new_boxes.append((x_box+dx, y_box+1))
            elif grid[x_box+dx][y_box+1] == "]":
                new_boxes.append((x_box+dx, y_box))
            elif grid[x_box+dx][y_box+1] == "#":
                return x,y
            boxes.extend(new_boxes)
            all_boxes.extend(new_boxes)
               
        for x_box, y_box in all_boxes:
            grid[x_box][y_box], grid[x_box][y_box+1] = ".", "."
        for x_box, y_box in all_boxes:
            grid[x_box+dx][y_box], grid[x_box+dx][y_box+1] = "[", "]"
        grid[x][y], grid[x+dx][y] = ".","@"
        return x+dx, y

    x_robot, y_robot = find_robot()
    for arrow in arrows:
        arrow_info = arrow_to_direction[arrow] 
        x_robot, y_robot = move_if_possible(x_robot, y_robot, arrow_info["direction"], arrow_info["is_vertical"])

def gps_sum(grid: list[list[str]]) -> int:
    height = len(grid)
    width = len(grid[0])

    res = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "[":
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
                grid.append(list(resize_line(line.strip())))
            elif parse_type == PARSE_ARROWS:
                move_grid(grid, line.strip())
    print(gps_sum(grid))


if __name__ == "__main__":
    main()