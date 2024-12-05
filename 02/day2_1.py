def is_safe(tab: list[int]) -> bool:
    def greater(a: int, b: int) -> bool:
        return a > b
    def lower(a: int, b: int) -> bool:
        return a < b

    if len(tab) <= 1:
        return True
    
    compare_func = greater if tab[0] > tab[1] else lower
    length = len(tab)
    return all([compare_func(tab[i], tab[i+1]) and abs(tab[i]-tab[i+1]) <= 3 for i in range(length - 1)])


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