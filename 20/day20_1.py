from collections import deque

THRESHOLD = 100

def number_of_good_cheats(grid: list[list[str]]) -> int:
    height = len(grid)
    width = len(grid[0])
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    def is_in_grid(i: int,j: int) -> bool:
        return 0 <= i < height and 0 <= j < width

    def find_extremities(type: str) -> tuple[int,int]:
        for i in range(height):
            for j in range(width):
                if grid[i][j] == type:
                    return i,j
        raise Exception("Extremity not found")
    
    def get_minimal_distances(grid: list[list[str]], x_start: int, y_start: int, x_end: int, y_end: int) -> int:

        minimal_distances = [[float("inf")] * width for _ in range(height)] 

        file = deque()
        file.append((x_start, y_start))
        minimal_distances[x_start][y_start] = 0

        while file:
            x, y = file.popleft()
            current_distance = minimal_distances[x][y]
            for dx, dy in directions:
                if is_in_grid(x+dx,y+dy) and grid[x+dx][y+dy] != "#" and current_distance + 1 < minimal_distances[x+dx][y+dy]:
                    minimal_distances[x+dx][y+dy] = current_distance + 1
                    file.append((x+dx,y+dy))
        
        return minimal_distances

    def get_normal_track(x_start: int, y_start: int, x_end: int, y_end: int) -> set[tuple[int,int]]:
        normal_track_squares = set()
        x, y = x_end, y_end
        while (x,y) != (x_start, y_start):
            normal_track_squares.add((x,y))
            current_distance = minimal_distances[x][y]
            for (dx, dy) in directions:
                if minimal_distances[x+dx][y+dy] == current_distance - 1:
                    x,y = x+dx, y+dy
                    break
        normal_track_squares.add((x,y))
        return normal_track_squares
    
    def distance_between_two_points(x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x2-x1) + abs(y2-y1)

    x_start, y_start = find_extremities("E")
    x_end, y_end = find_extremities("S")

    minimal_distances = get_minimal_distances(grid, x_start, y_start, x_end, y_end)
    normal_track = get_normal_track(x_start, y_start, x_end, y_end)

    res = 0
    for (x1, y1) in normal_track:
        for (x2, y2) in normal_track:
            if distance_between_two_points(x1,y1,x2,y2) == 2:
                saved_pico = abs(minimal_distances[x2][y2] - minimal_distances[x1][y1]) - 2
                if saved_pico >= THRESHOLD:
                    res += 1
                
    return res//2
                    
def main():
    grid = []
    with open("20/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            grid.append(list(line.strip()))
    print(number_of_good_cheats(grid))


if __name__ == "__main__":
    main()