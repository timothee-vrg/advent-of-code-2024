def count_xmas(lines: list[str]) -> int:
    height = len(lines)
    width = len(lines[0]) - 1 # Assume at least one line and all lines have the same length, -1 for the '\n'

    def is_in_tab(i: int, j: int) -> bool:
        return 0 <= i < height and 0 <= j < width
    
    def check_x_mas(x: int, y: int) -> bool:
        if lines[x][y] != "A":
            return False
        
        directions = [(1,1),(1,-1)]
        letters = {'M','S'}
        for dx, dy in directions:
            if not is_in_tab(x+dx,y+dy) or not is_in_tab(x-dx,y-dy):
                return False
            diag_letters = {lines[x+dx][y+dy], lines[x-dx][y-dy]}
            if diag_letters != letters:
                return False   
        return True

    number_of_xmas = 0
    for x in range(height):
        for y in range(width):
            if check_x_mas(x,y):
                number_of_xmas += 1

    return number_of_xmas

def main():
    with open("04/input.txt", "r") as f:
        lines = f.readlines()
    print(count_xmas(lines))


if __name__ == "__main__":
    main()