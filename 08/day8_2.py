def count_antinodes(grid: list[str]) -> int:
    height = len(grid)
    width = len(grid[0])

    def is_in_grid(i: int,j: int) -> bool:
        return 0 <= i < height and 0 <= j < width

    antennas = {}
    for i in range(height):
        for j in range(width):
            if grid[i][j] != ".":
                if grid[i][j] in antennas:
                    antennas[grid[i][j]].append((i,j)) 
                else:
                    antennas[grid[i][j]] = [(i,j)]
    
    antinodes_positions = set()
    for positions in antennas.values():
        for position_1 in positions:
            for position_2 in positions:
                if position_1 != position_2:
                    x_1, y_1 = position_1
                    x_2, y_2 = position_2
                    distance = 0
                    while is_in_grid(x_1+(x_1-x_2)*distance,y_1+(y_1-y_2)*distance):
                        antinodes_positions.add((x_1+(x_1-x_2)*distance,y_1+(y_1-y_2)*distance))
                        distance += 1
                    distance = 0
                    while is_in_grid(x_2+(x_2-x_1)*distance,y_2+(y_2-y_1)*distance):
                        antinodes_positions.add((x_2+(x_2-x_1)*distance,y_2+(y_2-y_1)*distance))
                        distance += 1

    return len(antinodes_positions)

def main():
    grid = []
    with open("08/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            grid.append(line[:-1]) # remove the "\n"
    print(count_antinodes(grid))


if __name__ == "__main__":
    main()