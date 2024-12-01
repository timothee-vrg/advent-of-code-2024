def compute_distance(list_1: list[int], list_2: list[int]) -> int:
    list_1.sort()
    list_2.sort()
    length = len(list_1)
    return sum([abs(list_2[i]-list_1[i]) for i in range(length)])

def main():
    with open("01/input.txt", "r") as f:
        lines = f.readlines()
        list_1, list_2 = [], []
        for line in lines:
            number_1, number_2 = map(int,line.split())
            list_1.append(number_1)
            list_2.append(number_2)
    print(compute_distance(list_1,list_2))


if __name__ == "__main__":
    main()