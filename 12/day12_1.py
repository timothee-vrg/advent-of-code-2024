def compute_price(grid: list[str]) -> int:
    height = len(grid)
    width = len(grid[0])

    def is_in_grid(i: int, j: int) -> bool:
        return 0 <= i < height and 0 <= j < width
    
    def compute_local_perimeter(x: int, y:int) -> int:
        local_perimeter = 0
        letter = grid[x][y]
        for dx, dy in directions:
            if not is_in_grid(x+dx,y+dy) or grid[x+dx][y+dy] != letter:
                local_perimeter += 1
        return local_perimeter        
    
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    seen = [[False for j in range(width)] for i in range(height)]

    price = 0
    for i in range(height):
        for j in range(width):
            if not seen[i][j]:
                seen[i][j] = True
                letter = grid[i][j]
                stack = [(i,j)]
                perimeter = 0
                area = 0
                while stack:
                    x,y = stack.pop()
                    area += 1
                    perimeter += compute_local_perimeter(x,y)
                    for dx, dy in directions:
                        if is_in_grid(x+dx,y+dy) and grid[x+dx][y+dy] == letter and not seen[x+dx][y+dy]:
                            seen[x+dx][y+dy] = True
                            stack.append((x+dx,y+dy))
                price += area*perimeter

    return price

def main():
    grid = []
    with open("12/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            grid.append(line.strip()) # remove the "\n"
    print(compute_price(grid))


if __name__ == "__main__":
    main()