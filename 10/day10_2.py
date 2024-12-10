def sum_of_scores(grid: list[str]) -> int:
    height = len(grid)
    width = len(grid[0])

    def is_in_grid(i: int,j: int) -> bool:
        return 0 <= i < height and 0 <= j < width

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    scores_dict = {}

    def score(x: int, y: int) -> int:
        if (x,y) in scores_dict:
            return scores_dict[(x,y)]
        if grid[x][y] == "0":
            return 1
        
        res = 0
        value = int(grid[x][y])
        for dx, dy in directions:
            if is_in_grid(x+dx,y+dy) and int(grid[x+dx][y+dy]) == value - 1:
                res += score(x+dx,y+dy)
        scores_dict[(x,y)] = res
        return res
    
    global_score = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "9":
                global_score += score(i,j)
    return global_score

def main():
    grid = []
    with open("10/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            grid.append(line[:-1]) # remove the "\n"
    print(sum_of_scores(grid))


if __name__ == "__main__":
    main()