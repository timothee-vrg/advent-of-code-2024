from collections import deque

def lowest_score(grid: list[str]) -> int:
    height = len(grid)
    width = len(grid[0])

    def find_extremities(type: str) -> tuple[int,int]:
        for i in range(height):
            for j in range(width):
                if grid[i][j] == type:
                    return i,j
        raise Exception("Start not found")
    
    directions = [(0,1), (-1,0), (0,-1), (1,0)]

    lowest_scores = [[[float("inf")]*4 for j in range(width)] for i in range(height)]

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

    x_end, y_end = find_extremities("E")
    return min(lowest_scores[x_end][y_end])

def main():
    grid = []
    with open("16/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            grid.append(line.strip())
    print(lowest_score(grid))


if __name__ == "__main__":
    main()