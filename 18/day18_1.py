from collections import deque

LENGTH = 71
NUMBER_OF_FALLEN_KB = 1024

def smallest_path(grid: list[list[str]]) -> int:

    def is_in_grid(i: int,j: int) -> bool:
        return 0 <= i < LENGTH and 0 <= j < LENGTH

    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    minimal_distances = [[float("inf")] * LENGTH for _ in range(LENGTH)] 

    file = deque()
    file.append((0,0))
    minimal_distances[0][0] = 0

    while file:
        x, y = file.popleft()
        current_distance = minimal_distances[x][y]
        for dx, dy in directions:
            if is_in_grid(x+dx,y+dy) and grid[x+dx][y+dy] != "#" and current_distance + 1 < minimal_distances[x+dx][y+dy]:
                minimal_distances[x+dx][y+dy] = current_distance + 1
                file.append((x+dx,y+dy))
    
    return minimal_distances[LENGTH-1][LENGTH-1]
    
def main():
    grid = [["."] * LENGTH for _ in range(LENGTH)] 
    with open("18/input.txt", "r") as f:
        lines = f.readlines()
        for i,line in enumerate(lines):
            x, y = map(int,line.strip().split(","))
            if i < NUMBER_OF_FALLEN_KB:
                grid[x][y] = "#"
    print(smallest_path(grid))


if __name__ == "__main__":
    main()