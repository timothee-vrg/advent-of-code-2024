def is_safe(tab: list[int]) -> bool:
    for i in range(len(tab)):
        if is_safe_with_bad_level(tab, i):
            return True
    return False

def is_safe_with_bad_level(tab: list[int], bad_level: int) -> bool:
    def greater(a: int, b: int) -> bool:
        return a > b
    def lower(a: int, b: int) -> bool:
        return a < b

    tab_copy = tab.copy()
    tab_copy.pop(bad_level)

    if len(tab_copy) <= 1:
        return True
    
    compare_func = greater if tab_copy[0] > tab_copy[1] else lower
    length = len(tab_copy)

    return all([compare_func(tab_copy[i], tab_copy[i+1]) and abs(tab_copy[i]-tab_copy[i+1]) <= 3 for i in range(length - 1)])



def main():
    number_of_safe = 0
    with open("02/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if is_safe(list(map(int,line.split()))):
                number_of_safe += 1
    print(number_of_safe)


if __name__ == "__main__":
    main()