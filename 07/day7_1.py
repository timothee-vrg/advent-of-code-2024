def is_accessible(numbers: list[int], goal: int) -> bool:
    if len(numbers) == 1:
        return numbers[0] == goal
    
    return is_accessible([numbers[0]+numbers[1]]+numbers[2:], goal) or is_accessible([numbers[0]*numbers[1]]+numbers[2:], goal)

def main():
    res = 0
    with open("07/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            goal_str, numbers_str = line.split(":")
            goal = int(goal_str)
            numbers = list(map(int,numbers_str.split()))  
            if is_accessible(numbers,goal):
                res+=goal
    print(res)


if __name__ == "__main__":
    main()