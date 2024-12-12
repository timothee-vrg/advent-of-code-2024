def compute_price(grid: list[str]) -> int:
    height = len(grid)
    width = len(grid[0])

    def is_in_grid(i: int, j: int) -> bool:
        return 0 <= i < height and 0 <= j < width
    
    def compute_number_of_sides(region: set[tuple[int,int]]) -> int:
        number_of_sides = 0
        for x,y in region:
            # Top borders
            if (x-1,y) not in region and (((x,y-1) in region and (x-1,y-1) in region) or (x,y-1) not in region):
                number_of_sides += 1
            # Bottom borders
            if (x+1,y) not in region and (((x,y+1) in region and (x+1,y+1) in region) or (x,y+1) not in region):
                number_of_sides += 1
            # Left borders
            if (x,y-1) not in region and (((x+1,y) in region and (x+1,y-1) in region) or (x+1,y) not in region):
                number_of_sides += 1
            # Right borders
            if (x,y+1) not in region and (((x-1,y) in region and (x-1,y+1) in region) or (x-1,y) not in region):
                number_of_sides += 1
        return number_of_sides
    
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    seen = [[False for j in range(width)] for i in range(height)]

    price = 0
    for i in range(height):
        for j in range(width):
            if not seen[i][j]:
                region = set()
                seen[i][j] = True
                letter = grid[i][j]
                stack = [(i,j)]
                area = 0
                while stack:
                    x,y = stack.pop()
                    region.add((x,y))
                    area += 1
                    for dx, dy in directions:
                        if is_in_grid(x+dx,y+dy) and grid[x+dx][y+dy] == letter and not seen[x+dx][y+dy]:
                            seen[x+dx][y+dy] = True
                            stack.append((x+dx,y+dy))
                number_of_sides = compute_number_of_sides(region)
                price += area*number_of_sides

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