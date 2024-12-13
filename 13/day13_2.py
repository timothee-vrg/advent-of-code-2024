def parse_line(line: str, value_type: str) -> tuple[int,int]:
    _, values = line.split(':')
    x_value, y_value = values.strip().split(",")
    _, x_value = x_value.strip().split(value_type)
    _, y_value = y_value.strip().split(value_type)
    return int(x_value), int(y_value)

def number_of_tokens(x_a: int, y_a: int, x_b: int, y_b: int, x_goal: int, y_goal: int) -> int:
    if (x_goal*y_a - y_goal*x_a) % (x_b*y_a-y_b*x_a) == 0:
        n_b = (x_goal*y_a - y_goal*x_a) // (x_b*y_a-y_b*x_a)
        if (x_goal*y_a - n_b*x_b*y_a) % (x_a*y_a) == 0:
            n_a = (x_goal*y_a - n_b*x_b*y_a) // (x_a*y_a)
            return 3*n_a + n_b
    return 0

def main():
    res = 0
    shift = 10**13
    with open("13/input.txt", "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 4): 
            x_a, y_a = parse_line(lines[i], '+')      
            x_b, y_b = parse_line(lines[i+1], '+')  
            x_goal, y_goal = parse_line(lines[i+2], '=')  
            res += number_of_tokens(x_a, y_a, x_b, y_b, x_goal+shift, y_goal+shift) 
    print(res)


if __name__ == "__main__":
    main()