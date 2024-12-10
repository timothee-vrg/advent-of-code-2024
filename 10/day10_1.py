def sum_of_scores(grid: list[str]) -> int:
    height = len(grid)
    width = len(grid[0])

    def is_in_grid(i: int,j: int) -> bool:
        return 0 <= i < height and 0 <= j < width

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    def trailhead_score(i: int, j: int) -> int:
        nine_heights_count = 0
        already_seen = set()
        positions = [(i,j)]
        while positions:
            x, y = positions.pop()
            value = int(grid[x][y])
            for dx, dy in directions:
                if is_in_grid(x+dx,y+dy) and int(grid[x+dx][y+dy]) == value + 1 and not (x+dx,y+dy) in already_seen:
                    already_seen.add((x+dx,y+dy))
                    if value == 8:
                        nine_heights_count += 1
                    else:
                        positions.append((x+dx,y+dy))
        return nine_heights_count
        
    res = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "0":
                res += trailhead_score(i,j)
    return res

def main():
    grid = []
    with open("10/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            grid.append(line[:-1]) # remove the "\n"
    print(sum_of_scores(grid))


if __name__ == "__main__":
    main()