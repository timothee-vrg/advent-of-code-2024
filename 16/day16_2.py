from collections import deque

def length_best_paths(grid: list[str]) -> int:
    height = len(grid)
    width = len(grid[0])

    def find_extremities(type: str) -> tuple[int,int]:
        for i in range(height):
            for j in range(width):
                if grid[i][j] == type:
                    return i,j
        raise Exception("Start not found")
    
    def opposite_direction_index(dir_index: int) -> int:
        return (dir_index + 2) % 4
    
    def build_lowest_scores() -> None:
        x, y =  find_extremities("S")
        direction_index = 0
        lowest_scores[x][y][direction_index] = 0
        
        file = deque()
        file.append((x,y,direction_index))
        
        while file:
            x, y, direction_index = file.popleft()
            current_score = lowest_scores[x][y][direction_index]
            
            clockwise_dir = (direction_index + 1) % 4
            counterclockwise_dir = (direction_index - 1) % 4
            dx, dy = directions[direction_index]
        
            if lowest_scores[x][y][clockwise_dir] > current_score + 1000:
                lowest_scores[x][y][clockwise_dir] = current_score + 1000
                file.append((x,y,clockwise_dir))
            
            if lowest_scores[x][y][counterclockwise_dir] > current_score + 1000:
                lowest_scores[x][y][counterclockwise_dir] = current_score + 1000
                file.append((x,y,counterclockwise_dir)) 
            
            if grid[x+dx][y+dy] != '#' and lowest_scores[x+dx][y+dy][direction_index] > current_score + 1:
                lowest_scores[x+dx][y+dy][direction_index] = current_score + 1
                file.append((x+dx,y+dy,direction_index))    

    
    directions = [(0,1), (-1,0), (0,-1), (1,0)]

    lowest_scores = [[[float("inf")]*4 for j in range(width)] for i in range(height)]
    build_lowest_scores()

    x_end, y_end = find_extremities("E")
    score = min(lowest_scores[x_end][y_end])
    direction_index = lowest_scores[x_end][y_end].index(score)

    in_best_paths = set()

    stack = [(x_end, y_end, direction_index)]
    while stack:
        x, y, direction_index = stack.pop()
        current_score = lowest_scores[x][y][direction_index]
        
        in_best_paths.add((x, y))

        opp_clockwise_dir = (direction_index - 1) % 4
        opp_counterclockwise_dir = (direction_index + 1) % 4

        if lowest_scores[x][y][opp_clockwise_dir] == current_score - 1000:
            stack.append((x,y,opp_clockwise_dir))
        
        if lowest_scores[x][y][opp_counterclockwise_dir] == current_score - 1000:
            stack.append((x,y,opp_counterclockwise_dir)) 
        
        for direction_index, (dx, dy) in enumerate(directions):
            opp_direction_index = opposite_direction_index(direction_index)
            if lowest_scores[x+dx][y+dy][opp_direction_index] == current_score - 1:
                stack.append((x+dx,y+dy,opp_direction_index))    

    return len(in_best_paths)

def main():
    grid = []
    with open("16/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            grid.append(line.strip())
    print(length_best_paths(grid))


if __name__ == "__main__":
    main()