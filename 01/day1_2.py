def compute_similarity(list_1: list[int], list_2: list[int]) -> int:
    dico = {}
    for elmt in list_2:
        if elmt in dico:
            dico[elmt] += 1
        else:
            dico[elmt] = 1

    score = 0
    for elmt in list_1:
        if elmt in dico:
            score += elmt*dico[elmt]
    return score  


def main():
    with open("01/input.txt", "r") as f:
        lines = f.readlines()
        list_1, list_2 = [], []
        for line in lines:
            number_1, number_2 = map(int,line.split())
            list_1.append(number_1)
            list_2.append(number_2)
    print(compute_similarity(list_1,list_2))


if __name__ == "__main__":
    main()